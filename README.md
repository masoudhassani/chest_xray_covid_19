# Pneumonia detection from chest x-ray
Training a neural network model to detect Pneumonia from chest X-rays
Note: This tool was solely developped for exploring the usability of deep learning
in identifying Pneumonia from chest x-ray scans. This CANNOT be used for medical purposes
in any way!

## How to start
Download the chest x-ray dataset and put it in the project folder
https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia/

### for 2-label training (normal and pneumonia)
run train_normal_pneumonia.ipynb

### for 3-label training (normal, viral and bacterial)
run train_normal_viral_bacterial.ipynb

## Requirements
### opencv
,,,
pip install opencv-python
,,,

### tensorflow
,,,
pip install --upgrade tensorflow
'''

### Misc
,,,
pip install pyh5
pip install matplotlib
pip install numpy
,,,


