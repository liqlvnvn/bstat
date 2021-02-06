from tkinter import *


class AddEditPlayerWindow():
    def __init__(self):
        players_database_window = Toplevel()
        players_database_window.title("Players Database")

        ok_button = Button(players_database_window, text="Ok", command=players_database_window.destroy)
        ok_button.grid(row=0, column=0)
        #view_list_of_players_button = Button(players_database_window, text="View List of Players", command=self.open_add_player)
        #view_list_of_players_button.grid(row=1, column=0)

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
        add_player_info = Button(player_info_frame, text="Add", command=self.add_player)
        add_player_info.grid(row=200, column=0)
        submit_player_info = Button(player_info_frame, text="Submit", command=self.submit_player)
        submit_player_info.grid(row=200, column=1)


    def add_player(self):
        conn = sqlite3.connect("player_database.db")

        # Create cursor
        c = conn.cursor()

        # Create table
        """
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

        c.execute("SELECT *, oid FROM players")

        records = c.fetchall()
        print(records)
        for i, record in enumerate(records):
            name_label = record[2] + ' ' + record[3]
            Button(list_of_players_window, text=name_label, command=lambda:edit_player(records[i])).pack()
            print(i)
            print(record[i])
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

    def submit_player(self):
        pass
