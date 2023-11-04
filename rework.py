import random
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
    'Y': 4, 'Z': 10}
letters_sack = ["A", "A", "A", "A", "A", "A", "A", "A", "A", "B", "B", "C", "C", "D", "D", "D", "D", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", 
                "F", "F", "G", "G", "G", "H", "H", "I", "I", "I", "I", "I", "I", "I", "I", "I", "J", "K", "L", "L", "L", "L", "M", "M", "N", "N", "N", "N", "N", 
                "N", "O", "O", "O", "O", "O", "O", "O", "O", "P", "P", "Q", "R", "R", "R", "R", "R", "R", "S", "S", "S", "S", "T", "T", "T", "T", "T", "T", "U", 
                "U", "U", "U", "V", "V", "W", "W", "X", "Y", "Y", "Z", "joker", "joker"]
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "CH", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "X", "Y", "Z"]
all_players = {"1": {"letters": [], "score": 0, "word": [], "y": 0, "x": 0, "direction": "", "status": ""}, 
               "2": {"letters": [], "score": 0, "word": [], "y": 0, "x": 0, "direction": "", "status": ""}, 
               "3": {"letters": [], "score": 0, "word": [], "y": 0, "x": 0, "direction": "", "status": ""}, 
               "4": {"letters": [], "score": 0, "word": [], "y": 0, "x": 0, "direction": "", "status": ""}}
sack_placeholder = letters_sack
score_memory = []
x = ""
y = ""
inp = ""
word = list(inp)
player_count = 0
player_switch = "1"
max1 = 0


#FUNCTIONS THAT EDIT OR DO SOMETHING
def main_func():
    for i in arr:
        for each in i:
            if each == 4:
                print("TW ", end=" ")
            elif each == 3:
                print("DW ", end=" ")
            elif each == 2:
                print("TL ", end=" ")
            elif each == 1:
                print("DL ", end=" ")
            elif each == 0:
                print("___", end=" ")
            elif each == 5:
                print("\n\n", end=" ")
            elif each == 6:
                print(" S ", end=" ")
            elif each == 7:
                print("__", end=" ")
            elif each == "A":
                print(" A ", end=" ")
            elif each == "B":
                print(" B ", end=" ")
            elif each == "C":
                print(" C ", end=" ")
            elif each == "D":
                print(" D ", end=" ")
            elif each == "E":
                print(" E ", end=" ")
            elif each == "F":
                print(" F ", end=" ")
            elif each == "G":
                print(" G ", end=" ")
            elif each == "H":
                print(" H ", end=" ")
            elif each == "CH":
                print("CH ", end=" ")
            elif each == "I":
                print(" I ", end=" ")
            elif each == "J":
                print(" J ", end=" ")
            elif each == "K":
                print(" K ", end=" ")
            elif each == "L":
                print(" L ", end=" ")
            elif each == "M":
                print(" M ", end=" ")
            elif each == "N":
                print(" N ", end=" ")
            elif each == "O":
                print(" O ", end=" ")
            elif each == "P":
                print(" P ", end=" ")
            elif each == "Q":
                print(" Q ", end=" ")
            elif each == "R":
                print(" R ", end=" ")
            elif each == "S":
                print(" S ", end=" ")
            elif each == "T":
                print(" T ", end=" ")
            elif each == "U":
                print(" U ", end=" ")
            elif each == "V":
                print(" V ", end=" ")
            elif each == "W":
                print(" W ", end=" ")
            elif each == "X":
                print(" X ", end=" ")
            elif each == "Y":
                print(" Y ", end=" ")
            elif each == "Z":
                print(" Z ", end=" ")
def letter_sack_func():
    for i in range(7):
        letter = random.choice(sack_placeholder)
        sack_placeholder.remove(letter)
        all_players["1"]["letters"].append(letter)
    for i in range(7):
        letter = random.choice(sack_placeholder)
        sack_placeholder.remove(letter)
        all_players["2"]["letters"].append(letter)
    for i in range(7):
        letter = random.choice(sack_placeholder)
        sack_placeholder.remove(letter)
        all_players["3"]["letters"].append(letter)
    for i in range(7):
        letter = random.choice(sack_placeholder)
        sack_placeholder.remove(letter)
        all_players["4"]["letters"].append(letter)
def sack_refill_func(player):
    while len(player["letters"]) < 7:
        letter = random.choice(sack_placeholder)
        sack_placeholder.remove(letter)
        player["letters"].append(letter)
def sack_replace_all_func(player):
    for i in player["letters"]:
        sack_placeholder.append(i)
    player["letters"] = []
    sack_refill_func(player)
def sack_replace_some_func(player):
    print("Your letters are: ", player["letters"])
    letter = input("Enter letter you want to replace ")
    while letter not in player["letters"]:
        print("Error")
        letter = input("Enter letter you want to replace ")
    sack_placeholder.append(letter)
    player["letters"].remove(letter)
    sack_refill_func(player)
def ifanything_wrong(player):
    player["word"] = input("Enter your word in CAPITALS ")
    player["x"]= input("Enter the x coordinate ")
    player["y"] = input("Enter the y coordinate ")
    player["direction"] = input("Enter the direction R, D ")
def score_counter(player):
    score = 0
    for i in player["word"]:
        score += letter_scores[i]
    if len(player["word"]) == 7:
        player["score"] += 50
    if score_multiplier_func_3W(player["word"], player["x"], player["y"], player["direction"]) == True:
        score *= 3
    elif score_multiplier_func_2W(player["word"], player["x"], player["y"], player["direction"]) == True:
        score *= 2
    elif score_multiplier_func_3L(player["word"], player["x"], player["y"], player["direction"]) != False:
        score += 2*letter_scores[score_multiplier_func_3L(player["word"], player["x"], player["y"], player["direction"])]
    elif score_multiplier_func_2L(player["word"], player["x"], player["y"], player["direction"]) != False:
        score += letter_scores[score_multiplier_func_2L(player["word"], player["x"], player["y"], player["direction"])]
    player["score"] += score
def printing_word(word, x, y, direction):
    p = 0
    for i in range(len(word)):
        if direction == "R":
            arr[int(y)-1][int(x)-1+p] = word[p]
            all_players[player_switch]["letters"].remove(word[i])
            p += 1
        elif direction == "D":
            arr[int(y)-1+p][int(x)-1] = word[p]
            all_players[player_switch]["letters"].remove(word[i])
            p += 1
def print_score(player):
    print("Player", player_switch, "score is: ", player["score"])
def asking_for_word(player):
    player["word"] = input("Enter your word in CAPITALS ")
    player["x"] = input("Enter the x coordinate ")
    player["y"] = input("Enter the y coordinate ")
    player["direction"] = input("Enter the direction R, D ")
def print_letters(player):
    print("Player", player_switch, player["letters"])
def ask_for_status(player):
    player["status"] = input("Do you want to pass, replace all or replace some? ")
def ask_number_of_players():
    global player_count
    player_count = int(input("Enter number of players 2-4 "))
    
    
#FUNCTIONS THAT CHECK AND RETURN TRUE OR FALSE
def center_checker(word, x, y, direction):
    global max1
    p = 0
    if max1 >= 1:
        return True
    else:
        for i in range(len(word)):
            if direction == "R":
                if arr[int(y)-1][int(x)-1+p] == 6:
                    max1 += 1
                    return True
            if direction == "D":
                if arr[int(y)-1+p][int(x)-1] == 6:
                    max1 += 1
                    return True
            else:
                p += 1
        print("Error, word doesn't go through center")
        return False
def valid_english_word(word):
    if word in en_words:
        return True
    else:
        print("Error, word not in dictionary")
        return False
def letters_inhand_checker(word, player):
    for i in word:
        if i not in player["letters"]:
            print("Error, you don't have the letter", i)
            return False
    return True
def score_multiplier_func_3W(word, x, y, direction):
    p = 0
    for i in range(len(word)):
        if direction == "R":
            if arr[int(y)-1][int(x)-1+p] == 4:
                return True
        elif direction == "D":
            if arr[int(y)-1+p][int(x)-1] == 4:
                return True
        else:
            p += 1
    return False
def score_multiplier_func_2W(word, x, y, direction):
    p = 0
    for i in range(len(word)):
        if direction == "R":
            if arr[int(y)-1][int(x)-1+p] == 3:
                return True
        elif direction == "D":
            if arr[int(y)-1+p][int(x)-1] == 3:
                return True
        else:
            p += 1
    return False
def score_multiplier_func_3L(word, x, y, direction):
    p = 0
    for i in word:
        if direction == "R":
            if arr[int(y)-1][int(x)-1+p] == 2:
                return i
        elif direction == "D":
            if arr[int(y)-1+p][int(x)-1] == 2:
                return i
        else:
            p += 1
    return False
def score_multiplier_func_2L(word, x, y, direction):
    p = 0
    for i in word:
        if direction == "R":
            if arr[int(y)-1][int(x)-1+p] == 1:
                return i
        elif direction == "D":
            if arr[int(y)-1+p][int(x)-1] == 1:
                return i
        else:
            p += 1
    return False
def checks_if_collide_or_gothrough(word, x, y, direction):
    p = 0
    for i in range(len(word)):
        if direction == "R":
            if arr[int(y)-1][int(x)-1+p] != 0 and arr[int(y)-1][int(x)-1+p] != word[i] and arr[int(y)-1][int(x)-1+p] == 6 and arr[int(y)-1][int(x)-1+p] == 1 and arr[int(y)-1][int(x)-1+p] == 2 and arr[int(y)-1][int(x)-1+p] == 3 and arr[int(y)-1][int(x)-1+p] == 4:
                print("Error, word collides with another word")
                return False
        elif direction == "D":
            if arr[int(y)-1][int(x)-1+p] != 0 and arr[int(y)-1][int(x)-1+p] != word[i] and arr[int(y)-1][int(x)-1+p] == 6 and arr[int(y)-1][int(x)-1+p] == 1 and arr[int(y)-1][int(x)-1+p] == 2 and arr[int(y)-1][int(x)-1+p] == 3 and arr[int(y)-1][int(x)-1+p] == 4:
                print("Error, word collides with another word")
                return False
        else:
            p += 1
    return True
def checks_ifword_fit(word, x, y, direction):
    if direction == "D":
        while len(word) > (16 - int(y)):
            print("Invalid coordinates")
            return False
    if direction == "R":
        while len(word) > (16 - int(x)):
            print("Invalid coordinates")
            return False
def checks_valid_coords(x, y):
    while int(y) not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]:
        print("Error, please enter number between 1 and 15")
        return False
    while int(x) not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]:
        print("Error, please enter number between 1 and 15")
        return False
# def checks_ifword_touches(word, x, y, direction):
#     p = 0
#     for i in word:
#         if direction == "R":
#             if arr[int(y)-1][int(x)-1+p] == i:
#                 pass
#             else:
#                 while arr[int(y)-1][int(x)-1+p] != 0:
    
    
#GAME
letter_sack_func()
ask_number_of_players()
while len(sack_placeholder) != 0:
    main_func()
    print_letters(all_players[player_switch])
    ask_for_status(all_players[player_switch])
    if all_players[player_switch]["status"] == "pass":
        pass
    elif all_players[player_switch]["status"] == "replace all":
        sack_replace_all_func(all_players[player_switch])
        print_letters(all_players[player_switch])
    elif all_players[player_switch]["status"] == "replace some":
        sack_replace_some_func(all_players[player_switch])
        print_letters(all_players[player_switch])
    else:
        asking_for_word(all_players[player_switch])
        while checks_valid_coords(all_players[player_switch]["x"], all_players[player_switch]["y"]) == False or checks_ifword_fit(all_players[player_switch]["word"], all_players[player_switch]["x"], all_players[player_switch]["y"], all_players[player_switch]["direction"]) == False or checks_if_collide_or_gothrough(all_players[player_switch]["word"], all_players[player_switch]["x"], all_players[player_switch]["y"], all_players[player_switch]["direction"]) == False or letters_inhand_checker(all_players[player_switch]["word"], all_players[player_switch]) == False or valid_english_word(all_players[player_switch]["word"]) == False or center_checker(all_players[player_switch]["word"], all_players[player_switch]["x"], all_players[player_switch]["y"], all_players[player_switch]["direction"]) == False:
            ifanything_wrong(all_players[player_switch])
        else:
            score_counter(all_players[player_switch])
            printing_word(all_players[player_switch]["word"], all_players[player_switch]["x"], all_players[player_switch]["y"], all_players[player_switch]["direction"])
            sack_refill_func(all_players[player_switch])
            print_score(all_players[player_switch])
    player_switch = "1" if player_switch == str(player_count) else str(int(player_switch) + 1)

        