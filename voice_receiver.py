import socket
import sounddevice as sd
import numpy as np

RECEIVE_IP = "0.0.0.0"  # Listen on all interfaces
PORT = 5005
CHUNK = 1024
RATE = 44100

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((RECEIVE_IP, PORT))

print(f"[+] Listening for audio on port {PORT}...")

def callback(outdata, frames, time, status):
    try:
        data, addr = sock.recvfrom(CHUNK * 2)
        audio = np.frombuffer(data, dtype=np.int16)
        # Ensure we have the right amount of frames
        if len(audio) == frames:
            outdata[:] = audio.reshape(-1, 1)
        else:
            # Pad or truncate to match expected frames
            if len(audio) < frames:
                padded = np.zeros(frames, dtype=np.int16)
                padded[:len(audio)] = audio
                outdata[:] = padded.reshape(-1, 1)
            else:
                outdata[:] = audio[:frames].reshape(-1, 1)
    except socket.timeout:
        # Fill with silence if no data received
        outdata.fill(0)
    except Exception as e:
        print(f"[-] Error in callback: {e}")
        outdata.fill(0)

# Set socket timeout to prevent blocking
sock.settimeout(0.1)

print("Starting audio output stream...")
with sd.OutputStream(samplerate=RATE, channels=1, dtype='int16', callback=callback, blocksize=CHUNK):
    print("Audio stream active. Press Ctrl+C to stop...")
    try:
        while True:
            sd.sleep(1000)  # Keep the stream alive
    except KeyboardInterrupt:
        print("\n[+] Stopping audio receiver...")
    except Exception as e:
        print(f"[-] Error: {e}")
