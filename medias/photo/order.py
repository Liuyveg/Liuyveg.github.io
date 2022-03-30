import os

path = os.getcwd()

i=0
#对目录下的文件进行遍历
for file in os.listdir(path):
	if file.split('.')[-1] == "JPG":
		print(file)
		os.rename(os.path.join(path,file), os.path.join(path, str(i)+".JPG"))
		i=i+1