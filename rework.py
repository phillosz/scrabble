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
max1 = 0
joker_value_nahrada = []
joker_coords = []
joker_x = 0
joker_y = 0
podium = []

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
        all_players[1]["letters"].append(letter)
    for i in range(7):
        letter = random.choice(sack_placeholder)
        sack_placeholder.remove(letter)
        all_players[2]["letters"].append(letter)
    for i in range(7):
        letter = random.choice(sack_placeholder)
        sack_placeholder.remove(letter)
        all_players[3]["letters"].append(letter)
    for i in range(7):
        letter = random.choice(sack_placeholder)
        sack_placeholder.remove(letter)
        all_players[4]["letters"].append(letter)
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
    player["input"] = player["word"]
    player["x"] = input("Enter the x coordinate ")
    player["y"] = input("Enter the y coordinate ")
    player["direction"] = input("Enter the direction R, D ")
def score_counter(player):
    score = 0
    for i in player["word"]:
        score += letter_scores[i]
    if len(player["word"]) == 7:
        player["score"] += 50
    if score_multiplier_func_3W(player["word"], player["x"], player["y"], player["direction"]) != False:
        score *= 3*score_multiplier_func_3W(player["word"], player["x"], player["y"], player["direction"])
        if len(all_players[player_switch]["joker_letter"]) != 0:
            score -= 3*sum(all_players[player_switch]["joker_value"])
    if score_multiplier_func_2W(player["word"], player["x"], player["y"], player["direction"]) != False:
        score *= 2*score_multiplier_func_2W(player["word"], player["x"], player["y"], player["direction"])
        if len(all_players[player_switch]["joker_letter"]) != 0:
            score -= 2*sum(all_players[player_switch]["joker_value"])
    if score_multiplier_func_3L(player["word"], player["x"], player["y"], player["direction"]) != False:
        score += score_multiplier_func_3L(player["word"], player["x"], player["y"], player["direction"])
    if score_multiplier_func_2L(player["word"], player["x"], player["y"], player["direction"]) != False:
        score += score_multiplier_func_2L(player["word"], player["x"], player["y"], player["direction"])
    player["score"] += score
def printing_word(inp, x, y, direction):
    global joker_coords, joker_status
    p = 0
    joker_pos = 0
    for i in range(len(inp)):
        if direction == "R":
            if arr[int(y)-1][int(x)-1+p] != inp[p]:
                arr[int(y)-1][int(x)-1+p] = inp[p]
                all_players[player_switch]["letters"].remove(all_players[player_switch]["input"][i])
            elif arr[int(y)-1][int(x)-1+p] == inp[p]:
                pass
            p += 1
        elif direction == "D":
            if arr[int(y)-1+p][int(x)-1] != inp[p]:
                arr[int(y)-1+p][int(x)-1] = inp[p]
                all_players[player_switch]["letters"].remove(all_players[player_switch]["input"][i])
            elif arr[int(y)-1+p][int(x)-1] == inp[p]:
                pass
            p += 1
    if joker_status != "No" and joker_status != "no" and joker_status != "n" and joker_status != "N":
        for i in all_players[player_switch]["word"]:
            if i != joker_replace:
                joker_pos += 1
            else:
                break
        if direction == "R":
            joker_coords.append([int(x)+joker_pos, int(y)])
        if direction == "D":
            joker_coords.append([int(x), int(y)+joker_pos])
def print_score(player, score):
    all_players[player_switch]["score_memory"].append(score)
    print("Player", player_switch)
    for i in range(len(all_players[player_switch]["score_memory"])):
        print("      ", all_players[player_switch]["score_memory"][i])
def asking_for_word(player):
    global joker_status
    joker_status = ""
    if "joker" in all_players[player_switch]["letters"]:
        joker_status = input("Do you want to use your joker tile in this round? ")
    else:
        joker_status = "no"
    if joker_status != "No" and joker_status != "no" and joker_status != "n" and joker_status != "N" and joker_status != "NO":
        joker_selection()   
    if len(joker_coords) != 0:
        joker_pick = input("Do you want to replace joker placed on the board? ")
        if joker_pick != "No" and joker_pick != "no" and joker_pick != "n" and joker_pick != "N" and joker_pick != "NO":
            joker_pickup()
    player["word"] = input("Enter your word in CAPITALS ")
    player["input"] = player["word"]
    player["x"] = input("Enter the x coordinate ")
    player["y"] = input("Enter the y coordinate ")
    player["direction"] = input("Enter the direction R, D ")
def print_letters(player):
    scores = []
    print("Player", player_switch, player["letters"])
    for i in player["letters"]:
        scores.append(str(letter_scores[i]))
    print(" Score is", scores)
def ask_for_status(player):
    player["status"] = input("Do you want to PASS, REPLACE ALL, REPLACE SOME or PLAY? ")
def ask_number_of_players():
    global player_count
    player_count = int(input("Enter number of players 2-4 "))
def load_whole_word(x, y, direction):
    new_word = ""
    p = 0
    p_main = 1
    move = 0
    if direction == "D":
        for i in all_players[player_switch]["input"]:
            new_word = i
            while type(arr[int(y)-1+move][int(x)-1+p+p_main]) is str:
                new_word = new_word + arr[int(y)-1+move][int(x)-1+p+p_main]
                p += 1
            p = 0
            while type(arr[int(y)-1+move][int(x)-1-p-p_main]) is str:
                new_word = arr[int(y)-1+move][int(x)-1-p-p_main] + new_word
                p += 1
            p = 0
            if len(new_word) <= 1:
                new_word = ""
                move += 1
            else:
                while valid_english_word(new_word) == False:
                    return False
                else:
                    move += 1
    p_main = 1
    if direction == "R":
        for i in all_players[player_switch]["input"]:
            new_word = i
            while type(arr[int(y)-1+p+p_main][int(x)-1+move]) is str:
                new_word = new_word + arr[int(y)-1+p+p_main][int(x)-1+move]
                p += 1
            p = 0
            while type(arr[int(y)-1-p-p_main][int(x)-1+move]) is str:
                new_word = arr[int(y)-1-p-p_main][int(x)-1+move] + new_word
                p += 1
            p = 0
            if len(new_word) <= 1:
                new_word = ""
                move += 1
            else:
                if valid_english_word(new_word) == False:
                    return False
                else:
                    move += 1
def add_before_after(word, x, y, direction):
    new_word = word
    p = 1
    if direction == "D":
        while type(arr[int(y)-1-p][int(x)-1]) is str:
            new_word = arr[int(y)-1-p][int(x)-1] + new_word
            p += 1
        p = 1
        while type(arr[int(y)-2+p+len(word)][int(x)-1]) is str:
            new_word = new_word + arr[int(y)-1+p+len(word)][int(x)-1]
            p += 1
        p = 1
        all_players[player_switch]["word"] = new_word
    if direction == "R":
        while type(arr[int(y)-1][int(x)-1-p]) is str:
            new_word = arr[int(y)-1][int(x)-1-p] + new_word
            p += 1
        p = 1
        while type(arr[int(y)-1][int(x)-1+p+len(word)]) is str:
            new_word = new_word + arr[int(y)-1][int(x)-1+p+len(word)]
            p += 1
        p = 1
        all_players[player_switch]["word"] = new_word
def joker_selection():
    global joker_replace
    joker_replace = input("What letter do you want to use instead of the joker? ")
    joker_value = letter_scores[joker_replace]
    all_players[player_switch]["joker_value"].append(joker_value)
    all_players[player_switch]["joker_letter"].append(joker_replace)
    for i in range(len(all_players[player_switch]["letters"])):
        if all_players[player_switch]["letters"][i] == "joker":
            all_players[player_switch]["letters"][i] = joker_replace
def joker_pickup():
    global joker_x, joker_y, joker_coords
    joker_x = input("Enter the x coordinate of joker ")
    joker_y = input("Enter the y coordinate of joker ")
    joker_picked_position = [int(joker_x), int(joker_y)]
    if joker_picked_position in joker_coords:
        all_players[player_switch]["letters"].append("joker")
        all_players[player_switch]["letters"].remove(arr[int(joker_y)-1][int(joker_x)-1])
        print("Player",player_switch, all_players[player_switch]["letters"])
        joker_coords.remove(joker_picked_position)
def score_deduction():
    for i in range(1, player_count+1):
        for j in all_players[i]["letters"]:
            all_players[i]["score"] -= letter_scores[j] 
def podium_print():
    podium_unsorted = {}
    for i in range(1, player_count+1):
       if i in all_players:
            podium_unsorted[i] = all_players[i]["score"]
    if podium_unsorted:
        max_score_player = max(podium_unsorted, key=podium_unsorted.get)
        print("Player", max_score_player, "WON with", podium_unsorted[max_score_player], "points!")
    else:
        print("No players found.")

    
    
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
                else:
                    p += 1
            elif direction == "D":
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
def letters_inhand_checker(inp, x, y, direction):
    p = 0
    for i in inp:
        if direction == "D":
            if i in all_players[player_switch]["letters"] or i == arr[int(y)-1+p][int(x)-1]:
                return True
            else:
                print("Error, you don't have the letter", i)
                return False
        if direction == "R":
            if i in all_players[player_switch]["letters"] or i == arr[int(y)-1][int(x)-1+p]:
                return True
            else:
                print("Error, you don't have the letter", i)
                return False
    
def score_multiplier_func_3W(word, x, y, direction):
    p = 0
    counter = 0
    for i in range(len(word)):
        if direction == "R":
            if arr[int(y)-1][int(x)-1+p] == 4:
                p += 1
                counter += 1
        elif direction == "D":
            if arr[int(y)-1+p][int(x)-1] == 4:
                p += 1
                counter += 1
        p += 1
    if counter > 0:
        return counter
    else:
        return False
def score_multiplier_func_2W(word, x, y, direction):
    p = 0
    counter = 0
    for i in range(len(word)):
        if direction == "R":
            if arr[int(y)-1][int(x)-1+p] == 3 or arr[int(y)-1][int(x)-1+p] == 6:
                p += 1
                counter += 1
        elif direction == "D":
            if arr[int(y)-1+p][int(x)-1] == 3 or arr[int(y)-1+p][int(x)-1] == 6:
                p += 1
                counter += 1
        p += 1
    if counter > 0:
        return counter
    else:
        return False
def score_multiplier_func_3L(word, x, y, direction):
    p = 0
    counter = 0
    joker_value_nahrada = all_players[player_switch]["joker_value"].copy()
    for i in word:
        if direction == "R":
            if arr[int(y)-1][int(x)-1+p] == 2:
                p += 1
                counter += letter_scores[i] 
                if letter_scores[i] in joker_value_nahrada:
                    counter -= 2*letter_scores[i]
                    joker_value_nahrada.remove(letter_scores[i])
            else:
                p += 1
        elif direction == "D":
            if arr[int(y)-1+p][int(x)-1] == 2:
                p += 1
                counter += letter_scores[i]
                if letter_scores[i] in joker_value_nahrada:
                    counter -= 2*letter_scores[i]
                    joker_value_nahrada.remove(letter_scores[i])
            else:
                p += 1
    if counter > 0:
        return 2*counter
    elif counter <= 0:
        return counter
    else:
        return False
def score_multiplier_func_2L(word, x, y, direction):
    p = 0
    counter = 0
    joker_value_nahrada = all_players[player_switch]["joker_value"].copy()
    for i in word:
        if direction == "R":
            if arr[int(y)-1][int(x)-1+p] == 1:
                p += 1
                counter += letter_scores[i]
                if letter_scores[i] in joker_value_nahrada:
                    counter -= 2*letter_scores[i]
                    joker_value_nahrada.remove(letter_scores[i])
            else:
                p += 1
        elif direction == "D":
            if arr[int(y)-1+p][int(x)-1] == 1:
                p += 1
                counter += letter_scores[i]
                if letter_scores[i] in joker_value_nahrada:
                    counter -= 2*letter_scores[i]
                    joker_value_nahrada.remove(letter_scores[i])
            else:
                p += 1
    if counter != 0:
        return counter
    else:
        return False
def checks_if_collide_or_gothrough(word, x, y, direction):
    p = 0
    same_word_check = 0
    for i in range(len(word)):
        if direction == "R":
            if arr[int(y)-1][int(x)-1+p] == word[i]:
                    same_word_check += 1
            if arr[int(y)-1][int(x)-1+p] != 0 and arr[int(y)-1][int(x)-1+p] != word[i] and arr[int(y)-1][int(x)-1+p] != 6 and arr[int(y)-1][int(x)-1+p] != 1 and arr[int(y)-1][int(x)-1+p] != 2 and arr[int(y)-1][int(x)-1+p] != 3 and arr[int(y)-1][int(x)-1+p] != 4:
                print("Error, word collides with another word")
                return False
            else:
                p += 1
        elif direction == "D":
            if arr[int(y)-1+p][int(x)-1] == word[i]:
                    same_word_check += 1
            if arr[int(y)-1+p][int(x)-1] != 0 and arr[int(y)-1+p][int(x)-1] != word[i] and arr[int(y)-1+p][int(x)-1] != 6 and arr[int(y)-1+p][int(x)-1] != 1 and arr[int(y)-1+p][int(x)-1] != 2 and arr[int(y)-1+p][int(x)-1] != 3 and arr[int(y)-1+p][int(x)-1] != 4:
                print("Error, word collides with another word")
                return False
            else:
                p += 1
    if same_word_check == len(word):
        print("You can't type same word")
        return False
    else:
        return True
def checks_if_touch(word, x, y, direction):
    p = 0
    touch = 0
    for i in range(len(word)):
        if direction == "R":
            if arr[int(y)-1][int(x)-1+p] == word[i] or arr[int(y)-1][int(x)-1+p] == 6:
                touch += 1
                p += 1
            else:
                p += 1
        elif direction == "D":
            if arr[int(y)-1+p][int(x)-1] == word[i] or arr[int(y)-1+p][int(x)-1] == 6:
                touch += 1
                p += 1
            else:
                p += 1
    if touch > 0:
        return True 
    else:
        print("Word has to touch other words")
        return False
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
    while y not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]:
        print("Error, please enter number between 1 and 15")
        return False
    while x not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]:
        print("Error, please enter number between 1 and 15")
        return False
    
    
#GAME
letter_sack_func()
ask_number_of_players()
while len(sack_placeholder) != 0:
    main_func()
    print_letters(all_players[player_switch])
    ask_for_status(all_players[player_switch])
    if all_players[player_switch]["status"] == "PASS":
        pass
    elif all_players[player_switch]["status"] == "REPLACE ALL":
        sack_replace_all_func(all_players[player_switch])
        print_letters(all_players[player_switch])
    elif all_players[player_switch]["status"] == "REPLACE SOME":
        sack_replace_some_func(all_players[player_switch])
        print_letters(all_players[player_switch])
    else:
        asking_for_word(all_players[player_switch])
        while valid_english_word(all_players[player_switch]["word"]) == False or checks_valid_coords(all_players[player_switch]["x"], all_players[player_switch]["y"]) == False:
            ifanything_wrong(all_players[player_switch])
        add_before_after(all_players[player_switch]["word"], all_players[player_switch]["x"], all_players[player_switch]["y"], all_players[player_switch]["direction"])
        while load_whole_word(all_players[player_switch]["x"], all_players[player_switch]["y"], all_players[player_switch]["direction"]) == False or valid_english_word(all_players[player_switch]["word"]) == False or checks_if_touch(all_players[player_switch]["word"], all_players[player_switch]["x"], all_players[player_switch]["y"], all_players[player_switch]["direction"]) == False or letters_inhand_checker(all_players[player_switch]["input"], all_players[player_switch]["x"], all_players[player_switch]["y"], all_players[player_switch]["direction"]) == False or checks_valid_coords(all_players[player_switch]["x"], all_players[player_switch]["y"]) == False or checks_ifword_fit(all_players[player_switch]["word"], all_players[player_switch]["x"], all_players[player_switch]["y"], all_players[player_switch]["direction"]) == False or checks_if_collide_or_gothrough(all_players[player_switch]["word"], all_players[player_switch]["x"], all_players[player_switch]["y"], all_players[player_switch]["direction"]) == False or center_checker(all_players[player_switch]["word"], all_players[player_switch]["x"], all_players[player_switch]["y"], all_players[player_switch]["direction"]) == False:
            ifanything_wrong(all_players[player_switch])
        add_before_after(all_players[player_switch]["word"], all_players[player_switch]["x"], all_players[player_switch]["y"], all_players[player_switch]["direction"])
        score_counter(all_players[player_switch])
        printing_word(all_players[player_switch]["input"], all_players[player_switch]["x"], all_players[player_switch]["y"], all_players[player_switch]["direction"])
        sack_refill_func(all_players[player_switch])
        print_score(all_players[player_switch], all_players[player_switch]["score"])
    player_switch = 1 if player_switch == player_count else int(player_switch) + 1
score_deduction()
podium_print()


        