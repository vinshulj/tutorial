stok=[]
iss=[]
class library:
    def  __init__(self,name,title):
        self.name=name
        self.title=title
    def add(self):
        stok.append((self.name,self.title))
class issue(library):
    def __init__(self,name,title,p_name):
        super().__init__(name,title)
        if (self.name,self.title) in stok:
            stok.remove((self.name,self.title))
        else:
            raise ValueError("not in stock")
        self.p_name=p_name
        
        
        

obj=library("alex","the rebound thory")