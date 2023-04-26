#####################################################################
# The idea is to create a smaller dataset of PubLayNet
# Only 5000 images would be picked for training
# Similarly, only 500 images would be taken for validation
#####################################################################

import json
import os 
import shutil
import argparse

def parse_args():
    parser = argparse.ArgumentParser(
                    prog='subsampler',
                    description='Subsample a small part of the actual dataset')
    
    parser.add_argument('--root_dir', 
                        help="Root directory where all the train, test, and validation data is present",
                        default=r"..\dataset_group0\labels\publaynet",)
    parser.add_argument('--out_dir',
                        help='Directory where the subsampled JSON label file needs to be stored',
                        default='..\dataset')
    parser.add_argument('--dataset',
                        help='The data subset that needs to be subsamples',
                        choices = ['train', 'test', 'val'],
                        required=True)
    parser.add_argument('--image_folder_path',
                        help="Full path to the folder containing images")
    parser.add_argument('--num_samples',
                        help='Number of images that needs to be subsampled',
                        default=5000)
    args = parser.parse_args()
    return args.root_dir, args.out_dir, args.dataset, args.image_folder_path, args.num_samples
    
if __name__ == '__main__':
    root_dir, out_dir, dataset, image_folder, num_samples = parse_args()

    num_samples = int(float(num_samples))

    data_file = f"{dataset}.json"
    
    print(f"\nData directory: {root_dir}\nOutput directory: {out_dir}\nFile: {data_file}\nImage folder: {image_folder}\n")

    with open(os.path.join(root_dir, data_file), 'r') as f:
        data = json.load(f)



    if num_samples > len(data['images']):
        exit(f"{num_samples} images not available in {dataset} dataset")

    if dataset == 'train':
        # because all the images in train.json may not be available in train-0 group
        image_names = os.listdir(image_folder)[:num_samples]
        image_data = [image for image in data['images'] if image['file_name'] in image_names]
    else:
        image_data = data['images'][:num_samples]

    image_ids = [item['id'] for item in image_data]
    
    annotations = []
    for ann in data['annotations']:
        if len(annotations) == len(image_ids):
            break
        if ann['image_id'] in image_ids:
            annotations.append(ann)
    
    final_data = {'images' : image_data, 'annotations': annotations, 'categories': data['categories']}

    if not os.path.exists(out_dir): os.makedirs(out_dir)

    with open(os.path.join(out_dir, data_file), 'w') as f:
        json.dump(final_data, f, indent=4)


    if not dataset == 'val':
        # copy the images to new datasest/train folder
        
        image_names = [item['file_name'] for item in image_data]

        save_to = os.path.join(out_dir, dataset)
        if not os.path.exists(save_to) : os.makedirs(save_to)

        for image in image_names:
            shutil.copy(os.path.join(image_folder, image), os.path.join(save_to, image))
