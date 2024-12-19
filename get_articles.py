# get_articles.py

from Bio import Entrez

# Set email (required by NCBI for access)
Entrez.email = "insert_email"

# Define the search query
query = "Stargardt disease OR macular degeneration"

# Define a function to search PubMed
def search_pubmed(query, retmax=100):
    """Search PubMed for articles matching the query."""
    handle = Entrez.esearch(db="pubmed", term=query, retmax=retmax)
    record = Entrez.read(handle)
    handle.close()
    return record["IdList"]

# Define a function to fetch PubMed articles
def fetch_pubmed_articles(id_list, retmode="xml"):
    """Fetch PubMed articles in the specified format (e.g., XML)."""
    handle = Entrez.efetch(db="pubmed", id=",".join(id_list), retmode=retmode)
    records = handle.read()
    handle.close()
    return records

# Search for articles
print("Searching for articles...")
article_ids = search_pubmed(query, retmax=100)  # Adjust retmax for more articles
print(f"Found {len(article_ids)} articles.")

# Fetch the articles
print("Fetching articles...")
articles = fetch_pubmed_articles(article_ids)

# Save articles to a file
output_file = "macular_degeneration_stargardts.xml"
with open(output_file, "w", encoding="utf-8") as f:
    f.write(articles.decode("utf-8"))  # Decode bytes to a string

print(f"Articles saved to {output_file}.")
