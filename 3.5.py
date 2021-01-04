def my_func():
    res = 0
    while True:
        numbers = input('Введите несколько чисел через пробел или Q для выхода: ').split()
        for i in numbers:
            try:
                if i == 'Q':
                    print(f'Sum is {res}. Exit')
                    return
                else:
                    res += int(i)
            except ValueError:
                print('Введите числа или Q для выхода')
        print(f'Sum is {res}')

my_func()