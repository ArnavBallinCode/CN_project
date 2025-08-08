import socket
import time

def test_connection():
    """Test if we can reach the receiver"""
    RECEIVER_IP = "10.0.1.217"
    PORT = 5005
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    print(f"Testing connection to {RECEIVER_IP}:{PORT}")
    
    try:
        # Send a test message
        test_message = b"TEST_MESSAGE"
        sock.sendto(test_message, (RECEIVER_IP, PORT))
        print("✓ Test message sent successfully")
        
        # Try to send multiple test packets
        for i in range(5):
            sock.sendto(f"Test packet {i}".encode(), (RECEIVER_IP, PORT))
            time.sleep(0.1)
        
        print("✓ Multiple test packets sent")
        
    except Exception as e:
        print(f"✗ Connection test failed: {e}")
    finally:
        sock.close()

if __name__ == "__main__":
    test_connection()
