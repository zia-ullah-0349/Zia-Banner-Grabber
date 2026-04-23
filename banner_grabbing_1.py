import socket

print("=== BANNER GRABBING_01 ===")
target = input("Enter target Ip: ")

print("Scanning Ports 1 to 100 and Interrogation ... ")
print("---------------------------")

for port in range(1, 101):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} is OPEN! ")
        
        try:
            s.send(b"Hello\r\n")               # Send message to open port
            banner = s.recv(1024)              # Leasten to reply of Port
            print(f" → Banner: {banner.decode().strip()}")
        except:
            print(f" → Banner: Port is Open but No reply! ...")   
        print("-----------------------")
    s.close()
print("Scan and Interrogation COMPLETED! ")