#!/usr/bin/python3

from tkinter import *
import time
import sqlite3



root = Tk()
root.title("Basketball Statistics")

def open_game_details():
    game_details_window = Toplevel()
    game_details_window.title("Game Details")
    # Game Details window
    v = IntVar()
    game_type_streetball_radiobutton = Radiobutton(game_details_window, text="Streetball", variable=v, value=1)
    game_type_basketball_radiobutton = Radiobutton(game_details_window, text="Basketball", variable=v, value=2)
    game_type_streetball_radiobutton.grid(row=0, column=0)
    game_type_basketball_radiobutton.grid(row=1, column=0)
    ### End of Game Details window
    basketball_rules_frame = LabelFrame(game_details_window, text="Basketball Rules")
    basketball_rules_frame.grid(row=2, column=0)
    basketball_number_of_periods_label = Label(basketball_rules_frame, text="Number of periods: ")
    basketball_number_of_periods_label.grid(row=0, column=0)
    #number_of_periods_input = simpledialog.askinteger("Input", "What is period length in minutes?",
    #        parent=game_details_window, minvalue=1, maxvalue=30)
    basketball_number_of_periods_input = Entry(basketball_rules_frame)
    basketball_number_of_periods_input.grid(row=0, column=1)
    basketball_periods_label = Label(basketball_rules_frame, text="Periods")
    basketball_periods_label.grid(row=1, column=0)
    basketball_period1_label = Label(basketball_rules_frame, text="1")
    basketball_period1_label.grid(row=1, column=1)
    basketball_period2_label = Label(basketball_rules_frame, text="2")
    basketball_period2_label.grid(row=1, column=2)
    basketball_period3_label = Label(basketball_rules_frame, text="3")
    basketball_period3_label.grid(row=1, column=3)
    basketball_period4_label = Label(basketball_rules_frame, text="4")
    basketball_period4_label.grid(row=1, column=4)
    basketball_period_ot_label = Label(basketball_rules_frame, text="OT")
    basketball_period_ot_label.grid(row=1, column=5)

    basketball_length_of_periods_label = Label(basketball_rules_frame, text="Length, min")
    basketball_length_of_periods_label.grid(row=2, column=0)
    basketball_period1_input = Entry(basketball_rules_frame)
    basketball_period1_input.grid(row=2, column=1)
    basketball_period2_input = Entry(basketball_rules_frame)
    basketball_period2_input.grid(row=2, column=2)
    basketball_period3_input = Entry(basketball_rules_frame)
    basketball_period3_input.grid(row=2, column=3)
    basketball_period4_input = Entry(basketball_rules_frame)
    basketball_period4_input.grid(row=2, column=4)
    basketball_period_ot_label = Entry(basketball_rules_frame)
    basketball_period_ot_label.grid(row=2, column=5)

    basketball_length_of_timeouts_label = Label(basketball_rules_frame, text="Timeout, min")
    basketball_length_of_timeouts_label.grid(row=3, column=0)
    basketball_timeout2_input = Entry(basketball_rules_frame)
    basketball_timeout2_input.grid(row=3, column=2)
    basketball_timeout3_input = Entry(basketball_rules_frame)
    basketball_timeout3_input.grid(row=3, column=3)
    basketball_timeout4_input = Entry(basketball_rules_frame)
    basketball_timeout4_input.grid(row=3, column=4)
    basketball_timeout_ot_input = Entry(basketball_rules_frame)
    basketball_timeout_ot_input.grid(row=3, column=5)

    basketball_team_fouls_label = Label(basketball_rules_frame, text="Team Fouls")
    basketball_team_fouls_label.grid(row=4, column=0)
    basketball_team_fouls1_input = Entry(basketball_rules_frame)
    basketball_team_fouls1_input.grid(row=4, column=1)
    basketball_team_fouls2_input = Entry(basketball_rules_frame)
    basketball_team_fouls2_input.grid(row=4, column=2)
    basketball_team_fouls3_input = Entry(basketball_rules_frame)
    basketball_team_fouls3_input.grid(row=4, column=3)
    basketball_team_fouls4_input = Entry(basketball_rules_frame)
    basketball_team_fouls4_input.grid(row=4, column=4)

    basketball_players_on_court_label = Label(basketball_rules_frame, text="Player on court")
    basketball_players_on_court_label.grid(row=5, column=0)
    basketball_players_on_court_input = Entry(basketball_rules_frame)
    basketball_players_on_court_input.grid(row=5, column=1)

    basketball_personal_fouls_label = Label(basketball_rules_frame, text="Personal Fouls")
    basketball_personal_fouls_label.grid(row=6, column=0)
    basketball_personal_fouls_input = Entry(basketball_rules_frame)
    basketball_personal_fouls_input.grid(row=6, column=1)


    basketball_number_of_points_label = Label(basketball_rules_frame, text="Number of points: ")
    basketball_number_of_points_label.grid(row=902, column=0)
    basketball_free_throw_points_label = Label(basketball_rules_frame, text="Free Throw")
    basketball_free_throw_points_label.grid(row=901, column=1)
    basketball_free_throw_points_input = Entry(basketball_rules_frame)
    basketball_free_throw_points_input.grid(row=902, column=1)
    basketball_game_shot_points_label = Label(basketball_rules_frame, text="Game Shot")
    basketball_game_shot_points_label.grid(row=901, column=2)
    basketball_game_shot_points_input = Entry(basketball_rules_frame)
    basketball_game_shot_points_input.grid(row=902, column=2)
    basketball_longrange_shot_points_label = Label(basketball_rules_frame, text="Long Range Shot")
    basketball_longrange_shot_points_label.grid(row=901, column=3)
    basketball_longrange_shot_points_input = Entry(basketball_rules_frame)
    basketball_longrange_shot_points_input.grid(row=902, column=3)
    #duration_of_the_period = 

    # STREETBALL SECTION
    streetball_rules_frame = LabelFrame(game_details_window, text="Streetball Rules")
    streetball_rules_frame.grid(row=3, column=0)
    streetball_number_of_periods_label = Label(streetball_rules_frame, text="Number of periods: ")
    streetball_number_of_periods_label.grid(row=0, column=0)
    #number_of_periods_input = simpledialog.askinteger("Input", "What is period length in minutes?",
    #        parent=game_details_window, minvalue=1, maxvalue=30)
    streetball_number_of_periods_input = Entry(streetball_rules_frame)
    streetball_number_of_periods_input.grid(row=0, column=1)
    streetball_periods_label = Label(streetball_rules_frame, text="Periods")
    streetball_periods_label.grid(row=1, column=0)
    streetball_period1_label = Label(streetball_rules_frame, text="1")
    streetball_period1_label.grid(row=1, column=1)
    streetball_period2_label = Label(streetball_rules_frame, text="2")
    streetball_period2_label.grid(row=1, column=2)
    streetball_period3_label = Label(streetball_rules_frame, text="3")
    streetball_period3_label.grid(row=1, column=3)
    streetball_period4_label = Label(streetball_rules_frame, text="4")
    streetball_period4_label.grid(row=1, column=4)
    streetball_period_ot_label = Label(streetball_rules_frame, text="OT")
    streetball_period_ot_label.grid(row=1, column=5)

    streetball_length_of_periods_label = Label(streetball_rules_frame, text="Length, min")
    streetball_length_of_periods_label.grid(row=2, column=0)
    streetball_period1_input = Entry(streetball_rules_frame)
    streetball_period1_input.grid(row=2, column=1)
    streetball_period2_input = Entry(streetball_rules_frame)
    streetball_period2_input.grid(row=2, column=2)
    streetball_period3_input = Entry(streetball_rules_frame)
    streetball_period3_input.grid(row=2, column=3)
    streetball_period4_input = Entry(streetball_rules_frame)
    streetball_period4_input.grid(row=2, column=4)
    streetball_period_ot_label = Entry(streetball_rules_frame)
    streetball_period_ot_label.grid(row=2, column=5)

    streetball_length_of_timeouts_label = Label(streetball_rules_frame, text="Timeout, min")
    streetball_length_of_timeouts_label.grid(row=3, column=0)
    streetball_timeout2_input = Entry(streetball_rules_frame)
    streetball_timeout2_input.grid(row=3, column=2)
    streetball_timeout3_input = Entry(streetball_rules_frame)
    streetball_timeout3_input.grid(row=3, column=3)
    streetball_timeout4_input = Entry(streetball_rules_frame)
    streetball_timeout4_input.grid(row=3, column=4)
    streetball_timeout_ot_input = Entry(streetball_rules_frame)
    streetball_timeout_ot_input.grid(row=3, column=5)

    streetball_team_fouls_label = Label(streetball_rules_frame, text="Team Fouls")
    streetball_team_fouls_label.grid(row=4, column=0)
    streetball_team_fouls1_input = Entry(streetball_rules_frame)
    streetball_team_fouls1_input.grid(row=4, column=1)
    streetball_team_fouls2_input = Entry(streetball_rules_frame)
    streetball_team_fouls2_input.grid(row=4, column=2)
    streetball_team_fouls3_input = Entry(streetball_rules_frame)
    streetball_team_fouls3_input.grid(row=4, column=3)
    streetball_team_fouls4_input = Entry(streetball_rules_frame)
    streetball_team_fouls4_input.grid(row=4, column=4)

    streetball_players_on_court_label = Label(streetball_rules_frame, text="Player on court")
    streetball_players_on_court_label.grid(row=5, column=0)
    streetball_players_on_court_input = Entry(streetball_rules_frame)
    streetball_players_on_court_input.grid(row=5, column=1)

    streetball_personal_fouls_label = Label(streetball_rules_frame, text="Personal Fouls")
    streetball_personal_fouls_label.grid(row=6, column=0)
    streetball_personal_fouls_input = Entry(streetball_rules_frame)
    streetball_personal_fouls_input.grid(row=6, column=1)

    streetball_number_of_points_label = Label(streetball_rules_frame, text="Number of points: ")
    streetball_number_of_points_label.grid(row=902, column=0)
    streetball_free_throw_points_label = Label(streetball_rules_frame, text="Free Throw")
    streetball_free_throw_points_label.grid(row=901, column=1)
    streetball_free_throw_points_input = Entry(streetball_rules_frame)
    streetball_free_throw_points_input.grid(row=902, column=1)
    streetball_game_shot_points_label = Label(streetball_rules_frame, text="Game Shot")
    streetball_game_shot_points_label.grid(row=901, column=2)
    streetball_game_shot_points_input = Entry(streetball_rules_frame)
    streetball_game_shot_points_input.grid(row=902, column=2)
    streetball_longrange_shot_points_label = Label(streetball_rules_frame, text="Long Range Shot")
    streetball_longrange_shot_points_label.grid(row=901, column=3)
    streetball_longrange_shot_points_input = Entry(streetball_rules_frame)
    streetball_longrange_shot_points_input.grid(row=902, column=3)
    #duration_of_the_period = 


def open_players_database():
    def add_player():
        conn = sqlite3.connect("player_database.db")

        # Create cursor
        c = conn.cursor()
    
        # Create table
        """
        c.execute('''
                CREATE TABLE players (
                #id integer,
                number integer,
                first_name_ru text,
                last_name_ru text,
                mid_name_ru text,
                first_name_en text,
                last_name_en text,
                mid_name_en text,
                height integer,
                weight integer,
                birthday_day integer,
                birthday_month integer,
                birthday_year integer
                )
                ''')
        """

        # Insert into table
        c.execute("INSERT INTO players(number, first_name_ru, last_name_ru, mid_name_ru, first_name_en, last_name_en, mid_name_en, height, weight, birthday_day, birthday_month, birthday_year) VALUES (:number, :first_name_ru, :last_name_ru, :mid_name_ru, :first_name_en, :last_name_en, :mid_name_en, :height, :weight, :birthday_day, :birthday_month, :birthday_year)",
                {
                    #'id': player_id_input.get(),
                    'number': player_number_input.get(),
                    'first_name_ru': player_ru_surname_input.get(),
                    'last_name_ru': player_ru_name_input.get(),
                    'mid_name_ru': player_ru_patronymic_input.get(),
                    'first_name_en': player_en_surname_input.get(),
                    'last_name_en': player_en_name_input.get(),
                    'mid_name_en': player_en_patronymic_input.get(),
                    'height': player_height_input.get(),
                    'weight': player_weight_input.get(),
                    'birthday_day': player_day_of_birthday_input.get(),
                    'birthday_month': player_month_of_birthday_input.get(),
                    'birthday_year': player_year_of_birthday_input.get()
                })

        # Commit changes
        conn.commit()

        # Close sqlite connection
        conn.close()


        # Clear The Text Boxes
        #player_id_input.delete(0, END)
        player_number_input.delete(0, END)
        player_ru_surname_input.delete(0, END)
        player_ru_name_input.delete(0, END)
        player_ru_patronymic_input.delete(0, END)
        player_en_surname_input.delete(0, END)
        player_en_name_input.delete(0, END)
        player_en_patronymic_input.delete(0, END)
        player_height_input.delete(0, END)
        player_weight_input.delete(0, END)
        player_day_of_birthday_input.delete(0, END)
        player_month_of_birthday_input.delete(0, END)
        player_year_of_birthday_input.delete(0, END)

    players_database_window = Toplevel()
    players_database_window.title("Players Database")

    ok_button = Button(players_database_window, text="Ok", command=players_database_window.destroy)
    ok_button.grid(row=0, column=0)
    view_list_of_players_button = Button(players_database_window, text="View List of Players", command=open_list_of_players)
    view_list_of_players_button.grid(row=1, column=0)

    player_info_frame = LabelFrame(players_database_window, text="Player")
    player_info_frame.grid(row=10, column=0)
    #player_id_label = Label(player_info_frame, text="ID")
    #player_id_label.grid(row=0, column=0)
    #player_id_input = Entry(player_info_frame)
    #player_id_input.grid(row=0, column=1)
    player_number_label = Label(player_info_frame, text="Playing #")
    player_number_label.grid(row=1, column=0)
    player_number_input = Entry(player_info_frame)
    player_number_input.grid(row=1, column=1)
    player_ru_surname_label = Label(player_info_frame, text="Surname, ru")
    player_ru_surname_label.grid(row=2, column=0)
    player_ru_surname_input = Entry(player_info_frame)
    player_ru_surname_input.grid(row=2, column=1)
    player_ru_name_label = Label(player_info_frame, text="Name, ru")
    player_ru_name_label.grid(row=3, column=0)
    player_ru_name_input = Entry(player_info_frame)
    player_ru_name_input.grid(row=3, column=1)
    player_ru_patronymic_label = Label(player_info_frame, text="Patronymic, ru")
    player_ru_patronymic_label.grid(row=4, column=0)
    player_ru_patronymic_input = Entry(player_info_frame)
    player_ru_patronymic_input.grid(row=4, column=1)
    player_en_surname_label = Label(player_info_frame, text="Surname")
    player_en_surname_label.grid(row=5, column=0)
    player_en_surname_input = Entry(player_info_frame)
    player_en_surname_input.grid(row=5, column=1)
    player_en_name_label = Label(player_info_frame, text="Name")
    player_en_name_label.grid(row=6, column=0)
    player_en_name_input = Entry(player_info_frame)
    player_en_name_input.grid(row=6, column=1)
    player_en_patronymic_label = Label(player_info_frame, text="Patronymic")
    player_en_patronymic_label.grid(row=7, column=0)
    player_en_patronymic_input = Entry(player_info_frame)
    player_en_patronymic_input.grid(row=7, column=1)
    player_height_label = Label(player_info_frame, text="Height")
    player_height_label.grid(row=8, column=0)
    player_height_input = Entry(player_info_frame)
    player_height_input.grid(row=8, column=1)
    player_weight_label = Label(player_info_frame, text="Weight")
    player_weight_label.grid(row=9, column=0)
    player_weight_input = Entry(player_info_frame)
    player_weight_input.grid(row=9, column=1)
    player_birthday_label = Label(player_info_frame, text="Birthday")
    player_birthday_label.grid(row=99, column=0)
    player_day_of_birthday_label = Label(player_info_frame, text="Day")
    player_day_of_birthday_label.grid(row=99, column=1)
    player_month_of_birthday_label = Label(player_info_frame, text="Month")
    player_month_of_birthday_label.grid(row=99, column=2)
    player_year_of_birthday_label = Label(player_info_frame, text="Year")
    player_year_of_birthday_label.grid(row=99, column=3)
    player_day_of_birthday_input = Entry(player_info_frame, width=3)
    player_day_of_birthday_input.grid(row=100, column=1)
    player_month_of_birthday_input = Entry(player_info_frame, width=3)
    player_month_of_birthday_input.grid(row=100, column=2)
    player_year_of_birthday_input = Entry(player_info_frame, width=3)
    player_year_of_birthday_input.grid(row=100, column=3)
    add_player_info = Button(player_info_frame, text="Add", command=add_player)
    add_player_info.grid(row=200, column=0)
    submit_player_info = Button(player_info_frame, text="Submit", command=submit_player)
    submit_player_info.grid(row=200, column=1)



def edit_player(record):
    def add_player():
        conn = sqlite3.connect("player_database.db")

        # Create cursor
        c = conn.cursor()
    
        # Create table
        """
        c.execute('''
                CREATE TABLE players (
                #id integer,
                number integer,
                first_name_ru text,
                last_name_ru text,
                mid_name_ru text,
                first_name_en text,
                last_name_en text,
                mid_name_en text,
                height integer,
                weight integer,
                birthday_day integer,
                birthday_month integer,
                birthday_year integer
                )
                ''')
        """

        # Insert into table
        c.execute("INSERT INTO players(number, first_name_ru, last_name_ru, mid_name_ru, first_name_en, last_name_en, mid_name_en, height, weight, birthday_day, birthday_month, birthday_year) VALUES (:number, :first_name_ru, :last_name_ru, :mid_name_ru, :first_name_en, :last_name_en, :mid_name_en, :height, :weight, :birthday_day, :birthday_month, :birthday_year)",
                {
                    #'id': player_id_input.get(),
                    'number': player_number_input.get(),
                    'first_name_ru': player_ru_surname_input.get(),
                    'last_name_ru': player_ru_name_input.get(),
                    'mid_name_ru': player_ru_patronymic_input.get(),
                    'first_name_en': player_en_surname_input.get(),
                    'last_name_en': player_en_name_input.get(),
                    'mid_name_en': player_en_patronymic_input.get(),
                    'height': player_height_input.get(),
                    'weight': player_weight_input.get(),
                    'birthday_day': player_day_of_birthday_input.get(),
                    'birthday_month': player_month_of_birthday_input.get(),
                    'birthday_year': player_year_of_birthday_input.get()
                })

        # Commit changes
        conn.commit()

        # Close sqlite connection
        conn.close()

    edit_player_window = Toplevel()
    edit_player_window.title("Edit Player")

    ok_button = Button(edit_player_window, text="Ok", command=edit_player_window.destroy)
    ok_button.grid(row=0, column=0)
    
    test_label = Label(edit_player_window, text=str(record)).grid(row=2, column=0)
    player_info_frame = LabelFrame(edit_player_window, text="Player")
    player_info_frame.grid(row=10, column=0)
    #player_id_label = Label(player_info_frame, text="ID")
    #player_id_label.grid(row=0, column=0)
    #player_id_input = Entry(player_info_frame)
    #player_id_input.grid(row=0, column=1)
    player_number_label = Label(player_info_frame, text="Playing #")
    player_number_label.grid(row=1, column=0)
    player_number_input = Entry(player_info_frame)
    player_number_input.insert(0, record[1])
    player_number_input.grid(row=1, column=1)
    player_ru_surname_label = Label(player_info_frame, text="Surname, ru")
    player_ru_surname_label.grid(row=2, column=0)
    player_ru_surname_input = Entry(player_info_frame)
    player_ru_surname_input.insert(0, record[2])
    player_ru_surname_input.grid(row=2, column=1)
    player_ru_name_label = Label(player_info_frame, text="Name, ru")
    player_ru_name_label.grid(row=3, column=0)
    player_ru_name_input = Entry(player_info_frame)
    player_ru_name_input.insert(0, record[3])
    player_ru_name_input.grid(row=3, column=1)
    player_ru_patronymic_label = Label(player_info_frame, text="Patronymic, ru")
    player_ru_patronymic_label.grid(row=4, column=0)
    player_ru_patronymic_input = Entry(player_info_frame)
    player_ru_patronymic_input.insert(0, record[4])
    player_ru_patronymic_input.grid(row=4, column=1)
    player_en_surname_label = Label(player_info_frame, text="Surname")
    player_en_surname_label.grid(row=5, column=0)
    player_en_surname_input = Entry(player_info_frame)
    player_en_surname_input.insert(0, record[5])
    player_en_surname_input.grid(row=5, column=1)
    player_en_name_label = Label(player_info_frame, text="Name")
    player_en_name_label.grid(row=6, column=0)
    player_en_name_input = Entry(player_info_frame)
    player_en_name_input.insert(0, record[6])
    player_en_name_input.grid(row=6, column=1)
    player_en_patronymic_label = Label(player_info_frame, text="Patronymic")
    player_en_patronymic_label.grid(row=7, column=0)
    player_en_patronymic_input = Entry(player_info_frame)
    player_en_patronymic_input.insert(0, record[7])
    player_en_patronymic_input.grid(row=7, column=1)
    player_height_label = Label(player_info_frame, text="Height")
    player_height_label.grid(row=8, column=0)
    player_height_input = Entry(player_info_frame)
    player_height_input.insert(0, record[8])
    player_height_input.grid(row=8, column=1)
    player_weight_label = Label(player_info_frame, text="Weight")
    player_weight_label.grid(row=9, column=0)
    player_weight_input = Entry(player_info_frame)
    player_weight_input.insert(0, record[9])
    player_weight_input.grid(row=9, column=1)
    player_birthday_label = Label(player_info_frame, text="Birthday")
    player_birthday_label.grid(row=99, column=0)
    player_day_of_birthday_label = Label(player_info_frame, text="Day")
    player_day_of_birthday_label.grid(row=99, column=1)
    player_month_of_birthday_label = Label(player_info_frame, text="Month")
    player_month_of_birthday_label.grid(row=99, column=2)
    player_year_of_birthday_label = Label(player_info_frame, text="Year")
    player_year_of_birthday_label.grid(row=99, column=3)
    player_day_of_birthday_input = Entry(player_info_frame, width=3)
    player_day_of_birthday_input.insert(0, record[10])
    player_day_of_birthday_input.grid(row=100, column=1)
    player_month_of_birthday_input = Entry(player_info_frame, width=3)
    player_month_of_birthday_input.insert(0, record[11])
    player_month_of_birthday_input.grid(row=100, column=2)
    player_year_of_birthday_input = Entry(player_info_frame, width=3)
    player_year_of_birthday_input.insert(0, record[12])
    player_year_of_birthday_input.grid(row=100, column=3)
    save_player_info = Button(edit_player_window, text="Save", command=add_player)
    save_player_info.grid(row=200, column=0)


def submit_player():
    pass


def open_list_of_players():
    def edit_player_info():
        pass

    list_of_players_window = Toplevel()
    list_of_players_window.title("List of Players")

    ok_button = Button(list_of_players_window, text="Ok", command=list_of_players_window.destroy)
    ok_button.pack()

    conn = sqlite3.connect('player_database.db')
    c = conn.cursor()

    c.execute("SELECT *, oid FROM players")

    records = c.fetchall()
    for i, record in enumerate(records):
        name_label = record[2] + ' ' + record[3]
        Button(list_of_players_window, text=name_label, command=lambda:edit_player(records[i])).pack()

    #Label(list_of_players_window, text=str(records)).pack()
    #player1_button = Button(list_of_players_window, text="Player1")
    #player1_button.grid(row=1, column=0)
    #player2_button = Button(list_of_players_window, text="Player2")
    #player2_button.grid(row=2, column=0)

    conn.commit()
    conn.close()

myLabel = Label(root, text=time.strftime('%H:%M:%S'))
myLabel.grid(row=0, column=0)

game_details_button = Button(text="Game Details", command=open_game_details)
game_details_button.grid(row=0, column=1)

players_database_button = Button(text="Players database", command=open_players_database)
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

root.mainloop()
