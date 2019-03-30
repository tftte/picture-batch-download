#!/anaconda3/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'hh'

"""
一个下载XATU教务系统所有学生照片的小程序
在代码相同路径新建一个'image'空文件夹
执行代码即可将所有照片下载到'image'文件夹中
"""

import multiprocessing
import os
import time

import requests

error = 0  # 网络也许会异常终端，看看终断次数


def main(grade, school, major, class_num):
    global error
    student_num = 1
    img_url = ('http://222.25.2.68/photo/1%d%02d%02d%02d1/1%d%02d%02d%02d1%02d.jpg'
               % (grade, school, major, class_num,
                  grade, school, major, class_num, student_num))
    response = requests.get(img_url)
    img_content = response.content

    # 判断班级是否存在
    if len(img_content) != 5100:
        os.mkdir('./image/1%d%02d%02d%02d1' % (grade, school, major, class_num))

        for student_num in range(1, 40):  # 学号
            try:
                img_url = ('http://222.25.2.68/photo/1%d%02d%02d%02d1/1%d%02d%02d%02d1%02d.jpg'
                           % (grade, school, major, class_num,
                              grade, school, major, class_num, student_num))
                response = requests.get(img_url)
                img_content = response.content

                # 判断学号是否存在
                if len(img_content) != 5100:
                    with open('./image/1%d%02d%02d%02d1/1%d%02d%02d%02d1%02d.jpg'
                              % (grade, school, major, class_num,
                                 grade, school, major, class_num, student_num), 'wb') as fb:
                        fb.write(img_content)
            except:
                print(error)
                error += 1
                continue


if __name__ == '__main__':
    time_a = time.time()
    p = multiprocessing.Pool(32)

    for grade in range(4, 8):  # 年级
        for school in range(1, 13):  # 学院
            for major in range(1, 7):  # 专业
                for class_num in range(1, 24):  # 班级
                    p.apply_async(main, (grade, school, major, class_num))

    p.close()
    p.join()
    time_b = time.time()
    print(time_b - time_a)  # 打印花费的时间，检测多进程的效果
