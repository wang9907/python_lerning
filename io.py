#_*_ coding: utf-8 _*_
import os
print 'python 是一个非常棒的语言，不是吗？'
#inp = raw_input("请输入你姓名")
#print "你的名字是：",inp
#str = input("请输入：")

fo = open("test.png.txt","r+")
print "文件名:",fo.name
print  "是否已关闭：",fo.closed
print "访问模式：",fo.mode
print "末尾是否强制加空格",fo.softspace

#fo.write("hello world !hello word ")
#fo.close()

#a = fo.read();
#print a
#fo.close()

