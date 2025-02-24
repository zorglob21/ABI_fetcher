import json

# Original JSON data

def load_networks(json_file):
    with open(json_file, 'r') as file:
        return json.load(file)

data = load_networks("chainlist.json")

def lowercase_values(obj):
    if isinstance(obj, dict):
        return {k: lowercase_values(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [lowercase_values(item) for item in obj]
    elif isinstance(obj, str):  # Only lowercase string values
        return obj.lower()
    else:
        return obj  # For non-string values, no change

# Convert all string values to lowercase
lowercase_data = lowercase_values(data)

# Print transformed JSON for debugging
print("Transformed JSON:", json.dumps(lowercase_data, indent=2))

# Save the transformed JSON to the file
with open("chainlist.json", "w") as file:
    json.dump(lowercase_data, file, indent=2)

print("✅ JSON file successfully updated with lowercase values!")