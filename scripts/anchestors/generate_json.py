import json
from collections import defaultdict

# Load the file
file_path = "my_genealogy.txt"  # Ensure the correct file path

# Read the file and construct relationships
relationships = []
with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        if "->" in line:
            student, advisor = map(str.strip, line.split("->"))
            relationships.append((student, advisor))  # Swap the order

# Build a mapping of students to advisors
student_map = defaultdict(list)
all_students = set()
all_advisors = set()

for student, advisor in relationships:
    student_map[student].append(advisor)  # Now student points to advisor
    all_students.add(student)
    all_advisors.add(advisor)

# Find the youngest (who is a student but never an advisor)
roots = all_students - all_advisors
if not roots:
    raise ValueError("No root found. Ensure your data is structured correctly.")

# Recursive function to construct the hierarchy
def build_tree(person):
    children = student_map.get(person, [])
    return {
        "name": person,
        "children": [build_tree(child) for child in children] if children else []
    }

# Construct the tree from all youngest students (roots)
genealogy_tree = {"name": "Genealogy", "children": [build_tree(root) for root in roots]}

# Save the JSON file
output_path = "genealogy.json"
with open(output_path, "w", encoding="utf-8") as json_file:
    json.dump(genealogy_tree, json_file, indent=2, ensure_ascii=False)

print(f"JSON file saved to {output_path}")
