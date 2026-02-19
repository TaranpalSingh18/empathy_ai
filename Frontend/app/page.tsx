'use client';

import { useState, useRef } from 'react';
import { Send, Volume2 } from 'lucide-react';
import VoiceInput from '@/components/VoiceInput';
import GeneratingCard from '@/components/GeneratingCard';
import AudioPlayer from '@/components/AudioPlayer';

export default function Home() {
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [audioUrl, setAudioUrl] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);

  const handleSend = async () => {
    if (!input.trim()) return;

    setIsLoading(true);
    setError(null);
    setAudioUrl(null);

    try {
      const backendUrl = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";
      
      const response = await fetch(`${backendUrl}/generate-speech`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: input }),
      });

      if (!response.ok) {
        throw new Error('Failed to generate speech');
      }

      // Assuming your FastAPI returns audio blob
      const audioBlob = await response.blob();
      const url = URL.createObjectURL(audioBlob);
      setAudioUrl(url);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An error occurred');
      console.error('Error:', err);
    } finally {
      setIsLoading(false);
    }
  };

  const handleClearAudio = () => {
    if (audioUrl) {
      URL.revokeObjectURL(audioUrl);
    }
    setAudioUrl(null);
    setInput('');
  };

  return (
    <main className="min-h-screen bg-background text-foreground flex flex-col items-center justify-center p-4">
      {/* Logo and Title */}
      <div className="mb-12 text-center">
        <h1 className="text-5xl font-light tracking-wide mb-2">
          Empathy AI
        </h1>
        <p className="text-sm text-muted-foreground">
          Transform text to natural speech
        </p>
      </div>

      {/* Main Content */}
      <div className="w-full max-w-2xl">
        {/* Audio Player - Shows when audio is generated */}
        {audioUrl && !isLoading && (
          <div className="mb-8">
            <AudioPlayer audioUrl={audioUrl} onClear={handleClearAudio} />
          </div>
        )}

        {/* Generating Card - Shows while loading */}
        {isLoading && <GeneratingCard />}

        {/* Voice Input - Main input area */}
        {!isLoading && (
          <VoiceInput
            value={input}
            onChange={setInput}
            onSend={handleSend}
            disabled={isLoading}
            error={error}
          />
        )}
      </div>
    </main>
  );
}
