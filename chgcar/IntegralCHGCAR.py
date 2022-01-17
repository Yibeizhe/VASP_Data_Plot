#!/usr/bin/python
# coding: utf-8

"""这个程序可以处理VASP输出文件CHGCAR,得到沿着某一方向的面积分电荷密度。"""

import math
import os
import time


def atom_list(vasp):
    """这个函数返回原子种类的字符串型列表。"""
    with open(vasp, 'r') as def_structure:
        # 跳过前5行
        for def_i in range(5):
            def_structure.readline()
        # 第6行原子种类行，将各个原子名称存入字符串型列表
        atom_name = def_structure.readline().split()
    return atom_name


def atom_num_list(vasp):
    """这个函数返回各个种类原子数目的整数型列表。"""
    with open(vasp, 'r') as def_structure:
        # 跳过前6行
        for def_i in range(6):
            def_structure.readline()
        # 第7行原子数目行，将各个种类原子数目存入整数型列表
        atom_num = map(int, def_structure.readline().split())
    return atom_num


def length_axis(vasp, axis):
    """这个函数返回指定文件中指定轴的长度。"""
    with open(vasp, 'r') as length_axis_file:
        # 跳过第1行
        length_axis_file.readline()
        # 读取晶格缩放系数
        lattice_scale = float(length_axis_file.readline().split()[0])
        print '晶格缩放系数为%f' % lattice_scale
        if axis == 'x':
            x_axis = map(float, length_axis_file.readline().split())
        elif axis == 'y':
            length_axis_file.readline()
            x_axis = map(float, length_axis_file.readline().split())
        else:
            length_axis_file.readline()
            length_axis_file.readline()
            x_axis = map(float, length_axis_file.readline().split())
        print '%s轴矢量为' % axis, x_axis
        length = lattice_scale * math.sqrt(x_axis[0] ** 2 + x_axis[1] ** 2 +
                                           x_axis[2] ** 2)
    return length


start_time = time.clock()
idir = raw_input('请输入你的真空层方向（x，y，z）：\n')
integralchgcar_data = []
vav = []
print '好的，%s是真空层方向。' % idir
print '看起来你的体系中有这些原子%s。' % atom_list('CHGCAR')
print '看起来对应原子的数目是%s。' % atom_num_list('CHGCAR')
with open('CHGCAR', 'r') as chgcar:
    with open('integralchgcar', 'w') as INTEGRALCHGCAR:
        # 跳过结构部分
        for j in range(9 + sum(atom_num_list('CHGCAR'))):
            chgcar.readline()
        print '我已经读完了结构部分数据，下面进入电势数据部分。'
        [NGX, NGY, NGZ] = map(int, chgcar.readline().split())
        print 'NGX = %d, NGY = %d, NGZ = %d' % (NGX, NGY, NGZ)
        NPLWV = NGX * NGY * NGZ
        print '一共有%d个数据' % NPLWV
        if idir == 'x':
            NOUT = NGX
        elif idir == 'y':
            NOUT = NGY
        elif idir == 'z':
            NOUT = NGZ
        else:
            NOUT = '我觉得你选的真空层不规范。'
            print NOUT
            exit()
        my_length = length_axis('CHGCAR', idir)
        print '%s轴长度为%f A.' % (idir, my_length)
        # scale = 1.0 / float(NPLWV / NOUT)
        scale = 1.0
        print 'scale = %f' % scale
        # print os.system('grep fermi OUTCAR | tail -1')
        # fermi = 0.0
        # 将所有的数据存入列表integralchgcar_data
        for lines in chgcar.readlines():
            line = lines.strip('\n')
            integralchgcar_data += line.split()
        integralchgcar_data = map(float, integralchgcar_data)
        if idir == 'x':
            vav += [0] * NGX
            for i in range(NGX):
                for j in range(NGZ):
                    for k in range(NGY):
                        IPL = i + (k + j * NGY) * NGX
                        vav[i] += integralchgcar_data[IPL] * scale
                INTEGRALCHGCAR.write('%d   %f   %f\n'
                                     % (i + 1, my_length / (NOUT - 1) * i,
                                        vav[i]))
        elif idir == 'y':
            vav += [0] * NGY
            for i in range(NGY):
                for j in range(NGZ):
                    for k in range(NGX):
                        IPL = k + (i + j * NGY) * NGX
                        vav[i] += integralchgcar_data[IPL] * scale
                INTEGRALCHGCAR.write('%d   %f   %f\n'
                                     % (i + 1, my_length / (NOUT - 1) * i,
                                        vav[i]))
        else:
            vav += [0] * NGZ
            for i in range(NGZ):
                for j in range(NGY):
                    for k in range(NGX):
                        IPL = k + (j + i * NGY) * NGX
                        vav[i] += integralchgcar_data[IPL] * scale
                INTEGRALCHGCAR.write('%d   %f   %f\n'
                                     % (i + 1, my_length / (NOUT - 1) * i,
                                        vav[i]))
# print '我猜测真空能级值为%f eV' % max(vav)
# print '我猜测功函数为%f eV' % (max(vav) - fermi)
print '我把输入写入文件integralchgcar中，格式为第一列格点，第二列长度，第三列面积分电荷密度。'
print '耗时%f S' % (time.clock() - start_time)
