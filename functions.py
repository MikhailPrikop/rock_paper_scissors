import random

#функция  выбора хода компьютера
def choice_computer(primary_choice = ['rock', 'paper', 'scissors']):
    return random.choice(primary_choice)

#функция выбора пользователя
def choice_user(input_user):
    if input_user.lower == 'КАМЕНЬ' or input_user.lower == 'ROCK' or input_user == '1':
        return 'rock'
    elif input_user.lower == 'БУМАГА' or input_user.lower == 'PAPER' or input_user == '2':
        return 'paper'
    else:
        return 'scissors'

#функция определения победителя
def winner(user, computer,):
    if (
            (user == 'rock' and computer == 'scissors')
            or
            (user == 'paper' and computer == 'rock' )
            or
            user == 'scissors' and computer == 'paper'
    ):
        return 'wine'

    elif (
            (user == 'rock' and computer == 'rock')
            or
            (user == 'paper' and computer == 'paper')
            or
            (user == 'scissors' and computer == 'scissors')
    ):
        return 'draw'

    else:
        return 'loss'







