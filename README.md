# Knowledge Graph-Enhanced RAG System

This project implements a Retrieval-Augmented Generation (RAG) system enhanced by a knowledge graph for processing scientific research articles and answering domain-specific queries. The system combines structured knowledge graph triples and unstructured document retrieval to provide accurate responses.

## Features
- Integration with a Neo4j knowledge graph for structured data retrieval.
- FAISS vector store for unstructured document retrieval.
- Powered by OpenAI's GPT-3.5-turbo for natural language generation.
- Hybrid retrieval combining structured and unstructured data sources.

## Setup Instructions

### 1. Prerequisites
- Python 3.9+
- Neo4j installed and running locally (with the knowledge graph loaded).
- An OpenAI API key for GPT-3.5-turbo.
- LangChain, FAISS, and related libraries installed in a virtual environment.

### 2. Installation
```bash
git clone https://github.com/your-repo-name/knowledge-graph-rag.git
cd knowledge-graph-rag
pip install -r requirements.txt
```

### 3. Configure Neo4j

Edit the `neo4j_driver.py` file to update your Neo4j connection details:

```python
uri = "bolt://localhost:7687"
username = "your-neo4j-username"
password = "your-neo4j-password"
```

### 4. Add OpenAI API Key

Set you OpenAI API key as an environment variable:

```bash
export OPENAI_API_KEY="your-openai-api-key"
```

### Usage

Run the main script to interact with the system:

```bash
python main.py
```

You will be prompted to enter a query.

The system will combine knowledge graph triples and retrieved documents to generate a comprehensive answer. 

### File Descriptions

- `main.py`: main script for running the RAG system
- `document_retrieval.py`: handles hybrid retrieval from the knowledge graph and vector store
- `neo4j_driver.py`: connects to Neo4j and executes queries to fetch triples 
- `rag_pipeline.py`: configures the RAG pipeline, including the vector store and LLM integration
- `extract_triples.py`: parses annotated data to extract triples and saves them in CSV format
- `get_articles.py`: etches PubMed articles related to Stargardt’s disease and macular degeneration
- `parse_extract.py`: parses XML files and extracts relevant article text 
- `preprocess_text.py`: preprocesses text for annotation by cleaning and tokenizing
- `split_articles_for_brat.py`: splits articles into individual files for BRAT annotation

### Example Query 

Input:
```text
"What is associated with age-related macular degeneration?"
```
Output:
```text
"Associated entities include "lipid pathway" and "complement system."
```

### Contributions

Contributions are welcome! Please fork this repository and submit a pull request with your changes.
