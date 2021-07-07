# mmseg_coco_to_HRF
## 准备工作
1. 直接把这个项目解压到mmsegmentation目录下
```
mmsegmentation-master
|-mmseg
|-mmseg_coco_to_HRF
  |--batch_labelme_json_to_dataset.py
  |--batch_convert_image_to_L.py
  |--build_and_split_dataset.py
|-checkpoints
|-configs
|-data
|-work_dir
...
```
2. 创建conda环境，环境下安装labelme(确认在哪个conda环境里有labelme也行)

## 使用方法
1、将对应的图像数据和标注后的json数据分别放进对应的两个文件夹
2、运行batch_labelme_json_to_dataset.py 用于将原json文件转成label图
    - 需要设置以下几个参数，分别是 
        - json文件目录
        - 提取label图保存目录
        - 存在labelme的环境名
```python
    img_dir = './base_jsons'
    save_path = './base_annotations'
    labelme_env_name = 'labelme'  # your conda env name with labelme
```
3、运行batch_convert_image_to_L.py 将带颜色版的label转换成不带颜色版的label
   - 需要设置以下几个参数，分别是 
       - 原label存放目录
       - 转换后label存放目录
```python
    ann_org = './base_annotations'
    ann_dir = './base_annotations_L'
```
4、运行build_and_split_dataset.py 将分配训练集验证集测试集比例
   - 需要设置以下几个参数，分别是 
       - 训练集+验证集 与 测试集的比例(在原HRF数据集中没测试集，直接设成1)
       - 训练集 与 验证集的比例
       - 原图像存放目录
       - 转换后label存放目录
       - 自制数据集存放路径
```python
    train_val_percent = 1
    train_percent = 0.4

    base_image_path = 'base_images'
    base_annotation_path = 'base_annotations_L'

    dataset_dir = '../data/HRF_new'
```
5、运行calcuate_mean_and_std.py 计算数据集的均值和方差（在mmseg设置数据集有用）
   - 需要设置以下几个参数，分别是 
       - 数据集图像目录
       - resize高度
       - resize宽度
```python
    imgs_path = './base_images'  # 图片目录
    img_h = 400 
    img_w = 600  # 根据自己数据集适当调整，别太大了，最开始头铁4000、6000速度特别慢
``` 
输出类似于以下结果
```python
normMean = [0.55044323, 0.37878156, 0.36924595]
normStd = [0.18972462, 0.15784022, 0.16161829]
``` 
