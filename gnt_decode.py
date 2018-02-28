# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 11:10:13 2018

@author: john
"""
import struct as st
import numpy as np
import os
class gnt_decode(object):    
    def __init__(self):
        '''
        参数说明：
        target_folder--目标文件夹
        target_dataset--数据集名称
        '''
        self.target_folder='E:/项目集合/wox/text detection/dataset'
        self.target_dataset='test'
    
    def file_seek(self):
        '''
        函数说明：搜索目标文件夹下所有的文件并生成完整文件路径
        返回值：
        s--列表，表里元素为文件夹里每个文件的完整路径
        '''
        path_1=self.target_folder+'/'+self.target_dataset
        files=os.listdir(path_1)
        s=[]
        for file in files:
            file=path_1+'/'+file
            s.append(file)
        return s
    def folder_create1(self):
        '''
        创建结果所在一级文件夹
        参数说明：
        folder--要创建的文件夹的名称
        '''
        folder_q=self.target_folder+'/'+self.target_dataset+'_result'
        if os.path.exists(folder_q):
            pass
        else:
            os.makedirs(folder_q)
        return folder_q
    def data_decode(self,folder__q,s):
        for i in s:
            name=i[-10:]#文件名称
            ###首先在folder_q里创建文件夹
            folder_aim=folder__q+'/'+name
            if os.path.exists(folder_aim):
                pass
            else:
                os.makedirs(folder_aim)
            with open(i,'rb') as f:
                length=len(f.read())#统计字节流的长度
            with open(i,'rb') as f:
                j=0
                while j<length:
                    a=st.unpack('<I',f.read(4))#数据长度
                    b=f.read(2).decode('gb2312')#数据label
                    c=st.unpack('<H',f.read(2))#数据宽
                    d=st.unpack('<H',f.read(2))#数据高
                    arr=[a[0],b,c[0],d[0]]
                    for k in range(a[0]-10):
                        e=st.unpack('<B',f.read(1))
                        arr.append(e[0])
                    j=j+a[0]
                    arr=np.array(arr)
                    np.save(folder_aim+'/'+name[:4]+'_'+b,arr)
    
aa=gnt_decode()
s=aa.file_seek()
folder_q=aa.folder_create1()
aa.data_decode(folder_q,s)
