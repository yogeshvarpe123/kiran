import logging

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    fileHandlers = logging.FileHandler("yogesh_debug.log")
    conslove_handler = logging.StreamHandler()

    formatters = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    fileHandlers.setFormatter(formatters)
    conslove_handler.setFormatter(formatters)

    logger.addHandler(fileHandlers)
    logger.addHandler(conslove_handler)
    return logger



