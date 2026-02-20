'use client';

import { useEffect, useRef, useState } from 'react';
import { Play, Pause, Volume2, X, Download } from 'lucide-react';
import { Button } from '@/components/ui/button';

interface AudioPlayerProps {
  audioUrl: string;
  onClear: () => void;
}

export default function AudioPlayer({ audioUrl, onClear }: AudioPlayerProps) {
  const audioRef = useRef<HTMLAudioElement>(null);
  const [isPlaying, setIsPlaying] = useState(false);
  const [currentTime, setCurrentTime] = useState(0);
  const [duration, setDuration] = useState(0);
  const [isVisible, setIsVisible] = useState(false);

  useEffect(() => {
    // Trigger animation on mount
    const timer = setTimeout(() => setIsVisible(true), 10);
    return () => clearTimeout(timer);
  }, []);

  const handlePlayPause = () => {
    if (audioRef.current) {
      if (isPlaying) {
        audioRef.current.pause();
      } else {
        audioRef.current.play();
      }
      setIsPlaying(!isPlaying);
    }
  };

  const handleTimeUpdate = () => {
    if (audioRef.current) {
      setCurrentTime(audioRef.current.currentTime);
    }
  };

  const handleLoadedMetadata = () => {
    if (audioRef.current) {
      setDuration(audioRef.current.duration);
    }
  };

  const handleProgressClick = (e: React.MouseEvent<HTMLDivElement>) => {
    if (audioRef.current && duration) {
      const rect = e.currentTarget.getBoundingClientRect();
      const percent = (e.clientX - rect.left) / rect.width;
      audioRef.current.currentTime = percent * duration;
    }
  };

  const handleEnded = () => {
    setIsPlaying(false);
  };

  const downloadAudio = () => {
    const a = document.createElement('a');
    a.href = audioUrl;
    a.download = 'speech.mp3';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
  };

  const formatTime = (time: number) => {
    if (isNaN(time)) return '0:00';
    const minutes = Math.floor(time / 60);
    const seconds = Math.floor(time % 60);
    return `${minutes}:${seconds.toString().padStart(2, '0')}`;
  };

  return (
    <div
      className={`transform transition-all duration-500 ease-out ${
        isVisible
          ? 'opacity-100 scale-100 translate-y-0'
          : 'opacity-0 scale-95 translate-y-4'
      }`}
    >
      <audio
        ref={audioRef}
        src={audioUrl}
        onTimeUpdate={handleTimeUpdate}
        onLoadedMetadata={handleLoadedMetadata}
        onEnded={handleEnded}
      />

      <div className="bg-gradient-to-br from-card to-secondary/50 border-2 border-black rounded-2xl p-6 shadow-2xl">
        <div className="flex items-center justify-between mb-4">
          <div className="flex items-center gap-3">
            <div className="p-2 bg-accent/20 rounded-lg">
              <Volume2 size={20} className="text-white" />
            </div>
            <h3 className="text-foreground font-semibold">Audio Generated</h3>
          </div>
          <Button
            onClick={onClear}
            variant="ghost"
            size="sm"
            className="rounded-full p-2 h-8 w-8 hover:bg-border"
          >
            <X size={16} />
          </Button>
        </div>

        {/* Play/Pause Button */}
        <div className="flex items-center gap-4 mb-4">
          <Button
            onClick={handlePlayPause}
            className="rounded-full p-3 h-12 w-12 bg-white hover:bg-white/90 text-black border-2 border-black flex items-center justify-center transition-all duration-200 shadow-lg hover:shadow-xl"
          >
            {isPlaying ? <Pause size={24} /> : <Play size={24} />}
          </Button>

          {/* Progress bar */}
          <div className="flex-1 flex items-center gap-3">
            <span className="text-xs text-muted-foreground min-w-10">
              {formatTime(currentTime)}
            </span>
            <div
              onClick={handleProgressClick}
              className="flex-1 h-2 bg-border rounded-full cursor-pointer group relative"
            >
              <div
                className="h-full bg-white rounded-full transition-all duration-100"
                style={{ width: `${duration ? (currentTime / duration) * 100 : 0}%` }}
              />
              <div
                className="absolute top-1/2 w-4 h-4 bg-white rounded-full transform -translate-y-1/2 opacity-0 group-hover:opacity-100 transition-opacity shadow-md"
                style={{ left: `${duration ? (currentTime / duration) * 100 : 0}%` }}
              />
            </div>
            <span className="text-xs text-muted-foreground min-w-10 text-right">
              {formatTime(duration)}
            </span>
          </div>
        </div>

        {/* Download Button */}
        <Button
          onClick={downloadAudio}
          className="w-full bg-white hover:bg-white/80 text-black rounded-lg py-2 transition-all duration-200 flex items-center justify-center gap-2 font-semibold shadow-lg hover:shadow-xl"
        >
          <Download size={18} />
          Download Audio
        </Button>
      </div>
    </div>
  );
}
