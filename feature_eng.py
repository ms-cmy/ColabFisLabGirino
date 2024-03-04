from typing import Generator
from readers import generate_dataset, load_random_data
from PIL import Image
import os
import numpy as np
from functools import partial
from itertools import chain
import shutil
import cv2


class GenerateNewImages:
    def __init__(self,
                 qtd_min: int = 5,
                 qtd_max: int = 30) -> None:
        # self.training, self.target = generate_dataset(qtd_min, qtd_max)
        self.training, self.target = load_random_data()
        self._modified_training = []
        self._modified_target = []
    # fazer dataclass para os dados
    @property
    def modified_training(self):
        return self._modified_training

    @modified_training.setter
    def modified_training(self, value):
        if isinstance(value, map):
            self._modified_training.append(value)
        else:
            self._modified_training = value

    @property
    def modified_target(self):
        return self._modified_target

    @modified_target.setter
    def modified_target(self, value):
        if isinstance(value, map):
            self._modified_target.append(value)
        else:
            self._modified_target = value

    def apply_function(self, function: callable, args: dict, arrays):
        return (map(partial(function, **args), array) for array in arrays)

    def apply_transformations(self, functions: dict[callable, dict]):
        for function, args in functions.items():
            self.modified_training, self.modified_target = self.apply_function(function, args, [self.training, self.target])
        return self

    def apply_transformations_to_training(self, functions: dict[callable, dict]):
        for function, args in functions.items():
            self.modified_training = self.apply_function(function, args, [self.training])
        return self

    def apply_transformations_to_target(self, functions: dict[callable, dict]):
        for function, args in functions.items():
            self.modified_target = self.apply_function(function, args, [self.target])
        return self

    def apply_transformations_to_gt(self, functions: dict[callable, dict]):
        for function, args in functions.items():
            self.training = self.apply_function(function, args, [self.training])
            self.target = self.apply_function(function, args, [self.target])
            self.training = self.unpack_array(self.training)
            self.target = self.unpack_array(self.target)
        return self
    
    def unpack_array(self, array_map):
        if isinstance(array_map, Generator):
            array_map = chain.from_iterable(array_map)
        unpacked_arrays = []
        for array_i in array_map:
            if array_i.ndim >= 3:
                unpacked_arrays.extend([sub_array for sub_array in array_i])
            else:
                unpacked_arrays.append(array_i)

        return np.array(unpacked_arrays)

    def apply_map(self):
        self.modified_training = self.unpack_array((self.modified_training))
        self.modified_training = np.concatenate([self.modified_training, self.training])
        self.modified_target = np.concatenate(list(chain.from_iterable([chain.from_iterable(self.modified_target), self.target])))
        self.modified_target = self.modified_target.astype(np.uint8)
        self.modified_training = self.modified_training.astype(np.uint8)

    def save_images(self, path: str = 'images'):
        self.check_if_path_exists(path)
        self.apply_map() # paralelizar
        for i in range(len(self.modified_training)):
            Image.fromarray(self.modified_training[i]).save(f'{path}/train/img_{i}.png')
            checker = cv2.imwrite(f'{path}/target/img_{i}.png', self.modified_target[i])
            if not checker:
                print('Error saving image')
                raise

    def check_if_path_exists(self, path: str):
        if os.path.exists(path):
            shutil.rmtree(path)
        os.makedirs(path)
        os.makedirs(f'{path}/train')
        os.makedirs(f'{path}/target')


im_class = GenerateNewImages()
