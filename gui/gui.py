#!/usr/bin/python3

from tkinter import *
import time
import sqlite3

# Project's imports
import game_settings
import player_database
import game_settings
import select_player
import player


root = Tk()
root.title("Basketball Statistics")

class MainWindow():
    def __init__(self, master):
        menu_frame = LabelFrame(root)
        menu_frame.grid(row=0, column=0)

        new_game_button = Button(menu_frame, text="New Game", command=self.new_game)
        new_game_button.grid(row=0, column=0)
        game_details_button = Button(menu_frame, text="Game Details", command=self.open_game_details)
        game_details_button.grid(row=0, column=1)

        players_database_button = Button(menu_frame, text="Players database", command=self.open_players_database)
        players_database_button.grid(row=0, column=2)

        close_button = Button(menu_frame, text="Close", command=root.destroy)
        close_button.grid(row=0, column=3)

        game_actions_frame = LabelFrame(root)
        game_actions_frame.grid(row=1, column=0)
        myLabel = Label(game_actions_frame, text=time.strftime('%H:%M:%S'))
        myLabel.grid(row=0, column=0)
        shot_button = Button(game_actions_frame, text="Shot")
        shot_button.grid(row=1, column=0)
        #made_bucket_button = Button(text="Made Bucket")
        #made_bucket_button.grid(row=1, column=0)

        rebound_button = Button(game_actions_frame, text="Rebound")
        rebound_button.grid(row=2, column=0)

        made_turnover_button = Button(game_actions_frame, text="Turnover")
        made_turnover_button.grid(row=3, column=0)

        #blockshot_button = Button(text="Block")
        #blockshot_button.grid(row=4, column=0)

        #steal_button = Button(text="Steal")
        #steal_button.grid(row=5, column=0)
        #grid(row=0, column=0)

        foul_button = Button(game_actions_frame, text="Foul")
        foul_button.grid(row=6, column=0)



        rosters_frame = LabelFrame(root, text="Rosters", padx=5, pady=5)
        rosters_frame.grid(row=100, column=0)

        self.team1_roster_list = []
        self.team2_roster_list = []
        self.team1_playing_list = []
        self.team2_playing_list = []

        self.team1_frame = LabelFrame(rosters_frame, text="Team1 roster", padx=5, pady=5)
        self.team1_frame.grid(row=0, column=0)
        self.team1_frame_roster = LabelFrame(self.team1_frame, text="Roster")
        team1_add_player_button = Button(self.team1_frame, text="+",
                command=lambda x = self.team1_frame_roster,
                               y = self.team1_roster_list:
                            self.add_player2roster(x, y))
        team1_add_player_button.pack()
        self.team1_frame_roster.pack()
        team1_player1_checkbox = Checkbutton(self.team1_frame_roster, text="Player1")
        team1_player2_checkbox = Checkbutton(self.team1_frame_roster, text="Player2")
        team1_player3_checkbox = Checkbutton(self.team1_frame_roster, text="Player3")
        team1_player4_checkbox = Checkbutton(self.team1_frame_roster, text="Player4")
        team1_player1_checkbox.pack()
        team1_player2_checkbox.pack()
        team1_player3_checkbox.pack()
        team1_player4_checkbox.pack()

        self.team2_frame = LabelFrame(rosters_frame, text="Team2 roster", padx=5, pady=5)
        self.team2_frame.grid(row=0, column=100)
        self.team2_frame_roster = LabelFrame(self.team2_frame, text="Roster")
        team2_add_player_button = Button(self.team2_frame, text="+",
                command=lambda x = self.team2_frame_roster,
                               y = self.team2_roster_list:
                            self.add_player2roster(x, y))
        team2_add_player_button.pack()
        self.team2_frame_roster.pack()
        team2_player1_checkbox = Checkbutton(self.team2_frame_roster, text="Player5")
        team2_player2_checkbox = Checkbutton(self.team2_frame_roster, text="Player6")
        team2_player3_checkbox = Checkbutton(self.team2_frame_roster, text="Player7")
        team2_player4_checkbox = Checkbutton(self.team2_frame_roster, text="Player8")
        team2_player1_checkbox.pack()
        team2_player2_checkbox.pack()
        team2_player3_checkbox.pack()
        team2_player4_checkbox.pack()

        self.playing_roster_frame = LabelFrame(rosters_frame, text="Playing rosters", padx=5, pady=5)
        self.playing_roster_frame.grid(row=0, column=2)
        r = IntVar()
        self.playing_roster_team1_frame = LabelFrame(self.playing_roster_frame,
                text="Team1")
        self.playing_roster_team1_frame.pack() #grid(row=0, column=0)
        self.playing_roster_team2_frame = LabelFrame(self.playing_roster_frame,
                text="Team2")
        self.playing_roster_team2_frame.pack() #grid(row=0, column=1)
        test_team11_radiobutton = Radiobutton(self.playing_roster_team1_frame,
                text="Player1", variable=r, value = 1)
        test_team12_radiobutton = Radiobutton(self.playing_roster_team1_frame,
                text="Player2", variable=r, value = 2)
        test_team13_radiobutton = Radiobutton(self.playing_roster_team1_frame,
                text="Player3", variable=r, value = 2)
        test_team21_radiobutton = Radiobutton(self.playing_roster_team2_frame,
                text="Player4", variable=r, value = 2)
        test_team22_radiobutton = Radiobutton(self.playing_roster_team2_frame,
                text="Player5", variable=r, value = 2)
        test_team23_radiobutton = Radiobutton(self.playing_roster_team2_frame,
                text="Player6", variable=r, value = 2)
        test_team11_radiobutton.grid(row=0, column=0)
        test_team12_radiobutton.grid(row=1, column=0)
        test_team13_radiobutton.grid(row=2, column=0)
        test_team21_radiobutton.grid(row=0, column=0)
        test_team22_radiobutton.grid(row=1, column=0)
        test_team23_radiobutton.grid(row=2, column=0)

        event_list_frame = LabelFrame(root, text="Events", padx=5, pady=5)
        event_list_frame.grid(row=100, column=1)
        test_event1_button = Label(event_list_frame, text="Event1")
        test_event2_button = Label(event_list_frame, text="Event2")
        test_event1_button.pack()
        test_event2_button.pack()

        substitution_button = Button(game_actions_frame, text="Substitution",
                command=self.substitution())
        substitution_button.grid(row=7, column=0)

    def new_game(self):
        for widget in self.team1_frame_roster.winfo_children():
            widget.destroy()

        for widget in self.team2_frame_roster.winfo_children():
            widget.destroy()

    def open_game_details(self):
        # game_settings.open_game_details()
        w = game_settings.GameSettingsWindow()

    def open_players_database(self):
        e = player_database.PlayerDatabase()

    def add_player2roster(self, frame, t_list):
        # open window with list of players
        s = select_player.PlayerSelection()
        p = s.player
        t_list = t_list.append(p)
        Checkbutton(frame, text=p.name()).pack()

    def substitution(self):
        for widget in self.playing_roster_team1_frame.winfo_children():
            widget.destroy()

        for widget in self.playing_roster_team1_frame.winfo_children():
            widget.destroy()

        for player in self.team1_roster_list:
            if player not in self.team1_playing_list:
                self.team1_playing_list.append(player)

        for player in self.team2_roster_list:
            if player not in self.team2_playing_list:
                self.team2_playing_list.append(player)

        for player in self.team1_playing_list:
            Radiobutton(self.playing_roster_team1_frame, text=player.name())

        for player in self.team2_playing_list:
            Radiobutton(self.playing_roster_team2_frame, text=player.name())


main_window = MainWindow(root)

root.mainloop()
