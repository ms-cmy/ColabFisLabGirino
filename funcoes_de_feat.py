import cv2
import numpy as np


def cut_image_into_four(image_array, remove_pixels: bool = True):
    # Calculate the center
    center_y, center_x = image_array.shape[0] // 2, image_array.shape[1] // 2

    # Cut the image into four pieces
    top_left = image_array[:center_y, :center_x]
    top_right = image_array[:center_y, center_x:]
    bottom_left = image_array[center_y:, :center_x]
    bottom_right = image_array[center_y:, center_x:]
    
    if remove_pixels is False:
        return np.array([top_left, top_right, bottom_left, bottom_right])
    return np.array([top_left, top_right, bottom_left, bottom_right])[:, :, :-8]


def rotate_image(image, angle, fill_color=(0, 0, 0)) -> np.ndarray:
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)

    M = cv2.getRotationMatrix2D((cX, cY), angle, 1.0)

    return np.array([cv2.warpAffine(image, M, (w, h), borderValue=fill_color)])
