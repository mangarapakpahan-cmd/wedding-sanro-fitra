import wave
import math
import struct
import os

audio_path = r"C:\Users\manga\.gemini\antigravity\scratch\wedding-sanro-fitra\assets\audio\wedding-song.mp3"
# Note: browsers can play .wav data even with .mp3 extension or we can make a proper wav
audio_wav_path = r"C:\Users\manga\.gemini\antigravity\scratch\wedding-sanro-fitra\assets\audio\wedding-song.wav"

sample_rate = 22050
duration = 16.0 # 16 seconds loop
num_samples = int(sample_rate * duration)

# Gentle romantic chords (Canon-like progression in D/G):
# G - D - Em - Bm - C - G - C - D
notes_freq = {
    'G3': 196.00, 'B3': 246.94, 'D4': 293.66,
    'F#4': 369.99, 'A4': 440.00,
    'E4': 329.63, 'G4': 392.00,
    'C4': 261.63, 'E3': 164.81, 'C3': 130.81, 'D3': 146.83
}

# Arpeggio pattern over 8 bars (2 sec per bar)
chords = [
    [196.00, 246.94, 293.66, 392.00], # G
    [146.83, 220.00, 293.66, 369.99], # D
    [164.81, 196.00, 246.94, 329.63], # Em
    [123.47, 185.00, 220.00, 293.66], # Bm
    [130.81, 196.00, 261.63, 329.63], # C
    [196.00, 246.94, 293.66, 392.00], # G
    [130.81, 164.81, 196.00, 261.63], # C
    [146.83, 220.00, 293.66, 369.99], # D
]

samples = [0.0] * num_samples

bar_duration = 2.0
note_duration = bar_duration / 4.0 # 4 arpeggio notes per chord

for bar_idx, chord in enumerate(chords):
    bar_start_time = bar_idx * bar_duration
    for note_idx, freq in enumerate(chord):
        start_time = bar_start_time + note_idx * note_duration
        start_sample = int(start_time * sample_rate)
        # Play each note with piano-like exponential decay and soft harmonics
        decay_time = 1.8
        note_samples_count = int(decay_time * sample_rate)
        
        for i in range(note_samples_count):
            curr_idx = start_sample + i
            if curr_idx >= num_samples:
                break
            t = i / sample_rate
            # Envelope: fast attack, exponential decay
            attack = min(1.0, t * 50)
            envelope = attack * math.exp(-t * 2.2)
            
            # Fundamental + soft harmonics for warm acoustic timbre
            val = (math.sin(2 * math.pi * freq * t) * 0.6 +
                   math.sin(2 * math.pi * freq * 2 * t) * 0.25 +
                   math.sin(2 * math.pi * freq * 3 * t) * 0.1) * envelope
            
            samples[curr_idx] += val

# Normalize and convert to 16-bit PCM
max_val = max(abs(s) for s in samples) or 1.0
scale = 32767 * 0.75 / max_val

for target in [audio_wav_path, audio_path]:
    with wave.open(target, 'w') as wav_file:
        wav_file.setnchannels(1) # mono
        wav_file.setsampwidth(2) # 16-bit
        wav_file.setframerate(sample_rate)
        
        packed_data = bytearray()
        for s in samples:
            val = int(s * scale)
            packed_data.extend(struct.pack('<h', max(-32768, min(32767, val))))
            
        wav_file.writeframes(packed_data)

print(f"Generated wedding ambient audio: {audio_wav_path} and {audio_path}")
