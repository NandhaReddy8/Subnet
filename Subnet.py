import ipaddress
import math

# Function to calculate the required subnet mask based on the number of hosts
def calculate_subnet_mask(hosts):
    return 32 - int(math.ceil(math.log2(hosts + 2)))  # Add 2 for network and broadcast address

# Function to calculate the number of available hosts in a subnet
def calculate_available_hosts(subnet_mask):
    return (2 ** (32 - subnet_mask)) - 2

# Function to create subnets with VLSM
def create_vlsm_subnets(ip_network, host_requirements):
    subnets = []
    ip_network = ipaddress.IPv4Network(ip_network)
    sorted_host_reqs = sorted(host_requirements, reverse=True)  # Sort by largest requirement first
    
    for hosts_needed in sorted_host_reqs:
        subnet_mask = calculate_subnet_mask(hosts_needed)
        new_subnet = list(ip_network.subnets(new_prefix=subnet_mask))[0]
        subnets.append((new_subnet, hosts_needed, calculate_available_hosts(subnet_mask)))
        ip_network = list(ip_network.subnets(new_prefix=subnet_mask))[1]  # Update network for next subnet

    return subnets

# Function to print subnet details
def print_subnet_details(subnets):
    for subnet, hosts_needed, available_hosts in subnets:
        print(f"Subnet: {subnet}")
        print(f"Required Hosts: {hosts_needed}, Available Hosts: {available_hosts}")
        print(f"Network Address: {subnet.network_address}, Broadcast Address: {subnet.broadcast_address}")
        print(f"Subnet Mask: {subnet.netmask}, Prefix Length: /{subnet.prefixlen}")
        print()

# Main program
def main():
    print("VLSM Subnetting Tool")
    ip_input = input("Enter the IP network (e.g., 192.168.1.0/24): ")
    num_subnets = int(input("Enter the number of subnets (up to 5): "))
    
    host_requirements = []
    for i in range(num_subnets):
        hosts = int(input(f"Enter the number of hosts required for subnet {i+1}: "))
        host_requirements.append(hosts)
    
    subnets = create_vlsm_subnets(ip_input, host_requirements)
    print_subnet_details(subnets)

if __name__ == "__main__":
    main()
