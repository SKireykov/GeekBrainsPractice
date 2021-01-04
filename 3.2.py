name = input('Укажите имя ')
surname = input('Укажите фамилию ')
year = (input('Год рождения '))
city = input('Укажите город ')
email = (input('Укажите электронную почту '))
phone = (input('Введите номер телефона '))


def my_func(name, surname, year, city, email, phone):
        return ' '.join([name, surname, year, city, email, phone])

print(my_func(surname = surname, name = name, year = year, city = city, email = email, phone = phone))