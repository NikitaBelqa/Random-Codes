import json
user = {"name": "Bob",
        "age": 19,
        "job": "Programmer",
        "is_active": True}

json_user_info = json.dumps(user, indent=3, ensure_ascii=False) #Запись строки в json формате
print(json_user_info)

json_to_string = json.loads(json_user_info) #Чтение строки json формата
print(json_to_string)


with open("profile.json", "w") as file:
    json.dump(user, file, indent=3, ensure_ascii=False) #Создали json файл в режиме записи и записали туда информацию о пользователе

with open("profile.json", "r") as file:
    data = json.load(file)
print(data)
