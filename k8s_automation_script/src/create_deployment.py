import subprocess
import yaml
import sys

def create_deployment(config_path):
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    
    try:
        subprocess.run(["kubectl", "apply", "-f", config['deployment']], check=True)
        subprocess.run(["kubectl", "apply", "-f", config['service']], check=True)
        subprocess.run(["kubectl", "apply", "-f", config['hpa']], check=True)
        print("Deployment created successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error creating deployment: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: create-deployment <config-path>")
        sys.exit(1)
    create_deployment(sys.argv[1])

if __name__ == "__main__":
    main()