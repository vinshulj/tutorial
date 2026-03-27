# print(None==True)
# print(None==False)
# print(None is True)
# print(None is False)
# print(None is None)
# print(None==None)
# print(bool(None))
# # print(int(None)) # this will give error
# # print(float(None)) # this will give error
# print(str(None))    
# print("None"==None)
# print(1 is None)
# print(bool(0))
# print(bool(1))
# print(bool(-1))
# print(bool([]))
# print(bool([0]))
# print(bool({}))
# print(bool({'a':1}))
# print(bool(()))
# print(bool((0,)))
# print(bool(set()))

# Tuples
a=()
print(type(a))
b=(1)
print(type(b))
c=(1,)
print(type(c))
d=1,2,3
print(type(d))
e=1,
print(type(e))
f="js","sk"
print(type(f))

# # Sets
# s1={}
# print(type(s1))
# s2=set()
# print(type(s2))
# s3={1,2,3}
# print(type(s3))
# s4=set([1,2,3])
# print(type(s4))

# # Frozensets
# fs1=frozenset()
# print(type(fs1))
# fs2=frozenset([1,2,3])
# print(type(fs2))
# fs3=frozenset((1,2,3))
# print(type(fs3))

# # Ranges
# r1=range(10)
# print(type(r1))
# r2=range(1,10)
# print(type(r2))
# r3=range(1,10,2)
# print(type(r3))
# r4=range(10,1,-1)
# print(type(r4))
# r5=range(10,1)
# print(type(r5))
# r6=range(0)
# print(type(r6))
# r7=range(-10)
# print(type(r7))
# r8=range(-10,0)
# print(type(r8))
# r9=range(-10,10)
# print(type(r9))
# r10=range(-10,10,2)

# #dictionaries
# dic1={}
# print(type(dic1))
# dic2=dict()
# print(type(dic2))
# dic3={'a':1,'b':2}
# print(type(dic3))
# dic4=dict(a=1,b=2)
# print(type(dic4))
# dic5=dict([('a',1),('b',2)])
# print(type(dic5))
# dic6=dict((('a',1),('b',2)))
# print(type(dic6))
# print(type(r10))


a=None
c=[({1:1},None,3,1)]
b=c[0][1]
d=c[0][3]
e=c[0][0][1]
print(a is b)
print(d is e)