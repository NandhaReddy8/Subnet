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