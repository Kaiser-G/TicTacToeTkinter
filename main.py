import tkinter

def check_nul():
    print("match nul")

def print_winner():
    global win

    if win is False:
        win = True
        print("Le joueur", current_player, "a gagné le jeu")

def switch_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"



def chek_win(clicked_row, clicked_col):
    # detecter victoire horiaontale
    count = 0
    for i in range(3):
        current_button = buttons[i][clicked_row]          
        if current_button["text"] == current_player:
            count += 1
    if count == 3:
        print_winner()


     # detecter victoire verticale
    count = 0
    for i in range(3):
        current_button = buttons[clicked_col][i]          
        if current_button["text"] == current_player:
            count += 1
    if count == 3:
        print_winner()



     # detecter victoire en diagonale
    count = 0
    for i in range(3):
        current_button = buttons[i][i]          
        if current_button["text"] == current_player:
            count += 1
    if count == 3:
        print_winner()

    # detecter victoire en diagonale inversee
    count = 0
    for i in range(3):
        current_button = buttons[2-i][i]          
        if current_button["text"] == current_player:
            count += 1
    if count == 3:
        print_winner()


    if win is False:
        count = 0
        for col in range(3):
            for row in range(3):
                current_button = buttons[col][row]
                if current_button["text"] == "X" or current_button["text"] == "O":
                    count += 1
                
                if count == 9:
                    print("match nul")


def place_symbol(row, column):
    print("click", row, column)

    clicked_button = buttons[column][row]
    clicked_button.config(text=current_player)

    chek_win(row, column)
    switch_player()




#permet de créer une grille a l'aide de button
def draw_grid():
    for column in range(3):
        buttons_in_cols = []
        for row in range(3):
            button = tkinter.Button(
                root, font=("Arial", 50),
                width=5, height=3,
                command=lambda r=row, c=column:place_symbol(r, c)
                )
            button.grid(row=row, column=column)
            buttons_in_cols.append(button)
        buttons.append(buttons_in_cols)

#stockage
buttons = []
current_player = "X"
win = False



#creer la fenetre du jeux
root = tkinter.Tk()

#personnalisation de la fenetre
root.title("TicTacToe")
root.minsize(500, 500)



draw_grid()
root.mainloop()