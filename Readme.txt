How the Script Works:
Input Parameters:

The script first prompts the user to enter the base network address (e.g., 192.168.1.0/24).
The user specifies how many subnets they need (up to 5).
Then, the user is prompted to input the number of hosts required for each subnet.
VLSM Calculation:

The script calculates the subnet mask for each subnet based on the number of required hosts.
It sorts the host requirements in descending order to allocate larger subnets first, ensuring proper allocation of IPs using VLSM.
Output:

The script prints the calculated subnets, including:
Subnet address
Required hosts vs. available hosts
Network and broadcast addresses
Subnet mask and prefix length

eg: 
Enter the IP network (e.g., 192.168.1.0/24): 172.21.42.0/24
Enter the number of subnets (up to 5): 4
Enter the number of hosts required for subnet 1: 10
Enter the number of hosts required for subnet 2: 57
Enter the number of hosts required for subnet 3: 26
Enter the number of hosts required for subnet 4: 117

answer:-
Subnet: 172.21.42.0/25
Required Hosts: 117, Available Hosts: 126
Network Address: 172.21.42.0, Broadcast Address: 172.21.42.127
Subnet Mask: 255.255.255.128, Prefix Length: /25

Subnet: 172.21.42.128/26
Required Hosts: 57, Available Hosts: 62
Network Address: 172.21.42.128, Broadcast Address: 172.21.42.191
Subnet Mask: 255.255.255.192, Prefix Length: /26

Subnet: 172.21.42.192/27
Required Hosts: 26, Available Hosts: 30
Network Address: 172.21.42.192, Broadcast Address: 172.21.42.223
Subnet Mask: 255.255.255.224, Prefix Length: /27

Subnet: 172.21.42.224/28
Required Hosts: 10, Available Hosts: 14
Network Address: 172.21.42.224, Broadcast Address: 172.21.42.239
Subnet Mask: 255.255.255.240, Prefix Length: /28


Key Points:
This code is designed for educational purposes and uses VLSM to efficiently allocate IP addresses based on the host requirements.
It automatically handles subnet calculations, ensuring no overlap between subnets.
