import json, datetime

class DB:
    def __init__(self, path="", file_name="db.json", indent=2):
        self.path = path + file_name
        self.indent = indent

        try:
            self.read()
        except:
            self.clear()

    def write(self, data: dict):
        with open(self.path, "w") as f:
            json.dump(data, f, indent=self.indent)

    def read(self):
        with open(self.path, "r") as f:
            return json.load(f)

    def add(self, key: str, value, group="default"):
        file = self.read()

        today = str(datetime.date.today())
        file[group] = {}
        file[group][today] = {}

        file[group][today][key] = value
        self.write(file)

    def clear(self):
        self.write({})


db = DB()
db.add("banana", 50)
db.add("banana", 20, "market")
