import os

from loguru import logger

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CHROMA_DATA_PATH = os.path.join(os.path.join(BASE_DIR, "data"), "chroma.db")


def main():
    logger.debug("Hello from demo!")
    logger.info(BASE_DIR)


if __name__ == "__main__":
    main()
