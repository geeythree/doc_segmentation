import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from segment_anything import SamPredictor, sam_model_registry
from utils.data_loader import get_data, get_ground_truth
from utils.visualize import show_box, show_mask
import torch

print(torch.cuda.is_available())
exit()

train_path = r"dataset/train.json"
val_path = r"dataset/val.json"

train_img_indices, train_images, _ = get_data(train_path)

train_bbox, train_ground_truth_masks = get_ground_truth(train_images)

val_img_indices, val_images, _ = get_data(val_path)

val_bbox, val_ground_truth_masks = get_ground_truth(val_images)

model_type = 'vit_b'
checkpoint = 'model/sam_vit_b_01ec64.pth'
device = 'cuda:0'

sam_model = sam_model_registry[model_type](checkpoint=checkpoint)
sam_model.to(device)
# sam_model.train();

# print(val_bbox)

# ToDo :
# 1. Read train and Val data separately - done
# 2. SAM model prep code
# 3. Check if multiple prompts can be passed at once (if not, train for any one object type)
