# Задача 1. Вариант 30.
'''
Напишите программу, которая будет сообщать род деятельности
и псевдоним под которым скрывается Симона Руссель. После вывода
информации программа должна дожидаться пока пользователь нажмет
Enter для выхода.
'''
# SHCHUKIN F. O.
# 24.02.2016

from sys import stdout as c
from time import sleep

quote = 'Французская актриса Симона Рене Руссель \
более известна, как Мишель Морган.'

sleep(1.0)

for char in quote:
    c.write(char)
    c.flush()
    pause = 0.8 if char is ',' else 0.03
    sleep(pause)

c.write('\n'*2)

input('ok')
