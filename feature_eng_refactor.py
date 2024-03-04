from functools import partial
from itertools import chain
import numpy as np

class ImgFeatureEng:
    def __init__(self, training, target) -> None:
        self.training = training
        self.target = target
        self.modified_training = []
        self.modified_target = []
    
    def apply_function(self, function: callable, args: dict, arrays):
        function_partial = partial(function, **args)
        return self.reshape_arrays(np.array([function_partial(array) for array in arrays]))
    
    def apply_transformations_to_gt(self, function: callable, args: dict = None):
        if args is None:
            args = {}
        self.training = self.apply_function(function, args, self.training)
        self.target = self.apply_function(function, args, self.target)
        return self
    
    def apply_transformations(self, function: callable, args: dict = None):
        if args is None:
            args = {}
        self.modified_training = self.apply_function(function, args, self.training)
        self.modified_target = self.apply_function(function, args, self.target)
        return self
    
    def reshape_arrays(self, arrays: np.ndarray):
        if arrays.ndim > 3:
            return arrays.reshape(-1, *arrays.shape[2:])
        return arrays
