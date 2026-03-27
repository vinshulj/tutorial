# import time
# from math import sqrt,floor
# from concurrent.futures import ThreadPoolExecutor
# from multiprocessing import Pool

# def fun(n):
#     if n<=2:
#         return False
#     else:
#         for i in range(2,floor(sqrt(n))):
#             if n%i==0:  #Gil concept,multi processing ,multi threding,
#                 return False
#         else:
#             return True
# ans=[]
# start_time = time.perf_counter()
# for i in range(1000000):
#     ans.append(fun(i))

# end_time = time.perf_counter()
# elapsed_time = end_time - start_time
# print(f"Execution time: {elapsed_time:.4f} seconds")




# start_time = time.perf_counter()
# with ThreadPoolExecutor() as ex:
#     ans2=[]
#     for i in range(100000):
#         answer = ex.submit(fun, i)
#         ans2.append(answer)

# end_time = time.perf_counter()
# elapsed_time = end_time - start_time
# print(f"Execution time with multitreading: {elapsed_time:.4f} seconds")


# start_time = time.perf_counter()
# with Pool() as ex:
#     data=range(100000)
#     ans3 = ex.map(fun,data)

# end_time = time.perf_counter()
# elapsed_time = end_time - start_time
# print(f"Execution time with multiprocessing: {elapsed_time:.4f} seconds")



import requests
import time
url = "https://jsonplaceholder.typicode.com/todos/"
def fun(a):
    response=requests.get(url+str(i))
    return response.text()
start_time = time.perf_counter()
result=[]
for i in range(1,2):
    data=fun(i)
    result.append(data)
    
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Execution time without: {elapsed_time:.4f} seconds")
print(result)


from multiprocessing import Pool
url = "https://jsonplaceholder.typicode.com/todos/"
def fun(a):
    response=requests.get(url+str(i))
    return response.text()
start_time = time.perf_counter()
result=[]
with Pool() as p:
    data=range(1,2)
    result=p.map(fun,data)
    
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Execution time with multiprocessing: {elapsed_time:.4f} seconds")
print(result)
