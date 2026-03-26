import time
from datetime import datetime
cur=time.time()
# print(cur)
# now=time.localtime(1767096189.772491)
# print(now)

while True:
    current=time.localtime(cur)
    formate=datetime.now().strftime("%Y/%d/%d %H:%M:%S %p")
    print(formate)
    time.sleep(1)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    