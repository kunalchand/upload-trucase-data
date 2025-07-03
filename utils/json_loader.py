import json
import os


class JsonLoader:
    @staticmethod
    def load_json(file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        with open(file_path, "r") as file:
            return json.load(file)
