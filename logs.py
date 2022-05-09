import logging



def home_page_logging(endpoint, raw_image):
    logger = logging.getLogger('thino.pics')
    fh = logging.FileHandler('logs/home.log')
    fh.setLevel(logging.DEBUG)
    logger.addHandler(fh)
    logger.setLevel(logging.DEBUG)