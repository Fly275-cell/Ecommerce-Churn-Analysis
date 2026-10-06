# class Car:
#     wheel=4
#     def __init__(self,color,brand,price):
#         self.color=color
#         self.brand=brand
#         self.price=price
#         print("added")
#     def running(self):
#         print(f"{self.brand} in {self.color} is running")
#     def cost(self,discount,rate):
#         return self.price*(discount+rate)
# c1 = Car("red", "Toyota", 50000)
# print(c1.__dict__)
# c2 = Car("yellow", "Toyota", 50000)
# print(c2.__dict__)
# c1.running()
# print("Total cost is:",c1.cost(discount=0.8,rate=0.1))
# print(c1.wheel)
# print(c2.wheel)



# class Student:
#     def __init__(self,name,Chinese,Math):
#         self.name=name
#         self.Chinese=Chinese
#         self.Math=Math
#     def __str__(self):
#         return f"name:{self.name},Chinese:{self.Chinese},Math:{self.Math},total:{self.Chinese+self.Math}"
#     def update(self,Chinese=None,Math=None):
#         if Chinese is not None:
#             self.Chinese=Chinese
#         if Math is not None:
#             self.Math=Math
#
# class System:
#     version=1.0
#     def __init__(self):
#         self.student_list=[]
#     def add_student(self):
#         name=input("enter student name:")
#         for s in self.student_list:
#             if s.name==name:
#                 print("Error")
#                 return
#         Chinese=int(input("enter the Chinese score:"))
#         Math=int(input("enter the Math score:"))
#         if 0<=Chinese<=100 and 0<=Math<=100:
#             stu=Student(name,Chinese,Math)
#             self.student_list.append(stu)
#             print("OK")
#         else:
#             print("Error")
#     def update_student(self):
#         name=input("enter student name:")
#         for s in self.student_list:
#             if s.name==name:
#                 print(f"{s}")
#                 Chinese = int(input("enter the Chinese score:"))
#                 Math = int(input("enter the Math score:"))
#                 if 0 <= Chinese <= 100 and 0 <= Math <= 100:
#                     s.update(Chinese,Math)
#                     print("OK")
#                     print(f"{s}")
#                     return
#                 else:
#                     print("Error")
#         print("Error")
#     def delete_student(self):
#         name=input("enter student name:")
#         for s in self.student_list:
#             if s.name==name:
#                 self.student_list.remove(s)
#                 print("OK")
#                 return
#         print("Error")
#     def query_student(self):
#         name=input("enter student name:")
#         for s in self.student_list:
#             if s.name==name:
#                 print(f"{s}")
#                 return
#         print("Error")
#     def list_student(self):
#         for s in self.student_list:
#             print(s)
#     def run(self):
#         print(f"welcome to the system {System.version}")
#         while True:
#             print("1. add student  2.update student  3.delete student  4.query student  5.all student  6.exit")
#             choice=int(input("enter choice:"))
#             match choice:
#                 case 1:
#                     self.add_student()
#                 case 2:
#                     self.update_student()
#                 case 3:
#                     self.delete_student()
#                 case 4:
#                     self.query_student()
#                 case 5:
#                     self.list_student()
#                 case 6:
#                     print("bye")
#                     break
#                 case _:
#                     print("Error")
# sys=System()
# sys.run()























