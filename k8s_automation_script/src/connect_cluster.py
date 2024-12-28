import subprocess
import sys

def connect_to_cluster(kubeconfig_path):
    try:
        subprocess.run(["kubectl", "config", "use-context", kubeconfig_path], check=True)
        print("Connected to Kubernetes cluster.")
    except subprocess.CalledProcessError as e:
        print(f"Error connecting to cluster: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: connect-cluster <kubeconfig-path>")
        sys.exit(1)
    connect_to_cluster(sys.argv[1])

if __name__ == "__main__":
    main()