import json


def save_to_file(file_path, data):
    with open(file_path, 'w') as f:
        f.writelines(json.dumps(data))


def load_agents(file_path):
    with open(file_path, 'r') as f:
        agents = json.loads(f.read())
    return agents
