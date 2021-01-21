f = open('file_2.txt')
line = 0
for i in f:
    line += 1

    word = 0
    for j in i:
        if j != ' ':
            word += 1

    print(i, len(i), 'симв.', word, 'сл.')

print(line, 'стр.')
f.close()