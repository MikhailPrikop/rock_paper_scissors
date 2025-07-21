from pyexpat.errors import messages

# основные функции
from functions import choice_computer, choice_user
from functions import choice_user
from functions import winner

import configparser

# чтение файла конфигурации,

config = configparser.ConfigParser()
config.read('config.ini')
language  = config.get('LANGUAGE', 'default_language')

# функция вывода сообщений в зависимости от выбранного языка общения
def output_message(language):
    if language == 'EN':
        greetings = "WELCOME TO THE GAME 'ROCK-PAPER-SCISSORS'!!!"
        menu_message = (f"{'='*65}\n"
                        f"- to select a language, press  key 1 - English, 2 - Russian;\n"
                        f"- to call the rules of the game, press the ? key; \n"
                        f"- to start the game, press the ENTER key;\n"
                        f"{'=' * 65}\n"
                        f"")
        rules_game = (f"{'=' * 65}\n"
                      f"1. The player and the computer choose: 'Rock, Paper, Scissors'\n"
                      f"2. The choices are compared\n"
                      f"3. The winner is determined by the following rules:\n"
                      f"    {'-' * 55}\n"
                      f"    - Paper beats Rock ('Paper wraps Rock')\n"
                      f"    - Stone beats Scissors ('Rock dulls Scissors')\n"
                      f"    - Scissors beat Paper ('Scissors cut Paper')\n"
                      f"    {'-' * 55}\n"
                      f"{'=' * 65}\n"
                      f"")
        input_choice_user = f"Make your choice 1 - rock, 2 - paper, 3 - scissors"
        input_error = f"Invalid values entered"
        your_choice = 'Your choice: '
        opponent_choice = 'Choice of opponent: '
        primary_choice = ['rock', 'paper', 'scissors']

    else:
        greetings = "ДОБРО ПОЖАЛОВАТЬ В ИГРУ 'КАМЕНЬ-НОЖНИЦЫ-БУМАГА'!!!"
        menu_message = (f"{'=' * 65}\n"
                        f"- для выбора языка, нажмите клавишу 1 - Английский язык, 2 - Русский язык\n"
                        f"- для вызова правил игры, внажмите клавишу ?; \n"
                        f"- для старта игры, нажмите клавишу ENTER;\n"
                        f"{'=' * 65}\n"
                        f"")
        rules_game = (f"{'=' * 65}\n"
                      f"1. Игрок и компьютер выбирают: «Камень, ножницы, бумага»\n"
                      f"2. Выбор сравнивается\n"
                      f"3.Победитель определяется по следующим правилам:\n"
                      f"    {'-' * 55}\n"
                      f"    - бумага побеждает камень ('бумага обёртывает камень')\n"
                      f"    - rамень побеждает ножницы ('камень затупляет ножницы')\n"
                      f"    - ножницы побеждают бумагу ('ножницы разрезают бумагу')\n"
                      f"    {'-' * 55}\n"
                      f"{'=' * 65}\n"
                      f"")
        input_choice_user = f" Сделайте свой выбор: 1 - камень, 2 - бумага, 3 - ножницы"
        input_error = f"Введены неверные значения"
        your_choice = 'Ваш выбор: '
        opponent_choice = 'Выбор соперника: '
        primary_choice = ['камень', 'бумага', 'ножницы']

    messages = {'greetings': greetings,
                 'menu_message': menu_message,
                 'rules_game': rules_game,
                 'input_choice_user': input_choice_user,
                 'input_error': input_error,
                 'your_choice': your_choice,
                 'opponent_choice':opponent_choice,
                 'primary_choice':primary_choice}

    return  messages


messages = output_message(language)


print(messages['greetings'])
print(messages['menu_message'])
config.set('LANGUAGE', 'default_language', 'RU')
input_user = None

while input_user != "":
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


while input_user.upper() != 'EXIT' and input_user.lower != 'ВЫХОД':
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

    else:
        print(messages['input_error'])








