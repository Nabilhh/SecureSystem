import os

class IntrusionDetectionSystem:
    def __init__(self, config_file):
        self.config_file = config_file

    def start(self):
        os.system(f"snort -c {self.config_file} -A console")
