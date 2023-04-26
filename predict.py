import cv2
import json

model_type = 'vit_b'
checkpoint = 'model/sam_vit_b_01ec64.pth'
device = 'cuda:0'

from segment_anything import SamAutomaticMaskGenerator, sam_model_registry
sam_model = sam_model_registry[model_type](checkpoint=checkpoint)

mask_generator = SamAutomaticMaskGenerator(sam_model)
image = cv2.imread(r"D:\github\doc_layout_analysis\dataset\train\PMC1187902_00002.jpg")
masks = mask_generator.generate(image)

for mask in masks:
    mask['segmentation'] = mask['segmentation'].tolist()
with open('dummy_result.json', 'w') as f:
    json.dump(masks, f, indent=4)
print(masks[0])