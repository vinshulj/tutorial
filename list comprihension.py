fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
a=[x for x in fruits if "a" in x]
print(a)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
a=["yes"*2 for x in fruits if "a" in x]
print(a)
lis=(1,3,4,5,8,9,11,15,32,45)
new_lis=list(filter(lambda x:x if x%2==0 else "",lis))
print(list(new_lis))


