# main
from logger import MyLogger
from module1 import do_something
from module2 import do_something as test

if __name__ == "__main__":
    logger = MyLogger("example", "example.log")
    logger.info("This is an info message")
    logger.debug ("This is a warning message")
    logger.error("This is an error message")

    do_something()
    test()

