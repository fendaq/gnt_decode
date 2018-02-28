# -*- coding: utf-8 -*-
'''
说明：本文件主要用于解析gnk数据,并将数据存储在npy文件中---单个解析文件
数据来源：http://www.nlpr.ia.ac.cn/databases/handwriting/Download.html
数据格式说明：http://www.nlpr.ia.ac.cn/databases/handwriting/Offline_database.html
参考资源：
Python中对字节流/二进制流的操作:struct：https://www.cnblogs.com/jiangzhaowei/p/6138972.html
廖雪峰--struct：https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/0013994173393204e80af1f8fa94c8e9d094d229395ea43000
struct官方说明：https://docs.python.org/3/library/struct.html
CASIA中文手写体字库gnt文件格式解析(python)：http://blog.csdn.net/zsjhxl/article/details/42294591
CASIA脱机汉字库数据提取工具：http://blog.csdn.net/QiaXi/article/details/52146526

'''
import struct as st
import numpy as np
with open('1242-c.gnt','rb') as f:
    length=len(f.read())#统计字节流的长度
with open('1242-c.gnt','rb') as f:
    i=0
    while i<length:
        a=st.unpack('<I',f.read(4))#数据长度
        b=f.read(2).decode('gb2312')#数据label
        c=st.unpack('<H',f.read(2))#数据宽
        d=st.unpack('<H',f.read(2))#数据高
        arr=[a[0],b,c[0],d[0]]
        for j in range(a[0]-10):
            e=st.unpack('<B',f.read(1))
            arr.append(e[0])
        i=i+a[0]
        arr=np.array(arr)
        np.save('1242'+b,arr)

        
