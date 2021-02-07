from tkinter import *
import sqlite3
import copy

import add_edit_player

class PlayerDatabase():
    def __init__(self):
        self.list_of_players_window = Toplevel()
        self.list_of_players_window.title("List of Players")

        ok_button = Button(self.list_of_players_window, text="Ok",
                           command=self.list_of_players_window.destroy)
        ok_button.pack()
        add_player_button = Button(self.list_of_players_window, text="+",
                                   command=lambda:self.open_add_player(self))
        add_player_button.pack()
        self.update_list_of_players()

    def update_list_of_players(self):
        conn = sqlite3.connect('player_database.db')
        c = conn.cursor()

        c.execute("SELECT oid, * FROM players")

        records = c.fetchall()
        print(records)
        for i, *record in records:
            print(str(i) + ":"+ str(record))
            name_label = record[4] + ' ' + record[5]
            Button(self.list_of_players_window, text=name_label,
                   command=lambda oid=i:self.edit_player(oid)).pack()
            #print(record[i])


        #Label(list_of_players_window, text=str(records)).pack()
        #player1_button = Button(list_of_players_window, text="Player1")
        #player1_button.grid(row=1, column=0)
        #player2_button = Button(list_of_players_window, text="Player2")
        #player2_button.grid(row=2, column=0)

        conn.commit()
        conn.close()

    def open_add_player(self, parent_window):
        e = add_edit_player.AddEditPlayerWindow(self)
        self.list_of_players_window.destroy()

    def edit_player(self, player_id):
        print("edit_player id:" + str(player_id))
        e = add_edit_player.AddEditPlayerWindow(self, player_id)

        conn = sqlite3.connect("player_database.db")

        # Create cursor
        c = conn.cursor()

        # Insert into table
        c.execute("SELECT * FROM players WHERE oid=" + str(player_id))

        records = c.fetchall()
        # Commit changes
        conn.commit()

        # Close sqlite connection
        conn.close()

        print(records)

        for record in records:
            e.player_number_input.insert(0, record[0])
            e.player_ru_surname_input.insert(0, record[1])
            e.player_ru_name_input.insert(0, record[2])
            e.player_ru_patronymic_input.insert(0, record[3])
            e.player_en_surname_input.insert(0, record[4])
            e.player_en_name_input.insert(0, record[5])
            e.player_en_patronymic_input.insert(0, record[6])
            e.player_height_input.insert(0, record[7])
            e.player_weight_input.insert(0, record[8])
            e.player_day_of_birthday_input.insert(0, record[9])
            e.player_month_of_birthday_input.insert(0, record[10])
            e.player_year_of_birthday_input.insert(0, record[11])

        self.list_of_players_window.destroy()
