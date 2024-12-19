# rag_pipeline.py
from langchain_community.vectorstores import FAISS
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_openai.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from neo4j_driver import fetch_triples

# Fetch triples from Neo4j
query = """
MATCH (e1)-[r]->(e2)
RETURN e1.name AS Entity1, type(r) AS Relation, e2.name AS Entity2
"""
triples = fetch_triples(query)
formatted_triples = [f"{t['Entity1']} {t['Relation']} {t['Entity2']}" for t in triples]

# Initialize FAISS vector store
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_texts(formatted_triples, embeddings)
retriever = vectorstore.as_retriever()

# Initialize LLM
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.0)

# Build the Retrieval QA Chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True,
)

