#!/usr/bin/python3

from tkinter import *

root = Tk()
root.title("Basketball Statistics")

def open():
    game_details_window = Toplevel()
    game_details_window.title("Game Details")

game_details_button = Button(text="Game Details", command=open)
game_details_button.grid(row=0, column=1)

myLabel = Label(root, text="Hello World!")
myLabel.grid(row=0, column=0)

made_bucket_button = Button(text="Made Bucket")
made_bucket_button.grid(row=1, column=0)

made_turnover_button = Button(text="Turnover")
made_turnover_button.grid(row=2, column=0)


rebound_button = Button(text="Rebound")
blockshot_button = Button(text="Block")
steal_button = Button(text="Steal")
#grid(row=0, column=0)


rosters_frame = LabelFrame(root, text="Rosters", padx=5, pady=5)
rosters_frame.grid(row=100, column=0)

team1_frame = LabelFrame(rosters_frame, text="Team1", padx=20, pady=50)
team1_frame.grid(row=0, column=0)
team1_player1_checkbox = Checkbutton(team1_frame, text="Player1")
team1_player1_checkbox.pack()

team2_frame = LabelFrame(rosters_frame, text="Team2", padx=20, pady=50)
team2_frame.grid(row=0, column=100)
team2_player1_checkbox = Checkbutton(team2_frame, text="Player1")
team2_player1_checkbox.pack()

test_team1_button = Button(rosters_frame, text="Team1")
test_team2_button = Button(rosters_frame, text="Team2")
test_team1_button.grid(row=0, column=1)
test_team2_button.grid(row=0, column=2)

event_list_frame = LabelFrame(root, text="Events", padx=50, pady=50)
event_list_frame.grid(row=100, column=1)
test_event1_button = Label(event_list_frame, text="Event1")
test_event2_button = Label(event_list_frame, text="Event2")
test_event1_button.pack()
test_event2_button.pack()

root.mainloop()
