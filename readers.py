from PIL import Image
import os
import numpy as np
import re

def get_full_path_sorted(path: str):
    paths = [os.path.join(path, f) for f in os.listdir(path)]
    return sorted(paths, key=extract_number)

def extract_number(filename):
    numbers = re.findall(r'\d+', filename)
    return int(numbers[0]) if numbers else None

def load_original_data(qtd_min, qtd_max):
    training_data = get_full_path_sorted('fotos/Original')[qtd_min: qtd_max]
    target_data = get_full_path_sorted('fotos/Ground Thruth')[qtd_min: qtd_max]
    return training_data, target_data

def open_image_with_PIL(path: str):
    return np.array(Image.open(path))

def better_name(data_list: list):
    return np.array([open_image_with_PIL(i) for i in data_list])

def remove_pixels(data: np.ndarray):
    return data[:, :-5, :]

# paralelizar
def generate_dataset(qtd_min: int = 0,
                     qtd_max:int = 100):
    training_data, target_data = load_original_data(qtd_min, qtd_max)
    training_data_loaded = remove_pixels(better_name(training_data))
    target_data_loaded = remove_pixels(better_name(target_data))
    target_data_loaded = target_data_loaded.astype(np.float32)

    return training_data_loaded, target_data_loaded

def load_random_data():
    paths_original = get_full_path_sorted('fotos/Original')
    paths_gt = get_full_path_sorted('fotos/Ground Thruth')
    low = np.random.randint(0, 50, 10)
    mid = np.random.randint(len(paths_original)-200, len(paths_original)-100, 50)
    high = np.random.randint(len(paths_original)-50, len(paths_original), 10)
    all_indexes = np.concatenate([low, mid, high])
    training_data = remove_pixels(better_name([paths_original[i] for i in all_indexes]))
    target_data = remove_pixels(better_name([paths_gt[i] for i in all_indexes]))
    target_data = target_data.astype(np.float32)
    return training_data[0:2], target_data[0:2]


def load_generated_data():
    target = get_full_path_sorted('images/target')
    training = get_full_path_sorted('images/train')
    training_data = better_name([i for i in training if i.endswith('.png')])
    target_data = better_name([i for i in target if i.endswith('.png')])
    return training_data, target_data