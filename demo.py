from loguru import logger
from dotenv import load_dotenv

load_dotenv()


def main():
    logger.debug("Hello from demo!")


if __name__ == "__main__":
    main()
