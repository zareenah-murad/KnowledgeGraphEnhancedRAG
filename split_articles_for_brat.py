# split_articles_for_brat.py

import os

# Input file with all articles
input_file = "preprocessed_articles.txt"

# Output directory for BRAT files
output_dir = "brat/data"  # Adjust this to your BRAT's data directory path

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Read the preprocessed articles
with open(input_file, "r", encoding="utf-8") as f:
    articles = f.read().strip().split("\n\n")  # Split articles by double newlines

# Save each article as a separate .txt file
for i, article in enumerate(articles, start=1):
    output_file = os.path.join(output_dir, f"article{i}.txt")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(article.strip())

print(f"Saved {len(articles)} articles to {output_dir}")
