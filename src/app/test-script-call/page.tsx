"use client";

import { useState } from "react";
import { api } from "@/trpc/react";

export default function Home() {
  const callScriptMutation = api.callPythonScript.useMutation();
  const [result, setResult] = useState<{
    messages: { character: string; content: string }[];
  } | null>(null);
  const [characters, setCharacters] = useState<string>("");

  const handleCallScript = async () => {
    setResult(null);
    const characterArray = characters.split(",").map((char) => char.trim());
    const response = await callScriptMutation.mutateAsync({
      characters: characterArray,
    });
    setResult(response.scriptResult);
  };

  return (
    <main className="p-4">
      <div className="mb-4">
        <label htmlFor="characters" className="mb-2 block font-bold">
          Enter characters (comma-separated):
        </label>
        <input
          type="text"
          id="characters"
          value={characters}
          onChange={(e) => setCharacters(e.target.value)}
          className="w-full rounded border px-3 py-2"
          placeholder="e.g. Albert Einstein, Marie Curie"
        />
      </div>
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
          <div>
            {result.messages.map((message, index) => (
              <div key={index} className="mb-2">
                <strong>{message.character}:</strong> {message.content}
              </div>
            ))}
          </div>
        ) : (
          <p>Enter characters and click the button to call the script</p>
        )}
      </div>
    </main>
  );
}
