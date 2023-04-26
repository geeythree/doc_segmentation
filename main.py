import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

from utils.data_loader import get_data, get_ground_truth
from utils.visualize import show_box, show_mask

path = r"dataset\train.json"

img_indices, images, _ = get_data(path)

bbox, ground_truth_masks = get_ground_truth(images)



# ToDo :
# 1. Read train and Val data separately
# 2. SAM model prep code
# 3. Check if multiple prompts can be passed at once (if not, train for any one object type)
