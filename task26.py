# Задача 26:  Напишите программу, которая на вход
# принимает два числа A и B, и возводит число А
# в целую неотрицательную степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

def exponentiation(A, B, count=0, res=1):
    if count == B:
        print(res)
    else:
        res = res*A
        count += 1
        exponentiation(A, B, count, res)


A = int(input("Введите число А: "))
B = int(input("Введите число B: "))
if B < 0:
    print("Степень(число В) должна быть положительной: ")
else:
    exponentiation(A, B)
