# # # import re
# # # string="""What problem does encapsulation solve at runtime, and how is it enforced in Python?

# # # sol. encapsulation means rapping up of data. it introduce the probability of data huiding in program. we can enforce it by __ for 
# # # private _ for protected and varible=value for public. allthough we cannot achive the protected as it is not possible and we can thing 
# # # as a developer we should not access _ varible. we can also access private element by obj/class_name.__var. there is another method by 
# # # which we can accive encapsulation which is clouser 

# # # How does method overriding differ from method overloading, and how does Python handle both?
# # # sol. method overriding is the process in which we create multiple method with same name and python overwrite it again and again without 
# # # even accessing it.it is genrally seen in inheritence. method overloading is the process by which we provide new functionality to 
# # # the in-built method . by updating the inbuilt property

# # # What is the role of super() in multiple inheritance, and how does MRO affect it?
# # # sol. super() key help us to inharit parent constucter,it help to increase reuability 


# # # Composition in OOP

# # # Definition:
# # # Composition is a design principle where a class contains objects of other classes to achieve functionality, instead of inheriting 
# # # from them.

# # # Think of it as a “has-a” relationship.

# # # Example: A Car has an Engine.

# # # It allows flexibility, reusability, and looser coupling between classes.

# # # Changes in one class don’t break others as easily (unlike deep inheritance).

# # # Quick comparison:
# # # Concept	Relationship	Example
# # # Inheritance	is-a	Car is a Vehicle
# # # Composition	has-a	Car has a Engine


# # # Q1 static method and dinamic mathod?
# # # note:The rationale for the order of application (bottom to top) is that it matches the usual order for function-application.
# # #  In mathematics, composition of functions (g o f)(x) translates to g(f(x)). In Python, @g @f def foo() translates to foo=g(f(foo)."""

# # # # with open("question.txt") as f:
# # # #     b=f.read().split()
# # # #     match=[]
# # # #     for i in b:
# # # #         if re.match("^e",i):
# # # #             match.append(i)
# # # #     print(match)

# # # # with open("question.txt") as f:
# # # #     b=f.read().split()
# # # #     match=[]
# # # #     for i in b:
# # # #         if re.match("[ef]",i):
# # # #             match.append(i)
# # # #     print(match)

# # # # with open("question.txt") as f:
# # # #     b=f.read().split()
# # # #     match=[]
# # # #     for i in b:
# # # #         if re.match("t*he",i):
# # # #             match.append(i)
# # # #     print(match)

# # # # with open("question.txt") as f:
# # # #     b=f.read().split()
# # # #     match=[]
# # # #     for i in b:
# # # #         if re.match("t{2,3}",i):
# # # #             match.append(i)
# # # #     print(match)
    
# # # # with open("question.txt") as f:
# # # #     b=f.read()
# # # #     x = re.findall("he.+o", b)#one or more occarance
# # # #     print(x)
# # # #     y = re.findall("he.*y", b)#zero or more occarance
# # # #     print(y)
# # # #     z = re.findall("he.?e", b)#zero or one occarance
# # # #     print(z)
# # # #     k = re.findall("he|the", b)#found this or that
# # # #     print(k)
# # # #     a = re.findall("\AWhat", b)#find if txt start with given string
# # # #     print(a)
# # # #     if a:
# # # #         print("Yes, there is a match!")
# # # #     else:
# # # #         print("No match")
# # # #     c = re.findall("\bWhat", b) #check if the starting and ending txt is given string
# # # #     print(c)
# # # #     if c:
# # # #         print("Yes, there is a match!")
# # # #     else:
# # # #         print("No match")
# # # #     B = re.findall("\Bthe", b)#Check if given string is present, but NOT at the beginning of a word:
# # # #     print(B)
# # # #     if B:
# # # #         print("Yes, there is a match!")
# # # #     else:
# # # #         print("No match")
# # # #     d = re.findall("\d", b)#return string where string contain 0-9
# # # #     print(d)
# # # #     if d:
# # # #         print("Yes, there is a match!")
# # # #     else:
# # # #         print("No match")
# # # #     d = re.findall("\da", b)#return string where string contain 0-9 and after if a
# # # #     print(d)
# # # #     if d:
# # # #         print("Yes, there is a match!")
# # # #     else:
# # # #         print("No match")
# # # #     D = re.findall("\Da", b)#return string where string contain not contain 0-9 and after if a
# # # #     print(D)
# # # #     if D:
# # # #         print("Yes, there is a match!")
# # # #     else:
# # # #         print("No match")
# # #     # s = re.findall("\s", b)#Returns a match where the string contains a white space character
# # #     # print(s)
# # #     # if s:
# # #     #     print("Yes, there is a match!")
# # #     # else:
# # #     #     print("No match")
# # #     # S = re.findall("\S", b)#Returns a match where the string DOES NOT contain a white space character
# # #     # print(S)
# # #     # if S:
# # #     #     print("Yes, there is a match!")
# # #     # else:
# # #     #     print("No match")
# # #     # w = re.findall("\w", b)#Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)
# # #     # print(w)
# # #     # if w:
# # #     #     print("Yes, there is a match!")
# # #     # else:
# # #     #     print("No match")
# # #     # W = re.findall("\W", b)#Returns a match where the string DOES NOT contain any word characters,digit or underscore
# # #     # print(W)
# # #     # if W:
# # #     #     print("Yes, there is a match!")
# # #     # else:
# # #     #     print("No match")
# # #     # Z = re.findall("\ZWhat", b)#Returns a match if the specified characters are at the end of the string
# # #     # print(Z)
# # #     # if Z:
# # #         # print("Yes, there is a match!")
# # #     # else:
# # #         # print("No match")
# # # # 





# # # txt='aaab aab aaaba ab b'
# # # print(re.findall('^[\w][\w]',txt))#if stART with two character

# # # txt='aaabwvsjxy'
# # # print(re.findall('^[\w]*$',txt))

# # # txt='aaab aab aaaba ab b'
# # # print(re.findall('a+?b',txt))#more than one

# # # txt='aaab aab aaaba ab b'
# # # print(re.findall('a*?b',txt))#any

# # # txt='aaab aab aaaba ab b'
# # # print(re.findall('a*+b',txt))#any

# # # # txt='aaab aab aaaba ab b'
# # # # print(re.findall('a?*b',txt))#error

# # # # txt='aaab aab aaaba ab b'
# # # # print(re.findall('a+*b',txt))#error

# # class A:
# #     def __init__(self,a):
# #         self.a=a
# #         print(a)
        
# # class B(A):
# #     def __init__(self,a,b):
# #         super().__init__(a)
# #         # self.a=a
# #         self.b=b
# #         print(a,b,sep="_")
        
        
        
# #         def sjflfhks(self):
# #             return 'dfgs'
# # obj=A(12)
# # obj1=B(13,14)
# # # print(obj1.a)


# class MyClass:
#     b=8
#     a=-1
#     def __init__(self, value):
#         self.value = value

#     @classmethod
#     def get_max_value(self,x, y):
#         print(max(x, y),self.a)


# # # Create an instance of MyClass
# # obj = MyClass(10)

# # # print(MyClass.get_max_value(20, 30))  

# # print(obj.get_max_value(20, 30))
# class MyClass2(MyClass):
#     a=5
#     @classmethod
#     def get_max_value(self,x, y):
#         print(max(x, y),self.a)


# print(MyClass2.get_max_value(20, 30))  
import re
tex="aeeb Fh"
print(re.findall("a.*my.*b",tex))
print(re.findall('^a(?=.*?[aeiou]).*b$',tex))
print(re.search(" ",tex,re.DEBUG))
