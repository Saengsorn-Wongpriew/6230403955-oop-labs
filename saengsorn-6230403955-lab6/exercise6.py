import json


file_json = open("hobbies.json", "r")
json_in = json.load(file_json)
file_json.close()
name = json_in["firstName"]
hobby = json_in["hobbies"]
hobby = ", ".join(hobby)
print(name, "has hobbies as", hobby)