import subprocess
import json
import sys

def get_health_status(deployment_id):
    try:
        result = subprocess.run(["kubectl", "get", "deployment", deployment_id, "-o", "json"], capture_output=True, check=True)
        deployment_status = json.loads(result.stdout)
        print(json.dumps(deployment_status, indent=4))
    except subprocess.CalledProcessError as e:
        print(f"Error retrieving health status: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: get-health-status <deplyoment-name>")
        sys.exit(1)
    get_health_status(sys.argv[1])

if __name__ == "__main__":
    main()