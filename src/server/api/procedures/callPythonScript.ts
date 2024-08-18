import { z } from "zod";

import { publicProcedure } from "@/server/api/trpc";
import { runScript } from "@/server/lib/runScript";
import { getThisProjectRoot } from "@/server/lib/getThisProjectRoot";
import path from "path";
import { quote as shellQuote } from "shlex";
import { env } from "@/env";

export const pythonResultSchema = z.object({
  messages: z.array(
    z.object({
      character: z.string(),
      content: z.string(),
    }),
  ),
});

export const callPythonScript = publicProcedure
  .input(
    z.object({
      characters: z.array(z.string()),
      theme: z.string(), // Add theme to the input schema
    }),
  )
  .mutation(async ({ input }) => {
    const llmConversationDir = path.resolve(
      await getThisProjectRoot(),
      "llm_conversation",
    );
    console.log("llmConversationDir", llmConversationDir);
    const pythonScriptPath = path.join(llmConversationDir, "main.py");
    const requirementsPath = path.join(llmConversationDir, "requirements.txt");

    // Install requirements separately
    await runScript(`
      pip3 install --break-system-packages -r ${shellQuote(requirementsPath)}
    `);

    // Run the main Python script
    const runRes = await runScript(`
      python3 ${shellQuote(pythonScriptPath)} --api_key ${shellQuote(env.OPENAI_API_KEY)} --characters ${shellQuote(input.characters.join(","))} --num_messages 6 --mode debate --max_sentences 3 --theme ${shellQuote(input.theme)}
    `);
    console.log("runRes", JSON.stringify(runRes, null, 2));

    // Parse the result using the schema
    const parsedResult = pythonResultSchema.parse(JSON.parse(runRes.stdout));

    return { scriptResult: parsedResult };
  });
