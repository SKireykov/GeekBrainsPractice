def div(x, y):

    x = int(input("Введите число "))
    y = int(input("Введите число "))
    if y != 0:
        result = x / y
        return result
    else:
        print("На ноль делить нельзя!")

print(f'result  {div(5, -7)}')