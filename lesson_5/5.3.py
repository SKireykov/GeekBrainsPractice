with open('file_3.txt', 'r') as my_file:
    up_money = []
    down_money = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
            down_money.append(i[0])
        up_money.append(i[1])
print(f'Получают меньше 20000 {down_money}, средний оклад {sum(map(int,up_money)) / len(up_money)}')