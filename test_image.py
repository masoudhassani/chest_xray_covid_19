import cv2
import tensorflow as tf
import tkinter as tk
from tkinter import filedialog
import numpy as np

# file dialogue initialization
root = tk.Tk()
root.withdraw()

# load a network weight file
file_path = filedialog.askopenfilename(filetypes=[("Model Weights", ".h5")])
model = tf.keras.models.load_model(file_path)

# open a file dialogue to select an image
file_path = filedialog.askopenfilename(filetypes=[("Image", ".jpg .jpeg .png")])

# process the selected image
size = 200
img_array = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
img_array_resized = cv2.resize(img_array, (size, size))
X_test = np.array(img_array_resized).reshape(-1, size, size, 1)
X_test = X_test/255.0 

# predict 
label = model.predict(X_test)[0]
idx = np.argmax(label)
if idx == 0:
    status = '{} percent healthy'.format(int(label[0]*100))
else:
    status = '{} percent pneumonia'.format(int(label[1]*100))

# show results
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img_array,status,(20,60),font, 1, (255,255,255), 2)
cv2.putText(img_array,'press any key to exit',(20,120),font, 1, (255,255,255), 2)
cv2.imshow('X-ray image', img_array)
cv2.waitKey(0); 
cv2.destroyAllWindows()