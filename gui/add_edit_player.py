from tkinter import *
import sqlite3

import player_database

class AddEditPlayerWindow():
    def __init__(self, list_of_players_window, player_id=None):
        self.player_id = player_id
        self.list_of_players_window = list_of_players_window
        self.players_database_window = Toplevel()
        self.players_database_window.title("Players Database")

        ok_button = Button(self.players_database_window, text="Cancel",
                           command=self.players_database_window.destroy)
        ok_button.grid(row=0, column=0)
        #view_list_of_players_button = Button(players_database_window, text="View List of Players", command=self.open_add_player)
        #view_list_of_players_button.grid(row=1, column=0)

        player_info_frame = LabelFrame(self.players_database_window, text="Player")
        player_info_frame.grid(row=10, column=0)
        #player_id_label = Label(player_info_frame, text="ID")
        #player_id_label.grid(row=0, column=0)
        #player_id_input = Entry(player_info_frame)
        #player_id_input.grid(row=0, column=1)
        player_number_label = Label(player_info_frame, text="Playing #")
        player_number_label.grid(row=1, column=0)
        self.player_number_input = Entry(player_info_frame)
        self.player_number_input.grid(row=1, column=1)
        player_ru_surname_label = Label(player_info_frame, text="Surname, ru")
        player_ru_surname_label.grid(row=2, column=0)
        self.player_ru_surname_input = Entry(player_info_frame)
        self.player_ru_surname_input.grid(row=2, column=1)
        player_ru_name_label = Label(player_info_frame, text="Name, ru")
        player_ru_name_label.grid(row=3, column=0)
        self.player_ru_name_input = Entry(player_info_frame)
        self.player_ru_name_input.grid(row=3, column=1)
        player_ru_patronymic_label = Label(player_info_frame, text="Patronymic, ru")
        player_ru_patronymic_label.grid(row=4, column=0)
        self.player_ru_patronymic_input = Entry(player_info_frame)
        self.player_ru_patronymic_input.grid(row=4, column=1)
        player_en_surname_label = Label(player_info_frame, text="Surname")
        player_en_surname_label.grid(row=5, column=0)
        self.player_en_surname_input = Entry(player_info_frame)
        self.player_en_surname_input.grid(row=5, column=1)
        player_en_name_label = Label(player_info_frame, text="Name")
        player_en_name_label.grid(row=6, column=0)
        self.player_en_name_input = Entry(player_info_frame)
        self.player_en_name_input.grid(row=6, column=1)
        player_en_patronymic_label = Label(player_info_frame, text="Patronymic")
        player_en_patronymic_label.grid(row=7, column=0)
        self.player_en_patronymic_input = Entry(player_info_frame)
        self.player_en_patronymic_input.grid(row=7, column=1)
        player_height_label = Label(player_info_frame, text="Height")
        player_height_label.grid(row=8, column=0)
        self.player_height_input = Entry(player_info_frame)
        self.player_height_input.grid(row=8, column=1)
        player_weight_label = Label(player_info_frame, text="Weight")
        player_weight_label.grid(row=9, column=0)
        self.player_weight_input = Entry(player_info_frame)
        self.player_weight_input.grid(row=9, column=1)
        player_birthday_label = Label(player_info_frame, text="Birthday")
        player_birthday_label.grid(row=99, column=0)
        player_day_of_birthday_label = Label(player_info_frame, text="Day")
        player_day_of_birthday_label.grid(row=99, column=1)
        player_month_of_birthday_label = Label(player_info_frame, text="Month")
        player_month_of_birthday_label.grid(row=99, column=2)
        player_year_of_birthday_label = Label(player_info_frame, text="Year")
        player_year_of_birthday_label.grid(row=99, column=3)
        self.player_day_of_birthday_input = Entry(player_info_frame, width=3)
        self.player_day_of_birthday_input.grid(row=100, column=1)
        self.player_month_of_birthday_input = Entry(player_info_frame, width=3)
        self.player_month_of_birthday_input.grid(row=100, column=2)
        self.player_year_of_birthday_input = Entry(player_info_frame, width=3)
        self.player_year_of_birthday_input.grid(row=100, column=3)
        add_player_info = Button(player_info_frame, text="Add", command=self.add_player)
        add_player_info.grid(row=200, column=0)
        submit_player_info = Button(player_info_frame, text="Submit", command=self.submit_player)
        submit_player_info.grid(row=200, column=1)
        delete_player = Button(player_info_frame, text="Delete", command=self.delete_player)
        delete_player.grid(row=201, column=0)


    def add_player(self):
        conn = sqlite3.connect("player_database.db")

        # Create cursor
        c = conn.cursor()

        # Insert into table
        c.execute("INSERT INTO players(number, first_name_ru, last_name_ru, mid_name_ru, first_name_en, last_name_en, mid_name_en, height, weight, birthday_day, birthday_month, birthday_year) VALUES (:number, :first_name_ru, :last_name_ru, :mid_name_ru, :first_name_en, :last_name_en, :mid_name_en, :height, :weight, :birthday_day, :birthday_month, :birthday_year)",
                {
                    #'id': player_id_input.get(),
                    'number': self.player_number_input.get(),
                    'first_name_ru': self.player_ru_surname_input.get(),
                    'last_name_ru': self.player_ru_name_input.get(),
                    'mid_name_ru': self.player_ru_patronymic_input.get(),
                    'first_name_en': self.player_en_surname_input.get(),
                    'last_name_en': self.player_en_name_input.get(),
                    'mid_name_en': self.player_en_patronymic_input.get(),
                    'height': self.player_height_input.get(),
                    'weight': self.player_weight_input.get(),
                    'birthday_day': self.player_day_of_birthday_input.get(),
                    'birthday_month': self.player_month_of_birthday_input.get(),
                    'birthday_year': self.player_year_of_birthday_input.get()
                })

        # Commit changes
        conn.commit()

        # Close sqlite connection
        conn.close()

        # self.list_of_players_window.update_list_of_players()
        self.clear_fields()

    def clear_fields(self):
        self.player_number_input.delete(0, END)
        self.player_ru_surname_input.delete(0, END)
        self.player_ru_name_input.delete(0, END)
        self.player_ru_patronymic_input.delete(0, END)
        self.player_en_surname_input.delete(0, END)
        self.player_en_name_input.delete(0, END)
        self.player_en_patronymic_input.delete(0, END)
        self.player_height_input.delete(0, END)
        self.player_weight_input.delete(0, END)
        self.player_day_of_birthday_input.delete(0, END)
        self.player_month_of_birthday_input.delete(0, END)
        self.player_year_of_birthday_input.delete(0, END)

    def submit_player(self):
        conn = sqlite3.connect("player_database.db")

        # Create cursor
        c = conn.cursor()

        # Insert into table
        c.execute('''UPDATE players SET
            number = :number,
            first_name_ru = :first_name_ru,
            last_name_ru = :last_name_ru,
            mid_name_ru = :mid_name_ru,
            first_name_en = :first_name_en,
            last_name_en = :last_name_en,
            mid_name_en = :mid_name_en,
            height = :height,
            weight = :weight,
            birthday_day = :birthday_day,
            birthday_month = :birthday_month,
            birthday_year = :birthday_year

            WHERE oid = :oid''',
            {
                #'id': player_id_input.get(),
                'number': self.player_number_input.get(),
                'first_name_ru': self.player_ru_surname_input.get(),
                'last_name_ru': self.player_ru_name_input.get(),
                'mid_name_ru': self.player_ru_patronymic_input.get(),
                'first_name_en': self.player_en_surname_input.get(),
                'last_name_en': self.player_en_name_input.get(),
                'mid_name_en': self.player_en_patronymic_input.get(),
                'height': self.player_height_input.get(),
                'weight': self.player_weight_input.get(),
                'birthday_day': self.player_day_of_birthday_input.get(),
                'birthday_month': self.player_month_of_birthday_input.get(),
                'birthday_year': self.player_year_of_birthday_input.get(),
                'oid': self.player_id
            })

        # Commit changes
        conn.commit()

        # Close sqlite connection
        conn.close()
        self.players_database_window.destroy()
        e = player_database.PlayerDatabase()

    def delete_player(self):
        conn = sqlite3.connect("player_database.db")

        # Create cursor
        c = conn.cursor()

        # Delete a record
        c.execute("DELETE from players WHERE oid = " + str(self.player_id))
        # Commit changes
        conn.commit()

        # Close sqlite connection
        conn.close()
        # self.list_of_players_window.update_list_of_players()
        self.players_database_window.destroy()
        e = player_database.PlayerDatabase()
