# Задача 6: Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
#
# *Пример:*
#
# 385916 -> yes
# 123456 -> no

tiket = input('Введите номер билета: ')
if len(tiket) == 6:
    left = 0
    right = 0
    for i in range(len(tiket)//2):
        left += int(tiket[i])
        right += int(tiket[len(tiket)//2 + i])
    if left == right:
        print('YES')
    else:
        print('NO')
else:
    print('Вы указали неверный номер билета')