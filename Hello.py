# print("Hello World!")
# print("Hello Python!")
# print(True-1)
# print(False+6)
# num=20.7
# num=num+50
# print(num)
# num=num+50
# print(num)
#
# x,y=20.7,50
# print("一个月后的播放量",x+y)
# print("二个月后的播放量",x+2*y)

# a=10
# b=20
# c=a
# a=b
# b=c
# print(a,b)
#
# print(type(None))

# s="""
# Hello:
# My name is Python
# """
# print(s)
#
# m='It\'s good'
# print(m)

# name="Fly"
# age="27"
# pro="统计学"
# hobby="Python"
# print(f"大家好，我是{name}，今年{age}，学习的专业是{pro}，爱好{hobby}")

# name=input("请输入您的名字：")
# age=input("请输入您的年龄：")
# print(f"您的姓名为{name},年龄为{age}")

# password=input("请输入您的密码：")
# withdraw=int(input("请输入取款金额："))
# print(f"您的余额为：{10000-withdraw}")

# x=float(input("请输入x的值："))
# y=float(input("请输入y的值："))
# z=float(input("请输入z的值："))
# print((x+y+z)/3)

# r=float(input("enter the radius :"))
# pi=3.14159
# print("the area of the circle is",pi*r*r,"the perimeter is",2*pi*r)

# num=float(input("Enter a number: "))
# print(not(num<10 or num>20))

# x=input("enter your account:")
# y=input("enter your password:")
# if int(x)==188888 and int(y)==666888:
#     print("you are logged in")
# else:
#     print("you are not logged in")

# x=int(input("enter a year:"))
# if (x%100!=0 and x%4==0) or (x%400==0):
#     print("leap year")
# else:
#     print("not leap year")
"""
x=int(input("enter the number:"))
if x>=85:
    print("excellent")
elif 60<=x<=80:
    print("average")
else:
    print("poor")
"""
from pickletools import string4

"""
a=float(input("enter the first number:"))
b=float(input("enter the second number:"))
c=float(input("enter the third number:"))
if a==b==c>0:
    print("equilateral triangle")
elif (a+b>c>0 and a+c>b>0 and b+c>a>0) and (a==b or b==c or c==a):
    print("isosceles triangle")
elif (a+b>c>0 and a+c>b>0 and b+c>a>0):
    print("triangle")
else:
    print("not triangle")
"""

# x=float(input("enter the first number:"))
# y=float(input("enter the second number:"))
# o=input("enter(+ - * /):")
# match o:
#     case "+":
#         print(x+y)
#     case"-":
#         print(x-y)
#     case "*":
#         print(x*y)
#     case "/" if y!=0:
#         print(x/y)
#     case _:
#         print("error")
"""
i=1
while i<=10:
    print("Hello! World!")
    i+=1
else:
    print("end")
"""
"""
i=0
total=0
while i<=100:
    total+=i
    i+=2
print(total)
"""
"""
m=input("enter the string:")
for i in m:
    print(i)
"""
# Total=0
# for i in range(1,101,2):
#     Total+=i
# print(Total)
# Total=0
# for i in range(100,500):
#     if i%3==0:
#         Total+=i
# print(Total)

# m=int(input("enter the first number:"))
# n=int(input("enter the second number:"))
# for j in range(n):
#     for i in range(m):
#         print('*',end='')
#     print()
"""
for j in range(3):
    print("外层j =", j)
    for i in range(5):
        print("  内层i =", i)
"""
"""
for j in range(1,10):
    for i in range(1,j+1):
        print(f"{i}x{j} = {i*j}", end=" ")
    print()
"""
"""
for i in range(4):
    for j in range(4):
        print("1 2",end=" ")
    print()
    for k in range(4):
        print("2 1",end=" ")
    print()
"""
"""
while True:
    x = input("enter the account:")
    y = input("enter the password:")
    if x=="123456" and y=="666666":
        print("login successful")
        break
    elif x=="234567" and y=="888888":
        print("login successful")
        break
    else:
        print("wrong password or username")
"""
"""
i=1
while i<6:
    x=input("enter the account:")
    y=input("enter the password:")
    if x=="123456" and y=="666666":
        print("login successful")
        break
    elif x=="234567" and y=="888888":
        print("login successful")
        break
    else:
        print("wrong password or username")
    i=i+1
else:
    print("locked")
"""
"""
import random
x=random.randint(1,100)
while True:
    y=int(input("enter the number:"))
    if y<x:
        print("low")
    elif y>x:
        print("high")
    else:
        print("ok")
        break
"""
"""
s="ncksdhfkewhfowefo"
print(s.count("f"))
"""
# s=[0,1,2,3,4,5,True,"Hello"]
# print(type(s))
# s[-1]="Python"
# print(s[-1])
# del s[6]
# print(s)
# for i in s:
#     print(i)
# print(s[0:-2:1])
# s.append(None)
# s.insert(7,"Pycharm")
# s.extend([True,False])
# print(s)

# s=[0,100,200,300,400,500,600]
# print(s)
# s.insert(3,300)
# print(s)
# s.remove(300)
# print(s)
# s.pop(2)
# print(s)
# s.insert(2,200)
# print(s)
# s.reverse()
# print(s)
# s.sort()
# print(s)
# s=[]
# for i in range(10):
#     x=int(input("enter the number:"))
#     s.append(x)
# print(s)
# s.sort()
# print(s[0])
# print(s[9])
# print(sum(s)/len(s))

# s1=[0,1,2,3,4,5,6]
# s2=[5,6,7,8,9]
# s3=[*s1,*s2]
# print(s3)
# s=[]
# for i in s3:
#     if i not in s:
#         s.append(i)
# print(s)

# s1=[1,2,3]
# s2=[4,5,6]
# s3=s1+s2
# print(s3)

# s=[i**2 for i in range(1,21)]
# print(s)

# x=[0,1,2,3,4,5]
# y=[i**2 for i in x if i%2==0]
# print(y)
"""
s="Hello-Python"
print(s.find("l"))
print(s.count("o"))
print(s.upper())
print(s.lower())
print(s.split("-"))
print(s.strip())
print(s.replace("-","_"))
print(s.startswith("H"))
print(s.endswith("o"))
"""
"""
x=input("enter the string:")
y=(x[::-1])
z=y.upper()
s=[i for i in z]
for i in s:
    print(i)
"""
"""
x=input("enter the string:")
y=(x[::-1])
if x==y:
    print("yes")
else:
    print("no")
"""
# s=(0,1,2,3)
# a,b,c,d=s
# print(a,b,c,d)
# a=10
# b=20
# a,b=(b,a)
# print(a)
# print(b)
# s1={5,3,0,-1,5}
# print(s1)
# s2=set()
# print(type(s2))
# s3={}
# print(type(s3))
# s={3,-1,0,5,6,5}
# print(s)
# s.add(9)
# print(s)
# s.remove(9)
# print(s)
# s.pop()
# print(s)
# s.clear()
# print(s)
"""
s1={1,2,3,4}
s2={2,3,5}
print(s1.difference(s2))
print(s1.union(s2))
print(s1.intersection(s2))
print(s1&s2)
print(s1-s2)
s3={i for i in s1 if i not in s2}
print(s3)
list=[*s1,*s2]
for i in list:
    print(f"{i} occurs {list.count(i)} times")
"""
# d={}
# d["Tom"]=300
# print(d)
# d["Tom"]=200
# print(d)
# d["Alice"]=500
# print(d)
# del d["Tom"]
# print(d)

# d={"Tom":500,"Lily":600}
# for info in d.values():
#     print(f"{info}")

# def f():
#     print("hello")
# f()
# f()

# def circle_area(r):
#     return 3.14*r**2
# print(circle_area(10))
#
#
# def rectangle_area(l,w):
#     """
#
#     :param l: 长度
#     :param w: 宽度
#     :return: 面积
#     """
#     return l*w
# print(rectangle_area(5,4))
# # help(rectangle_area)
#
# def circle_area_length(r):
#     """
#     根据圆的半径计算圆的面积和周长
#     :param r: 半径
#     :return: 面积，周长
#     """
#     return 3.14*r**2,round(2*3.14*r,1)
# print(circle_area_length(10))
# area,length=circle_area_length(10)
# print(area)
# print(length)

# def count_aeiou(s):
#     """
#     统计字符串中元音字母个数
#     :param s: 字符串
#     :return: 元音字母个数
#     """
#     num=0
#     for i in s:
#         if i in "aeiouAEIOU":
#             num+=1
#     return num
# print(count_aeiou("hello"))
#
# def score(score_list):
#     max_score=max(score_list)
#     min_score=min(score_list)
#     avg_score=round(sum(score_list)/len(score_list),1)
#     return max_score,min_score,avg_score
# print(score([1,2,3,4,5,6,7,8,9]))

# def f(score):
#     if score>=90:
#         return "A"
#     elif score>=75:
#         return "B"
#     elif score>=60:
#         return "C"
#     else:
#         return "D"
# print(f(90))

# def f(s):
#     if s==s[::-1]:
#         return True
#     else:
#         return False
# print(f("level"))
"""
def data(*args):
    min_data=min(args)
    max_data=max(args)
    avg_data=sum(args)/len(args)
    return min_data,max_data,avg_data
print(data(1,2,3,4,5,6,7))

def data(*args,**kwargs):
    min_data=min(args)
    max_data=max(args)
    avg_data=sum(args)/len(args)
    if kwargs.get("round") is not None:
        avg_data=round(avg_data,kwargs.get("round"))
    if kwargs.get("print"):
        print(f"{min_data},{max_data},{avg_data}")
    return min_data,max_data,avg_data
print(data(1,2,3,4,5,6,7,round=3,print=True))
"""

# def add(x,y):
#     return x+y
# def f(x,y,oper):
#     return oper(x,y)
# print(f(1,2,add))

# f=lambda x,y:x+y
# print(f(1,2))
#
# list=["C","Java","Python","SQL"]
# list.sort(key=lambda a:len(a),reverse=True)
# print(list)

# def f(n):
#     T=1
#     for i in range(n,0,-1):
#         T=T*i
#     return T
# print(f(0))
#
# def j(n):
#     if n==1:
#         return 1
#     else:
#         return n*j(n-1)
# print(j(5))

# def calc_order_cost(*args:tuple[str,float,int],coupon=0,score=0,delivery=0.0):
#     total_price=[goods[1]*goods[2] for goods in args]
#     total_cost=sum(total_price)
#     if total_cost>=5000 and coupon<=total_cost:
#         total_cost-=coupon
#     if total_cost>=5000 and score//100<=total_cost:
#         total_cost-=score//100
#     total_cost+=delivery
#     return total_cost
# print(calc_order_cost(("鼠标",188,2),("键盘",388,1),delivery=9.9))

















































































