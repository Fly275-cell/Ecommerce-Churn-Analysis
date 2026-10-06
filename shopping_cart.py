# shopping_cart={}
# while True:
#     print("""
#         1.添加购物车
#         2.修改购物车
#         3.删除购物车
#         4.查询购物车
#         5.退出购物车
#         """)
#     choice=input("enter the choice:")
#     if choice=="1":
#         name=input("enter the name:")
#         if name in shopping_cart:
#             print("the name already exists")
#             continue
#         price=float(input("enter the price:"))
#         num=int(input("enter the num:"))
#         shopping_cart[name]={"price":price,"num":num}
#         print("添加完毕")
#     elif choice=="2":
#         name=input("enter the name:")
#         if name not in shopping_cart:
#             print("the name does not exist")
#             continue
#         price=float(input("enter the price:"))
#         num=int(input("enter the num:"))
#         shopping_cart[name]={"price":price,"num":num}
#         print("修改完毕")
#     elif choice=="3":
#         name=input("enter the name:")
#         if name not in shopping_cart:
#             print("the name does not exist")
#         else:
#             del shopping_cart[name]
#             print("删除完毕")
#     elif choice=="4":
#         for name in shopping_cart:
#             info=shopping_cart[name]
#             print(f"{name},price:{info["price"]}$,num:{info["num"]}")
#     elif choice=="5":
#         print("Bye")
#         break
#     else:
#         print("error")
from random import choice

# system={}
# while True:
#     print("""
#     1.添加学生信息
#     2.修改学生信息
#     3.删除学生信息
#     4.查询学生信息
#     5.查询所有学生信息
#     6.查询成绩统计
#     7.退出系统
#     """)
#     choice=input("enter your choice:")
#     if choice=="1":
#         name=input("enter your name:")
#         if name in system:
#             print(f"the name already exists")
#             continue
#         Chinese=int(input("enter Chinese grade:"))
#         Math=int(input("enter Math grade:"))
#         system[name]={'Chinese':Chinese,'Math':Math}
#         print("添加完毕")
#     elif choice=="2":
#         name=input("enter your name:")
#         if name not in system:
#             print(f"the name doesn't exist")
#             continue
#         Chinese=int(input("enter Chinese grade:"))
#         Math=int(input("enter Math grade:"))
#         system[name]={'Chinese':Chinese,'Math':Math}
#         print("修改完毕")
#     elif choice=="3":
#         name=input("enter your name:")
#         if name not in system:
#             print(f"the name doesn't exist")
#             continue
#         del system[name]
#         print("删除成功")
#     elif choice=="4":
#         name=input("enter your name:")
#         if name not in system:
#             print(f"the name doesn't exist")
#             continue
#         info=system[name]
#         print(f"{name},Chinese:{info['Chinese']},Math:{info['Math']}")
#     elif choice=="5":
#         for i in system:
#             print(f"{i} {system[i]['Chinese']} {system[i]['Math']}")
#     elif choice=="6":
#         Chinese=[info['Chinese'] for info in system.values()]
#         Math=[info['Math'] for info in system.values()]
#         max_Chinese=max(Chinese)
#         max_Math=max(Math)
#         average_Chinese=sum(Chinese)/len(Chinese)
#         average_Math=sum(Math)/len(Math)
#         max_Chinese_name=[name for name,info in system.items() if info['Chinese']==max_Chinese][0]
#         max_Math_name=[name for name,info in system.items() if info['Math']==max_Math][0]
#         print("语文最高分",max_Chinese_name,max_Chinese)
#         print("数学最高分",max_Math_name,max_Math)
#         print("语文平均分",average_Chinese)
#         print("数学平均分",average_Math)
#     elif choice=="7":
#         break
#     else:
#         print("enter valid choice")







