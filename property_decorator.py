# #Class Without Getters and Setters
# class tempa:
#     def __init__(self,temp=0):
#         self.temp=temp# local to object
#         # temp=self.temp# object to local
        
#     def far(self):
#         return print((1.8*self.temp)+32)
# obj=tempa()
# obj.temp=37
# print(obj.temp)
# obj.far()
# print(37*1.8) # floting point error

# class tempa:
#     def __init__(self,temp=0):
#         self.temp=temp
        
#     def far(self):
#         return print((1.8*self.temp)+32)
#     def getter(self):
#         return print(self.temp)
#     def setter(self,value):
#         if value<-273:
#             raise ValueError("temparature should be grater than -273")
#         self.temp=value
# obj=tempa()
# obj.temp=37
# print(obj.temp)
# obj.far()
# obj.setter(-200)
# obj.getter()
# obj.far()
# # obj.setter(-300)# give error
# temp=property(getattr,setattr)
# print(type(temp))


# class tempa:
#     def __init__(self,temp=0):
#         self._temp=temp
#     def far(self):
#         return print((1.8*self.temp)+32)
#     @property
#     def temp(self):
#         print("gitting a value")
#         return self._temp
#     @temp.setter
#     def temp(self,value):
#         print("setting value")
#         if value<-273:
#             raise ValueError("temparature should be grater than -273")
#         self._temp=value
#     @temp.deleter
#     def temp(self):
#         print("deletting value")
#         del self._temp
# obj=tempa(37)
# print(obj.temp)
# obj.temp=31
# print(obj.temp)


class circle:
    def __init__(self,radius,area):
        self._radius=radius
        self._area=area
    _unknown=25
    @property
    def radius(self):
        return self._radius
    @radius.setter
    def radius(self,value):
        self._radius=value
    @radius.deleter
    def radius(self):
        del self._radius
    @property
    def area(self):
        return self._radius*self._radius*3.14
    @area.setter
    def area(self,value):
        self._area=value
    @property
    def curcumfarence(self):
        return self._radius*2*3.14
    @property
    def unknown(self):
        return self._unknown
    @unknown.setter
    def unknown(self,value):
        self._unknown=value
    
obj=circle(5,20)
print(obj.radius)
print(obj.area)
print(obj.curcumfarence)
print(obj.unknown)

obj.radius=32
print(obj.radius)
print(obj.area)
print(obj.curcumfarence)

obj.unknown=52
print(obj.unknown)