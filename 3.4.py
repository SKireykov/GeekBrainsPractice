print("Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить возведение числа x в степень y")
def my_func(x, y):
    result = x ** y
    return result

print(my_func(4, -5))

def my_func1(x, y):
    i = 1
    x1 = x * x
    while i < (-y - 1):
        x1 = x1 * x
        i += 1
    result = 1 / x1
    return result
print(my_func1(4, -5))

