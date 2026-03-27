# class A:
#     def __init__(self,a=None):
#         self.a=a
#         print(id(self))
# obj=A(45)
# print(id(obj))
# obj2=A(30)
# print(id(obj2))

# def func(**kwarg):
#     print(kwarg)
# func(one="one", name="two")

def func(**kwarg):
    print(kwarg)
# func(None="one", name="two")#error
# func(True="one", name="two")#error
# func(1="one", name="two")#error
func(__Main__="one", name="two")

def func(**kwarg):
    print(kwarg)
func()

def func(**kwarg):
    print(kwarg)
# func(one="one", "name"="two") # SyntaxError: keyword can't be an expression

# def func(**kwarg):
#     print(kwarg)
# func(1="one", 2="two") # SyntaxError: keyword can't be an expression

def func (*args):
    print(args)
func(1,2,3,4)

# def func (*args):
#     print(args)
# func()

# # # def func (*args):
# # #     print(args)
# # # func(1,2,"three",{"name":"four"}) # TypeError: func() got an unexpected keyword argument 'name'

# # # def func (*args,**kwargs):
# # #     print(args)
# # #     print(kwargs)
# # # func([],{1:'helo'},nma='kk')


class a:
    def __init__(self,a):
        self.__var=a
    def change(self,b):
        self.__var=b
        #return self.__var
    def dis (self):
        print(self.__var)
        
obj=a(15)
obj.dis()
obj.change(20)
obj.dis()

# # # b=a(5)
# # # b.change(b)
# # # obj.dis()
# # # b.dis()

# # # def adds(d,e):
# # #     return d+e
# # # def adds(a,b,c):
# # #     return a+b+c
# # # # print(adds(d=1,e=2)) #give type error because Python does not support traditional function 
# # # # overloading based on the number of parameters (arity) in the same scope [1]. 
# # # # The interpreter only maintains one active definition for a given function name at any time
# # # print(adds(1,2,3))

# # # def adds(d,e):
# # #     return d+e
# # # def adds(*args):
# # #     sum=0
# # #     for a in args:
# # #         sum+=a
# # #     return sum
# # # print(adds(d=2,e=5))

# # # class A:
# # #     pass
# # # print(dir(A))

# # # obj=A

# # # # print(A.__dict__)
# # # print(obj.__class__)
# # # print(A.__doc__)
# # # print(A.__eq__)

# declare our own string class
class String:
    
    # magic method to initiate object
    def __init__(self, string):
        self.string = string 
        
    # print our string object
    def __repr__(self):
        return 'Object: {}'.format(self.string)
        
    def __add__(self, other):
        return self.string + other

# Driver Code
if __name__ == '__main__':
    
    # object creation
    string1 = String('Hello')
    
    # concatenate String object and a string
    print(string1 +' Geeks')

# # # class A:
# # #     # a=10
# # #     def __new__(cls,s):
# # #         cls.a=32
# # #         print("Creating instance")
# # #         return super(A, cls).__new__(cls)
    
# # #     def __init__(self,c):
# # #         self.c=c
# # #         print(c)
# # #         print(self.a)
# # #         print("Initializing instance")

# # # b=A(12)

class GeeksforGeeks:
    def __str__(self):
        return "GeeksforGeeks Instance"

class Geek:
    def __new__(cls):
        return GeeksforGeeks()
    
    def __init__(self):
        print("Inside init")

print(Geek())

# # class a:
# #     def __init__(self,b):
# #         self.b=b
# #     def __add__(self, other):
# #         return self.b + other
# # obj=a(10)
# # obj2=a(30)
# # print(obj+20)

# # class a:
# #     def __init__(self,b):
# #         self.b=b
# #     def __neg__(self):
# #         return self.b*5
# # obj=a(10)
# # obj2=a(30)
# # print(-obj)

# # import math
# # class b:
# #     def __init__(self,b):
# #         self.b=b
# #     def __round__(self,c):
# #         return self.b*c
# # obj=b(1)
# # print(round(obj,10))

# # Python program to demonstrate writing of __repr__ and
# # __str__ for user defined classes

# # A user defined class to represent Complex numbers
# class Complex:

#     # Constructor
#     def __init__(self, real, imag):
#         self.real = real
#         self.imag = imag

#     # For call to repr(). Prints object's information
#     # def __repr__(self):
#     #     return 'Rational(%s, %s)' % (self.real, self.imag)    

#     # For call to str(). Prints readable form
#     def __str__(self):
#         return '%s + i%s' % (self.real, self.imag)    


# # Driver program to test above
# t = Complex(10, 20)

# # Same as "print t"
# # print (str(t))
# print (repr(t))

class A:
    a=10
    b=20
    def dis(cls):
        return cls.a+cls.b
del A


# Python program to demonstrate
# __delete__


class Example(object):

    # Initializing
    def __init__(self):
        print("Example Instance.")

    # Calling __delete__
    def __delete__(self, instance):
        print ("Deleted in Example object.")


# Creating object of Example
# class as an descriptor attribute
# of this class
class Foo(object):
    exp = Example()

# Driver's code
f = Foo()
# del f.exp

# defining the class.
class gfg:
    
    # defining the slots.
    __slots__ =('course', 'price',"b")
    
    def __init__(self,b):
        
        # initializing the values
        self.course ='DSA Self Paced'
        self.price = 2333
        self.b=b

# create an object of gfg class
a = gfg(32)

# print the slot
# print(a.__slots__)

# print the slot variable
print(a.course, a.price,a.b)
# print(a.__dict__)
print(a.__getstate__)


class b(gfg):
    def __init__(self,data):
        super().__init__(data)
obj=b(12)
print(obj.course, obj.price) 