from functions_for_decrypt import main_decrypt
from logg import Logger
import sys

if __name__ == "__main__":
    logger = Logger("result_of_searched_key.txt")
    sys.stdout = logger

    main_decrypt()

    sys.stdout = logger.terminal
    logger.log.close()
