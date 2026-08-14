# public address ranges
# 0-126, 128-191, 192-223, 224-239, 240-255
# 127 is used for troubleshooting, so we dont consider it in this one.

ip_address = input("Enter a valid public IP address (Format: XXX.XXX.XXX.XXX): ")

ip_address_first_octet = int(ip_address.split(".")[0])

if ip_address_first_octet == 127:
    print("127 is a loopback address; used for troubleshooting, not a valid IP.")
elif ip_address_first_octet >= 0 and ip_address_first_octet <= 126:
    print("Your IP address belongs to Class A.")
    print("Default Subnet Mask: 255.0.0.0")
    print("No. of hosts: 2^24 - 2 = 16,777,214")
    print("No. of networks: 2^7 - 2 = 126")
    print("Network Range: 0.0.0.0 to 126.0.0.0")
    print("You subtract 2 from the no. of hosts be cause you remove the following 2: Broadcast and Host address.\n")
elif ip_address_first_octet >= 128 and ip_address_first_octet <= 191:
    print("Your IP address belongs to Class B.")
    print("Default Subnet Mask: 255.255.0.0")
    print("No. of hosts: 2^16 - 2 = 65,534")
    print("No. of networks: 2^14 = 16,384")
    print("Network Range: 128.0.0.0 to 191.255.0.0")
    print("You subtract 2 from the no. of hosts be cause you remove the following 2: Broadcast and Host address.\n")
elif ip_address_first_octet >= 192 and ip_address_first_octet <= 223:
    print("Your IP address belongs to Class C.")
    print("Default Subnet Mask: 255.255.255.0")
    print("No. of hosts: 2^8 - 2 = 254")
    print("No. of networks: 2^21 = 2,097,152")
    print("Network Range: 192.0.0.0 to 223.255.255.0")
    print("You subtract 2 from the no. of hosts be cause you remove the following 2: Broadcast and Host address.\n")
elif ip_address_first_octet >= 224 and ip_address_first_octet <= 239:
    print("Your IP address belongs to Class D.")
    print("No default subnet mask, Multicast group")
    print("No. of hosts: N/A")
    print("No. of networks: N/A")
    print("Network Range: 224.0.0.0 to 239.255.255.255")
elif ip_address_first_octet >= 240 and ip_address_first_octet <= 255:
    print("Your IP address belongs to Class E.")
    print("No default subnet mask")
    print("No. of hosts: N/A")
    print("No. of networks: N/A")
    print("Network Range: 240.0.0.0 to 255.255.255.255")
else:
    print("Your IP is invalid, enter again")