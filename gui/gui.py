#!/usr/bin/python3

from tkinter import *
import time
import sqlite3

# Project's imports
import game_settings
import player_database


root = Tk()
root.title("Basketball Statistics")

class MainWindow():
    def __init__(self, master):
        myLabel = Label(root, text=time.strftime('%H:%M:%S'))
        myLabel.grid(row=0, column=0)

        game_details_button = Button(text="Game Details", command=self.open_game_details)
        game_details_button.grid(row=0, column=1)

        players_database_button = Button(text="Players database", command=self.open_players_database)
        players_database_button.grid(row=0, column=2)

        close_button = Button(text="Close", command=root.destroy)
        close_button.grid(row=0, column=3)

        shot_button = Button(text="Shot")
        shot_button.grid(row=1, column=0)
        #made_bucket_button = Button(text="Made Bucket")
        #made_bucket_button.grid(row=1, column=0)

        rebound_button = Button(text="Rebound")
        rebound_button.grid(row=2, column=0)

        made_turnover_button = Button(text="Turnover")
        made_turnover_button.grid(row=3, column=0)

        #blockshot_button = Button(text="Block")
        #blockshot_button.grid(row=4, column=0)

        #steal_button = Button(text="Steal")
        #steal_button.grid(row=5, column=0)
        #grid(row=0, column=0)

        foul_button = Button(text="Foul")
        foul_button.grid(row=6, column=0)


        rosters_frame = LabelFrame(root, text="Rosters", padx=5, pady=5)
        rosters_frame.grid(row=100, column=0)

        team1_frame = LabelFrame(rosters_frame, text="Team1 roster", padx=5, pady=5)
        team1_frame.grid(row=0, column=0)
        team1_add_player_button = Button(team1_frame, text="+")
        team1_add_player_button.pack()
        team1_player1_checkbox = Checkbutton(team1_frame, text="Player1")
        team1_player2_checkbox = Checkbutton(team1_frame, text="Player2")
        team1_player3_checkbox = Checkbutton(team1_frame, text="Player3")
        team1_player4_checkbox = Checkbutton(team1_frame, text="Player4")
        team1_player1_checkbox.pack()
        team1_player2_checkbox.pack()
        team1_player3_checkbox.pack()
        team1_player4_checkbox.pack()

        team2_frame = LabelFrame(rosters_frame, text="Team2 roster", padx=5, pady=5)
        team2_frame.grid(row=0, column=100)
        team2_add_player_button = Button(team2_frame, text="+")
        team2_add_player_button.pack()
        team2_player1_checkbox = Checkbutton(team2_frame, text="Player5")
        team2_player2_checkbox = Checkbutton(team2_frame, text="Player6")
        team2_player3_checkbox = Checkbutton(team2_frame, text="Player7")
        team2_player4_checkbox = Checkbutton(team2_frame, text="Player8")
        team2_player1_checkbox.pack()
        team2_player2_checkbox.pack()
        team2_player3_checkbox.pack()
        team2_player4_checkbox.pack()

        playing_roster_frame = LabelFrame(rosters_frame, text="Playing rosters", padx=5, pady=5)
        playing_roster_frame.grid(row=0, column=2)
        r = IntVar()
        test_team11_radiobutton = Radiobutton(playing_roster_frame, text="Player1", variable=r, value = 1)
        test_team12_radiobutton = Radiobutton(playing_roster_frame, text="Player2", variable=r, value = 2)
        test_team13_radiobutton = Radiobutton(playing_roster_frame, text="Player3", variable=r, value = 2)
        test_team21_radiobutton = Radiobutton(playing_roster_frame, text="Player4", variable=r, value = 2)
        test_team22_radiobutton = Radiobutton(playing_roster_frame, text="Player5", variable=r, value = 2)
        test_team23_radiobutton = Radiobutton(playing_roster_frame, text="Player6", variable=r, value = 2)
        test_team11_radiobutton.grid(row=0, column=0)
        test_team12_radiobutton.grid(row=1, column=0)
        test_team13_radiobutton.grid(row=2, column=0)
        test_team21_radiobutton.grid(row=0, column=1)
        test_team22_radiobutton.grid(row=1, column=1)
        test_team23_radiobutton.grid(row=2, column=1)

        event_list_frame = LabelFrame(root, text="Events", padx=5, pady=5)
        event_list_frame.grid(row=100, column=1)
        test_event1_button = Label(event_list_frame, text="Event1")
        test_event2_button = Label(event_list_frame, text="Event2")
        test_event1_button.pack()
        test_event2_button.pack()


    def open_game_details(self):
        game_settings.open_game_details()

    def open_players_database(self):
        e = player_database.PlayerDatabase()


main_window = MainWindow(root)

root.mainloop()
