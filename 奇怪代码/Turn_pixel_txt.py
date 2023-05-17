import cv2
import os               # 导入os模块
import numpy as np
import time

img = cv2.imread(r"C:\Users\86136\Pictures\p_face.jpg")
img = cv2.resize(img, (30,15))
cv2.imshow("out1",img)
w,h,_ = img.shape
output = [[0 for i in range(h)]for j in range(w)]
shading = [" ","⊙"]
for i in range(w):
	for j in range(h):
		color = img[i,j]
		if color[0]>130:
			color = [255,255,255]
			output[i][j] = shading[0]
		else:
			color = [0,0,0]
			output[i][j] = shading[1]
		img[i,j] = color
outcome = []
for i in range(w):
	outcome.append("".join(output[i]))
for each in outcome:
	print(each)
time.sleep(3)
os.system("cls")
