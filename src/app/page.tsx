"use client";

import { useState } from "react";
import { api } from "@/trpc/react";
const celebrities = [
  "Donald Trump",
  "Kamala Harris",
  "Joe Biden",
  "Elon Musk",
  "Bill Gates",
  "Steve Jobs",
  "Brad Pitt",
  "Jennifer Lawrence",
  "Tom Hanks",
  "Meryl Streep",
  "Leonardo DiCaprio",
];
const modes = ["Date", "Debate"];

export default function Home() {
  const [player1, setPlayer1] = useState(celebrities[0]);
  const [player2, setPlayer2] = useState(celebrities[1]);
  const [mode, setMode] = useState(modes[0]);
  const [topic, setTopic] = useState("");
  const [messages, setMessages] = useState<
    { character: string; content: string }[]
  >([]);
  const [startCount, setStartCount] = useState(0);
  const callScriptMutation = api.callPythonScript.useMutation();
  const [result, setResult] = useState<{
    messages: { character: string; content: string }[];
  } | null>(null);
  const [characters, setCharacters] = useState<string>("");

  const handleReset = () => {
    setStartCount(0);
    setMessages([]);
  };

  const handleStart = async () => {
    if (!player1 || !player2 || !mode) return; // Check if all required fields are filled
    setStartCount((prevCount) => prevCount + 1);
    // Logic to start the date/debate and generate messages
    setMessages([
      { character: player1, content: `Hello, I'm ${player1}!` },
      {
        character: player2,
        content: `Hi ${player1}, I'm ${player2}. Let's ${mode.toLowerCase()}!`,
      },
    ]);
    setCharacters([player1, player2].join(", "));

    // Incorporated handleCallScript logic
    setResult(null);
    const characterArray = [player1, player2];
    const response = await callScriptMutation.mutateAsync({
      characters: characterArray,
      theme: topic || "Artificial Intelligence",
    });
    setResult(response.scriptResult);

    console.log("result after script call", response.scriptResult);
    response.scriptResult?.messages.forEach((resp) => {
      const newMessage = { character: resp.character, content: resp.content };
      setMessages((prevMessages) => [...prevMessages, newMessage]);
    });
  };

  return (
    <main className="min-h-screen bg-gray-100 p-8">
      <div className="mx-auto max-w-2xl rounded-lg bg-white p-6 shadow-lg">
        <h1 className="mb-6 text-center text-3xl font-bold">Date or Debate</h1>

        <div className="mb-4 flex justify-between">
          <select
            className="rounded border p-2"
            value={player1}
            onChange={(e) => {
              setPlayer1(e.target.value);
              handleReset();
            }}
          >
            {celebrities.map((celeb) => (
              <option key={celeb} value={celeb}>
                {celeb}
              </option>
            ))}
          </select>
          <select
            className="rounded border p-2"
            value={player2}
            onChange={(e) => {
              setPlayer2(e.target.value);
              handleReset();
            }}
          >
            {celebrities.map((celeb) => (
              <option key={celeb} value={celeb}>
                {celeb}
              </option>
            ))}
          </select>
        </div>

        <select
          className="mb-4 w-full rounded border p-2"
          value={mode}
          onChange={(e) => {
            setMode(e.target.value);
            handleReset();
          }}
        >
          {modes.map((m) => (
            <option key={m} value={m}>
              {m}
            </option>
          ))}
        </select>

        <div className="mb-4 flex">
          <input
            type="text"
            className="flex-grow rounded-l border p-2"
            placeholder="Enter a topic"
            value={topic}
            onChange={(e) => setTopic(e.target.value)}
          />
          <button
            className="rounded-r bg-blue-500 px-4 py-2 text-white"
            onClick={handleStart}
          >
            {startCount === 0 ? "Start" : "Continue"}
          </button>
        </div>

        <div className="h-64 overflow-y-auto rounded border p-4">
          {messages.map((message, index) => (
            <div
              key={index}
              className={`mb-2 ${message.character === player1 ? "text-left" : "text-right"}`}
            >
              <span className="font-bold">{message.character}: </span>
              {message.content}
            </div>
          ))}
        </div>
      </div>
    </main>
  );
}
