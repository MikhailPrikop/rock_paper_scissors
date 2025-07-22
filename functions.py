import random


# функция вывода сообщений в зависимости от выбранного языка общения
def output_message(language):
    if language == 'EN':
        greetings = "WELCOME TO THE GAME 'ROCK-PAPER-SCISSORS'!!!"
        menu_message = (f"{'='*65}\n"
                        f"- to select a language, press  key <1> - English, <2> - Russian\n"
                        f"- to call the rules of the game, press the <?> key  \n"
                        f"- to start the game, press the <ENTER> key \n"
                        f"- to exit to the main menu, enter <MENU> \n"
                        f"- to exit the game, enter <EXIT> \n"
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
        end_game = 'GAME OVER!!!'

    else:
        greetings = "ДОБРО ПОЖАЛОВАТЬ В ИГРУ 'КАМЕНЬ-НОЖНИЦЫ-БУМАГА'!!!"
        menu_message = (f"{'=' * 75}\n"
                        f"- для выбора языка, нажмите клавишу <1> - Английский язык, <2> - Русский язык\n"
                        f"- для вызова правил игры, внажмите клавишу <?>\n"
                        f"- для старта игры, нажмите клавишу <ENTER>\n"
                        f"- для выхода в основное меню, введите <МЕНЮ>\n"
                        f"- для выхода из игры введите <ВЫХОД>\n"
                        f"{'=' * 75}\n"
                        f"")
        rules_game = (f"{'=' * 65}\n"
                      f"1. Игрок и компьютер выбирают: «Камень, ножницы, бумага»\n"
                      f"2. Выбор сравнивается\n"
                      f"3. Победитель определяется по следующим правилам:\n"
                      f"    {'-' * 55}\n"
                      f"    - бумага побеждает камень ('бумага обёртывает камень')\n"
                      f"    - rамень побеждает ножницы ('камень затупляет ножницы')\n"
                      f"    - ножницы побеждают бумагу ('ножницы разрезают бумагу')\n"
                      f"    {'-' * 55}\n"
                      f"{'=' * 65}\n"
                      f"")
        input_choice_user = f"Сделайте свой выбор: 1 - камень, 2 - бумага, 3 - ножницы"
        input_error = f"Введены неверные значения"
        your_choice = 'Ваш выбор: '
        opponent_choice = 'Выбор соперника: '
        primary_choice = ['камень', 'бумага', 'ножницы']
        end_game = "ИГРА ЗАКОНЧЕНА!!!"

    messages = {'greetings': greetings,
                 'menu_message': menu_message,
                 'rules_game': rules_game,
                 'input_choice_user': input_choice_user,
                 'input_error': input_error,
                 'your_choice': your_choice,
                 'opponent_choice':opponent_choice,
                 'primary_choice':primary_choice,
                 'end_game':end_game
                }

    return  messages

#функция  выбора хода компьютера
def choice_computer(primary_choice = ['rock', 'paper', 'scissors'], language = 'EN'):
    if language == 'RU':
        primary_choice = ['камень', 'бумага', 'ножницы']
    return random.choice(primary_choice)

#функция выбора пользователя
def choice_user(input_user, language = 'EN'):
    if language == 'RU':
        if input_user.upper == 'КАМЕНЬ' or input_user == '1':
            return 'камень'
        elif input_user.upper == 'БУМАГА' or input_user == '2':
            return 'бумага'
        else:
            return 'ножницы'
    else :
        if input_user.upper == 'ROCK' or input_user == '1':
            return 'rock'
        elif input_user.upper == 'PAPER' or input_user == '2':
            return 'paper'
        else:
            return 'scissors'

#функция определения победителя
def winner(user, computer, language = 'EN'):
    if language == 'RU':
        if (
                (user == 'камень' and computer == 'ножницы')
                or
                (user == 'бумага' and computer == 'камень')
                or
                user == 'ножницы' and computer == 'бумага'
        ):
            return 'ВЫ ПОБЕДИЛИ :)'

        elif (
                (user == 'камень' and computer == 'КАМЕНЬ')
                or
                (user == 'бумага' and computer == 'бумага')
                or
                (user == 'ножницы' and computer == 'НОЖНИЦЫ')
        ):
            return 'НИЧЬЯ :|'

        else:
            return 'ВЫ ПРОИГРАЛИ :('
    else:
        if (
                (user == 'rock' and computer == 'scissors')
                or
                (user == 'paper' and computer == 'rock' )
                or
                user == 'scissors' and computer == 'paper'
        ):
            return 'WINE :)'

        elif (
                (user == 'rock' and computer == 'rock')
                or
                (user == 'paper' and computer == 'paper')
                or
                (user == 'scissors' and computer == 'scissors')
        ):
            return 'DRAW :|'

        else:
            return 'LOSS :('







