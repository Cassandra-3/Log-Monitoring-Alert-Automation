#Python script to parse logs and alert

import re
from pathlib import Path
shared_folder = r"Z:"  # Path to shared folder		# Shared folder path and log file
log_file = Path(shared_folder) / "access.log"
# Known IPs
known_ips = {"127.0.0.1", "10.0.2.6"}
if not log_file.exists():			# Check if the log file exists
    print("Log file not found!")
else:
    failed_requests = []
    unknown_ips = []
    with log_file.open() as logs:	    # Parse the log file
        for line in logs:
            # Check for HTTP errors 400 or 500
            if " 404 " in line or " 500 " in line:
                failed_requests.append(line.strip())
            elif (ip := re.match(r"^(\d+\.\d+\.\d+\.\d+)", line)):		# Check for unknown IPs
                if ip.group(1) not in known_ips:
                    unknown_ips.append(line.strip())   
    if failed_requests: 				# Display alerts for failed requests
        print("\n[ALERT] Failed or Error Requests (404 or 500):")    
    if unknown_ips:				# Display alerts for unknown IP access
        print("\n[ALERT] Unknown IP Access Detected:")
