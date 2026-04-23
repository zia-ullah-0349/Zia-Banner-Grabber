import socket

print("=== BANNER GRABBING_02 ===")
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
            banner = s.recv(1024)            # Listen to reply of Port
            if not banner and port == 80:
                s.send(b"GET / HTTP/1.0\r\n\r\n")
                banner = s.recv(1024)

            if banner:
                 print(f" → Banner: {banner.decode().strip()}")
            else:
                 print(f" → Banner: Port is Open but No reply! ...")  
        except:
            print(f" → Banner: Timeout ... ")   
        print("-----------------------")
    s.close()
print("Scan and Interrogation COMPLETED! ")