import json
import numpy as np
from PIL import Image, ImageDraw, ImageOps

def get_data(path: str):
    """
    Read coords and masks from dataset 
    """
    with open(path, 'r') as f:
        data = json.load(f)


    images = {}
    for image in data['images']:
        images[image['id']] = {'file_name': image['file_name'],
                               'height' : image['height'],
                               'width' : image['width'],
                               'annotations': []}
    for ann in data['annotations']:
        images[ann['image_id']]['annotations'].append(ann)

    img_indices = {}
    for image in data['images']:
        img_indices[image['id']] = image['file_name']

    return img_indices, images, data['categories']
    # keys in 'annotations' -> 'segmentation', 'area', ,'iscrowd', 'image_id', 'bbox', 'category_id'
   

def get_binary_mask(height: int, width: int, mask: list):
    '''
    Convert the polygon points to segmentation mask
    '''
    blank_image_array = np.zeros((height, width))   
    blank_image = Image.fromarray(blank_image_array, 'RGBA')
    ImageDraw.Draw(blank_image).polygon(mask, outline=1, fill=(255, 255, 255))
    #binary_mask = np.where()
    binary_image = ImageOps.grayscale(blank_image)
    binary_mask = np.where(np.asarray(binary_image) < 255, False, True)
    
    return binary_mask

def get_ground_truth(images: dict):
    """
    Makes two dictionaries for bboxes and ground truth masks 
    """
    bbox = {}
    ground_truth_masks = {}
    for image in images:
        if images[image]['annotations'] != []:
            ground_truth_masks[image] = []  
            bbox[image] = []  
            for ann in images[image]['annotations']:
                bbox[image].append(ann['bbox'])
                for mask in ann['segmentation']:
                    bin_mask = get_binary_mask(images[image]['height'], images[image]['width'], mask)
                    ground_truth_masks[image].append(bin_mask)

    return bbox, ground_truth_masks