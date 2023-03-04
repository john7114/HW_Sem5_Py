# Задача 2
#    Словом в данной задаче считается последовательность букв,
#    ограниченная пробелами или началом или концом строки.
#    Выведите все слова из строки в столбик. НЕЛЬЗЯ ПОЛЬЗОВАТЬСЯ МЕТОДАМИ СТРОК (split)

# Формат ввода
# Вводится строка.

# Формат вывода
# Выведите слова из строки по одному.

# Пример 1
# Ввод

# Hello, world!
# Вывод
# Hello,
# world!
# Пример 2
# Ввод

# My heart in the Highland
# Вывод
# My
# heart
# in
# the
# Highland

str_a = "Python is an easy to learn, powerful programming language."


for i in range(len(str_a)):
    if str_a[i] != ' ':
        print(str_a[i], end='')
    else:
        print('\n', end='')
