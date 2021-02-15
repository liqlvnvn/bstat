# Приложение для ведения баскетбольной статистики в наших играх.
# Основная часть - ведение статистики матчей, из которой потом будем извлекать статистики по остальным критериям.


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
