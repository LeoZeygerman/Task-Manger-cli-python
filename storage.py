import json

def load_data():
    try:
        with open('task.json', 'r') as f:
            return json.load(f)
    except:
        return []
    
def save_data(data):
    with open('task.json', 'r') as f:
        json.dump(data, f)