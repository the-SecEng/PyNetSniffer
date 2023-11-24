import os
import platform
import json
from datetime import datetime

def scan_network(net, start, end):
    net1 = net.split('.')
    a = '.'

    net2 = net1[0] + a + net1[1] + a + net1[2] + a

    oper = platform.system()

    if oper == "Windows":
        ping1 = "ping -n 1 "
    elif oper == "Linux" or oper == "Darwin":  # Add 'Darwin' for macOS
        ping1 = "ping -c 1 "
    else:
        ping1 = "ping -c 1 "
    
    t1 = datetime.now()
    print("Scanning in Progress:")

    scan_results = []

    for ip in range(start, end + 1):
        addr = net2 + str(ip)
        comm = ping1 + addr
        response = os.popen(comm)

        for line in response.readlines():
            if line.count("TTL"):
                break
            if line.count("TTL"):
                print(addr, "--> Live")
                scan_results.append({"ip": addr, "status": "Live"})

    t2 = datetime.now()
    total = t2 - t1
    print("Scanning completed in: ", total)

    return scan_results

if __name__ == "__main__":
    net_address = input("Enter the Network Address: ")
    start_number = int(input("Enter the Starting Number: "))
    last_number = int(input("Enter the Last Number: "))
    
    scan_results = scan_network(net_address, start_number, last_number)

    # Save scan results to JSON file
    output_file = 'scan_report.json'
    with open(output_file, 'w') as json_file:
        json.dump(scan_results, json_file, indent=4)

    print(f"Scan results saved to {output_file}")
