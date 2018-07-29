#!/usr/bin/python
# -*- coding: utf-8 -*-
from PIL import Image

image_name = 'res/test.png'
img = Image.open(image_name) # type: Image.Image
#assert isinstance(img,Image.Image)  指定对象类型
#img = img.convert('L')
#img.save('huidu.png')
print(img.size)
w, h = img.size

if w > 100:
    h = 100
    w = 100
img = img.resize((w, h))
img.save("suoxiao.png")

#将缩小的图片像素点的颜色值转为字符并存放到列表
#保存像素字符的列表
data = []
#替换字符列表（从左到右颜色是逐渐加深）
chars = [' ',',','1','+','n','D','@','M']
for i in range(0,h):
    line =  ''
    print('i:'+str(i))
    for j in range(0,w):
        print('j:' + str(j))
        #取出像素点的值
        pi = img.getpixel((j,i))
        print( pi)
        #用字符去替换像素点的颜色值
        for k in range(0,8):
            print('k:' + str(k))
            if pi[0] <(k+1)*32:
                line += chars[7-k]
                break
    data.append(line)
f = open(image_name+'.txt','w')
for d in data:
    print(d)
    f.write(d)
f.close()
print('转换成功！')