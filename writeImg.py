import sys
import os
from pathlib import Path


my_dir = '/Users/sangna/SunruiFans/SunruiFans.github.io/assets/img/gallery/VelvetCapri729'

files = os.listdir(my_dir) #采用listdir来读取所有文件
files.sort(reverse=False) #排序

f = open("VelvetCapri729.txt", "wt")
i = 1

for file_ in files:     #循环读取每个文件名
#    print(path +file_)
    if not os.path.isdir(my_dir + file_):  #判断该文件是否是一个文件夹
        f_name = str(file_)
        if f_name == '.DS_Store':
            continue
        # picSuffix = os.path.splitext(my_dir + file_)[1]
        thumbnail_name = '/thumbnails/' + f_name

        data  = '- filename: ' + f_name +'\n'
        data += '  original: ' + f_name +'\n'
        data += '  sizes:\n'
        data += '  - ' + f_name +'\n'
        data += '  thumbnail: ' + thumbnail_name +'\n'
        data += '\n'
        i += 1
        print(i)
        f.write(data)
