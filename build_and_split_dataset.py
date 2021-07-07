import os
import random
import shutil


def generate_HRF_dataset_dirs(dataset_dir):
    dir_list = [
        '',
        '/images',
        '/images/training',
        '/images/validation',
        '/annotations',
        '/annotations/training',
        '/annotations/validation'
    ]
    for append_dir in dir_list:
        try:
            os.makedirs(dataset_dir + append_dir, exist_ok=True)
            print("create dir " + dataset_dir + append_dir)
        except:
            pass


def split_dataset(train_val_percent,train_percent,base_image_path,base_annotation_path,dataset_dir):
    temp_imgs = os.listdir(base_image_path)    # image file name list
    temp_anns = os.listdir(base_annotation_path)  # ann file name list (without append same as temp_imgs)

    total_imgs = []
    for temp_img in temp_imgs:
        if temp_img.endswith(".jpg"):
            total_imgs.append(temp_img)

    num = len(total_imgs)
    total_list = range(num)
    tv = int(num * train_val_percent)  # train and val image number
    tr = int(tv * train_percent)  # train image number
    trainval = random.sample(total_list, tv)  # train and val img
    train = random.sample(trainval, tr)  # train img

    for i in total_list:
        name = total_imgs[i].split('.jpg')[0]
        if i in trainval:
            # print('train val {}'.format(name))
            if i in train:
                shutil.copy(base_image_path + '/' + name + '.jpg', dataset_dir + '/images/training/' + name + '.png') # for the reason HRF img append type is png
                shutil.copy(base_annotation_path + '/' + name + '.png', dataset_dir + '/annotations/training/' + name + '.png')
                print('    belong to train {}'.format(name))
            else:
                shutil.copy(base_image_path + '/' + name + '.jpg', dataset_dir + '/images/validation/' + name + '.png')
                shutil.copy(base_annotation_path + '/' + name + '.png', dataset_dir + '/annotations/validation/' + name + '.png')
                print('    belong to val {}'.format(name))
        else:
            shutil.copy(base_image_path + '/' + name + '.jpg', dataset_dir + '/images/testing/' + name + '.png')
            shutil.copy(base_annotation_path + '/' + name + '.png', dataset_dir + '/annotations/testing/' + name + '.png')
            print('    belong to test {}'.format(name))


if __name__ == '__main__':
    train_val_percent = 1
    train_percent = 0.4

    base_image_path = 'base_images'
    base_annotation_path = 'base_annotations_L'

    dataset_dir = '../data/HRF_new'

    generate_HRF_dataset_dirs(dataset_dir)
    split_dataset(train_val_percent, train_percent, base_image_path, base_annotation_path, dataset_dir)








