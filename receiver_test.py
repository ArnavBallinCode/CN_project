import socket

def test_receiver():
    """Simple receiver to test if data is being received"""
    RECEIVE_IP = "0.0.0.0"
    PORT = 5005
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(5.0)  # 5 second timeout
    
    try:
        sock.bind((RECEIVE_IP, PORT))
        print(f"✓ Listening on port {PORT}")
        print("Waiting for data (5 second timeout)...")
        
        packet_count = 0
        while packet_count < 10:  # Receive up to 10 packets
            try:
                data, addr = sock.recvfrom(1024)
                packet_count += 1
                print(f"✓ Received packet {packet_count} from {addr}: {len(data)} bytes")
                
                # If it's a test message, print it
                if len(data) < 50:
                    try:
                        message = data.decode()
                        print(f"  Message: {message}")
                    except:
                        print(f"  Binary data: {data[:20]}...")
                        
            except socket.timeout:
                print("✗ Timeout - no data received")
                break
                
    except Exception as e:
        print(f"✗ Receiver test failed: {e}")
    finally:
        sock.close()

if __name__ == "__main__":
    test_receiver()
