import random

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







