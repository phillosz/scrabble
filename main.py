import random
import scrabble_engine as sc
with open("dic.txt", "r") as file:
    en_words = file.read().splitlines()
    
#VARIABLES
arr = [[4, 0, 0, 1, 0, 0, 0, 4, 0, 0, 0, 1, 0, 0, 4, 5,],
    [0, 3, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 3, 0, 5,],
    [0, 0, 3, 0, 0, 0, 1, 0, 1, 0, 0, 0, 3, 0, 0, 5,],
    [1, 0, 0, 3, 0, 0, 0, 1, 0, 0, 0, 3, 0, 0, 1, 5,],
    [0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 5,],
    [0, 2, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 2, 0, 5,],
    [0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 5,],
    [4, 0, 0, 1, 0, 0, 0, 6, 0, 0, 0, 1, 0, 0, 4, 5,],
    [0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 5,],
    [0, 2, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 2, 0, 5,],
    [0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 5,],
    [1, 0, 0, 3, 0, 0, 0, 1, 0, 0, 0, 3, 0, 0, 1, 5,],
    [0, 0, 3, 0, 0, 0, 1, 0, 1, 0, 0, 0, 3, 0, 0, 5,],
    [0, 3, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 3, 0, 5,],
    [4, 0, 0, 1, 0, 0, 0, 4, 0, 0, 0, 1, 0, 0, 4, 5]]
letter_scores = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4,
    'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3,
    'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8,
    'Y': 4, 'Z': 10, "joker": 0}
letters_sack = ["A", "A", "A", "A", "A", "A", "A", "A", "A", "B", "B", "C", "C", "D", "D", "D", "D", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", 
                "F", "F", "G", "G", "G", "H", "H", "I", "I", "I", "I", "I", "I", "I", "I", "I", "J", "K", "L", "L", "L", "L", "M", "M", "N", "N", "N", "N", "N", 
                "N", "O", "O", "O", "O", "O", "O", "O", "O", "P", "P", "Q", "R", "R", "R", "R", "R", "R", "S", "S", "S", "S", "T", "T", "T", "T", "T", "T", "U", 
                "U", "U", "U", "V", "V", "W", "W", "X", "Y", "Y", "Z", "joker", "joker"]
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "CH", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "X", "Y", "Z"]
all_players = {1: {"letters": [], "score": 0, "word": [], "y": 0, "x": 0, "direction": "", "status": "", "input": [], "joker_value": [], "joker_letter": [], "score_memory": []}, 
               2: {"letters": [], "score": 0, "word": [], "y": 0, "x": 0, "direction": "", "status": "", "input": [], "joker_value": [], "joker_letter": [], "score_memory": []},
               3: {"letters": [], "score": 0, "word": [], "y": 0, "x": 0, "direction": "", "status": "", "input": [], "joker_value": [], "joker_letter": [], "score_memory": []},
               4: {"letters": [], "score": 0, "word": [], "y": 0, "x": 0, "direction": "", "status": "", "input": [], "joker_value": [], "joker_letter": [], "score_memory": []}}
sack_placeholder = letters_sack
score_memory = []
x = ""
y = ""
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
def asking_for_word(player):
    global joker_status
    joker_status = ""
    if "joker" in all_players[player_switch]["letters"]:
        joker_status = input("Do you want to use your joker tile in this round? ")
    else:
        joker_status = "no"
    if joker_status not in ["NO", "no", "N", "n", "No", "nO"]:
        joker_selection()   
        
    if len(joker_coords) != 0:
        joker_pick = input("Do you want to replace joker placed on the board? ")
        if joker_pick not in ["NO", "no", "N", "n", "No", "nO"]:
            joker_pickup()
    ifanything_wrong(player)
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
    sc.locate_joker(joker_replace, all_players, player_switch, letter_scores)
def joker_pickup():
    global joker_x, joker_y, joker_coords
    joker_x = input("Enter the x coordinate of joker ")
    joker_y = input("Enter the y coordinate of joker ")
    joker_picked_position = [int(joker_x), int(joker_y)]
    sc.joker_pickup_engine(joker_picked_position, all_players, player_switch, arr, joker_y, joker_x, joker_coords)
    
    
#GAME
ask_number_of_players()
sc.letter_distribution(player_count, sack_placeholder, all_players)
while len(sack_placeholder) != 0:
    sc.main(arr)
    sc.print_letters(all_players[player_switch], player_switch, letter_scores)
    ask_for_status(all_players[player_switch])
    if all_players[player_switch]["status"] == "PASS":
        pass
    elif all_players[player_switch]["status"] == "REPLACE ALL":
        sc.sack_replace_all(all_players[player_switch], sack_placeholder)
        sc.print_letters(all_players[player_switch], player_switch, letter_scores)
    elif all_players[player_switch]["status"] == "REPLACE SOME":
        sack_replace_some(all_players[player_switch])
        sc.print_letters(all_players[player_switch], player_switch, letter_scores)
    else:
        asking_for_word(all_players[player_switch])
        while sc.valid_english_word(all_players[player_switch]["word"]) == False or sc.checks_valid_coords(all_players[player_switch]["x"], all_players[player_switch]["y"]) == False:
            ifanything_wrong(all_players[player_switch])
        sc.add_before_after(all_players[player_switch]["word"], all_players[player_switch]["x"], all_players[player_switch]["y"], all_players[player_switch]["direction"], all_players, player_switch, arr)
        while sc.load_whole_word(all_players[player_switch]["x"], all_players[player_switch]["y"], all_players[player_switch]["direction"], all_players, player_switch, arr) == False or sc.valid_english_word(all_players[player_switch]["word"]) == False or sc.checks_if_touch(all_players[player_switch]["word"], all_players[player_switch]["x"], all_players[player_switch]["y"], all_players[player_switch]["direction"], arr) == False or sc.letters_inhand_checker(all_players[player_switch]["input"], all_players[player_switch]["x"], all_players[player_switch]["y"], all_players[player_switch]["direction"], all_players, player_switch, arr) == False or sc.checks_valid_coords(all_players[player_switch]["x"], all_players[player_switch]["y"]) == False or sc.checks_if_collide_or_gothrough(all_players[player_switch]["word"], all_players[player_switch]["x"], all_players[player_switch]["y"], all_players[player_switch]["direction"], arr) == False or sc.checks_ifword_fit(all_players[player_switch]["word"], all_players[player_switch]["x"], all_players[player_switch]["y"], all_players[player_switch]["direction"]) == False or sc.center_checker(all_players[player_switch]["word"], all_players[player_switch]["x"], all_players[player_switch]["y"], all_players[player_switch]["direction"], arr, max1) == False:
            ifanything_wrong(all_players[player_switch])
        sc.add_before_after(all_players[player_switch]["word"], all_players[player_switch]["x"], all_players[player_switch]["y"], all_players[player_switch]["direction"], all_players, player_switch, arr)
        sc.score_counter(all_players[player_switch], letter_scores, all_players, player_switch, arr)
        sc.printing_word(all_players[player_switch]["input"], all_players[player_switch]["x"], all_players[player_switch]["y"], all_players[player_switch]["direction"], joker_replace,  arr, all_players, player_switch, joker_status, joker_coords)
        sc.sack_refill(all_players[player_switch], sack_placeholder)
        sc.print_score(all_players[player_switch]["score"], all_players, player_switch)
    player_switch = 1 if player_switch == player_count else int(player_switch) + 1
sc.score_deduction(all_players, letter_scores, player_count)
sc.podium_print(all_players, player_count)


        