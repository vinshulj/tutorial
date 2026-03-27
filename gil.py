# import sys

# a = "Geek"
# print(sys.getrefcount(a))
# geek_var="Gek"
# b = geek_var
# print(sys.getrefcount(b))
import threading
import multiprocessing

def count(n):
  s = 0
  for i in range(n):
    s += i * i 
  print("Done")

# Threaded: still runs one at a time
t1 = threading.Thread(target=count, args=(10**7,))
t2 = threading.Thread(target=count, args=(10**7,))

t1.start()
t2.start()

t1.join()
t2.join()

# Multiprocess: actually runs in parallel
p1 = multiprocessing.Process(target=count, args=(10**7,))
p2 = multiprocessing.Process(target=count, args=(10**7,))

# p1.start()
# p2.start()

# p1.join()
# p2.join()

import multiprocessing as mp

def foo(q):
    q.put('hello')

if __name__ == '__main__':
    mp.set_start_method('spawn')
    q = mp.Queue()
    p = mp.Process(target=foo, args=(q,))
    p.start()
    print(q.get())
    p.join()
    ctx = mp.get_context('spawn')
    q = ctx.Queue()
    p = ctx.Process(target=foo, args=(q,))
    p.start()
    print(q.get())
    p.join()