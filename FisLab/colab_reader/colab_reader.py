from FisLab.colab_reader import GOOGLE_BASE_PATH
import os
from google.colab import drive

from logging import getLogger

logger = getLogger(__name__)

def mount_drive(path: str):
    drive.mount(GOOGLE_BASE_PATH)
    logger.info("Drive is mounted")

def get_path(path: str):
    if not path.startswith(GOOGLE_BASE_PATH):
        path = os.path.join(GOOGLE_BASE_PATH, path)
    return os.listdir(path)