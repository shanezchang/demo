import chromadb
from dotenv import load_dotenv
from loguru import logger

import constants

# chroma_client = chromadb.Client()
chroma_client = chromadb.PersistentClient(constants.BASE_DIR)
load_dotenv()

def demo():
    collection = chroma_client.get_or_create_collection(name="my_collection")

    collection.upsert(
        documents=[
            "This is a document about pineapple",
            "This is a document about oranges"
        ],
        ids=["id1", "id2"]
    )

    results = collection.query(
        query_texts=["This is a query document about florida"],  # Chroma will embed this for you
        n_results=2  # how many results to return
    )

    logger.info(results)


def main():
    logger.debug("Hello from demo!")
    demo()


if __name__ == "__main__":
    main()
