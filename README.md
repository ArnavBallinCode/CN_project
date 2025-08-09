# Real-Time Voice Streaming over UDP

This project demonstrates real-time audio streaming from one computer (sender) to another (receiver) over a local network using Python, UDP sockets, and the sounddevice library.

## How It Works

### 1. Sender (`voice_sender.py`)
- Captures audio from the microphone in small chunks (frames) using the sounddevice library.
- Each chunk is converted to bytes and sent as a UDP packet to the receiver's IP address and port.
- Uses UDP for low-latency, real-time transmission (no retransmission, no ordering, no connection setup).

### 2. Receiver (`voice_receiver.py`)
- Listens for incoming UDP packets on a specified port (default: 5005) on all network interfaces.
- For each received packet, the audio data is extracted and played immediately using the sounddevice library.
- If no packet is received within a short timeout, silence is played to avoid audio glitches.

## Network Details
- **Addressing:**
  - The sender targets the receiver's IP address (e.g., `10.0.1.217`).
  - The receiver binds to `0.0.0.0`, meaning it listens on all available network interfaces.
- **Port:**
  - Both sender and receiver use the same UDP port (default: 5005).
- **Protocol:**
  - UDP (User Datagram Protocol) is used for fast, connectionless communication.
  - No guarantee of delivery, order, or duplication protection (ideal for real-time audio).

## Audio Details
- **Sample Rate:** 44100 Hz (CD quality)
- **Channels:** Mono (1 channel)
- **Chunk Size:** 1024 samples per packet
- **Format:** 16-bit signed integers (`int16`)

## How to Run
1. **On the receiver (Windows):**
   - Run `python voice_receiver.py`.
2. **On the sender (Mac):**
   - Set the correct `RECEIVER_IP` in `voice_sender.py` to the receiver's IP.
   - Run `python voice_sender.py`.

## What Happens Internally
- The sender continuously captures and sends audio packets to the receiver.
- The receiver's callback function fetches each UDP packet, converts it to audio, and plays it in real time.
- If a packet is lost or delayed, the receiver fills the gap with silence (no blocking or waiting).
- This setup is unicast (one-to-one), connectionless, and optimized for low-latency streaming.

## Requirements
- Python 3.x
- `sounddevice` and `numpy` libraries (install via `pip install sounddevice numpy`)
- Both devices must be on the same local network and have UDP port 5005 open (check firewall settings).

---

This project is a simple example of real-time audio streaming and can be extended for more advanced use cases (e.g., multi-user, encryption, error correction, etc.).
