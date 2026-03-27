# # # try:
# # #     raise ValueError("spam", "eggs", "ham",[1,2,3])
# # # except Exception as inst:
# # #     print(type(inst))    # the exception instance
# # #     print(inst.args)     # arguments stored in .args
# # #     print(inst)          # __str__ allows args to be printed directly
# # #     # x, y, z = inst.args  # unpacking arguments
# # #     # print("x =", x)
# # #     # print("y =", y)
    
# # x = -1

# # assert x >= 0, "x nahi be non-negative"

# try:
#     open("database.sqlite")
# except OSError:
#     raise RuntimeError("unable to handle error")

# def func():
#     raise ConnectionError

# try:
#     func()
# except ConnectionError as exc:
#     raise RuntimeError('Failed to open database') from exc

# try:
#     open('database.sqlite')
# except OSError:
#     raise RuntimeError from None

def divide(x, y):
    try:
        print(x)
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

divide(2, 1)
divide(2, 0)
divide("2", "1")

