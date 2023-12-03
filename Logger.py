from loguru import logger 

logger.add("logs/test.log",rotation = "500 MB",level = "INFO")


def get_logger():
    return logger