#!/bin/bash
# Update and install dependencies
sudo apt-get update
sudo apt-get install -y python3-pip

# Install Python libraries
pip3 install prometheus_client

# Create the application file
cat <<EOF > /home/azureuser/latency_app.py
# (Paste the Python code from step 1 here)
EOF

# Run the application in the background
nohup python3 /home/azureuser/latency_app.py > /home/azureuser/app.log 2>&1 &