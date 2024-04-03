
import os

from logging import getLogger

from FisLab.config import GOOGLE_BASE_PATH

logger = getLogger(__name__)


def get_filepaths(path: str, sort: bool = True):
    if not path.startswith(GOOGLE_BASE_PATH):
        path = os.path.join(GOOGLE_BASE_PATH, path)
    paths = walk_paths(path)
    if sort:
        paths.sort()
    return paths

def walk_paths(path: str):
    return [os.path.join(path, file) for path, _, files in os.walk(path) for file in files]

