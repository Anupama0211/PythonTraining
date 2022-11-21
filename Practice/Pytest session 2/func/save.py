import json

def save_data(data, filepath):
    with open(filepath, 'w') as file:
        file.write(data)
    return