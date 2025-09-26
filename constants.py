import os

from loguru import logger

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def main():
    logger.debug("Hello from demo!")
    logger.info(BASE_DIR)


if __name__ == "__main__":
    main()
