'use client';

import { useRef, useEffect } from 'react';
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
  const textareaRef = useRef<HTMLTextAreaElement>(null);

  // Auto-expand textarea height based on content
  useEffect(() => {
    if (textareaRef.current) {
      textareaRef.current.style.height = 'auto';
      textareaRef.current.style.height = Math.min(textareaRef.current.scrollHeight, 300) + 'px';
    }
  }, [value]);

  const handleKeyDown = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
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
      
      <div className="relative group">
        <div className="absolute inset-0 bg-gradient-to-r from-accent/20 to-accent/5 rounded-lg blur-xl group-focus-within:blur-2xl opacity-0 group-focus-within:opacity-100 transition-all duration-300"></div>
        <textarea
          ref={textareaRef}
          value={value}
          onChange={(e) => onChange(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="Enter your text (Shift+Enter for new line)..."
          disabled={disabled}
          className="relative w-full px-6 py-4 pr-16 bg-card border border-border rounded-2xl text-foreground placeholder-muted-foreground focus:outline-none focus:ring-2 focus:ring-accent focus:border-accent transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed shadow-lg resize-none overflow-hidden min-h-16 max-h-80"
        />
        
        <Button
          onClick={onSend}
          disabled={disabled || !value.trim()}
          className="absolute right-2 top-4 rounded-lg p-2 h-10 w-10 bg-accent hover:bg-accent/90 text-accent-foreground transition-all duration-200 shadow-md hover:shadow-lg disabled:opacity-50"
          size="sm"
        >
          <Send size={20} />
        </Button>
      </div>
    </div>
  );
}
