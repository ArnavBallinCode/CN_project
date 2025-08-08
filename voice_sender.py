import socket
import sounddevice as sd
import numpy as np
import time

RECEIVER_IP = "10.0.1.217"  # IP of the Windows machine
PORT = 5005
CHUNK = 1024
RATE = 44100

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Counter for debugging
packet_count = 0

def callback(indata, frames, time, status):
    global packet_count
    if status:
        print(f"Input overflow: {status}")
    
    # Convert to int16 and send
    audio = (indata * 32767).astype(np.int16).tobytes()
    try:
        sock.sendto(audio, (RECEIVER_IP, PORT))
        packet_count += 1
        if packet_count % 100 == 0:
            print(f"Sent {packet_count} packets")
    except Exception as e:
        print(f"Error sending audio: {e}")

print(f"[+] Streaming audio to {RECEIVER_IP}:{PORT}")
print(f"[+] Audio format: {RATE}Hz, 1 channel, int16")
print(f"[+] Chunk size: {CHUNK} samples")

try:
    with sd.InputStream(samplerate=RATE, channels=1, dtype='float32', 
                       callback=callback, blocksize=CHUNK):
        input("Press Enter to stop streaming...\n")
except KeyboardInterrupt:
    print("\n[+] Stopping audio sender...")
except Exception as e:
    print(f"[-] Error: {e}")
finally:
    sock.close()
    print(f"[+] Total packets sent: {packet_count}")
