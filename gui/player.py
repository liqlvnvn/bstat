class Player:

    def __init__(self):
        self.player_id = None
        self.number = 0
        self.ru_surname = ""
        self.ru_name = ""
        self.ru_patronymic = ""
        self.en_surname = ""
        self.en_name = ""
        self.en_patronymic = ""
        self.height = 0
        self.weight = 0
        self.birthday_day = 0
        self.birthday_month = 0
        self.birthday_year = 0
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

    def __init__(self, number, ru_surname, ru_name, ru_patronymic,
            en_surname, en_name, en_patronymic,
            height, weight,
            birthday_day, birthday_month, birthday_year):
        self.player_id = None
        self.number = number
        self.ru_surname = ru_surname
        self.ru_name = ru_name
        self.ru_patronymic = ru_patronymic
        self.en_surname = en_surname
        self.en_name = en_name
        self.en_patronymic = en_patronymic
        self.height = height
        self.weight = weight
        self.birthday_day = birthday_day
        self.birthday_month = birthday_month
        self.birthday_year = birthday_year
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

    def name(self):
        return self.en_surname + ' ' + self.en_name

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


