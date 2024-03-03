import random
from tkinter import *
from tkinter.constants import *
from tkinter import ttk
import time
from threading import Thread
# Function for buttons of GUI
def snake():
    # comp choice from choices list
    
    comp_choice = random.choice(choices)
    player_choice = "snake"
    game(comp_choice,player_choice)
    
def water():
    # comp choice from choices list
    comp_choice = random.choice(choices)
    player_choice = "water"
    game(comp_choice,player_choice)

def gun():
    # comp choice from choices list
    comp_choice = random.choice(choices)
    player_choice = "gun"
    game(comp_choice,player_choice)

def res_stat():
    reset_button.config(text="reseting...")
    reset_button.config(state=DISABLED)
    snake_button.config(state=DISABLED)
    water_button.config(state=DISABLED)
    gun_button.config(state=DISABLED)
    with open("stats.txt","w") as file:
        file.write("Games Won = 0\nGames Lost = 0\nGames Tied = 0")
        get_data()
    reset_button.config(text="Reset stats")
    reset_button.config(state=ACTIVE)
    snake_button.config(state=ACTIVE)
    water_button.config(state=ACTIVE)
    gun_button.config(state=ACTIVE)

def reset_thread():
    thread = Thread(target=res_stat)
    thread.start()

main = Tk()
main.title("Snake,Water&Gun Game")# configuring Title of main window
main.geometry("400x300")# configuring size/geometry of main window
main.config(bg="black")
try:
    main.iconbitmap("icon.ico")
except:
    pass

# Labels for game and stats
Heading = Label(main,text="Game",font=("Times New Roman",18),foreground="white",relief=SOLID,background="black")
stats = Label(main,font=("Times New Roman",18),foreground="white",relief=SOLID,background="black")
comp_chosed_label = Label(main,text="Computer Choosed. Now its your turn.\nChoices are",font=("Times New Roman",18),foreground="white",relief=FLAT,background="black")
players_choices_label = Label(main,font=("Times New Roman",18),foreground="white",background="black")
result_label = Label(main,font=("Times New Roman",18),foreground="green",background="black")

# packing of Labels
Heading.pack(side=TOP,pady=5)
stats.pack(side=TOP,pady=5)
comp_chosed_label.pack(side=TOP)

# <=======================  Button Bar starts here ===========================>
button_bar = ttk.Label(main,background="black")
button_bar.pack(side=TOP, fill=X,pady=5)
button_bar_2 = ttk.Label(main,background="black")
button_bar_2.pack(side=TOP, fill=X,pady=5)

# button to run snake function
snake_button = Button(button_bar,text="Snake",font=("Times New Roman",14),foreground="black",command=snake,relief=RAISED)
snake_button.grid(row=0,column=0,padx=40)

# button to activate water function
water_button = Button(button_bar,text="Water",font=("Times New Roman",14),foreground="black",command=water,relief=RAISED)
water_button.grid(row=0,column=1,padx=40)

# button to activate gun function
gun_button = Button(button_bar,text="Gun",font=("Times New Roman",14),foreground="black",command=gun,relief=RAISED)
gun_button.grid(row=0,column=2,padx=40)

# button to reset static
reset_button = Button(button_bar_2,text="Reset stats",font=("Times New Roman",14),foreground="black",command=reset_thread,relief=RAISED)
reset_button.grid(row=0,column=0,padx=60)


# button to destroy main window
exit_button = Button(button_bar_2,text="Exit",font=("Times New Roman",14),foreground="black",command=main.destroy,relief=RAISED)
exit_button.grid(row=0,column=1,padx=60)

# Choices list for computer to choose random item
choices = ['snake','water','gun']

# reading previous record from stats file
def get_data():
    global game_tied,game_lost,game_won
    try:
        with open("stats.txt","r") as file:
            lines = file.readlines()

            won_statment = lines[0].replace("\n","")
            splited_won_statement = won_statment.split("=")
            game_won = splited_won_statement[1].replace("\n","").replace(" ","")

            lost_statment = lines[1].replace("\n","")
            splited_lost_statement = lost_statment.split("=")
            game_lost = splited_lost_statement[1].replace("\n","").replace(" ","")

            tied_statement = lines[2].replace("\n","")
            splited_tied_statement = tied_statement.split("=")
            game_tied = splited_tied_statement[1].replace("\n","").replace(" ","")
           
        stat = f"Games Won = {game_won}\nGames Lost = {game_lost}\nGames Tied = {game_tied}"
        stats.config(text=stat)
        
    except:
        with open("stats.txt","a+") as file:
            file.write("Games Won = 0\nGames Lost = 0\nGames Tied = 0")

        time.sleep(3)

        with open("stats.txt","r") as file:
            lines = file.readlines()

            won_statment = lines[0].replace("\n","")
            splited_won_statement = won_statment.split("=")
            game_won = splited_won_statement[1].replace("\n","").replace(" ","")

            lost_statment = lines[1].replace("\n","")
            splited_lost_statement = lost_statment.split("=")
            game_lost = splited_lost_statement[1].replace("\n","").replace(" ","")

            tied_statement = lines[2].replace("\n","")
            splited_tied_statement = tied_statement.split("=")
            game_tied = splited_tied_statement[1].replace("\n","").replace(" ","")
            
            stat = f"Games Won = {game_won}\nGames Lost = {game_lost}\nGames Tied = {game_tied}"
            stats.config(text=stat)
    
get_data()

# main function for game
def game(comp,you):
    game_won_data = int(game_won)
    game_lost_data = int(game_lost)
    game_tied_data = int(game_tied)
    result = None
    # If both choices are equal declares a tie
    if comp == you:
        result = None

    # check for all possibilties if comp chooses snake
    elif comp == "snake":
        if you == "water":
            result = False
        elif you == "gun":
            result = True
        
    # check for all possibilties if comp chooses gun
    elif comp == "gun":
        if you == "snake":
            result = False
        elif you == "water":
            result = True

    # check for all possibilties if comp chooses water
    elif comp == "water":
        if you == "snake":
            result = True
        elif you == "gun":
            result = False

# Checking the BOOL Returned by function and declaring result based on that BOOL value
    if result == None:
        players_choices_label.config(text=f"Computer Choosed {comp} and You Choosed {you}.",wraplength=420)
        main.geometry("420x410")
        result_label.config(text="This game is a tie.",foreground="white")
        button_bar_2.pack_forget()
        players_choices_label.pack(side=TOP,pady=5)
        result_label.pack(side=TOP,pady=5)
        button_bar_2.pack(side=TOP, fill=X,pady=5)
        game_tied_data = game_tied_data + 1
        with open("stats.txt","w") as file:
            file.write(f"Games Won = {game_won_data}\nGames Lost = {game_lost_data}\nGames Tied = {game_tied_data}")
        get_data()        
    
    elif result:
        players_choices_label.config(text=f"Computer Choosed {comp} and You Choosed {you}.",wraplength=420)
        main.geometry("420x410")
        result_label.config(text="Hurray! You won this match.",foreground="green")
        button_bar_2.pack_forget()
        players_choices_label.pack(side=TOP,pady=5)
        result_label.pack(side=TOP,pady=5)
        button_bar_2.pack(side=TOP, fill=X,pady=5)
        game_won_data = game_won_data + 1
        with open("stats.txt","w") as file:
            file.write(f"Games Won = {game_won_data}\nGames Lost = {game_lost_data}\nGames Tied = {game_tied_data}")
        get_data()        
    
    else:
        players_choices_label.config(text=f"Computer Choosed {comp} and You Choosed {you}.",wraplength=420)
        main.geometry("420x410")
        result_label.config(text="Alas! You lost this match.",foreground="red")
        button_bar_2.pack_forget()
        players_choices_label.pack(side=TOP,pady=5)
        result_label.pack(side=TOP,pady=5)
        button_bar_2.pack(side=TOP, fill=X,pady=5)
        game_lost_data = game_lost_data + 1
        with open("stats.txt","w") as file:
            file.write(f"Games Won = {game_won_data}\nGames Lost = {game_lost_data}\nGames Tied = {game_tied_data}")
        get_data()    

if __name__ == "__main__" :
    main.mainloop()