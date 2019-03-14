
import tkinter as tk
from tkinter import *
import tkinter.messagebox
import struct
import numpy as np
import matplotlib.pyplot as plt
import random


'''
#filename : input the file name which you want to read
#sizeofnum: the sizeof each num
#formatnum: the format of the number, maybe 'int' 'unsigned int'.etc
#           +=============================       data type       =============================+           #
#           +---------------------------------------------------------------------------------+           #
#           |  FORMAT  |       C Type       |     PYTHON SIZE     |  STANDARD SIZE  |  NOTES  |           #
#           |---------------------------------------------------------------------------------|           #
#           |    x     |      pad byte      |      no value       |                 |         |           #
#           |---------------------------------------------------------------------------------|           #
#           |    c     |        char        |  string of length 1 |       1         |  (3)    |           #
#           |---------------------------------------------------------------------------------|           #
#           |    b     |    singned char    |      integer        |       1         |  (3)    |           #
#           |---------------------------------------------------------------------------------|           #
#           |    B     |    unsigned char   |      integer        |       1         |  (1)    |           #
#           |---------------------------------------------------------------------------------|           #
#           |    ?     |       _Bool        |       bool          |       1         |  (3)    |           #
#           |---------------------------------------------------------------------------------|           #
#           |    h     |       short        |      integer        |       2         |  (3)    |           #
#           |---------------------------------------------------------------------------------|           #
#           |    H     |    unsigned short  |      integer        |       2         |  (3)    |           #
#           |---------------------------------------------------------------------------------|           #
#           |    i     |        int         |      integer        |       4         |  (3)    |           #
#           |---------------------------------------------------------------------------------|           #
#           |    I     |    unsigned int    |      integer        |       4         |  (3)    |           #
#           |---------------------------------------------------------------------------------|           #
#           |    l     |      long          |      integer        |       4         |  (3)    |           #
#           |---------------------------------------------------------------------------------|           #
#           |    L     |    unsigned long   |      integer        |       4         |  (3)    |           #
#           |---------------------------------------------------------------------------------|           #
#           |    q     |     long long      |      integer        |       8         | (2)(3)  |           #
#           |---------------------------------------------------------------------------------|           #
#           |    Q     | unsinged long long |      integer        |       8         | (2)(3)  |           #
#           |---------------------------------------------------------------------------------|           #
#           |    f     |       float        |       float         |       4         |  (4)    |           #
#           |---------------------------------------------------------------------------------|           #
#           |    d     |      double        |       float         |       8         |  (4)    |           #
#           |---------------------------------------------------------------------------------|           #
#           |    s     |      char[]        |       string        |                 |         |           #
#           |---------------------------------------------------------------------------------|           #
#           |    p     |      char[]        |       string        |                 |         |           #
#           |---------------------------------------------------------------------------------|           #
#           |    P     |      void *        |      integer        |                 | (5)(3)  |           #
#           +---------------------------------------------------------------------------------+           #
#    (1) q 和 Q 只在机器支持64位操作系统有意义
#    (2) 每个格式前可以有一个数字，表示个数
#    (3) s格式表示一定长度的字符串，4s表示长度为4的字符串，但是p表示的是Pascal字符串
#    (4) P用来转换一个指针，其长度和机器字长相关
#    (5) 最后一个可以用来表示指针类型的，占4个字节
#
#           +===========================        align type       =============================+           #
#           +---------------------------------------------------------------------------------+           #
#           |      CHARACTER      |         BYTE ORDER         |     SIZE     |   ALIGNMENT   |           #
#           |---------------------------------------------------------------------------------|           #
#           |          @          |           native           |    native    |     native    |           #
#           |---------------------------------------------------------------------------------|           #
#           |          =          |           native           |   standard   |     native    |           #
#           |---------------------------------------------------------------------------------|           #
#           |          <          |       little-endian        |   standard   |     native    |           #
#           |---------------------------------------------------------------------------------|           #
#           |          >          |         big-endian         |   standard   |     native    |           #
#           |---------------------------------------------------------------------------------|           #
#           |          !          |    network(=big-endian)    |   standard   |     native    |           #
#           +---------------------------------------------------------------------------------+           #
# 这里仅仅使用"[align type]+[data type]"的方式，例如"<i"表示小端下的int数据类型
'''

def read_bin_file(filename, sizeofnum, formatnum):
    with open(filename,'rb') as f:
        all_num = []
        while True:
            get_num = f.read(sizeofnum)
            if(get_num == b''):
                break
            num = struct.unpack(formatnum, get_num)
            all_num.append(num[0])
        
    print('finish read bin file ')
    f.close()
    return all_num

    
def read_bin_file_2(filename, sizeofnum, formatnum):
    with open(filename,'rb') as f:
        get_num = f.read()
        
        if len(formatnum) == 2:
            num = struct.unpack( ("%s%d%s" %( formatnum[0], (len(get_num) / sizeofnum), formatnum[1] )), get_num)
        else :
            if len(formatnum) == 1:
                num = struct.unpack( ("%d%s" %( (len(get_num) / sizeofnum), formatnum )), get_num)
    f.close()
    return num

def read_bin_file_3(filename, sizeofnum, formatnum):
    try:
        with open(filename,'rb') as f:
                #tk.messagebox.showerror("illegal input file name")
            #print(f)
            get_num = f.read()
            
            if len(formatnum) == 2:
                num = struct.unpack( ("%s%d%s" %( formatnum[0], (len(get_num) / sizeofnum), formatnum[1] )), get_num)
            else :
                if len(formatnum) == 1:
                    num = struct.unpack( ("%d%s" %( (len(get_num) / sizeofnum), formatnum )), get_num)
        f.close()
    except:
        num =0
        tk.messagebox.showinfo("error","illegal input file name")
        tk.mainloop()
    return num


if __name__=='__main__':
    
    num = read_bin_file_2('C:/Users/zhang/Desktop/tmp2.bin', 4, '<f')
    num1 = read_bin_file('C:/Users/zhang/Desktop/tmp.bin', 4, '<I')
    num2 = read_bin_file_3('C:/Users/zhang/Desktop/tmp3.bin', 4, '<f')
    plt.subplot(2,1,1)
    plt.plot(np.array(num))
    plt.subplot(2,2,3)
    plt.plot(np.array(num1))
    plt.subplot(2,2,4)  
    plt.plot(np.array(num) * np.array(num1))


    """
    #num = read_bin_file('C:/Users/zhang/Desktop/tmp.bin', 4, 'I')
    num = read_bin_file('C:/Users/zhang/Desktop/tmp2.bin', 4, 'f')
    #print(num)
    amp=[]

    #print(num)
    #plt.plot(num)
    #plt.plot(amp)
    '''
    a = [1,2,3,4,5,6]
    b = [1,2,3,4,5,6]
    a_np = np.array(a)
    b_np = np.array(b)
    plt.plot(a_np - b_np + 1)
    '''
    plt.figure()
    plt.plot(np.array(num) * 1e-12)
    
    plt.figure()
    plt.plot(np.array(num) * 1e-7)

    plt.figure()
    plt.plot(np.array(num) * random.random())
    """
    plt.show()

