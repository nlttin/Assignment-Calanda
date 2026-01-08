import time
import subprocess
from prometheus_client import start_http_server, Gauge

# Configuration
TARGET_IP = "10.0.1.5"  # Private IP of the Target Server
PORT = 8000

# Define Prometheus Metric
LATENCY_METRIC = Gauge('network_latency_ms', 'Network latency to the target server in milliseconds')

def get_latency(ip):
    """Measures ICMP latency using the system ping command."""
    try:
        # Run ping command: -c 1 (1 packet), -W 1 (1 second timeout)
        output = subprocess.check_output(
            ["ping", "-c", "1", "-W", "1", ip], 
            universal_newlines=True
        )
        # Parse the 'time=' value from the output
        latency = output.split("time=")[1].split(" ms")[0]
        return float(latency)
    except Exception as e:
        print(f"Error measuring latency: {e}")
        return -1.0

if __name__ == '__main__':
    # Start Prometheus HTTP server
    start_http_server(PORT)
    print(f"Latency app started on port {PORT}. Monitoring {TARGET_IP}...")
    
    while True:
        ms = get_latency(TARGET_IP)
        if ms != -1.0:
            LATENCY_METRIC.set(ms)
            print(f"Current Latency: {ms}ms")
        time.sleep(5) # Measure every 5 seconds