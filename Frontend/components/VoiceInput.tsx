'use client';

import { Send } from 'lucide-react';
import { Button } from '@/components/ui/button';

interface VoiceInputProps {
  value: string;
  onChange: (value: string) => void;
  onSend: () => void;
  disabled?: boolean;
  error?: string | null;
}

export default function VoiceInput({
  value,
  onChange,
  onSend,
  disabled = false,
  error,
}: VoiceInputProps) {
  const handleKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      onSend();
    }
  };

  return (
    <div className="w-full">
      {error && (
        <div className="mb-4 p-3 bg-destructive/10 border border-destructive/30 rounded-lg text-destructive text-sm">
          {error}
        </div>
      )}
      
      <div className="relative">
        <input
          type="text"
          value={value}
          onChange={(e) => onChange(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="Enter your text"
          disabled={disabled}
          className="w-full px-6 py-4 pr-16 bg-secondary border border-border rounded-full text-foreground placeholder-muted-foreground focus:outline-none focus:ring-2 focus:ring-accent focus:ring-opacity-50 transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed"
        />
        
        <Button
          onClick={onSend}
          disabled={disabled || !value.trim()}
          className="absolute right-2 top-1/2 transform -translate-y-1/2 rounded-full p-2 h-10 w-10 bg-accent hover:bg-accent/90 text-accent-foreground transition-all duration-200"
          size="sm"
        >
          <Send size={20} />
        </Button>
      </div>
    </div>
  );
}
