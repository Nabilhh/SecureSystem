import subprocess

class PatchManagement:
    def __init__(self):
        pass

    def check_for_updates(self):
        result = subprocess.run(["apt-get", "-s", "upgrade"], capture_output=True, text=True)
        return result.stdout

    def apply_patches(self):
        subprocess.run(["apt-get", "upgrade", "-y"])
