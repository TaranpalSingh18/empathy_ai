#!/usr/bin/env python
"""Test script for recalibrated pipeline"""
import sys
sys.path.insert(0, r'd:\darwix\empathy_engine')

from pipeline import run_pipeline

# Test with mixed emotions
test_text = "Everyone congratulated me on my presentation. They said I looked confident and sharp. I nodded and thanked them, but inside I kept replaying the one slide where I stumbled. I don’t know why I can’t just feel proud."

print("Testing pipeline with recalibrated voice parameters...")
print("=" * 60)

result = run_pipeline(test_text)

print("\n=== EMOTION ANALYSIS ===")
print(f"Dominant Emotion: {result['dominant_emotion']}")
print(f"Weighted Emotion: {result['weighted_emotion']}")
print(f"Volatility: {result['volatility_score']:.2f}")
print(f"Valence Score: {result['valence_score']:.2f}")
print(f"Base Pitch Adjustment: {result['base_pitch']:.2f} semitones")

print(f"\n=== OUTPUT AUDIO ===")
print(f"Path: {result['output_audio_path']}")

print(f"\n=== PER-SENTENCE ANALYSIS ===")
for i, sent in enumerate(result['timeline'], 1):
    sentence_text = sent.get('sentence', 'N/A')[:70]
    emotions = sent.get('emotions', [])
    print(f"\nSentence {i}: {sentence_text}...")
    if emotions:
        top_emotion = emotions[0]
        print(f"  Emotion: {top_emotion['label']}")
        print(f"  Confidence: {top_emotion['confidence']:.2%}")
        print(f"  Intensity: {top_emotion['intensity']}")
    voice = sent.get('voice_params', {})
    if voice:
        print(f"  Voice Params: Speed={voice['speed']:.2f}x, Pitch={voice['pitch_semitones']:+d} semitones, Volume={voice['volume_db']:+.1f} dB")
    else:
        print(f"  Voice Params: (not yet applied)")

print("\n" + "=" * 60)
print("✓ Pipeline completed successfully!")
print(f"  Audio file size: {__import__('os').path.getsize(result['output_audio_path']) / 1024:.1f} KB")
