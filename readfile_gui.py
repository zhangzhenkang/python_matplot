import os
import tkinter as tk
from tkinter import filedialog as tf
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt 

#sys.path.append('C:/Users/zhang/Documents/study/0_Raco/Python/1_program/4_file')
from fileopen import *
#layout
entry_file_width = 40



#window
window = tk.Tk()
window.title('Compare file -- 假设使用者是一个资深程序员，不会犯低级错误')
window.geometry('550x200')

frame_file_op = tk.Frame(window)
frame_select_dataType = tk.Frame(window)
frame_input_file = tk.Frame(frame_file_op)
frame_execute = tk.Frame(frame_file_op)

frame_file_op.pack(padx = 10,
                   pady = 5)
frame_select_dataType.pack(padx = 10,
                           pady = 5)
frame_input_file.pack(side=LEFT,
                      padx = 0,
                      pady = 5)
frame_execute.pack(side=RIGHT,
                   padx = 10,
                   pady = 5)


#file information
tk.Label(frame_input_file, text='file1 name: ').grid(row = 0,
                                           column = 0,
                                           sticky=W)
tk.Label(frame_input_file, text='file2 name: ').grid(row = 1,
                                           column = 0,
                                           sticky=W)

def select_file():
    tmp = tf.askopenfilename(title = '选择文件',
                             filetype = [('BIN', '*.bin'),
                                         ('TEXT', '*.txt'),
                                         ('ALL FILE', '*.*')],
                       initialdir='c:/')
    return tmp

def sel_file1():
    var_file1_name.set(select_file())

def sel_file2():
    var_file2_name.set(select_file())

#file name
var_file1_name = tk.StringVar()
var_file1_name.set('c:/filename1.bin')
entry_file1_name = tk.Entry(frame_input_file,
                            textvariable = var_file1_name,
                            width = entry_file_width).grid(row = 0,
                                                           column = 1,
                                                           sticky = W)
#button 1: select file
btn_file1 = tk.Button(frame_input_file,
                      text='选择文件',
                      command=sel_file1).grid(row = 0,
                                            column = 2,
                                            sticky = W)



var_file2_name = tk.StringVar()
var_file2_name.set('c:/filename2.bin')
entry_file2_name = tk.Entry(frame_input_file,
                            textvariable = var_file2_name,
                            width = entry_file_width).grid(row = 1,
                                                           column = 1,
                                                           sticky = W)

btn_file1 = tk.Button(frame_input_file,
                      text='选择文件',
                      command = sel_file2).grid(row = 1,
                                                column = 2,
                                                sticky = W)

var = tk.StringVar()
var.set('f')
var_tmp = tk.StringVar()
sizeofnum_datatpye = 4

switcher_datatypesize = {
    "x" : 0,
    "c" : 1,
    "b" : 1,
    "B" : 1,
    "?" : 1,
    "h" : 2,
    "H" : 2,
    "i" : 4,
    "I" : 4,
    "l" : 4,
    "L" : 4,
    "q" : 8,
    "Q" : 8,
    "f" : 4,
    "d" : 8,
    "s" : 0,
    "p" : 0,
    "P" : 0
    }


def print_selection():
    #print('print_selection:'+var.get())
    #print('sizeof : %d' %switcher_datatypesize[var.get()])
    var_tmp = var
    sizeofnum_datatpye = switcher_datatypesize[var.get()]
    


r_width = 10
#select data type, RadioButton
r_char = tk.Radiobutton(frame_select_dataType,
                          text = 'char',
                          variable = var,
                          value='c',
                          command=print_selection).grid(row = 3,
                                                        column = 0,
                                                        sticky = W)
#r_char.pack()

r_schar = tk.Radiobutton(frame_select_dataType,
                          text = 'signed char',
                          variable = var,
                          value='b',
                          command=print_selection).grid(row = 4,
                                                        column = 0,
                                                        sticky = W)
#r_schar.pack()

r_uchar = tk.Radiobutton(frame_select_dataType,
                          text = 'unsigned char',
                          variable = var,
                          value='B',
                          command=print_selection).grid(row = 5,
                                                        column = 0,
                                                        sticky = W)
#r_uchar.pack()

r_bool = tk.Radiobutton(frame_select_dataType,
                          text = '_Bool',
                          variable = var,
                          value='?',
                          command=print_selection).grid(row = 6,
                                                        column = 0,
                                                        sticky = W)
#r_bool.pack()

r_short = tk.Radiobutton(frame_select_dataType,
                          text = 'short',
                          variable = var,
                          value='h',
                          command=print_selection).grid(row = 3,
                                                        column = 1,
                                                        sticky = W)
#r_short.pack()

r_ushort = tk.Radiobutton(frame_select_dataType,
                          text = 'unsigned short',
                          variable = var,
                          value='H',
                          command=print_selection).grid(row = 4,
                                                        column = 1,
                                                        sticky = W)
#r_ushort.pack()

r_int = tk.Radiobutton(frame_select_dataType,
                          text = 'int',
                          variable = var,
                          value='i',
                          command=print_selection).grid(row = 5,
                                                        column = 1,
                                                        sticky = W)
#r_int.pack()

r_uint = tk.Radiobutton(frame_select_dataType,
                          text = 'unsigned int',
                          variable = var,
                          value='I',
                          command=print_selection).grid(row = 6,
                                                        column = 1,
                                                        sticky = W)
#r_uint.pack()

r_long = tk.Radiobutton(frame_select_dataType,
                          text = 'long',
                          variable = var,
                          value='l',
                          command=print_selection).grid(row = 3,
                                                        column = 2,
                                                        sticky = W)
#r_long.pack()

r_ulong = tk.Radiobutton(frame_select_dataType,
                          text = 'unsigned long',
                          variable = var,
                          value='L',
                          command=print_selection).grid(row = 4,
                                                        column = 2,
                                                        sticky = W)
#r_ulong.pack()

r_ll = tk.Radiobutton(frame_select_dataType,
                          text = 'long long',
                          variable = var,
                          value='q',
                          command=print_selection).grid(row = 5,
                                                        column = 2,
                                                        sticky = W)
#r_ll.pack()

r_ull = tk.Radiobutton(frame_select_dataType,
                          text = 'unsigned long long',
                          variable = var,
                          value='Q',
                          command=print_selection).grid(row = 6,
                                                        column = 2,
                                                        sticky = W)
#r_ull.pack()

r_float = tk.Radiobutton(frame_select_dataType,
                          text = 'float',
                          variable = var,
                          value='f',
                          command=print_selection).grid(row = 3,
                                                        column = 3,
                                                        sticky = W)
#r_float.pack()

r_double = tk.Radiobutton(frame_select_dataType,
                          text = 'double',
                          variable = var,
                          value='d',
                          command=print_selection).grid(row = 4,
                                                        column = 3,
                                                        sticky = W)
#r_double.pack()
#btn_plot
def plot_diff():
    #print('file1:'+var_file1_name.get())
    #print('file2:'+var_file2_name.get())
    #print('string format: ' + var.get())
    file1_data = read_bin_file_2(var_file1_name.get(), sizeofnum_datatpye, var.get())
    file2_data = read_bin_file_2(var_file2_name.get(), sizeofnum_datatpye, var.get())

    ar_fd1 = np.array(file1_data)
    ar_fd2 = np.array(file2_data)
    plt.figure()
    plt.plot(ar_fd1 - ar_fd2)
    plt.show()

    
#btn_cancel
def soft_cancel():
    #print("this is cancel")
   
    os._exit(0) 
    
btn_plot = tk.Button(frame_execute,
                    text = '画出差异',
                    width = 8,
                    height = 1,
                    command = plot_diff).grid(row = 0,
                                               column = 0,
                                               sticky = W)
btn_cancel = tk.Button(frame_execute,
                    text = '取消',
                    width = 8,
                    height = 1,
                    command = soft_cancel).grid(row = 1,
                                               column = 0,
                                               sticky = W)
#print(this)

window.mainloop()

