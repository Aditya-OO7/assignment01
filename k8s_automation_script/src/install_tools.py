import subprocess
import shutil
import os

def install_helm():
    helm_path = shutil.which("helm")
    if helm_path is None or not os.access(helm_path, os.X_OK):
        print("Helm is not installed or not executable. Installing Helm...")
        subprocess.run(["curl", "-fsSL", "https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3", "-o", "get_helm.sh"], check=True)
        subprocess.run(["chmod", "+x", "get_helm.sh"], check=True)
        subprocess.run(["./get_helm.sh"], check=True)
        print("Helm installed successfully.")
    else:
        print("Helm is already installed.")

def install_keda():
    try:
        subprocess.run(["helm", "repo", "add", "kedacore", "https://kedacore.github.io/charts"], check=True)
        subprocess.run(["helm", "repo", "update"], check=True)
        subprocess.run(["helm", "install", "keda", "kedacore/keda"], check=True)
        print("KEDA installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing KEDA: {e}")