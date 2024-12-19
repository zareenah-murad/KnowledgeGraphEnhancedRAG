# neo4j_driver.py
from neo4j import GraphDatabase

# Neo4j connection details
uri = "bolt://localhost:7687"
username = "neo4j"
password = "insert_password"

def fetch_triples(query):
    with GraphDatabase.driver(uri, auth=(username, password)) as driver:
        with driver.session() as session:
            results = session.run(query)
            return [record for record in results]