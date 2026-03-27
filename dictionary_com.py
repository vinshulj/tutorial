keys = ['a','b','c','d','e']
values = [x for x in range(len(keys))]  
new_dic={k:v for k,v in zip(keys,values)}
print(new_dic)

keys = ['a','b','c','d','e',"r","j"]
values = [1,2,3,4,5]  
new_dic={k:v for k,v in zip(keys,values)}
print(new_dic)
# work fine no error will be shown for extra keys 
new_dic1={x:x**2 for x in range(10) if x%2==0}
print(new_dic1)