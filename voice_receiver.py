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

def callback(indata, frames, time, status):
    pass  # Needed by sounddevice, no-op here

with sd.OutputStream(samplerate=RATE, channels=1, dtype='int16'):
    while True:
        try:
            data, addr = sock.recvfrom(CHUNK * 2)
            audio = np.frombuffer(data, dtype=np.int16)
            sd.play(audio, samplerate=RATE)
        except Exception as e:
            print(f"[-] Error: {e}")
            break
