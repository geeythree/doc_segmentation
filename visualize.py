from PIL import Image
from utils.visualize import show_box, show_mask
from utils.data_loader import get_data
import matplotlib.pyplot as plt


path = r"dataset/train.json"

img_indices, images, categories = get_data(path)

pos = 0
image_id = list(images.keys())[pos]
name = img_indices[image_id]

image_path = r"dataset/train/%s"%name
print(image_path)

image = Image.open(image_path)

# Visualize an image
plt.figure(figsize=(10,10))
plt.imshow(image)
for box in images[image_id]['annotations']: 
    show_box(box['bbox'], plt.gca())
for mask in images[image_id]['annotations']:
    #print(mask)
    show_mask(categories, mask, plt.gca())
plt.axis('off')
plt.show()