# main.py
from document_retrieval import hybrid_retrieval

def query_rag_system(user_query):
    print("\nRunning hybrid retrieval...")
    answer = hybrid_retrieval(user_query)
    print("\nFinal Answer:")
    print(answer)

if __name__ == "__main__":
    print("\nWelcome to the Knowledge Graph-Enhanced RAG System!")
    while True:
        user_input = input("\nEnter your query (or type 'exit' to quit): ")
        if user_input.lower() == "exit":
            print("Exiting... Goodbye!")
            break
        query_rag_system(user_input)

