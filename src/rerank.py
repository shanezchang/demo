from loguru import logger
from dotenv import load_dotenv

load_dotenv()

from sentence_transformers import CrossEncoder

# Load a pre-trained CrossEncoder model
model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L6-v2")


def main():
    logger.debug("Hello from demo!")

    # Predict scores for a pair of sentences
    scores = model.predict([
        ("How many people live in Berlin?",
         "Berlin had a population of 3,520,031 registered inhabitants in an area of 891.82 square kilometers."),
        ("How many people live in Berlin?", "Berlin is well known for its museums."),
    ])
    # => array([ 8.607138 , -4.3200774], dtype=float32)
    logger.debug(scores)


if __name__ == "__main__":
    main()
