import json

def load_data():
    try:
        with open('data/task.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return []
    
def save_data(data):
    with open('data/task.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)