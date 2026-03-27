# method in dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
# Using items() method
items = my_dict.items()
print(items)  # dict_items([('a', 1), ('b', 2), ('c', 3)])
# Using keys() method
keys = my_dict.keys()
print(keys)  # dict_keys(['a', 'b', 'c'])
# Using values() method
values = my_dict.values()
print(values)  # dict_values([1, 2, 3])
# Using get() method
value_b = my_dict.get('b')
print(value_b)  # 2
# Using pop() method
popped_value = my_dict.pop('c')
print(popped_value)  # 3
print(my_dict)  # {'a': 1, 'b': 2}
# Using update() method
my_dict.update({'d': 4})
print(my_dict)  # {'a': 1, 'b': 2, 'd': 4}
# Using clear() method
# my_dict.clear()
print(my_dict)  # {} 

key=["name","age","city","d"]
value=["vinshul",20,"new delhi"]
new_dict=dict.fromkeys(key,value)
print(new_dict)


print(my_dict.get("a"))
print(my_dict.keys())
print(my_dict.pop("a"))
print(my_dict.pop("e","not found"))
print(my_dict.items())
print(my_dict.keys())

dic={'a':1,'b':2,'c':3}
l=list(dic)
print(l)
print(type(l))

dic1={'a':1,'b':2,'c':3}
print(dic1.get("b"))
print(dic1.get("d",))
print(dic1.get("d","not found"))
print(dic1.get("a",5))
print(dic1.get(-1))

# print(dic1.pop())# will give error because pop need at least one argument
print(dic1.pop("b"))
# print(dic1.pop("d"))# will give error because d is not present
print(dic1.pop("d","not found"))

key=["name","age","city","d"]
value=["vinshul",20,"new delhi"]
dic3={}
for keys,values in zip(key,value):
    dic3[keys]=values
print(dic3)