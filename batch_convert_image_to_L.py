from PIL import Image
import numpy as np
import os


def change_type(ann_org, ann_dir):
    try:
        os.makedirs(ann_dir, exist_ok=True)
        print("create dir " + ann_dir)
    except:
        pass

    for root, dirs, files in os.walk(ann_org):
        continue
    for file in files:
        img_path_org = ann_org+'/'+file
        img_path_dir = ann_dir+'/'+file
        img_org = Image.open(img_path_org)
        img_arr = np.array(img_org)
        img_dir = Image.fromarray(img_arr)
        img_dir.save(img_path_dir)
        print('{} mode {} change to {} mode {}'.format(img_path_org,img_org.mode,img_path_dir,img_dir.mode))


if __name__ == '__main__':
    ann_org = './base_annotations'
    ann_dir = './base_annotations_L'
    change_type(ann_org, ann_dir)