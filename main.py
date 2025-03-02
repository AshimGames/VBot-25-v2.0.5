import random
import time

#-----------------------------------------------------------------------------------------------

#начинаю писать ОС
time.sleep(1)
print('Добро пожаловать! загрузка драйвера VBot...')
time.sleep(1)
for i in range(21):
    print(i)
    time.sleep(0.5)
time.sleep(1)
print('Идет загрузка ОС, пожалуйста подожите...')
time.sleep(5)
print('Загрузка завершена!')
time.sleep(1)
print('Загруззка VBot завершена!')
login = input('Введите ваше имя: ')
if login == 'TRS':
    print('Здраствуйте создатель!')
    cmd = input('Какую команду вы выберете?: console')
    if cmd == "console":
        print('Консоль VbotOS запущена!')
if login == login:
    print('Здравсвуйте', login, "!")
    while True:  # Бесконечный цс 15 до 53
        command = input(
            'Введите команду если команды НЕ знаете напишите help: ')
        if command == 'Квест':
            print('ОЙ... Ошибочка Сдесь ведуться дорожные работы:/')
        elif command == 'Настройки':
            print('Здравствуйте!')
            time.sleep(1)
            cc = input('Сколько fps должно быть у вашей ОС?: ')
            print(cc, 'отлично!')
        elif command == 'Профиль':
            print('Здравствуйте! Ваш прифиль: ', login, ('!'))
        elif command == 'help':
            print(
                'Вот список команд: Квест, Настройки, Профиль, inf, help, Проекты,'
            )
        elif command == 'Проекты':
            print('Вот список проектов: VBotOS')
        elif command == 'Выход':
            print('Вы вышли из VBotOS')
        elif command == 'ПTS':
            print(
                'Вот список проектов Truss Studio: VBotOS, Wundios 11 beta, 2D platformer 200+'
            )
        elif command == 'inf':
            print(
                'Об этой ОС! имя ОС: VBotOS, версия: pro 1.5.90, разработчик: Truss Studio'
            )
            print('Создатель Truss Studio: Михаил Бровин')
        elif command == 'Обновы':
            print(
                'Обновления: 1.0.0 поект был создан, 1.0.1: добавлена команда Профиль...'
            )
            print(
                '1.5.82 BETA добавлена команада inf, 1.5.90 добавлена команда Проекты'
            )
        elif command == 'VBOT DRIVER INF':
            print('Версия VBotOS DRIVER: 1.98.54.67.56')
        elif command == 'Выкл':
            print('Вы выключили VBotOS')
            break
        elif command == 'Рандом сила и герой':
            heroes = ['Бэтмен','Соник','Супермен']
            power = ['Деньги','Скорость','Сила']

            print(random.choice(heroes))
            print(random.choice(power))
        elif command == 'Рандом число':
            print(random.randint(1, 100))
        elif command == 'Рандом число 2':
            print('Эта функция не доступна')
        else:
            print('Не знаю такой команды:/')
