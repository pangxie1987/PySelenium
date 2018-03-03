#-*- coding:utf-8 -*-
'''
比较两张图片是否一致
'''
from PIL import Image
import math
import operator
from functools import reduce

def asser2photo(img1,img2):
    image1 = Image.open(img1)
    image2 = Image.open(img2)

    h1 = image1.histogram()
    h2 = image2.histogram()

    result=math.sqrt(reduce(operator.add, list(map(lambda a,b:(a-b)*2,h1,h2)))/len(h1))
    return result

if __name__=='__main__':
    img1='123.jpg'
    img2='223533.jpg'

    print(asser2photo(img1,img2))