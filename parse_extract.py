# parse_extract.py

import xml.etree.ElementTree as ET

# Define the input and output files
input_file = "macular_degeneration_stargardts.xml"
output_file = "processed_articles.txt"

# Parse the XML file
tree = ET.parse(input_file)
root = tree.getroot()

# Extract relevant data (e.g., titles and abstracts)
articles = []
for article in root.findall(".//PubmedArticle"):
    title = article.find(".//ArticleTitle")
    abstract = article.find(".//AbstractText")
    
    # Combine title and abstract, if available
    if title is not None and abstract is not None:
        articles.append(f"Title: {title.text}\nAbstract: {abstract.text}\n")

# Save the extracted text to a file
with open(output_file, "w", encoding="utf-8") as f:
    for article in articles:
        f.write(article + "\n\n")

print(f"Processed {len(articles)} articles. Saved to {output_file}.")
