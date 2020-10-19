# Приложение для ведения баскетбольной статистики в наших играх.
# Основная часть - ведение статистики матчей, из которой потом будем извлекать статистики по остальным критериям.


class Player:

    def __init__(self, name=""):
        self.__name = name
        self.__minutes = 0
        self.__points = 0
        self.__fdm = 0
        self.__fga = 0
        self.__3pm = 0
        self.__3pa = 0
        self.__ftm = 0
        self.__fta = 0
        self.__rebounds = 0
        self.__offensive_rebounds = 0
        self.__defensive_rebounds = 0
        self.__assists = 0
        self.__steals = 0
        self.__blocks = 0
        self.__shots_blocked = 0
        self.__turnovers = 0
        self.__fouls = 0

    def make_shot(self, points):
        self.__fga += 1
        self.__points += points

    def miss_shot(self):
        self.__fga += 1

    def make_orebound(self):
        self.__rebounds += 1
        self.__offensive_rebounds += 1

    def make_assist(self):
        self.__assists += 1

    def make_steal(selft):
        self.__steals += 1

class Team:
    # team stats
    def __init__(self):
        self.__name__ = ""
        self.__player_list__ = []
        self.__points__ = 0
        self.__rebound__ = 0
        self.__oreb__ = 0
        self.__dreb__ = 0
        self.__assists__ = 0
        self.__steals__ = 0
        self.__blocks__ = 0
        self.__turnovers__ = 0
        self.__foul__ = 0

class Game:
    # game stats
    def __init__(self):
        self.__place__
        self.__team1__
        self.__team2__
        self.__score1__
        self.__score2__


class Event:
    def __init__(self, time, score):
        self.__time__ = time
        self.__score__ = (score[0], score[1])
t='''
        Shot Missed
        Shot Maden (Type of shot? Assisted? Who defended?)
        Foul
        Rebound
        Timeout
        Turnover (Bad Pass, Base Line, Lost ball(Walking, Double Dribbling))
        Steal (By Who) From
        SUBSTITUTION

'''
