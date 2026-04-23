import socket

print("=== BANNER GRABBING_03 ===")
target = input("Enter target Ip: ")

print("Scanning Ports 1 to 100 and Interrogation ... ")
print("---------------------------")

for port in range(1, 101):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)           # Increasing time 
    result = s.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} is OPEN! ")
        
        try:
            banner = s.recv(1024)            # Listen to reply of Port
            if not banner and port == 80:
                s.send(b"GET / HTTP/1.0\r\n\r\n")
                banner = s.recv(1024)

            if banner:
                 print(f" → Banner: {banner.decode('utf-8', errors='ignore').strip()}")    # Using ignore to avoide error
            else:
                 print(f" → Banner: Port is Open but No reply! ...")  
        except socket.timeout:
            print(f" → Banner: Timeout ... ")   
        except Exception as e:
            print(f" → Banner: Error... {e}")
    
        print("-----------------------")
    s.close()
print("Scan and Interrogation COMPLETED! ")