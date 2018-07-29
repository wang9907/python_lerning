# _*_ coding: UTF-8 _*_
str = 'Hello World'
print  str
print  str[0]
print str[1:5]

list =['runoob',786,2.86,'john',70.2]
tinylist = [123,'john']
print list
print list[0]
print(list[1:3])
print list * 3
print list + tinylist

tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')
print tuple
print tuple[1]
print tuple * 3
print tuple + tinytuple

dict = {}
dict['one']='This is one'
dict[2]='This is two'

tinydict = {'name':'john','code':6745,'dept':'sales'}

print dict['one']
print dict[2]
print tinydict
print tinydict.keys()
print tinydict.values()

list.append("eeee")