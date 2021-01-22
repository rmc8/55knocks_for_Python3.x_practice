def my_div(i: int, j: int):
    try:
        return i / j
    except ZeroDivisionError:
        return "zero division"


a: int = 0
b: int = 5

print(my_div(a, b))
print(my_div(b, a))
