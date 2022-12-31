import json

user = {"id": "yohan", "password": 1234, "hobby": ["drawing", "coding"]}

with open("user.json", "w", encoding="utf-8") as file:
    json_data = json.dump(user, file, indent=4)
