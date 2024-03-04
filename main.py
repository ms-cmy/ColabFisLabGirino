from feature_eng import im_class
from functools import partial
from funcoes_de_feat import cut_image_into_four, rotate_image

im_class.apply_transformations_to_gt({cut_image_into_four: {}}) \
            .apply_transformations({rotate_image: {'angle': 15}}) \
                .apply_transformations({rotate_image: {'angle': -15}}).save_images()