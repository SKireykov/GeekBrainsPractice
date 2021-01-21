f = open('file_1.txt', 'w')
while True:
    text = input('Введите тектс: ')
    if text == '': break
    f.write(text+'\n')
f.close