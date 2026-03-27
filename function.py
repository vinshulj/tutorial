# def fun(a,b=5):
#     return a+b

# print(fun(3))
# print(fun(3,7))

# #note it take default value only once at the time of function definition
# i = 5
# def f(arg=i):
#     print(arg)

# i = 6
# f()

# lis=[]
# def fun1(a, L=lis):
#     L.append(a)
#     return L
# print(lis)
# print(fun1(1))
# print(lis)
# print(fun1(2,[1,2,3]))

# #function behavier when we overright the things and when we modify the things 
# lis={1,2,3}
# def fun1(L=lis):
#     lis2={4,5,6}
#     L=L.union(lis2)
#     return L
# print(lis)
# print(fun1())
# print(lis)

# lis={1,2,3}
# def fun1(L=lis):
#     lis2={4,5,6}
#     lis.update(lis2)
#     return lis
# print(lis)
# print(fun1())
# print(lis)


# def standard_arg(arg):
#     print(arg)

# def pos_only_arg(arg, /):
#     print(arg)

# def kwd_only_arg(*, arg):
#     print(arg)

# standard_arg(2)
# # pos_only_arg(arg=3) # this will give error keyword argument not allowed
# pos_only_arg(3)
# # kwd_only_arg(3) # this will give error positional argument not allowed
# kwd_only_arg(arg=3)


print(list(range(10)))

#lambda function in function arguments
def fun2(x,f):
    return f(x)
print(fun2(5,lambda x:x**2))

#or
def square(x):
    return lambda y:y**x
f=square(2)
print(f(3))
print(f(4))

# lambda function
def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
print(f(0))

print(f(1))

# Nested functions
f=lambda x: (lambda y: x * y)
o=f(5)
print(o(3))

f=lambda x: lambda y: lambda z:x+y+z
print(f(3)(4)(5))

f=lambda x: lambda y: lambda z:x+y+z
g=f(3)
h=g(4)
print(h(5))                                                                                 

tup=(1,2,3)
def fun():
    tup=(1,2,3)
    def ret():
        nonlocal tup
        tup=(4,5,6)
        return tup
    ret()
    return tup
print(fun())
# print(tup)

a=[4,5,6,7,8,7,6,6,6,2,1,9]
maap1=list(map(lambda x:x*2,a))
print(maap1)
filter1=list(filter(lambda x:x%2==0,a))
print(filter1)


def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)
