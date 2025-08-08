import socket
import sounddevice as sd
import numpy as np

RECEIVER_IP = "10.0.1.217"  # IP of the Windows machine
PORT = 5005
CHUNK = 1024
RATE = 44100

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def callback(indata, frames, time, status):
    audio = indata.astype(np.int16).tobytes()
    sock.sendto(audio, (RECEIVER_IP, PORT))

print(f"[+] Streaming audio to {RECEIVER_IP}:{PORT}")
with sd.InputStream(samplerate=RATE, channels=1, dtype='int16', callback=callback):
    input("Press Enter to stop streaming...\n")
