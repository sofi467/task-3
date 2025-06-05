import json
import os


class ConfigReader:
    def __init__(self, config_file='config.json'):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.config_path = os.path.join(base_dir, config_file)
        self.config_data = self.load_config()

    def load_config(self):
        if not os.path.isfile(self.config_path):
            raise FileNotFoundError(f"Config file not found: {self.config_path}")
        with open(self.config_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def get_value(self, key):
        return self.config_data.get(key)
