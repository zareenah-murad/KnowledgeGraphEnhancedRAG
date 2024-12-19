# preprocess_text.py

import re

# Load the processed articles
input_file = "processed_articles.txt"
output_file = "preprocessed_articles.txt"

with open(input_file, "r", encoding="utf-8") as f:
    articles = f.readlines()

# Preprocessing function
def preprocess_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r"\d+", "", text)  # Remove numbers
    text = re.sub(r"[^\w\s]", "", text)  # Remove special characters
    text = re.sub(r"\s+", " ", text).strip()  # Remove extra spaces
    return text

# Apply preprocessing and save to a new file
with open(output_file, "w", encoding="utf-8") as f:
    for line in articles:
        if line.strip():  # Skip empty lines
            f.write(preprocess_text(line) + "\n")

print(f"Preprocessed text saved to {output_file}.")
