set1 = {1, 2, 3}
print(set1)
print(type(set1))
print(len(set1))
set2 = set((4, 5, 6))
print(set2)
print(set1.add(7))
print(set1)
# print(set1.add({1,2,3}))  # This will raise an error because sets are unhashable
# print(set1.add([1,2,3]))  # This will raise an error because lists are unhashable
print(set1.update([8, 9]))
print(set1.discard(7))
print(set1)
print(set1.pop())
print(set1)

set1.clear()
set1.update([1,2,3])
set3={7,8,9}
set4=set1.union([1,2,3],set2)
print(set4)
set5={}
print(set4.issubset(set1))
print(set1)
print(set2)
print(set4)
print(set2.issubset(set4))
print(set3.isdisjoint(set4))


s={1,"eee",3.5,(1,2,3),"www"}
print(s.pop())  