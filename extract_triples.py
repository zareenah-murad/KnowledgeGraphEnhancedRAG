# extract_triples.py

import os

def parse_ann_file(file_path):
    entities = {}
    relations = []

    with open(file_path, "r") as f:
        for line in f:
            parts = line.strip().split("\t")
            if parts[0].startswith("T"):  # Entity
                entity_id, entity_info, text = parts
                entity_type, start, end = entity_info.split()
                entities[entity_id] = {"type": entity_type, "start": start, "end": end, "text": text}
            elif parts[0].startswith("R"):  # Relation
                relation_id, relation_info = parts
                relation_type, arg1, arg2 = relation_info.split()
                relations.append({
                    "id": relation_id,
                    "type": relation_type,
                    "arg1": arg1.split(":")[1], 
                    "arg2": arg2.split(":")[1]
                })
    return entities, relations

# Directory containing BRAT files
brat_data_dir = "brat/data"

# Iterate over all .ann files
all_triples = []

for file_name in os.listdir(brat_data_dir):
    if file_name.endswith(".ann"):
        file_path = os.path.join(brat_data_dir, file_name)
        entities, relations = parse_ann_file(file_path)
        
        # Extract triples
        for relation in relations:
            arg1 = entities[relation["arg1"]]["text"]
            arg2 = entities[relation["arg2"]]["text"]
            all_triples.append((arg1, relation["type"], arg2))

# Save triples to a CSV file
import csv
output_file = "extracted_triples.csv"
with open(output_file, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Entity1", "Relation", "Entity2"])  # Header
    writer.writerows(all_triples)

print(f"Triples saved to {output_file}")
