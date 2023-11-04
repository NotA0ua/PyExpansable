import json, datetime

# TODO: Make groups and date
class DB:
    def __init__(self, path="", file_name="db.json", indent=4):
        self.path = path + file_name
        self.indent = indent

        try:
            self.read()
        except FileNotFoundError:
            self.clear()

    def write(self, data: dict):
        with open(self.path, "w") as f:
            json.dump(data, f, indent=self.indent)

    def read(self):
        with open(self.path, "r") as f:
            return json.load(f)

    def add(self, key: str, value):
        file = self.read()
        file[key] = value
        self.write(file)

    def clear(self):
        self.write({})
