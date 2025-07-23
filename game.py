# основные функции
from functions import choice_computer, choice_user
from functions import choice_user
from functions import winner
from functions import output_message
from functions import save_history

import configparser
import sys
import os.path
import json

class ScoreBoard:
    # Конструктор
    def __init__(self, user_count, comp_count,
                 msg_current_score, msg_total_score,
                 total_count_user, total_count_comp, result):
        self.user_count = user_count  # Текущие победы пользователя
        self.comp_count = comp_count  # Текущие победы компьютера
        self.result = result # Текущий результат игры
        self.msg_current_score = msg_current_score # сообщение о текущем счете
        self.msg_total_score = msg_total_score # сообщение о общем счете
        self.total_count_user = total_count_user #общий счет побед пользователя
        self.total_count_comp = total_count_comp #общий счет побед компьютера

   # метод обновления сетчика
    def counter_update(self):
        if self.result in ['\033[32m ВЫ ПОБЕДИЛИ :) \033[0m', '\033[32m WINE :) \033[0m']:
            self.user_count += 1
            self.total_count_user += 1
        elif self.result in ['НИЧЬЯ :|', 'DRAW :|']:
            self.user_count += 0.5
            self.comp_count += 0.5
            self.total_count_user += 0.5
            self.total_count_comp += 0.5
        else:
            self.comp_count += 1
            self.total_count_comp += 1
        return self.user_count, self.comp_count, self.total_count_user, self.total_count_comp


    #метод отображения счетчика
    def print_score(self, user_count, comp_count,
                    total_count_user, total_count_comp):
        score = f"{user_count} : {comp_count}"
        score = f" {score:^40}"
        print(f'{self.msg_current_score} {score}')

        score = f"{total_count_user} : {total_count_comp}"
        score = f" {score:^40}"
        print(f'{self.msg_total_score} {score}')



#директория файла
path = os.path.dirname(__file__)

# чтение файла конфигурации,
path_ini = path + '\\config.ini'
config = configparser.ConfigParser()
if os.path.isfile(path_ini) == True:
    config.read(path_ini)
    language  = config.get('LANGUAGE', 'default_language')
else:
    config.add_section('LANGUAGE')
    config.set('LANGUAGE', 'default_language', 'EN')
    with open(path_ini, 'w') as configfile:
        config.write(configfile)
        language = 'EN'


# чтение файла истории игр
path = path + '\\history_games.json'
if os.path.isfile(path) == True:
    with open(path, 'r') as file:
        data = json.load(file)
else:
    data = {}

#вывод приветствия
messages = output_message(language)
print(messages['greetings'])
print(messages['menu_message'])
config.set('LANGUAGE', 'default_language', 'RU')
input_user = None

while True:
    # изначальный результат игры неопределен
    result = ''
    language = language
    messages = output_message(language)
    #основное меню
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
        #Ввод имени игрока
        name_user = str(input(messages['name_user']))

        #поиск игрока в истории игр
        if bool(data) != False:
                if name_user in data:
                    total_count_user = data[name_user][0]
                    total_count_comp = data[name_user][1]
                else:
                    total_count_user = 0
                    total_count_comp = 0
        else:
            total_count_user = 0
            total_count_comp = 0

        user_count = 0
        comp_count = 0

        while input_user.upper() != 'EXIT' and input_user.upper() != 'ВЫХОД':
            print(messages['input_choice_user'])
            input_user = str(input())
            data_score = ScoreBoard(user_count=user_count,
                                    comp_count=comp_count,
                                    total_count_user=total_count_user,
                                    total_count_comp=total_count_comp,
                                    msg_current_score=messages['msg_current_score'],
                                    msg_total_score=messages['msg_total_score'],
                                    result=result)
            #проверка правильности ввода, игра
            if input_user.upper() in ['КАМЕНЬ','НОЖНИЦЫ','БУМАГА', 'ROCK', 'PAPER', 'SCISSORS', '1','2','3']:
                user = choice_user(input_user, language = language)
                print(f"{messages['your_choice']} {user}")
                computer = choice_computer(messages['primary_choice'], language = language)
                print(f"{messages['opponent_choice']} {computer}")
                result = winner(user, computer, language=language)
                print(result)
                print(' ')
                data_score = ScoreBoard(user_count=user_count,
                                        comp_count=comp_count,
                                        total_count_user=total_count_user,
                                        total_count_comp=total_count_comp,
                                        msg_current_score=messages['msg_current_score'],
                                        msg_total_score=messages['msg_total_score'],
                                        result=result)
                user_count, comp_count, total_count_user, total_count_comp = data_score.counter_update()
            # вывод счета
            elif input_user.upper() == '4':
                print('-'*40)
                data_score.print_score(user_count, comp_count, total_count_user, total_count_comp)
                print('-' * 40)
                print(' ')

            # выход из игры
            elif input_user.upper() == 'EXIT' or input_user.upper() == 'ВЫХОД':
                print(messages['end_game'])
                data[name_user] = [total_count_user,total_count_comp]
                save_history(data)
                sys.exit()

            #переход в меню
            elif input_user.upper() == 'MENU' or input_user.upper() == "МЕНЮ":
                print(messages['menu_message'])
                result = ''
                data[name_user] = [total_count_user, total_count_comp]
                save_history(data)
                break
            else:
                print(messages['input_error'])

    #рейтинг игроков
    elif input_user.upper() == 'RATING' or input_user.upper() == "РЕЙТИНГ":
        data_dict = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))
        print(f' {"_" * 47}')
        print(f'|{"Игрок":^15}|{"Победы":^15}|{"Поражения":^15}|')
        print(f' {"_"*47}')
        for key in data_dict:
            print(f'|{key:^15}|{data_dict[key][0]:^15}|{data_dict[key][1]:^15}|')
        print(f' {"_" * 47}')

    #выход из игры
    elif input_user.upper() == 'EXIT' or input_user.upper() == 'ВЫХОД':
        (print(messages['end_game']))
        sys.exit()









