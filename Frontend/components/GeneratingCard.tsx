'use client';

import { useEffect, useState } from 'react';

export default function GeneratingCard() {
  const [isVisible, setIsVisible] = useState(false);

  useEffect(() => {
    // Trigger animation on mount
    const timer = setTimeout(() => setIsVisible(true), 10);
    return () => clearTimeout(timer);
  }, []);

  return (
    <div
      className={`transform transition-all duration-500 ease-out ${
        isVisible
          ? 'opacity-100 scale-100 translate-y-0'
          : 'opacity-0 scale-95 translate-y-4'
      }`}
    >
      <div className="bg-gradient-to-br from-card to-secondary/50 border border-accent/20 rounded-2xl p-8 backdrop-blur-sm shadow-2xl">
        <div className="flex items-center justify-center gap-4">
          {/* Animated dots */}
          <div className="flex gap-2">
            {[0, 1, 2].map((i) => (
              <div
                key={i}
                className="w-3 h-3 bg-white rounded-full animate-pulse"
                style={{
                  animationDelay: `${i * 0.15}s`,
                  animation: `pulse 1.5s cubic-bezier(0.4, 0, 0.6, 1) infinite`,
                }}
              />
            ))}
          </div>
          
          <div className="flex-1">
            <p className="text-foreground font-medium">Generating speech...</p>
            <p className="text-muted-foreground text-sm mt-1">
              Please wait while we process your text
            </p>
          </div>
        </div>

        {/* Animated waveform */}
        <div className="mt-6 flex items-end justify-center gap-1 h-12">
          {[...Array(20)].map((_, i) => (
            <div
              key={i}
              className="w-1 bg-white rounded-full"
              style={{
                height: `${Math.sin(i / 5) * 100 + 50}%`,
                animation: `waveform 1.5s ease-in-out infinite`,
                animationDelay: `${i * 0.05}s`,
              }}
            />
          ))}
        </div>
      </div>

      <style>{`
        @keyframes waveform {
          0%, 100% {
            height: 30%;
            opacity: 0.6;
          }
          50% {
            height: 100%;
            opacity: 1;
          }
        }
      `}</style>
    </div>
  );
}
