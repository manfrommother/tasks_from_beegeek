import json

def is_correct_json(string):
    try:
        result = json.loads(string)
        return True
    except:
        return False