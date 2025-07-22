# основные функции
from functions import choice_computer, choice_user
from functions import choice_user
from functions import winner
from functions import output_message

import configparser
import sys

# чтение файла конфигурации,

config = configparser.ConfigParser()
config.read('config.ini')
language  = config.get('LANGUAGE', 'default_language')

messages = output_message(language)


print(messages['greetings'])
print(messages['menu_message'])
config.set('LANGUAGE', 'default_language', 'RU')
input_user = None

while True:
    language = language
    messages = output_message(language)
    input_user = str(input())
    if input_user == '1':
        language = 'EN'
        config.set('LANGUAGE', 'default_language', 'EN')
        with open('config.ini', 'w') as configfile:
            config.write(configfile)

    elif input_user == '2':
        language = 'RU'
        config.set('LANGUAGE', 'default_language', 'RU')
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
    elif input_user == "?":
        print(messages['rules_game'])
    elif input_user == "":
        while input_user.upper() != 'EXIT' or input_user.upper() != 'ВЫХОД':
            print(messages['input_choice_user'])
            input_user = str(input())
            #проверка правильности ввода
            if input_user.upper() in ['КАМЕНЬ','НОЖНИЦЫ','БУМАГА', 'ROCK', 'PAPER', 'SCISSORS', '1','2','3']:
                user = choice_user(input_user, language = language)
                print(f"{messages['your_choice']} {user}")
                computer = choice_computer(messages['primary_choice'], language = language)
                print(f"{messages['opponent_choice']} {computer}")
                result = winner(user, computer, language=language)
                print(result)
                print('')
            elif input_user.upper() == 'EXIT' or input_user.upper() == 'ВЫХОД':
                print(messages['end_game'])
                sys.exit()
            elif input_user.upper() == 'MENU' or input_user.upper() == "МЕНЮ":
                print(messages['menu_message'])
                break
            else:
                print(messages['input_error'])
    elif input_user.upper() == 'EXIT' or input_user.upper() == 'ВЫХОД':
        print(messages['end_game'])
        sys.exit()









