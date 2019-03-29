#!/anaconda3/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'hh'

import os
import time
import requests
import multiprocessing

error = 0


def main(k, l, dd, j):
    global error
    i = 1
    img_url = ('http://222.25.2.68/photo/1%d%02d%02d%02d1/1%d%02d%02d%02d1%02d.jpg'
               % (k, l, dd, j, k, l, dd, j, i))
    response = requests.get(img_url)
    img_content = response.content

    # 判断班级是否存在
    if len(img_content) != 5100:
        os.mkdir('./image/1%d%02d%02d%02d1' % (k, l, dd, j))

        for i in range(1, 40):  # 学号
            try:
                img_url = ('http://222.25.2.68/photo/1%d%02d%02d%02d1/1%d%02d%02d%02d1%02d.jpg'
                           % (k, l, dd, j, k, l, dd, j, i))
                response = requests.get(img_url)
                img_content = response.content

                # 判断学号是否存在
                if len(img_content) != 5100:
                    with open('./image/1%d%02d%02d%02d1/1%d%02d%02d%02d1%02d.jpg'
                              % (k, l, dd, j, k, l, dd, j, i), 'wb') as fb:
                        fb.write(img_content)
            except:
                print(error)
                error += 1
                continue


if __name__ == '__main__':
    time_a = time.time()
    p = multiprocessing.Pool(32)

    for k in range(4, 8):  # 年级
        for l in range(1, 13):  # 学院
            for dd in range(1, 7):  # 专业
                for j in range(1, 24):  # 班级
                    p.apply_async(main, (k, l, dd, j))

    p.close()
    p.join()
    time_b = time.time()
    print(time_b - time_a)
