def int_func(text):
    ls = []
    for i in range(len(text)):
        ls.append(text[i][0:1].title() + text[i][1:])
    return ' '.join(ls)

print(int_func(input('Введите несколько слов с маленькой буквы: ').split()))