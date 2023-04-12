import json
def ConfigLoad():
    data = {}
    try:         
        with open("config.json", "r") as read_it:
            data = json.load(read_it)
    except:
        return -1
    return data
        
def ConfigWrite(data):
    try:
        with open("config.json", "w") as p:
            json.dump(data, p)
        return 1
    except:
        return -1
        
data = {"user":{"username": None, "first": None, "last": None}}

ConfigWrite(data)
data = ConfigLoad()
print(data)