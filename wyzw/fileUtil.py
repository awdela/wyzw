# -*- coding:utf-8 -*-
import sys
import os
import pdb
#from wyzw import fileSetting

#保存爬取内容
def save_content(file_name,content):
    FILE_DIR = '/home/scrapy/wyzw/file'
    b = os.path.exists(FILE_DIR)
    if not b:
        os.mkdir(FILE_DIR)
        print('Successfully create dirctory', FILE_DIR)
    file_path = FILE_DIR +'/'+ file_name + '.txt'
    fo = open(file_path,'ab')
    fo.write(content.encode('utf-8'))
    fo.close()
if __name__ == "__main__":
    save_content('test','attention : this is a test!\n')
   

