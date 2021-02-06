from tkinter import *
import sqlite3

import add_edit_player

class PlayerDatabase():
    def __init__(self):
        list_of_players_window = Toplevel()
        list_of_players_window.title("List of Players")

        ok_button = Button(list_of_players_window, text="Ok", command=list_of_players_window.destroy)
        ok_button.pack()
        add_player_button = Button(list_of_players_window, text="+", command=self.open_add_player)
        add_player_button.pack()

        conn = sqlite3.connect('player_database.db')
        c = conn.cursor()

        c.execute("SELECT *, oid FROM players")

        records = c.fetchall()
        print(records)
        for i, record in enumerate(records):
            name_label = record[2] + ' ' + record[3]
            Button(list_of_players_window, text=name_label, command=lambda:edit_player(records[i])).pack()
            print(i)
            print(record[i])

        #Label(list_of_players_window, text=str(records)).pack()
        #player1_button = Button(list_of_players_window, text="Player1")
        #player1_button.grid(row=1, column=0)
        #player2_button = Button(list_of_players_window, text="Player2")
        #player2_button.grid(row=2, column=0)

        conn.commit()
        conn.close()

    def edit_player_info():
        pass

    def open_add_player(self):
        e = add_edit_player.AddEditPlayerWindow()
