import os
import logging

def setup_logger():
    log_directory = "logs"
    log_file_path = os.path.join(log_directory, "logs.log")

    # Ensure the logs directory exists
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    logging.basicConfig(filename=log_file_path, level=logging.INFO)
    logging.info("Logger is set up.")

logger = logging.getLogger(__name__)