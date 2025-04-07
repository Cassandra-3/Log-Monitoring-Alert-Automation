#Bash script to move logs to a shared folder
  GNU nano 6.2                                          collectlogs.sh                                                    
#!/bin/bash
# Define variables
LOG_DIR="/var/log/apache2"
ACCESS_LOG="$LOG_DIR/access.log"
SHARED_FOLDER="/media/sf_Shared"  # Path to the shared folder

# Copy logs to the shared folder
cp $ACCESS_LOG $SHARED_FOLDER/access.log
