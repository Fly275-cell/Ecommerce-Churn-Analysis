"""
x=int(input("enter the first number:"))
y=int(input("enter the second number:"))
for j in range(y):
    for i in range(x):
        print("*",end="")
    print()
"""

"""
students=(
("01","Tom",60,70,80),
("02","Alice",80,70,90),
("03","Jack",70,90,70)
)
print("id\t name\tChinese\tMath\tEnglish\ttotal\t avg")
for s in students:
    total=s[2]+s[3]+s[4]
    avg=total/3
    print(f"{s[0]} \t {s[1]} \t {s[2]} \t {s[3]} \t {s[4]} \t {total} \t {avg:.1f}")
print()
Chinese=[s[2] for s in students]
Math=[s[3] for s in students]
English=[s[4] for s in students]
print(f"Chinese highest:{max(Chinese)},lowest:{min(Chinese)},avg:{sum(Chinese)/len(Chinese)}")
print(f"Math highest:{max(Math)},lowest:{min(Math)},avg:{sum(Math)/len(Math):.1f}")
print(f"English highest:{max(English)},lowest:{min(English)},avg:{sum(English)/len(English)}")
print()
print("excellent students:")
for s in students:
    total=s[2]+s[3]+s[4]
    avg=total/3
    if avg>75:
        print(f"{s[1]}")
"""

# shopping_cart={}
# menu="""
# #购物车系统#
# 1.添加购物车
# 2.修改购物车
# 3.删除购物车
# 4.查询购物车
# 5.退出购物车
# """
# print("欢迎使用购物车管理系统")
# while True:
#     print(menu)
#     choice=input("请选择需要执行的操作：")
#     match choice:
#         case "1":
#             goods_name=input("请输入商品名称：")
#             goods_price=float(input("请输入商品价格："))
#             goods_num=int(input("请输入商品数量："))
#             if goods_name in shopping_cart:
#                 print("该商品已存在，请重新选择")
#             else:
#                 shopping_cart[goods_name]={"price":goods_price,"num":goods_num}
#                 print("商品添加完毕")
#         case "2":
#             goods_name=input("请输入要修改的商品名称：")
#             if goods_name not in shopping_cart:
#                 print("该商品不存在")
#                 continue
#             goods_price=float(input("请输入商品最新的价格："))
#             goods_num=int(input("请输入商品最新的数量："))
#             shopping_cart[goods_name]={"price":goods_price,"num":goods_num}
#             print("商品修改完毕")
#         case "3":
#             goods_name=input("请输入要删除的商品名称：")
#             if goods_name not in shopping_cart:
#                 print("该商品不存在")
#             else:
#                 del shopping_cart[goods_name]
#                 print("该商品已删除")
#         case "4":
#             for goods_name in shopping_cart.keys():
#                 goods_info=shopping_cart[goods_name]
#                 print(f"商品名称：{goods_name},商品价格：{goods_info['price']},商品数量：{goods_info['num']}")
#         case "5":
#             print("Bye")
#             break
#         case _:
#             print("输入错误")


# import random
# for _ in range(100):
#     print(random.randint(1,100))

# from random import randint
# print(randint(1,100))

# from random import *
# print(randint(1,100))

# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
#
# class System:
#     def __init__(self):
#         self.student_list = []
#
#     def add_student(self):
#         name = input("输入姓名：")
#         score = int(input("输入分数："))
#         stu = Student(name, score)
#         self.student_list.append(stu)
#         print("添加成功")
#
#
# # 真正运行的地方
# sys = System()
# sys.add_student()


class Goods:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def __str__(self):
        return f"name:{self.name},price:{self.price}"
class ShoppingCart:
    def __init__(self):
        self.goods=[]
    def add_goods(self):
        name=input("enter the name:")
        for s in self.goods:
            if s.name==name:
                print("error")
                return
        price=float(input("enter the price:"))
        if price>0:
            self.goods.append(Goods(name,price))
            print("goods added")
        else:
            print("error")
    def show_goods(self):
        for s in self.goods:
            print(f"{s}")
    def run(self):
        print("Welcome to the shopping cart")
        while True:
            print("1.add goods 2.show all goods 3.exit")
            choice=int(input("enter your choice:"))
            try:
                if choice==1:
                    self.add_goods()
                elif choice==2:
                    self.show_goods()
                elif choice==3:
                    print("Good Bye")
                    break
                else:
                    print("error")
            except Exception as e:
                print(e)
ShoppingCart().run()

# try:
#     print("abc"[10])
#     print(name)
#     print(1 / 0)
# except Exception as e:
#     print("Error:",e)
# finally:
#     print("finally")
# def fun1():
#     print("hello")
#     fun2()
# def fun2():
#     print(world)
# if __name__=="__main__":
#     try:
#         fun1()
#     except Exception as e:
#         print(e)














