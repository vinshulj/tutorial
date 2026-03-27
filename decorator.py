def out(x):
    def inner(y):
        z=x+y
        print(z)
        def ininner(k):
            return print(x+y+k)
        return ininner
    def exinner(y):
        print(x-y)
        def inexinner(z):
            return print(x-y-z)
        return inexinner
      
    return exinner,inner

obj=out(10)
# obj1=obj(20)
ex,inner=obj # we need to perform unpacking as object is in form of tuple
exx=ex(20)
inn=inner(20)
exx(30)
inn(30)

#__call()__ method
class Gfg:
    def __init__(self):
        print("Instance Created")
    
    def __call__(self):
        print("Instance is called via special method")

e = Gfg()
e()

class vin:
    def __call__(self,x,y):
        return x*y
obj2=vin()
print(obj2(10,20))

def out(x):
    def inner(y):
        z=x+y
        print(z)
    def __call__(self,w,a):
        return self.x * w *a
    return inner
obj3=out(10)
# obj3(20,30) #call method not work because call method work on class ,not on the function and return inner make obj a function it is not 
# a class instance anymore
obj3(20) 

# decorator
def vins(fun):
    def inner():
        print("hi i am inner function")
        fun()
        print("inner function close")
    return inner

def decorator():
    print("i am decorator")

dec=vins(decorator)
dec()
print(vins(decorator))

@vins
def decorator2():
    print("i am the real one")
decorator2()

# using same function for multiple decorator
def vins(fun):
    def inner(a,b):
        print(20*"*")
        print(20*"*")
        fun(a,b)
        print(20*"*")
        print(20*"*")
    return inner


@vins
def decorator2(a,b):
    print(f"{a}+{b} = {a+b}")

@vins
def decorator3(a,b):
    print(f"{a}*{b} = {a*b}")
    
decorator2(10,20)
decorator3(10,20)

# multiple funtion as decorator

def add(func):
    def inner(a,b):
       print(20*"*")
       print(f"{a}+{b}={a+b}")
       func(a,b)
    return inner
def sub(func):
    def inner(a,b):
       print(f"{a}-{b}={a-b}")
       func(a,b)
    return inner
def mul(func):
    def inner(a,b):
       print(f"{a}*{b}={a*b}")
       func(a,b)
    return inner
def div(func):
    def inner(a,b):
       print(f"{a}/{b}={a/b}")
       func(a,b)
       print(20*"*")
    return inner
@add
@sub
@mul
@div
def cal(a,b):
    print("cal close")
cal(20,30)