import socket
import time

class HydraRecon:
    def __init__(self, target_range):
        self.target_range = target_range
        self.live_hosts = []

    def passive_scan(self):
        """
        Performs a low-noise TCP scan to identify open ports 
        without triggering standard IDS (Intrusion Detection) alerts.
        """
        print(f"[*] Hydra-Shadow: Initiating Recon on {self.target_range}...")
        common_ports = [80, 443, 22, 3389, 8080]
        
        for port in common_ports:
            # We use a tiny timeout to keep the scan 'snappy' and quiet
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.1)
            result = s.connect_ex((self.target_range, port))
            
            if result == 0:
                print(f"  [!] DISCOVERY: Port {port} is OPEN on {self.target_range}")
                self.live_hosts.append(port)
            s.close()
            # Adding 'Shadow Jitter' to avoid timing-based detection
            time.sleep(0.5)

if __name__ == "__main__":
    observer = HydraRecon("127.0.0.1")
    observer.passive_scan()
    print("[+] Recon Mission Complete. Intelligence cached.")
