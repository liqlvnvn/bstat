from tkinter import *
import sqlite3

import player_database
import player

class PlayerSelection():
    def __init__(self):
        self.list_of_players_window = Toplevel()
        self.list_of_players_window.title("List of Players")

        cancel_button = Button(self.list_of_players_window, text="Cancel",
                               command=self.list_of_players_window.destroy)
        cancel_button.pack()

        self.player_list = []
        self.update_list_of_players()
        self.display_list_of_players()
        self.list_of_players_window.wait_window()
        self.list_of_players_window.destroy()

    def display_list_of_players(self):
        for player in self.player_list:
            name_label = player.name()
            Button(self.list_of_players_window, text=name_label,
                   command=lambda i = player:self.select_player(i)).pack()

    def update_list_of_players(self):
        conn = sqlite3.connect('player_database.db')
        c = conn.cursor()

        c.execute("SELECT oid, * FROM players")

        records = c.fetchall()
        print(records)
        for i, *record in records:
            #print(str(i) + ":"+ str(record))
            name_label = record[4] + ' ' + record[5]
            #print(record)
            #print("Object")
            #print(player.Player(*record))
            self.player_list.append(player.Player(*record))
            #Button(self.list_of_players_window, text=name_label,
            #       command=lambda oid=i:self.select_player(oid)).pack()
            #print(record[i])


        #Label(list_of_players_window, text=str(records)).pack()
        #player1_button = Button(list_of_players_window, text="Player1")
        #player1_button.grid(row=1, column=0)
        #player2_button = Button(list_of_players_window, text="Player2")
        #player2_button.grid(row=2, column=0)

        conn.commit()
        conn.close()

    def select_player(self, player):
        #self.player_list.pop(player)
        self.player = player
        self.list_of_players_window.destroy()
        #return player

