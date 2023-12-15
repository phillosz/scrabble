import random
with open("dic.txt", "r") as file:
    en_words = file.read().splitlines()


def main(arr):
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
            elif each in ["A", "B", "C", "D", "E", "F", "G", "H", "CH", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]:
                print(f" {each} ", end=" ")
def sack_refill(player, sack_placeholder):
    while len(player["letters"]) < 7:
        letter = random.choice(sack_placeholder)
        sack_placeholder.remove(letter)
        player["letters"].append(letter)
def letter_distribution(player_count, sack_placeholder, all_players):
    for i in range(player_count):
        for j in range(7):
            letter = random.choice(sack_placeholder)
            sack_placeholder.remove(letter)
            all_players[i+1]["letters"].append(letter)
def sack_replace_all(player, sack_placeholder):
    for i in player["letters"]:
        sack_placeholder.append(i)                              
    player["letters"] = []
    sack_refill(player, sack_placeholder)
def sack_append_letters_remove(player, letter, sack_placeholder):
    sack_placeholder.append(letter)
    player["letters"].remove(letter)
    sack_refill(player, sack_placeholder)
def score_counter(player, letter_scores, all_players, player_switch, arr):
    score = 0
    for i in player["word"]:
        score += letter_scores[i]
    if len(player["word"]) == 7:
        player["score"] += 50
    if score_multiplier_func_3W(player["word"], player["x"], player["y"], player["direction"], arr) != False:
        score *= 3*score_multiplier_func_3W(player["word"], player["x"], player["y"], player["direction"], arr)
        if len(all_players[player_switch]["joker_letter"]) != 0:
            score -= 3*sum(all_players[player_switch]["joker_value"])
            all_players[player_switch]["joker_value"] = []
    if score_multiplier_func_2W(player["word"], player["x"], player["y"], player["direction"], arr) != False:
        score *= 2*score_multiplier_func_2W(player["word"], player["x"], player["y"], player["direction"], arr)
        if len(all_players[player_switch]["joker_letter"]) != 0:
            score -= 2*sum(all_players[player_switch]["joker_value"])
            all_players[player_switch]["joker_value"] = []     
    if score_multiplier_func_3L(player["word"], player["x"], player["y"], player["direction"], all_players, player_switch, letter_scores, arr) != False:
        score += score_multiplier_func_3L(player["word"], player["x"], player["y"], player["direction"], all_players, player_switch, letter_scores, arr)
    if score_multiplier_func_2L(player["word"], player["x"], player["y"], player["direction"], all_players, player_switch, letter_scores, arr) != False:
        score += score_multiplier_func_2L(player["word"], player["x"], player["y"], player["direction"], all_players, player_switch, letter_scores, arr)
    if len(all_players[player_switch]["joker_value"]) != 0:
        for i in all_players[player_switch]["joker_value"]:
            score -= i    
    player["score"] += score
def printing_word(inp, x, y, direction, joker_replace, arr, all_players, player_switch, joker_status, joker_coords):
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
    if joker_status not in ["NO", "no", "N", "n", "No", "nO"]:
        for i in all_players[player_switch]["word"]:
            if i != joker_replace:                                                                         
                joker_pos += 1
            else:
                break
        if direction == "R":
            joker_coords.append([int(x)+joker_pos, int(y)])
        if direction == "D":                                                                                  
            joker_coords.append([int(x), int(y)+joker_pos])
def print_score(score, all_players, player_switch):
    all_players[player_switch]["score_memory"].append(score)
    print("Player", player_switch)
    for i in range(len(all_players[player_switch]["score_memory"])):                                       
        print("      ", all_players[player_switch]["score_memory"][i])
def print_letters(player, player_switch, letter_scores):
    scores = []
    print("Player", player_switch, player["letters"])
    for i in player["letters"]:
        scores.append(str(letter_scores[i]))
    print(" Score is", scores)
def load_whole_word(x, y, direction, all_players, player_switch, arr):
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
def add_before_after(word, x, y, direction, all_players, player_switch, arr):
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
def locate_joker(joker_replace, all_players, player_switch, letter_scores):
    joker_value = letter_scores[joker_replace]
    all_players[player_switch]["joker_value"].append(joker_value)
    all_players[player_switch]["joker_letter"].append(joker_replace)                                           
    for i in range(len(all_players[player_switch]["letters"])):
        if all_players[player_switch]["letters"][i] == "joker":
            all_players[player_switch]["letters"][i] = joker_replace
def joker_pickup_engine(joker_picked_position, all_players, player_switch, arr, joker_y, joker_x, joker_coords):    
    if joker_picked_position in joker_coords:
        all_players[player_switch]["letters"].append("joker")
        all_players[player_switch]["letters"].remove(arr[int(joker_y)-1][int(joker_x)-1])
        print("Player",player_switch, all_players[player_switch]["letters"])
        joker_coords.remove(joker_picked_position)
def score_deduction(all_players, letter_scores, player_count):
    for i in range(1, player_count+1):
        for j in all_players[i]["letters"]:
            all_players[i]["score"] -= letter_scores[j] 
def podium_print(all_players, player_count):
    podium_unsorted = {}
    for i in range(1, player_count+1):
       if i in all_players:
            podium_unsorted[i] = all_players[i]["score"]
    if podium_unsorted:
        max_score_player = max(podium_unsorted, key=podium_unsorted.get)
        print("Player", max_score_player, "WON with", podium_unsorted[max_score_player], "points!")
    else:
        print("No players found.")
def center_checker(word, x, y, direction, arr, max1):
    p = 0
    if len(max1) >= 1:
        return True
    else:
        for i in range(len(word)):
            if direction == "R":
                if arr[int(y)-1][int(x)-1+p] == 6:
                    max1.append(1)
                    return True
                else:
                    p += 1
            elif direction == "D":
                if arr[int(y)-1+p][int(x)-1] == 6:
                    max1.append(1)
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
def letters_inhand_checker(inp, x, y, direction, all_players, player_switch, arr):
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
    
def score_multiplier_func_3W(word, x, y, direction, arr):
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
def score_multiplier_func_2W(word, x, y, direction, arr):
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
def score_multiplier_func_3L(word, x, y, direction, all_players, player_switch, letter_scores, arr):
    p = 0
    counter = 0
    for i in word:
        if direction == "R":
            if arr[int(y)-1][int(x)-1+p] == 2:
                p += 1
                counter += letter_scores[i] 
                if letter_scores[i] in all_players[player_switch]["joker_value"]:
                    counter -= 2*letter_scores[i]
                    all_players[player_switch]["joker_value"].remove(letter_scores[i])
            else:
                p += 1
        elif direction == "D":
            if arr[int(y)-1+p][int(x)-1] == 2:
                p += 1
                counter += letter_scores[i]
                if letter_scores[i] in all_players[player_switch]["joker_value"]:
                    counter -= 2*letter_scores[i]
                    all_players[player_switch]["joker_value"].remove(letter_scores[i])
            else:
                p += 1
    if counter > 0:
        return 2*counter
    elif counter <= 0:
        return counter
    else:
        return False
def score_multiplier_func_2L(word, x, y, direction, all_players, player_switch, letter_scores, arr):
    p = 0
    counter = 0
    for i in word:
        if direction == "R":
            if arr[int(y)-1][int(x)-1+p] == 1:
                p += 1
                counter += letter_scores[i]
                if letter_scores[i] in all_players[player_switch]["joker_value"]:
                    counter -= 2*letter_scores[i]
                    all_players[player_switch]["joker_value"].remove(letter_scores[i])
            else:
                p += 1
        elif direction == "D":
            if arr[int(y)-1+p][int(x)-1] == 1:
                p += 1
                counter += letter_scores[i]
                if letter_scores[i] in all_players[player_switch]["joker_value"]:
                    counter -= 2*letter_scores[i]
                    all_players[player_switch]["joker_value"].remove(letter_scores[i])
            else:
                p += 1
    if counter != 0:
        return counter
    else:
        return False
def checks_if_collide_or_gothrough(word, x, y, direction, arr):
    p = 0
    same_word_check = 0
    for i in range(len(word)):
        if direction == "R":
            if arr[int(y)-1][int(x)-1+p] == word[i]:
                    same_word_check += 1
            if arr[int(y)-1][int(x)-1+p] not in [0, 1, 2, 3, 4, 6, word[i]]:
                print("Error, word collides with another word")
                return False
            else:
                p += 1
        elif direction == "D":
            if arr[int(y)-1+p][int(x)-1] == word[i]:
                    same_word_check += 1
            if arr[int(y)-1+p][int(x)-1] not in [0, 1, 2, 3, 4, 6, word[i]]:
                print("Error, word collides with another word")
                return False
            else:
                p += 1
    if same_word_check == len(word):
        print("You can't type same word")
        return False
    else:
        return True
def checks_if_touch(word, x, y, direction, arr):
    p = 0
    touch = 0
    for i in range(len(word)):
        if direction == "R":
            if arr[int(y)-1][int(x)-1+p] in [6, word[i]]:
                touch += 1
                p += 1
            else:
                p += 1
        elif direction == "D":
            if arr[int(y)-1+p][int(x)-1] in [6, word[i]]:
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