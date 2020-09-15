import json


person = { 
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "sky diving", "singing"]
}

file_hobbie = open("hobbies.json", "w")
json.dump(person, file_hobbie)
file_hobbie.close()
