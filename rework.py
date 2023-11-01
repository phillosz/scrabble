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
player1 = {"letters": [], "score": 0, "word": [], "y": 0, "x": 0}
player2 = {"letters": [], "score": 0, "word": [], "y": 0, "x": 0}
player3 = {"letters": [], "score": 0, "word": [], "y": 0, "x": 0}
player4 = {"letters": [], "score": 0, "word": [], "y": 0, "x": 0}
sack_placeholder = letters_sack
score_memory = []
word = []
x = ""
y = ""
#FUNCTIONS
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
        player1["letters"].append(letter)
    for i in range(7):
        letter = random.choice(sack_placeholder)
        sack_placeholder.remove(letter)
        player2["letters"].append(letter)
    for i in range(7):
        letter = random.choice(sack_placeholder)
        sack_placeholder.remove(letter)
        player3["letters"].append(letter)
    for i in range(7):
        letter = random.choice(sack_placeholder)
        sack_placeholder.remove(letter)
        player4["letters"].append(letter)
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
def center_checker(word, x, y):
    p = 0
    for i in range(len(word)):
        if arr[int(y)-1+p][int(x)-1] == 6 or arr[int(y)-1][int(x)-1+p] == 6:
            return True
        else:
            p += 1
        return False
def valid_english_word(word):
    if word in en_words:
        return True
    else:
        return False
def letters_inhand_checker(word, player):
    for i in word:
        if i not in player["letters"]:
            return False
    return True
def inp_modifier():
    global inp, word
    inp = input("Enter your word in CAPITALS ")
    word = list(inp)
def score_multiplier_func_3W(word, x, y):
    p = 0
    for i in range(len(word)):
        if arr[int(y)-1+p][int(x)-1] == 4 or arr[int(y)-1][int(x)-1+p] == 4:
            return True
        else:
            p += 1
    return False
def score_multiplier_func_2W(word, x, y):
    p = 0
    for i in range(len(word)):
        if arr[int(y)-1+p][int(x)-1] == 3 or arr[int(y)-1][int(x)-1+p] == 3:
            return True
        else:
            p += 1
    return False
def score_multiplier_func_3L(word, x, y):
    p = 0
    for i in word:
        if arr[int(y)-1+p][int(x)-1] == 2 or arr[int(y)-1][int(x)-1+p] == 2:
            return i
        else:
            p += 1
    return False
def score_multiplier_func_2L(word, x, y):
    p = 0
    for i in word:
        if arr[int(y)-1+p][int(x)-1] == 1 or arr[int(y)-1][int(x)-1+p] == 1:
            return i
        else:
            p += 1
    return False
def score_counter(player):
    score = player["score"]
    for i in player["word"]:
        score += letter_scores[i]
    player["score"] += score
    if len(player["word"]) == 7:
        player["score"] += 50
    if score_multiplier_func_3W(player["word"], player["x"], player["y"]) == True:
        player["score"] *= 3
    elif score_multiplier_func_2W(player["word"], player["x"], player["y"]) == True:
        player["score"] *= 2
    elif score_multiplier_func_3L(player["word"], player["x"], player["y"]) != False:
        player["score"] += letter_scores[score_multiplier_func_3L(player["word"], player["x"], player["y"])]
    elif score_multiplier_func_2L(player["word"], player["x"], player["y"]) != False:
        player["score"] += letter_scores[score_multiplier_func_2L(player["word"], player["x"], player["y"])]