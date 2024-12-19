# document_retrieval.py
from neo4j_driver import fetch_triples
from rag_pipeline import retriever, qa_chain

def hybrid_retrieval(query):
    # Retrieve structured triples
    kg_query = f"""
    MATCH (e1)-[r]->(e2)
    WHERE e1.name CONTAINS '{query}' OR e2.name CONTAINS '{query}'
    RETURN e1.name AS Entity1, type(r) AS Relation, e2.name AS Entity2
    """
    triples = fetch_triples(kg_query)
    structured_context = "\n".join([f"{t['Entity1']} {t['Relation']} {t['Entity2']}" for t in triples])
    
    # Retrieve unstructured documents
    docs = retriever.invoke(query)
    unstructured_context = "\n".join([doc.page_content for doc in docs])
    
    # Combine contexts and query QA system
    combined_context = structured_context + "\n" + unstructured_context
    prompt = {"query": query, "context": combined_context}
    response = qa_chain.invoke(prompt)
    return response["result"]

