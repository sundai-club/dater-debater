import { spawn } from "child_process";

type RunBashScriptResult = {
  stdout: string;
  stderr: string;
  combinedOutput: string;
  exitCode: number;
};

export async function runScript(
  script: string,
  opts?: {
    cwd?: string; // default tmp
    throwOnNonZeroExitCode?: boolean; // default true
    emitOutput?: boolean; // default true
  },
): Promise<RunBashScriptResult> {
  // // print first 80 characters or 4 lines of script
  // let toPrint = script;
  // if (script.length > 80) {
  //   toPrint = script.slice(0, 80) + "...";
  // }
  // if (script.split("\n").length > 4) {
  //   toPrint = script.split("\n").slice(0, 4).join("\n") + "...";
  // }
  // console.log(`\nRunning script:\n---\n${toPrint}\n---\n`);

  const cwd = opts?.cwd ?? process.cwd();
  const throwOnNonZeroExitCode = opts?.throwOnNonZeroExitCode ?? true;
  const emitOutput = opts?.emitOutput ?? true;

  return new Promise((resolve, reject) => {
    const child = spawn("bash", ["-x", "-e", "-c", script], { cwd });

    let stdout = "";
    let stderr = "";
    let combinedOutput = "";

    child.stdout.on("data", (data) => {
      // eslint-disable-next-line @typescript-eslint/no-unsafe-call, @typescript-eslint/no-unsafe-member-access
      const chunk = data.toString() as string;
      stdout += chunk;
      combinedOutput += chunk;
      if (emitOutput) {
        process.stdout.write(chunk);
      }
    });

    child.stderr.on("data", (data) => {
      // eslint-disable-next-line @typescript-eslint/no-unsafe-call, @typescript-eslint/no-unsafe-member-access
      const chunk = data.toString() as string;
      stderr += chunk;
      combinedOutput += chunk;
      if (emitOutput) {
        process.stderr.write(chunk);
      }
    });

    child.on("close", (code) => {
      const result: RunBashScriptResult = {
        stdout,
        stderr,
        combinedOutput,
        exitCode: code ?? 0,
      };

      if (throwOnNonZeroExitCode && code !== 0) {
        console.error("=== Failed Script ===");
        console.error(script);
        console.error("=== End Failed Script ===");
        reject(new Error(`Command failed with exit code ${code}\n${stderr}`));
      } else {
        resolve(result);
      }
    });

    child.on("error", (error) => {
      reject(error);
    });
  });
}
