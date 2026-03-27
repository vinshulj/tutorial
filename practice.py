# def gen():
#     for i in range(10):
#         yield i

# print(next(gen()))
# print(next(gen()))
# print(next(gen()))

# #Now this will print 0 0 0 
# # why because we dont create a generator instance where we can preserve the state of function

# #Now to solve this 
# a=gen()
# print(next(a))
# print(next(a))
# print(next(a))
 
# a=10
# b=5
# a,b=b,a
# print(a,b ,sep="\t")

# a="abc"
# def fun():
#     a=32
#     return a
# print(a,fun(),sep="\t")

# a=["a","b","c"]
# def fun():
#     del a
#     return 5
# print(a,fun(),sep="\t")

# def my_function():
#     x = 5
#     return x
# print(x)    

# PI=45
# PI=32

# a = b + 10
# x = "10.5"
# y = int(float(x))
# print(y)


# my_data = {'name': 'Alice', 'scores': [85, 92, 78], 'address': {'city': 'NYC', 'zipcode': '10001'}}
# print(my_data["address"]['zipcode'])
# # print(my_data['scores'][3])

# a = "Python"
# b = a[1:4]
# print(b)

# a={1,2,3}
# b={3,4,5}
# print(a ^ b)

# word = "hello"
# word[0] = 'H'
# print(word)
# x = int("abc")


# string = "hello"
# converted_list = list(string)
# converted_tuple = tuple(string)

# print(converted_list)  # What does this print?
# print(converted_tuple) # What does this print?

# my_dict = {"a": 1, "b": 2, "c": 3}
# list_of_keys = list(my_dict)
# tuple_of_items = tuple(my_dict.items())

# print(list_of_keys)  # What will this print?
# print(tuple_of_items)  # What will this print?

# pi = 3.1415926535
# pi_str = str(pi)
# print(pi_str)


# a=5
# b=10
# c=6
# d=10
# print(a<b>c<d)


# x=10
# def fun():
#     global x
#     x+=5
# print(fun(),x)

# x = 15
# y = 5

# if x > 10 and y < 10:
#     print("x is greater than 10, and y is less than 10")


# def fun(a,b):
#     return a+b
# print(fun(1,2))

# def fun(name): print("Hello "+name)
# fun("elex")


# def fun3():
#     print("hi")
#     exit()
#     print("by")
# fun3()


# def fun(a,b):
#  return a+b
# print(fun(0,10))

# dic={
#     "a":"agdd",
#     "b":"sk"
# }
# print(dic)


# lis=[i for i in range(10) if i%3==0]
# print(lis)


# a="32" 
# b="40"
# c=[a,b]
# print("*".join(dic))


# a=lambda x:print(x) if x>10 else print("enter no. grater than 10")
# a(5)

# b=lambda x:lambda y:x+y
# # print(b(10))
# c=b(10)
# print(c(20))


# s={1,2,3,4}
# s1={4,5,6,7}
# print(s.difference_update(s1))
# print(s)

# def rfun(n):
#     if n==1:
#          return 1
#     elif n<=0:
#         return 0
#     return rfun(n-1)+rfun(n-2)
# for i in range(10):
#     print(rfun(i))


# with open("dum.txt","r+") as f:
#     print(f.readline(),end="")
#     print(f.tell())
#     print(f.readline(),end="")
#     print(f.readline(),end="")
#     # f.seek(0)
#     f.write("swayam dhamunia ")
#     f.seek(0)
#     print(f.tell())
#     print(f.read(5))
#     print(f.tell())

# class class1:
#     def __new__(cls,n,m):
#         return None
#     def __init__(self,fname,lname):
#         self.fname=fname
#         self.lname=lname
#     def __add__(self,other):
#         return self.fname+","+other.fname
#     def __sub__(self, other):
#         return self.fname+ " " +other.lname
    
# obj=class1("vin","jain")
# obj2=class1("shul","kumar")
# print(type(obj))
# print(obj-obj2 )


# import re 
# string="fjh gggu ukyy o8oy ygf utyg itg7 u8y yih"
# print(re.findall("\w*[u]\w*",string))
# lst = [1, 2, 3, 4, 5]
# new_lst = [x**2 for x in lst if x % 2 == 0]
# print(new_lst)
# 
# lst = [0, 1, 2, 3, 4]
# new_lst = [x if x % 2 == 0 else x**2 for x in lst]
# print(new_lst)
# 
# lst = [1, 2, 3, 4, 5]
# new_lst = [x+y for x in lst for y in lst if x != y]
# print(new_lst)
# lst = [1,2,3,4,6,5]
# # new_lst = [y for x in lst for y in x if y % 2 == 0]
# new_lst = [[x, x**2] for x in lst if x % 2 == 0]

# print(new_lst)

# t = (1, 2, 3, 4, 5)
# new_t = t * 2
# t = (10, 20, 30, 40)
# new_t = t + (50, 60)
# x, y, *z = t
# print(x, y, z)
# # new_t = t[1, 2]
# t = (1, 2, 3, 4, 5)
# new_t = t[::2]
# t[1:3] = (99, 100)

# print(new_t)
# s = "hello world"
# print(s[::2])
# # s[1] = 'a'

# # s[1:4] = "xyz"
# print(s*3)

# s = "I am learning Python"
# print("".join(s))
# s = {1, 2, 3, 4, 5}
# new_s = {x ** 2 for x in s}
# print(new_s)

# s1 = {1, 2, 3, 4}
# s2 = {3, 4, 5, 6}
# print(s1 <= s2
# )

# d = {'a': 1, 'b': 2, 'c': 3}
# d['d'] = 4
# del d['b']
# d = {'a': 1, 'b': 2, 'c': 3}
# print(d.get('d'))

# print(d)
# d = {'a': 1, 'b': 2, 'c': 3}
# print(d.items())
# d = {'a': 1, 'b': 2, 'c': 3}
# d.update({'d': 4})
# print(d)

# d = {'a': 1, 'b': 2, 'c': 3}
# del d['d']

# class A:
#     def method(self):
#         return "A"

# class B:
#     def method(self):
#         return "B"

# class C(A, B):
#     pass

# c = C()
# print(c.method())


# numbers = [1, 2, 3]
# iterator = iter(numbers)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# numbers = [1, 2, 3]
# iterator = iter(numbers)
# print(next(iterator))
# iterator = iter(numbers)  # Reinitialize the iterator
# print(next(iterator))


# numbers = [1, 2, 3]
# iterator = iter(numbers)
# print(next(iterator))
# print(next(iterator))
# next(iterator)


# def en))

# def outer():
#     x = 5
#     def inner():
#         nonlocal x
#         x += 1
#         return x
#     return inner

# closure = outer()
# print(closure())
# print(closure())


# def decorator(func):
#     def wrapper(x):
#         print(f"Calling function with argument {x}")
#         return func(x)
#     return wrapper

# @decorator
# def square(n):
#     return n ** 2

# print(square(4))


# def add_2(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result + 2
#     return wrapper

# @add_2
# def add_numbers(a, b):
#     return a + b

# print(add_numbers(3, 5))
# def multiplier(factor):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             result = func(*args, **kwargs)
#             return result * factor
#         return wrapper
#     return decorator

# @multiplier(3)
# def add(a, b):
#     return a + b

# print(add(2, 3))

# import re

# pattern = r"\b\w{5}\b"
# text = "This is a simple test sentence."
# matches = re.findall(pattern, text)
# print(matches,end="\n")

# numbers = [1, 2, 3, 4, 5]
# result = [(lambda x: x * 2)(num) for num in numbers]
# print(result)
# if None



    # print('

# if None:
#     print('-1')
# else:
#     print('eseee')
    
    
# for i in range(5):
    # print(i)
    # break
# else:
    # print("else")
    
    
    
# try:
#     n=1
# except ZeroDivisionError as z:
#     print(z)
# else:
#     print('he')
    
    
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = [lambda x: x if x % 2 == 0 else pass for x in numbers]
# result = [i(i) if i else None for i in even_numbers]
# print(result)
# print(even_numbers)

# from functools import reduce

# words = ["Hello", " ", "World", "!"]

# # Function to concatenate two strings
# def concat(x, y):
#     return x + y

# result = reduce(concat, words)
# print(result)
# lis=[1,2,3,4,5,6,7,8,9]
# group={True:[x for x in lis if x%2==0],False:[x for x in lis if x%2!=0]}
# print(group)

# data = [1, 2, 3, 4, 5]

# result = [
#     x * y
#     for x in data
#     if x % 2 == 0
#     for y in range(x)
#     if y % 2 != 0
# ]

# print(result)

# def fab(n):
#     if n<2:
#         return n
#     return fab(n-1)+fab(n-2)
# fab(5)

# print(list(map(str,range(3))))

# dic={1:2}
# dic["Key"].append(1)
# print(dic)

# import json

# json.dumps({1:[1]})

# with open("dum.txt") as f:
#     del f

# *a,b=1,*c=10

# n = 10
try:
    res = 10 / 0
except ZeroDivisionError as e:
    print(e)

# from itertools import chain
# print(list(chain([1,2],[3])))

