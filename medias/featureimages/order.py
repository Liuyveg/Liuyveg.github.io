# import os

# path = os.getcwd()

# i=0
# #对目录下的文件进行遍历
# for file in os.listdir(path):
# 	if file.split('.')[-1] == "jpg" or file.split('.')[-1] == "png":
# 		print(file)
# 		os.rename(os.path.join(path,file), os.path.join(path, str(i)+".jpg"))
# 		i=i+1
import os
from PIL import Image

path = os.getcwd()

#对目录下的文件进行遍历
for file in os.listdir(path):
	if file.split('.')[-1] == "jpg":
		
		im=Image.open(file)
		name = os.path.join(path, file)
		print(name)
		print(im.format, im.size, im.mode)
		im.thumbnail((1920,1280))
		#os.rename(os.path.join(path,file), os.path.join(path, str(i)+".JPG"))
		im.save(name, 'JPEG')