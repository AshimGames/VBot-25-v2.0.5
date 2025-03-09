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
while True:  # Бесконечный цс 22 до 137
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
           print("Translator")
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
            print('         <--САЙТ Vbot25-->')
            print('|Вы сможете найти сайт в файлах OS|')
        elif command == 'eula':
            print('We are using eula protection, if you want to use it type eula=true')
        elif command == 'eula=true':
            print('Eula is active now!')       
        elif command == 'Переводчик':
            print('error A94 socured. В разработке...')
            print('       ||||| |||||')
            print('       ||||| |||||')
            print('          .....   ')
            print("         |||||||  ")
            print('       ||||   ||||') 
        #     eng_words = ['Hi','Bye','Task', 'Programm']
        #     ru_words = ['Привет','Пока','Задача', 'Программа']
        #     score = 0

        #     mod = input("Выбери режим работы тренажера: 0 - добавить новые слова, 1 - тренироваться: \n")
        #     while ((mod != '0') and (mod != '1')):
        #         mod = input("Недопустимый символ! Выбери 0 или 1. (0 - добавить новые слова, 1 - тренироваться) \n")

        #     if mod == "1":
        #         print("Переведи как можно больше слов правильно! У тебя 10 попыток!")
        #         for i in range(10):
        #             number = random.randint(0, len(eng_words))
        #             print("Как переводится слово: "+eng_words[number])
        #             if input() == ru_words[number]:
        #                 print("Отлично!!!")
        #                 score += 1
        #             else:
        #                 print("Нет... Это слово - " + ru_words[number])
        #     else:
        #         word = input("Введите слово на русском языке: ")
        #         translate = input("Введите перевод этого слова: ")
        #         if len(word) > 0 and len(translate) > 0:
        #             ru_words.append(word)
        #             eng_words.append(translate)
        #             print("Слово успешно добавлено!")   
        if command == 'Калькулятор':
            print ('Приветствуем вас в калькуляторе VBot 25')
            q1 = int (input('Введите число 1: '))
            q2 = int (input('Введите число 2: '))

            v = int (input('Какую операцию вы хотите выполнить? \n 1 Сложение \n 2 Вычитание \n 3 Деление \n 4 Умножение \n'))

            if v == 1:
                r = q1 + q2
                p = 'сложения'
                t = p
            if v == 2:
                r = q1 - q2
                l = 'вычитания'
                t = l
            if v == 3:
                r = float(q1 / q2)
                m = 'деления'
                t = m
            if v == 4:
                r = q1 * q2
                n = 'умножения'
                t = n
            print ('Результат ',t,' = ',r)
        #Файловый менеджер
        if command == 'file manager':
            from pathlib import Path

            class bcolors:
                HEADER = '\033[95m'
                OKBLUE = '\033[94m'
                OKGREEN = '\033[92m'
                WARNING = '\033[93m'
                FAIL = '\033[91m'
                ENDC = '\033[0m'
                BOLD = '\033[1m'
                UNDERLINE = '\033[4m'

            def err_msg(text):
                '''
                Prints input text with red color
                :param text:
                :return:
                '''
                print(bcolors.FAIL, text, bcolors.ENDC)

            def cd(curr_dir, dir_name=''):
                '''
                :param curr_dir: Path object of directory from which 'cd' was called \n
                :param dir_name: Str name of the path user want to go into \n
                :return: if dir_name is empty then Path.home(), if dir_name is valid then Path of curr_dir/dir_name otherwise curr_dir
                '''

                if not dir_name: return Path.home()

                new_dir = curr_dir/dir_name

                if not new_dir.exists():
                    err_msg('Path "{}" doesn\'t exist'.format(new_dir))
                elif not new_dir.is_dir():
                    err_msg('"{}" is not a directory'.format(new_dir))
                else:
                    curr_dir = new_dir
                return curr_dir.resolve()

            def pwd(curr_dir):
                '''
                Prints working directory
                :param curr_dir:
                '''

                print(str(curr_dir))

            def mkdir(curr_dir, dir_name):
                '''
                Makes a directory with name "dir_name" in curr_dir
                :param curr_dir:
                :param dir_name:
                '''

                new_dir = curr_dir/dir_name
                try:
                    Path.mkdir(new_dir)
                except FileExistsError:
                    err_msg('Directory "{}" already exists'.format(str(new_dir)))

            def ls(curr_dir):
                '''
                Lists all files and directories in a given directory
                :param curr_dir:
                :return:
                '''

                for f in curr_dir.iterdir():
                    if f.is_dir():
                        print(bcolors.OKBLUE, f.parts[-1:][0], bcolors.ENDC)
                    else:
                        print(f.parts[-1:][0])

            def touch(curr_dir, file_name):
                '''
                Create new file at curr_dir with file_name
                :param curr_dir:
                :param file_name:
                '''
                new_file = curr_dir/file_name
                open(str(new_file), 'w')

            def cat(curr_dir, file_name):
                '''
                Opens and outputs file with file_name from curr_dir
                :param curr_dir:
                :param file_name:
                '''
                new_file = curr_dir/file_name
                if not new_file.exists():
                    err_msg('File "{}" doesn\'t exist'.format(str(new_file)))
                elif not new_file.is_file():
                    err_msg('{} is not a file'.format(str(new_file)))
                else:
                    with new_file.open() as f:
                        try:
                            print(f.readline(), end='')
                        except UnicodeError as e:
                            print(e)
                            err_msg("Error during reading")

            def main():
                curr_dir = Path.home().resolve()
                while True:
                    command = input('current_dir:{}$ '.format(curr_dir))
                    command = command.split()

                    if len(command) < 1: continue
                    if command[0] == 'cd':
                        if len(command) == 2:
                            curr_dir = cd(curr_dir, command[1])
                        elif len(command) == 1:
                            curr_dir = cd(curr_dir)
                        else:
                            err_msg('Wrong number of arguments')

                    elif command[0] == 'pwd':
                        if not len(command) == 1:
                            err_msg('pwd command doesn\'t have arguments')
                        else:
                            pwd(curr_dir)

                    elif command[0] == 'mkdir':
                        if not len(command) == 2:
                            err_msg('Wrong number of arguments')
                        else:
                            mkdir(curr_dir, command[1])

                    elif command[0] == 'ls':
                        if not len(command) == 1:
                            err_msg('ls command doesn\'t have arguments')
                        else:
                            ls(curr_dir)

                    elif command[0] == 'touch':
                        if not len(command) == 2:
                            err_msg('Wrong number of arguments')
                        else:
                            touch(curr_dir, command[1])

                    elif command[0] == 'cat':
                        if not len(command) == 2:
                            err_msg('Wrong number of arguments')
                        else:
                            cat(curr_dir, command[1])
                    else:
                        err_msg('Unknown command "{}"'.format(command[0]))
        

            if __name__ == '__main__':
                main()
        if command == 'Открытие приложений':
            print('error A94 socured. В разработке...')
            print('       ||||| |||||')
            print('       ||||| |||||')
            print('          .....   ')
            print("         |||||||  ")
            print('       ||||   ||||') 
            # import tkinter as tk
            # # Library used to open applications
            # import AppOpener 
            
            # # Create Object
            # root = tk.Tk()
            
            # # Set geometry
            # root.geometry("500x500")
            
            # # Create the text area
            # text_area = tk.Text(root, height=10, width=30, font=("",20))
            # text_area.pack()
            # # Autofocus cursor in text area
            # text_area.focus()
            # # Create the button
            # button = tk.Button(root, text="Open App", font=("", 20))
            # button.pack()
            
            # # Create the label
            # label = tk.Label(root, text="", font=("", 15))
            # label.pack()
            # label.config(text="JUST ENTER NAME OF APPLICATION TO OPEN")
            
            # def open_app(event):
            # # Get application name
            #  app_name = text_area.get("1.0", "end")
            # # Open application
            #  AppOpener.open(app_name)
            # # Change the label accordingly
            #  label.config(text=str("Looking for "+app_name))
            #  text_area.delete("1.0", "end")
            
            # # Bind the button to the function
            # button.bind("<Button-1>", open_app)
            # root.mainloop()
        if command == 'Генератор паролей':
                chars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOOOOPASDFGHJKLZXCVBNM1234567890!@#$%^&*№?*'
                symbols = ''
                lenght = int(input('Какой длинны будет ваш пароль?'))
                for i in range(lenght):
                    symbols += random.choice(chars)
                print(symbols)
        else:
            print('error A81 socured: Такой команды не существует.')
            print('       ||||| |||||')
            print('       ||||| |||||')
            print('          .....  ')
            print("         |||||||")
            print('       ||||   |||| ')

