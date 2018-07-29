# _*_ coding: UTF-8 _*_
#返回数字的绝对值
print abs(-1223)
print abs(1222L)

#函数把除数和余数运算结果结合起来，返回一个包含商和余数的元组
print divmod(10,3)

#staticmethod() 函数staticmethod 返回函数的静态方法。
class C(object):
    @staticmethod
    def cus():
        print "静态方法"

#all()函数用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，如果是返回 True，否则返回 False。
print all(['a', 'b', 'c', 'd'])

#enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
list(enumerate(seasons, start=1))       # 小标从 1 开始
for i, element in enumerate(seasons):
    print i, element

#int() 函数用于将一个字符串或数字转换为整型。
print int(3)
print  int(3.6)
print int('12',6)
print int('0xa',16)
print int('10',8)

#ord() 函数是 chr() 函数（对于8位的ASCII字符串）或 unichr() 函数（对于Unicode对象）的配对函数，它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值，
# 如果所给的 Unicode 字符超出了你的 Python 定义范围，则会引发一个 TypeError 的异常。
print ord('a')

# str()函数将对象转化为适于人阅读的形式。
print str({'runoob': 'runoob.com', 'google': 'google.com'})

#any() 函数用于判断给定的可迭代参数 iterable 是否全部为 False，则返回 False，如果有一个为 True，则返回 True。
print any(['a', 'b', 'c', 'd'])  # 列表list，元素都不为空或0

#eval() 函数用来执行一个字符串表达式，并返回表达式的值。
x = 7
print eval( '3 * x' )
print eval('pow(2,2)')
print eval('2 + 2')
n=81
print eval("n + 4")

#isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()。
#isinstance() 与 type() 区别：
#type() 不会认为子类是一种父类类型，不考虑继承关系。
#isinstance() 会认为子类是一种父类类型，考虑继承关系。
#如果要判断两个类型是否相同推荐使用 isinstance()。
a = 2
isinstance (a,int)

#pow() 方法返回 xy（x的y次方） 的值。
print pow(100, 2)

#sum() 方法对系列进行求和计算。
print sum([0,1,2])
print sum((2, 3, 4), 3)

#execfile() 函数可以用来执行一个文件。
print execfile('hello.py')

#issubclass() 方法用于判断参数 class 是否是类型参数 classinfo 的子类。
class A:
    pass
class B(A):
    pass
print issubclass(B,A)

#bin() 返回一个整数 int 或者长整数 long int 的二进制表示。
print bin(10)

#file() 函数用于创建一个 file 对象，它有一个别名叫 open()，更形象一些，它们是内置函数。参数是以字符串的形式传递的
f = file('test.txt')

#iter() 函数用来生成迭代器。
lst = [1, 2, 3]
for i in iter(lst):
    print(i)