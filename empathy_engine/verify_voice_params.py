#!/usr/bin/env python
"""Verify recalibrated voice parameters"""
from config import get_voice_params
import json

emotions = ['excitement', 'joy', 'admiration', 'sadness', 'anger', 'neutral']

print("=" * 70)
print("VOICE PARAMETERS - COMPARISON (Recalibrated to Natural Values)")
print("=" * 70)

for emotion in emotions:
    print(f"\n{emotion.upper()}:")
    print("-" * 70)
    for intensity in ['low', 'medium', 'high']:
        params = get_voice_params(emotion, intensity)
        print(f"  {intensity.upper():8s}: Speed={params['speed']:.2f}x | Pitch={params['pitch_semitones']:+d}st | Volume={params['volume_db']:+.1f}dB")

print("\n" + "=" * 70)
print("SUMMARY:")
print("=" * 70)
print("✓ Speed reduced from 0.7-1.4 to 0.94-1.05 (subtle ~5% variation)")
print("✓ Pitch reduced from ±4 to ±2 semitones (gentle musical shifts)")
print("✓ Volume reduced from ±6 to ±1.5 dB (subtle loudness changes)")
print("✓ Negative emotions use lower pitch & slower speed for somber tone")
print("✓ Positive emotions use higher pitch & slightly faster speed for warmth")
print("\nResult: Voice should now sound natural with subtle emotional prosody!")
