import requests
import time
url = "https://sakani.sa/app/land-projects/"
def fun(a):
    response=requests.get(url+str(i))
    return response.text
start_time = time.perf_counter()
result=[]
for i in range(1,2):
    data=fun(i)
    result.append(data)
    
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Execution time without: {elapsed_time:.4f} seconds")


from multiprocessing import Pool
def fun(a):
    response=requests.get(url+str(i))
    return response.text
start_time = time.perf_counter()
result=[]
with Pool() as p:
    data=range(1,2)
    result=p.map(fun,data)
    
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Execution time with multiprocessing: {elapsed_time:.4f} seconds")
print(len(result))
# print(result)

# file_name = "dummy_file.txt"

# # Open file in write mode (creates file if it doesn't exist)
# with open(file_name, "w",encoding="utf-8") as file:
#     file.write(str(result))
# print(f"File '{file_name}' created and saved successfully.")
    