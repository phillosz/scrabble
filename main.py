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
    global canvas_coordinates, players_clicked_this_round, canvas_clicked, all_players, player_switch, score
    if not is_straight_and_adjacent(canvas_coordinates):
        display_error()
        for canvas in canvas_clicked:
            remove_text(canvas)
        for canvas in players_clicked_this_round:
            canvas.configure(bg="white")
        canvas_coordinates = []
        canvas_clicked = []
        players_clicked_this_round = []
        all_players[player_switch]["word"] = ""
        return
    for canvas in players_clicked_this_round:
        all_players[player_switch]["letters"].remove(canvas_letters[canvas])
        remove_text(canvas)
    for canvas in canvas_clicked:
        all_players[player_switch]["score"] += letter_scores[canvas_letters[canvas]]
    update_score()
    canvas_coordinates = []
    print(all_players[player_switch]["word"])
    show_next_player()
    
def is_straight_line(canvas_coordinates):
    if not canvas_coordinates or len(canvas_coordinates) == 1:
        return True
    
    x_set = set()
    y_set = set()
    
    for x, y in canvas_coordinates:
        x_set.add(x)
        y_set.add(y)
    
    if len(x_set) == 1 or len(y_set) == 1:
        return True
    else:
        return False

def is_adjacent(canvas_coordinates):
    if not canvas_coordinates or len(canvas_coordinates) == 1:
        return True
    
    canvas_items = []
    canvas_coords = []
    for x, y in canvas_coordinates:
        x1 = x - 1
        y1 = y - 1
        x2 = x + 1
        y2 = y + 1
        overlapping = canvas.find_overlapping(x1, y1, x2, y2)
        if len(overlapping) == 1:
            item = overlapping[0]
            canvas_items.append(item)
            coords = canvas.coords(item)
            canvas_coords.append(coords)
        else:
            return False
    
    for i in range(len(canvas_items) - 1):
        current_coords = canvas_coords[i]
        next_coords = canvas_coords[i + 1]
        x1, y1 = current_coords
        x2, y2 = next_coords
        if y1 == y2:
            if x1 == x2 + 1 or x1 == x2 - 1:
                continue
            else:
                return False
        elif x1 == x2:
            if y1 == y2 + 1 or y1 == y2 - 1:
                continue
            else:
                return False
        else:
            return False
    return True


def is_straight_and_adjacent(canvas_coordinates):
    if not is_straight_line(canvas_coordinates):
        return False
    if not is_adjacent(canvas_coordinates):
        return False
    return True
    
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
    global last_clicked_canvas, whole_word, all_players, player_switch, previous_canvas
    current_canvas = event.widget
    row, col = current_canvas.grid_info()["row"], current_canvas.grid_info()["column"]
    print(f"Clicked canvas: {current_canvas}")
    print(f"Clicked coords are {row, col}")

    if len(current_canvas.find_withtag("text")) == 0:
        current_letter = canvas_letters[last_clicked_canvas]
        canvas_letters[current_canvas] = current_letter
        last_clicked_canvas.configure(bg="grey")
        current_canvas.create_text(tile_size // 2, tile_size // 2, text=current_letter, font=("Arial", 16), fill="black", tags="text")
        all_players[player_switch]["word"] += current_letter
        last_clicked_canvas = None
    elif current_canvas is not None:
        all_players[player_switch]["word"] += canvas_letters[current_canvas]
    else:
        display_error()
        
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

for j in range(15):
    for i in range(15):
        canvas = Canvas(root, width=tile_size, height=tile_size, bg='white')
        canvas.grid(row=j, column=i, sticky=(N, W))
        canvas.bind('<Button-1>', change_letters_canvases)
        canvas_letters[canvas] = ""
        
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