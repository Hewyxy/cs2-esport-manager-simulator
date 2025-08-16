import json, os, time

def save_game(data, filename="saves/savegame.json"):
  # Create folder if it doesn't exist
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    print("Game saved!")
    time.sleep(3)
    os.system("cls")

def load_game(filename="saves/savegame.json"):
    with open(filename, "r") as f:
        data = json.load(f)
    print("Game loaded!")
    time.sleep(3)
    os.system("cls")
    return data
