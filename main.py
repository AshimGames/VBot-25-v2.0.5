import random
import time

#VBot Simple OS 
time.sleep(1)
print('Starting DDOs')
time.sleep(2)
print('VBot file exeption started')
time.sleep(1)
print('Importing Vbot32X')
time.sleep(0.6) 
print('Importing VBot64X')
time.sleep(0.7)
print('OS Has been started!')
time.sleep(1)
print("|||| ||||")
print("|||| ||||")
print("|||| ||||")
print("|||| ||||")
print("  |||||  ")
time.sleep(1)
while True:  # Бесконечный цс 15 до 53
        command = input(
            'Введите команду или настройку, если команды не знаете напишите help: ')
        if command == 'help':
           print("Список команд:")
           print("Settings")
           print("Site")
           print("info")
           print("DDOs -- включить/выключить DDOs защиту")
           print("eula")
           print("For Creators") 
        elif command == 'Settings':
            print('<---НАСТРОЙКИ--->')
            print(' Настройки сети..,')
            print(' Защита..,')
            print(' Персональные данные..,')
            print('<-----СКОРО----->')
        elif command == 'Сеть':
            print('<---НАСТРОЙКИ СЕТИ--->')
            print('Установка соидения невозможна на данный момент')
        elif command == 'Защита':
            print('<---ЗАЩИТА--->')
            print('DDOs.., для выключения напишите команду DDOs off')
            print('Для включения напишите команду DDOs on')
        elif command == 'DDOoff':
            print('Защита DDOs успешно выключена!')
        elif command == 'DDOon':
            print('Защита DDOs успешно включена!')
        elif command == 'Персона':
            print('<---ДАННЫЕ ПОЛЬЗОВАТЕЛЯ--->')
            login = input('Введите ваше имя: ')
            if login == login:
                print(login, 'Добро пожаловать в VBot 25! Ваши данные сохранены!')
        elif command == 'Info':
            print("|||| ||||   |||||||||")
            print("|||| ||||   ||       |")
            print("|||| ||||   ||||||||||")
            print("|||| ||||   ||       |")
            print("  |||||     |||||||||")
            time.sleep(3)
            print('Информацио о VBot:')
            print('VBot начал создаватся в 2024 году,')
            print('его создает 1 человек,')
            print('он надеется что когда-то этот бот станет популярным!')
        elif command == 'Site':
            print('error A94 socured. В разработке...')
            print('       ||||| |||||')
            print('       ||||| |||||')
            print('          .....   ')
            print("         |||||||  ")
            print('       ||||   ||||') 
        elif command == 'eula':
            print('We are using eula protection, if you want to use it type eula=true')
        elif command == 'eula=true':
            print('Eula is active now!')          
        else:
            print('error A81 socured: Такой команды не существует.')
            print('       ||||| |||||')
            print('       ||||| |||||')
            print('          .....  ')
            print("         |||||||")
            print('       ||||   |||| ')
