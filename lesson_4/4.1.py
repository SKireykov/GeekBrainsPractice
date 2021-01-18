def money_calc(time, sal, bonus):
    money = float((time * sal) + bonus)
    print(f'Зарплата составит: {money}')
money_calc(100, 600, 15000)
