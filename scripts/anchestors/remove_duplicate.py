import json

def update_children(node, name_counts):
    """
    Recursively update children for duplicate names.
    """
    name = node["name"]
    
    # Increment count of name occurrences
    if name in name_counts:
        name_counts[name] += 1
    else:
        name_counts[name] = 1

    # If this name has been seen before, replace children
    if name_counts[name] > 1:
        node["children"] = [{"name": "A.E", "children": []}]
    elif "children" in node:
        for child in node["children"]:
            update_children(child, name_counts)

def process_json(input_file, output_file):
    """
    Load JSON, process duplicate names, and save the output.
    """
    # Load JSON data from file
    with open(input_file, "r") as file:
        data = json.load(file)
    
    # Dictionary to track name occurrences
    name_counts = {}
    
    # Process JSON tree
    update_children(data, name_counts)
    
    # Save updated JSON to a file
    with open(output_file, "w") as file:
        json.dump(data, file, indent=2)
    
    print(f"Processed JSON saved to {output_file}")

if __name__ == "__main__":
    input_filename = "input.json"  # Replace with actual input file
    output_filename = "output.json"  # Replace with desired output file
    process_json(input_filename, output_filename)
