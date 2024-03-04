import pytest
import numpy as np
from feature_eng_refactor import ImgFeatureEng
from funcoes_de_feat import cut_image_into_four

@pytest.fixture
def test_data():
    return np.random.randint(0, 100, (3, 100, 100))


def test_class(test_data):
    im_class = ImgFeatureEng(test_data, test_data)
    im_class.apply_transformations_to_gt(cut_image_into_four, {'remove_pixels': True})
    assert np.array(im_class.training).shape == (12, 50, 42)
    assert np.array(im_class.target).shape == (12, 50, 42)

@pytest.fixture
def test_data_2():
    return np.random.randint(0, 100, (3, 200, 200))

def test_class_chain(test_data_2):
    im_class = ImgFeatureEng(test_data_2, test_data_2)
    im_class.apply_transformations_to_gt(cut_image_into_four, {'remove_pixels': False})\
        .apply_transformations_to_gt(cut_image_into_four, {'remove_pixels': False})
    assert np.array(im_class.training).shape == (48, 50, 50)
    assert np.array(im_class.target).shape == (48, 50, 50)