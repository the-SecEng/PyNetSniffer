# PyNetSniffer

PyNetSniffer is a simple Python script designed to scan a range of IP addresses within a specified network to identify live hosts. The script uses the ping command to check the reachability of each IP address and records the results in a JSON file.
Usage

    Run the script by executing the Python file.
    Enter the network address, starting number, and last number when prompted.

Requirements

    Python 3
    Compatible with Windows, Linux, and macOS.

How It Works

The script utilizes the ping command to check the status of each IP address within the specified range. The results are then displayed in the console and saved to a JSON file named scan_report.json.
File Description

    PyNetSniffer.py: The main Python script.
    scan_report.json: JSON file containing the scan results.

Running the Script

    Open a terminal or command prompt.
    Navigate to the directory containing the script.
    Run the script by executing the command: python PyNetSniffer.py.
    Enter the required network information as prompted.

Output

The script will display live hosts in the console and save the scan results to a JSON file (scan_report.json) in the script's directory.
Notes

    The script uses the ping command differently based on the operating system (Windows, Linux, or macOS).
    The scan results include the IP address and its status (Live).
    The JSON file is formatted with an indentation of 4 spaces for better readability.

Feel free to use and modify this script as needed. If you encounter any issues or have suggestions for improvements, please let me know!