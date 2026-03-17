import json

#load the HEALIX data from a JSON file
def load_healix(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

if __name__ == "__main__":
    # example usage
    data = load_healix("HEALIX.json")
    print(f"Loaded {len(data)} objects")