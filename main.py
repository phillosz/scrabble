from tkinter import *
from tkinter import Tk, N, W, ttk
import scrabble_engine as sc
with open("dic.txt", "r") as file:
    en_words = file.read().splitlines()
    
#VARIABLES
letter_scores = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4,
    'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3,
    'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8,
    'Y': 4, 'Z': 10, "joker": 0}
letters_sack = ["A", "A", "A", "A", "A", "A", "A", "A", "A", "B", "B", "C", "C", "D", "D", "D", "D", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", 
                "F", "F", "G", "G", "G", "H", "H", "I", "I", "I", "I", "I", "I", "I", "I", "I", "J", "K", "L", "L", "L", "L", "M", "M", "N", "N", "N", "N", "N", 
                "N", "O", "O", "O", "O", "O", "O", "O", "O", "P", "P", "Q", "R", "R", "R", "R", "R", "R", "S", "S", "S", "S", "T", "T", "T", "T", "T", "T", "U", 
                "U", "U", "U", "V", "V", "W", "W", "X", "Y", "Y", "Z", "joker", "joker"]
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "CH", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "X", "Y", "Z"]
all_players = {1: {"letters": [], "score": 0, "word": "", "y": 0, "x": 0, "direction": "", "status": "", "input": [], "joker_value": [], "joker_letter": [], "score_memory": []}, 
               2: {"letters": [], "score": 0, "word": "", "y": 0, "x": 0, "direction": "", "status": "", "input": [], "joker_value": [], "joker_letter": [], "score_memory": []},
               3: {"letters": [], "score": 0, "word": "", "y": 0, "x": 0, "direction": "", "status": "", "input": [], "joker_value": [], "joker_letter": [], "score_memory": []},
               4: {"letters": [], "score": 0, "word": "", "y": 0, "x": 0, "direction": "", "status": "", "input": [], "joker_value": [], "joker_letter": [], "score_memory": []}}
sack_placeholder = letters_sack
score_memory = []
inp = ""
word = list(inp)
player_count = 0
player_switch = 1
max1 = []
joker_value_nahrada = []
joker_coords = []
joker_x = 0
joker_y = 0
podium = []
joker_replace = ""


#FUNCTIONS THAT EDIT OR DO SOMETHING
def sack_replace_some(player):
    print("Your letters are: ", player["letters"])
    letter = input("Enter letter you want to replace ")
    while letter not in player["letters"]:
        print("Error")
        letter = input("Enter letter you want to replace ")
    sc.sack_append_letters_remove(all_players[player_switch], letter, sack_placeholder)
def ifanything_wrong(player):
    player["word"] = input("Enter your word in CAPITALS ")
    player["input"] = player["word"]
    player["x"] = input("Enter the x coordinate ")
    player["y"] = input("Enter the y coordinate ")
    player["direction"] = input("Enter the direction R, D ")
def ask_for_status(player):
    player["status"] = input("Do you want to PASS, REPLACE ALL, REPLACE SOME or PLAY? ")
def ask_number_of_players():
    global player_count
    input_number = input("Enter number of players 2-4 ")
    if input_number in ["2", "3", "4"]:
        player_count = int(input_number)
    else:
        ask_number_of_players()
def joker_selection():
    global joker_replace
    joker_replace = input("What letter do you want to use instead of the joker? ")
    sc.locate_joker(all_players[player_switch], joker_replace, letter_scores)
    
#TKINTER
def on_tile_click(event):
    global last_clicked_canvas, players_clicked_this_round
    canvas = event.widget
    row, col = canvas.grid_info()["row"], canvas.grid_info()["column"]

    if row == 1 and 15 <= col <= 21:
        last_clicked_canvas = canvas
        players_clicked_this_round.append(canvas)
    
def check_word():
    pass
#     global canvas_coordinates, players_clicked_this_round, canvas_clicked, all_players, player_switch, score
#     words, all_valid = crossing_words()
#     if not any(canvas in canvas_clicked for canvas in canvas_letters) or not all_valid:
#         display_error()
#         for canvas in canvas_clicked:
#             remove_text(canvas)
#         for canvas in players_clicked_this_round:
#             canvas.configure(bg="white")
#         canvas_coordinates = []
#         canvas_clicked = []
#         players_clicked_this_round = []
#         all_players[player_switch]["word"] = ""
#         return
#     for canvas in players_clicked_this_round:
#         all_players[player_switch]["letters"].remove(canvas_letters[canvas])
#         remove_text(canvas)
#     for word in words:
#         for letter in word:
#             all_players[player_switch]["score"] += letter_scores[letter]
#     update_score()
#     canvas_coordinates = []
#     print(all_players[player_switch]["word"])
#     show_next_player()


    
# def is_straight_line(canvas_coordinates):
#     if not canvas_coordinates or len(canvas_coordinates) == 1:
#         return True
    
#     x_set = set()
#     y_set = set()
    
#     for x, y in canvas_coordinates:
#         x_set.add(x)
#         y_set.add(y)
    
#     if len(x_set) == 1 or len(y_set) == 1:
#         return True
#     else:
#         return False

def is_adjacent(row1, col1, row2, col2):
    pass
#     if abs(row1 - row2) <= 1:
#         if abs(col1 - col2) <= 1:
#             if row1 == row2 or col1 == col2:
#                 return True
#     return False


# def is_straight_and_valid(canvas_coordinates):
#     if not is_straight_line(canvas_coordinates):
#         return False
#     if not crossing_words():
#         return False
#     return True
    
def remove_text(canvas):
    for item in canvas.find_all():
        if canvas.type(item) == "text":
            canvas.delete(item)

def create_players():
    global player_count
    player_count = int(player_count_var.get())

    if 2 <= player_count <= 4:
        num_players_entry.grid_forget()
        create_players_button.grid_forget()

        sc.letter_distribution(player_count, sack_placeholder, all_players)
        asign_letters()
        player_label.grid(row=0, column=15, columnspan=7, sticky=(N, W))
        check_button.grid(row=3, column=15, columnspan=3, sticky=(N, W))
        skip_turn.grid(row=3, column=18, columnspan=3, sticky=(N, W))
        score_board.grid(row=6, column=15, columnspan=7, sticky=(N, W))
        replace_all.grid(row=5, column=15, columnspan=3, sticky=(N, W))
        replace_some.grid(row=5, column=18, columnspan=3, sticky=(N, W))
        
def asign_letters():
    for idx, canvas in enumerate(player_canvases):
            canvas.grid(row=1, column=15 + idx, sticky=(N, W))
            canvas.create_text(tile_size // 2, tile_size // 2, text=all_players[player_switch]["letters"][idx], fill='black')
            canvas.create_text(tile_size // 1.2, tile_size // 1.2, text=letter_scores[all_players[player_switch]["letters"][idx]], fill="gray25")
            canvas.bind('<Button-1>', on_tile_click)
            canvas_letters[canvas] = all_players[player_switch]["letters"][idx]
    
def change_letters_canvases(event):
    global last_clicked_canvas, whole_word, all_players, player_switch, previous_canvas, canvas_coordinates, canvas_clicked, players_clicked_this_round
    current_canvas = event.widget
    row, col = current_canvas.grid_info()["row"], current_canvas.grid_info()["column"]
    print(f"Clicked canvas: {current_canvas}")
    print(f"Clicked coords are {row, col}")

    if len(current_canvas.find_withtag("text")) == 0:
        current_letter = canvas_letters[last_clicked_canvas]
        canvas_letters[current_canvas] = current_letter
        last_clicked_canvas.configure(bg="grey")
        current_canvas.create_text(tile_size // 2, tile_size // 2, text=current_letter, font=("Arial", 16), fill="black", tags="text")
        if len(canvas_coordinates) == 0 or is_adjacent(row, col, canvas_coordinates[-1][0], canvas_coordinates[-1][1]):
            all_players[player_switch]["word"] += current_letter
            last_clicked_canvas = None
        else:
            canvas_clicked.append(current_canvas)
            all_players[player_switch]["word"] = ""
            display_error()
            for canvas in canvas_clicked:
                remove_text(canvas)
            for canvas in players_clicked_this_round:
                canvas.configure(bg="white")
            canvas_coordinates = []
            canvas_clicked = []
            players_clicked_this_round = []
            return
    elif current_canvas is not None:
        if len(canvas_coordinates) == 0 or is_adjacent(row, col, canvas_coordinates[-1][0], canvas_coordinates[-1][1]):
            all_players[player_switch]["word"] += canvas_letters[current_canvas]
        else:
            canvas_clicked.append(current_canvas)
            all_players[player_switch]["word"] = ""
            display_error()
            for canvas in canvas_clicked:
                remove_text(canvas)
            for canvas in players_clicked_this_round:
                canvas.configure(bg="white")
            canvas_coordinates = []
            canvas_clicked = []
            players_clicked_this_round = []
            return
    else:
        display_error()
        return
        
    canvas_coordinates.append((row, col))
    canvas_clicked.append(current_canvas)
    print(canvas_coordinates)

def display_error():
    error_label.grid(row=6, column=6, columnspan=5, sticky=(S, W))
    root.after(3000, hide_error)
    
def hide_error():
    error_label.grid_remove()
    
def show_next_player():
    for canvas in player_canvases:
        canvas.grid_forget()
    replace_all.grid_forget()
    replace_some.grid_forget()
    next_player.grid(row=4, column=15, columnspan=7, sticky=(N, W))

def next_player():
    global player_canvases, player_switch, players_clicked_this_round, canvas_clicked
    next_player.grid_forget()
    sc.sack_refill(all_players[player_switch], sack_placeholder)
    all_players[player_switch]["word"] = ""
    player_switch = 1 if player_switch == player_count else int(player_switch) + 1
    players_clicked_this_round = []
    canvas_clicked = []
    for canvas in player_canvases:
        canvas.delete("all")
        canvas.configure(bg="white")
    player_label.configure(text=f"Player {player_switch}")
    update_score()
    asign_letters()
    replace_all.grid(row=5, column=15, columnspan=3, sticky=(N, W))
    replace_some.grid(row=5, column=18, columnspan=3, sticky=(N, W))
    
    
def update_score():
    score_board.configure(text=f"Score: {all_players[player_switch]['score']}")
    
def replace_all():
    for canvas in player_canvases:
        sack_placeholder.append(canvas_letters[canvas])
        remove_text(canvas)
        canvas.configure(bg="white")
    for canvas in canvas_clicked:
        remove_text(canvas)
    reset_all_needed()
    sc.sack_replace_all(all_players[player_switch], sack_placeholder)
    asign_letters()
    check_word()

def reset_all_needed():
    global last_clicked_canvas, players_clicked_this_round, previous_canvas, canvas_coordinates, canvas_clicked
    last_clicked_canvas = None
    players_clicked_this_round = []
    canvas_coordinates = []
    canvas_clicked = []
    
def skip():
    for canvas in player_canvases:
        remove_text(canvas)
        canvas.configure(bg="white")
    for canvas in canvas_clicked:
        remove_text(canvas)
    reset_all_needed()
    check_word()

def replace_some():
    for canvas in player_canvases:
        sack_placeholder.append(canvas_letters[canvas])
        remove_text(canvas)
        canvas.configure(bg="white")
    for canvas in canvas_clicked:
        remove_text(canvas)
    sc.sack_append_letters_remove(all_players[player_switch], canvas_letters[last_clicked_canvas], sack_placeholder)
    reset_all_needed()
    asign_letters()
    check_word()  
    
# def crossing_words():
#     all_valid = True
#     words = [] # a list to store the words
#     for i in range(15):
#         for j in range(15):
#             horizontal_word = ""
#             horizontal_canvases = [] # a list to store the canvases that form the horizontal word
#             for k in range(j, 15):
#                 letter = canvas_letters[grid[i][k]]
#                 if letter:
#                     horizontal_word += letter
#                     horizontal_canvases.append(grid[i][k]) # add the canvas to the list
#                 else:
#                     break
#             # check if the horizontal word is longer than one letter
#             if len(horizontal_word) > 1:
#                 # check if the horizontal word is connected to the player's word
#                 if any(canvas in horizontal_canvases for canvas in canvas_clicked):
#                     # add it to the list of words
#                     words.append(horizontal_word)
#             vertical_word = ""
#             vertical_canvases = [] # a list to store the canvases that form the vertical word
#             for k in range(i, 15):
#                 letter = canvas_letters[grid[k][j]]
#                 if letter:
#                     vertical_word += letter
#                     vertical_canvases.append(grid[k][j]) # add the canvas to the list
#                 else:
#                     break
#             # check if the vertical word is longer than one letter
#             if len(vertical_word) > 1:
#                 # check if the vertical word is connected to the player's word
#                 if any(canvas in vertical_canvases for canvas in canvas_clicked):
#                     # add it to the list of words
#                     words.append(vertical_word)
#     # loop through the list of words and check if they are valid
#     for word in words:
#         if word in en_words:
#             pass
#         else:
#             all_valid = False
#     # return a tuple of two values: a list of words and a boolean
#     return words, all_valid

def hard_skip():
    global players_clicked_this_round, canvas_coordinates, canvas_clicked
    display_error()
    for canvas in canvas_clicked:
        remove_text(canvas)
    for canvas in players_clicked_this_round:
        canvas.configure(bg="white")
    canvas_coordinates = []
    canvas_clicked = []
    players_clicked_this_round = []

root = Tk()
root.title("SCRABBLE")

tile_size = 30 
canvas_letters = {}
last_clicked_canvas = None
players_clicked_this_round= []
canvas_coordinates = []
canvas_clicked = []

player_count_var = StringVar()
num_players_entry = Entry(root, textvariable=player_count_var)
num_players_entry.grid(row=0, column=15, columnspan=7, sticky=(N, W))

grid = []
for j in range(15):
    row = []
    for i in range(15):
        canvas = Canvas(root, width=tile_size, height=tile_size, bg='white')
        canvas.grid(row=j, column=i, sticky=(N, W))
        canvas.bind('<Button-1>', change_letters_canvases)
        canvas_letters[canvas] = ""
        row.append(canvas)
    grid.append(row)
        
create_players_button = Button(root, text="Create Players", command=create_players)
create_players_button.grid(row=1, column=15, columnspan=7, sticky=(N, W))

check_button = Button(root, text="Check Word", command=check_word)
player_label = Label(root, text=f"Player {player_switch}")
error_label = Label(root, text="Error try something else")
next_player = Button(root, text="Next Player", command=next_player)
replace_all = Button(root, text="Replace All", command=replace_all)
skip_turn = Button(root, text="Skip Turn", command=skip)
replace_some = Button(root, text="Replace Some", command=replace_some)

player_canvases = []
for i in range(7):
    canvas = Canvas(root, width=tile_size, height=tile_size, bg='white')
    player_canvases.append(canvas)
    
score_board = Label(root, text="Score: 0", font=("Arial", 16))

root.mainloop()