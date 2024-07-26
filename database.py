
import json

class Database:
    @staticmethod
    def save_data(file_name, data):
        with open(file_name, 'w') as f:
            json.dump(data, f)

    @staticmethod
    def load_data(file_name):
        try:
            with open(file_name, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []
