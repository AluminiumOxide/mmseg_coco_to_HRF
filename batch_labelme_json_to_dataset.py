import os
import shutil

def json_to_dataset_list(img_dir,labelme_env_name):

    #  获取文件夹内的文件名
    FileNameList = os.listdir(img_dir)
    print(FileNameList)
    #  激活labelme环境
    os.system("activate " + labelme_env_name)
    for i in range(len(FileNameList)):
        #  判断当前文件是否为json文件
        if (os.path.splitext(FileNameList[i])[1] == ".json"):
            json_file = img_dir + "/" + FileNameList[i]
            # print(json_file)
            #  将该json文件转为png
            os.system("labelme_json_to_dataset " + json_file)


def remove_other_file(remove_path):
    # remove that dir and file below
    filelist = os.listdir(remove_path)
    print(filelist)
    for filename in filelist:
        filename = remove_path + filename
        print(filename)
        if os.path.isfile(filename):
            os.remove(filename)
        elif os.path.isdir(filename):  # which is not need for the reason that without spawn extra dir
            shutil.rmtree(filename)
        else:
            pass
    if os.path.isdir(remove_path):
        shutil.rmtree(remove_path)


def get_label_png(img_dir, save_path):
    try:
        os.makedirs(save_path, exist_ok=True)
        print("create dir " + save_path)
    except:
        pass
    # FileNameList = os.listdir(img_dir)
    for root, dirs, files in os.walk(img_dir):
        # print(root)
        if dirs:
            # print(dirs)
            for inter_dir in dirs:
                ori_path = img_dir + '/' + inter_dir + '/label.png'
                new_name = save_path + '/' + inter_dir.split('_json')[0] + '.png'
                remove_path = img_dir + '/' + inter_dir+ '/'
                # print(new_name)
                os.rename(ori_path, new_name)
                remove_other_file(remove_path)


if __name__ == '__main__':
    img_dir = './base_jsons'
    save_path = './base_annotations'
    labelme_env_name = 'labelme'  # your conda env name with labelme
    json_to_dataset_list(img_dir,labelme_env_name)
    get_label_png(img_dir, save_path)
