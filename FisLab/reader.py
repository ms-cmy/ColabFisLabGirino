import os
import re

def get_full_path_sorted(path: str):
    paths = [os.path.join(path, f) for f in os.listdir(path)]
    return sorted(paths, key=extract_number)

def extract_number(filename):
    numbers = re.findall(r'\d+', filename)
    return int(numbers[0]) if numbers else None