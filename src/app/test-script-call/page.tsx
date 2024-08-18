"use client";

import { useState } from "react";
import { api } from "@/trpc/react";

export default function Home() {
  const callScriptMutation = api.callPythonScript.useMutation();
  const [result, setResult] = useState<string | null>(null);

  const handleCallScript = async () => {
    setResult(null);
    const response = await callScriptMutation.mutateAsync({ text: "Hello" });
    setResult(response.scriptResult);
  };

  return (
    <main className="p-4">
      <button
        onClick={handleCallScript}
        className="rounded bg-blue-500 px-4 py-2 font-bold text-white hover:bg-blue-700"
        disabled={callScriptMutation.isPending}
      >
        Call Script
      </button>
      <div className="mt-4 rounded border p-4">
        {callScriptMutation.isPending ? (
          <p>Loading...</p>
        ) : result ? (
          <pre>{result}</pre>
        ) : (
          <p>Click the button to call the script</p>
        )}
      </div>
    </main>
  );
}
