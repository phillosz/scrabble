import random
#TW = triple word
#DW = double word 
#TL = triple letter 
#DL = double letter 

#MAIN BOARD
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

#MAIN SCOREBOARD
# score_arr = [[1, 2, 3, 4,],
#              [0, 0, 0, 0,],
#              [0, 0, 0, 0,],
#              [0, 0, 0, 0,],
#              [0, 0, 0, 0,],
#              [0, 0, 0, 0,],
#              [0, 0, 0, 0,],
#              [0, 0, 0, 0,],
#              [0, 0, 0, 0,],
#              [0, 0, 0, 0,],
#              [0, 0, 0, 0,],
#              [0, 0, 0, 0,],
#              [0, 0, 0, 0,],
#              [0, 0, 0, 0,],
#              [0, 0, 0, 0,],
#              [0, 0, 0, 0,]]

# #MAIN FUNCTION THAT PRINTS SCOREBOARD
# def main_scoreboard():
#     for i in score_arr:
#         for each in i:
#             if each == 1:
#                 print("Player 1", end=" | ")
#             elif each == 2:
#                 print("Player 2", end=" | ")
#             elif each == 3:
#                 print("Player 3", end=" | ")
#             elif each == 4:
#                 print("Player 4", end=" | ")
#             elif each == 0:
#                 print("........", end=" | ")
#         print()

#MAIN FUNCTION FOR PRINTING THE BOARD AND ADDING LETTERS
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
            elif each == "X":
                print(" X ", end=" ")
            elif each == "Y":
                print(" Y ", end=" ")
            elif each == "Z":
                print(" Z ", end=" ")
        print()
letter_scores = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4,
    'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3,
    'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8,
    'Y': 4, 'Z': 10}

letters_sack = ["A", "A", "A", "A", "A", "A", "A", "A", "A", "B", "B", "C", "C", "D", "D", "D", "D", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", 
                "F", "F", "G", "G", "G", "H", "H", "I", "I", "I", "I", "I", "I", "I", "I", "I", "J", "K", "L", "L", "L", "L", "M", "M", "N", "N", "N", "N", "N", 
                "N", "O", "O", "O", "O", "O", "O", "O", "O", "P", "P", "Q", "R", "R", "R", "R", "R", "R", "S", "S", "S", "S", "T", "T", "T", "T", "T", "T", "U", 
                "U", "U", "U", "V", "V", "W", "W", "X", "Y", "Y", "Z", "joker", "joker"]
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "CH", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "X", "Y", "Z"]
player1 = []
player2 = []

#PLAYER 1
#PLAYER 1
#PLAYER 1
#PLAYER 1
#PLAYER 1
#PLAYER 1
#PLAYER 1
#PLAYER 1
#PLAYER 1
#PLAYER 1
main_func()
#main_scoreboard()
print()

#RANDOM LETTER
sack_placeholder = letters_sack
for i in range(7):
    ran = random.choice(sack_placeholder)
    player1.append(ran)
for i in player1:
    sack_placeholder.remove(i)

for i in range(7):
    ran = random.choice(sack_placeholder)
    player2.append(ran)
for i in player2:
    sack_placeholder.remove(i)

print("Player 1 has ", player1, " on your hand")

#PLAYER INPUTS 
y = input("Enter Y coords of the start ")
x = input("Enter X coords of the start ")

def coords_y_modifier():
    global y
    y = input("Enter Y coords of the start ")   
def coords_x_modifier():
    global x 
    x = input("Enter X coords of the start ")

def letters_inhand():
    global word
    global inp
    word = []
    inp = input("Enter your word in CAPITALS ")
    word = list(inp)
    
while int(y) not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]:
    print("Error, please enter number between 1 and 15")
    coords_y_modifier()
      
while int(x) not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]:
    print("Error, please enter number between 1 and 15")
    coords_x_modifier()

def draws_to_7():
    for i in range(7-len(player1)):
        ran = random.choice(sack_placeholder)
        player1.append(ran)
    for i in ran:
        sack_placeholder.remove(i)
          
word = []
inp = input("Enter your word in CAPITALS ")
word = list(inp)
while not all(letter in player1 for letter in word):
    print("Please use only letters in your hand")
    letters_inhand()
player_storage = player1
for letter in word:
    if letter in player1:
        player1.remove(letter)
    else:
        player1 = player_storage
        letters_inhand()
       
draws_to_7()
print(player1)

#CHECKS IF THE WORD FITS INSIDE THE BORDERS
def inp_modifier():
    global inp, word
    inp = input("Enter your word in CAPITALS ")
    word = list(inp)
direction = input("In which direction should your word be? D R? ")

if direction == "D":
    while len(word) > (16 - int(y)):
        print("Error, word colides with the border")
        inp_modifier()
if direction == "R":
    while len(word) > (16 - int(x)):
        print("Error, word colides with the border")
        inp_modifier()

#WRITES PLAYERS WORD
def checker_D():
    p = 0
    q = 1
    z = 0
    for i in range(len(word)):
        if arr[int(y)-1+p][int(x)-1] not in ["A", "B", "C", "D", "E", "F", "G", "H", "CH", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "X", "Y", "Z"]:
            z += 1
        p += 1
        q += 1
    if z == int(len(word)):
        return True

def checker_R():
    p = 0
    q = 1
    z = 0
    for i in range(len(word)):
        if arr[int(y)-1][int(x)-1+p] not in ["A", "B", "C", "D", "E", "F", "G", "H", "CH", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "X", "Y", "Z"]:
            z += 1
        p += 1
        q += 1
    if z == int(len(word)):
        return True

if direction == "D":
    p = 0
    q = 1
    if checker_D() == True:
        for i in range(len(word)):
            arr[int(y)-1+p][int(x)-1] = word[q-1]
            p += 1
            q += 1
    else:
        print("Error, please enter different coordinations that don't colide with other words")
        y = input("Enter Y coords of the start ")
        x = input("Enter X coords of the start ")
        if checker_D() == True:
            for i in range(len(word)):
                arr[int(y)-1+p][int(x)-1] = word[q-1]
                p += 1
                q += 1
        else:
            pass
        
if direction == "R":
    p = 0
    q = 1
    if checker_R() == True:
        for i in range(len(word)):
            arr[int(y)-1][int(x)-1+p] = word[q-1]
            p += 1
            q += 1
    else:
        print("Error, please enter different coordinations that don't colide with other words")
        y = input("Enter Y coords of the start ")
        x = input("Enter X coords of the start ")
        if checker_R() == True:
            for i in range(len(word)):
                arr[int(y)-1][int(x)-1+p] = word[q-1]
                p += 1
                q += 1
        else:
            pass
        
#SCORING SYSTEM
score = 0
for i in word:
    value = letter_scores[i]
    score += value

#SCORE PRINTING
score_memory1 = []
def print_score_1():
    print("Player 1's Score:")
    for i in score_memory1:
        print(i)
    score_memory1.append(score)
    print(score)
    print("Total:")
    print(sum(score_memory1))
         
main_func()
#main_scoreboard() 
print_score_1()   
print()
           
#PLAYER 2
#PLAYER 2
#PLAYER 2
#PLAYER 2
#PLAYER 2
#PLAYER 2
#PLAYER 2
#PLAYER 2
#PLAYER 2
#PLAYER 2     
print("Player 2 has ", player2, " on your hand")

#PLAYER INPUTS 
y = input("Enter Y coords of the start ")
x = input("Enter X coords of the start ")

def coords_y_modifier():
    global y
    y = input("Enter Y coords of the start ")   
def coords_x_modifier():
    global x 
    x = input("Enter X coords of the start ")

def letters_inhand():
    global word
    global inp
    word = []
    inp = input("Enter your word in CAPITALS ")
    word = list(inp)
    
while int(y) not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]:
    print("Error, please enter number between 1 and 15")
    coords_y_modifier()
      
while int(x) not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]:
    print("Error, please enter number between 1 and 15")
    coords_x_modifier()

def draws_to_7_2():
    for i in range(7-len(player2)):
        ran = random.choice(sack_placeholder)
        player2.append(ran)
    for i in ran:
        sack_placeholder.remove(i)
          
word = []
inp = input("Enter your word in CAPITALS ")
word = list(inp)
while not all(letter in player2 for letter in word):
    print("Please use only letters in your hand")
    letters_inhand()
player_storage = player2
for letter in word:
    if letter in player2:
        player2.remove(letter)
    else:
        player2 = player_storage
        letters_inhand()
       
draws_to_7_2()
print(player2)

#CHECKS IF THE WORD FITS INSIDE THE BORDERS
def inp_modifier():
    global inp, word
    inp = input("Enter your word in CAPITALS ")
    word = list(inp)
direction = input("In which direction should your word be? D R? ")
    
if direction == "D":
    while len(word) > (16 - int(y)):
        print("Error, word colides with the border")
        inp_modifier()
if direction == "R":
    while len(word) > (16 - int(x)):
        print("Error, word colides with the border")
        inp_modifier()
        
#WRITES PLAYERS WORD
def checker_D():
    p = 0
    q = 1
    z = 0
    for i in range(len(word)):
        if arr[int(y)-1+p][int(x)-1] not in ["A", "B", "C", "D", "E", "F", "G", "H", "CH", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "X", "Y", "Z"]:
            z += 1
        p += 1
        q += 1
    if z == int(len(word)):
        return True

def checker_R():
    p = 0
    q = 1
    z = 0
    for i in range(len(word)):
        if arr[int(y)-1][int(x)-1+p] not in ["A", "B", "C", "D", "E", "F", "G", "H", "CH", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "X", "Y", "Z"]:
            z += 1
        p += 1
        q += 1
    if z == int(len(word)):
        return True

if direction == "D":
    p = 0
    q = 1
    if checker_D() == True:
        for i in range(len(word)):
            arr[int(y)-1+p][int(x)-1] = word[q-1]
            p += 1
            q += 1
    else:
        print("Error, please enter different coordinations that don't colide with other words")
        y = input("Enter Y coords of the start ")
        x = input("Enter X coords of the start ")
        if checker_D() == True:
            for i in range(len(word)):
                arr[int(y)-1+p][int(x)-1] = word[q-1]
                p += 1
                q += 1
        else:
            pass
        
if direction == "R":
    p = 0
    q = 1
    if checker_R() == True:
        for i in range(len(word)):
            arr[int(y)-1][int(x)-1+p] = word[q-1]
            p += 1
            q += 1
    else:
        print("Error, please enter different coordinations that don't colide with other words")
        y = input("Enter Y coords of the start ")
        x = input("Enter X coords of the start ")
        if checker_R() == True:
            for i in range(len(word)):
                arr[int(y)-1][int(x)-1+p] = word[q-1]
                p += 1
                q += 1
        else:
            pass
                   
score = 0
for i in word:
    value = letter_scores[i]
    score += value                   
#SCORE PRINTING
score_memory2 = []
def print_score_2():
    print("Player 2's Score")
    for i in score_memory2:
        print(i)
    score_memory2.append(score)
    print(score)    
    print("Total:")
    print(sum(score_memory2))              

main_func() 
#main_scoreboard() 
print_score_2()








































#LOOP THAT LETS YOU PLAY THE GAME
#PLAYER 1
#PLAYER 1
#PLAYER 1
#PLAYER 1
#PLAYER 1
#PLAYER 1
#PLAYER 1
#PLAYER 1
#PLAYER 1
#PLAYER 1
while len(sack_placeholder) != 0:
    print("Player 1 has ", player1, " on your hand")
    y = input("Enter Y coords of the start ")
    x = input("Enter X coords of the start ")
    
    
    while int(y) not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]:
        print("Error, please enter number between 1 and 15")
        coords_y_modifier() 
    while int(x) not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]:
        print("Error, please enter number between 1 and 15")
        coords_x_modifier()
        
        
    word = []
    inp = input("Enter your word in CAPITALS ")
    word = list(inp)
    while not all(letter in player1 for letter in word):
        print("Please use only letters in your hand")
        letters_inhand()
    player_storage = player1
    for letter in word:
        if letter in player1:
            player1.remove(letter)
        else:
            player1 = player_storage
            letters_inhand()  
    draws_to_7()
    print(player1)
    
    
    direction = input("In which direction should your word be? D R? ")
    if direction == "D":
        while len(word) > (16 - int(y)):
            print("Error, word colides with the border")
            inp_modifier()
    if direction == "R":
        while len(word) > (16 - int(x)):
            print("Error, word colides with the border")
            inp_modifier()        
    if direction == "D":
        p = 0
        q = 1
        if checker_D() == True:
            for i in range(len(word)):
                arr[int(y)-1+p][int(x)-1] = word[q-1]
                p += 1
                q += 1
        else:
            print("Error, please enter different coordinations that don't colide with other words")
            y = input("Enter Y coords of the start ")
            x = input("Enter X coords of the start ")
            if checker_D() == True:
                for i in range(len(word)):
                    arr[int(y)-1+p][int(x)-1] = word[q-1]
                    p += 1
                    q += 1
            else:
                pass 
    if direction == "R":
        p = 0
        q = 1
        if checker_R() == True:
            for i in range(len(word)):
                arr[int(y)-1][int(x)-1+p] = word[q-1]
                p += 1
                q += 1
        else:
            print("Error, please enter different coordinations that don't colide with other words")
            y = input("Enter Y coords of the start ")
            x = input("Enter X coords of the start ")
            if checker_R() == True:
                for i in range(len(word)):
                    arr[int(y)-1][int(x)-1+p] = word[q-1]
                    p += 1
                    q += 1
            else:
                pass
    score = 0
    for i in word:
        value = letter_scores[i]
        score += value
        
    main_func()
    #main_scoreboard() 
    print_score_1()   
    print()
    
    #PLAYER 2
    #PLAYER 2
    #PLAYER 2
    #PLAYER 2
    #PLAYER 2
    #PLAYER 2
    #PLAYER 2
    #PLAYER 2
    #PLAYER 2
    #PLAYER 2
    print("Player 2 has ", player2, " on your hand")
    y = input("Enter Y coords of the start ")
    x = input("Enter X coords of the start ")
    
    while int(y) not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]:
        print("Error, please enter number between 1 and 15")
        coords_y_modifier()
        
    while int(x) not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]:
        print("Error, please enter number between 1 and 15")
        coords_x_modifier()
        
    word = []
    inp = input("Enter your word in CAPITALS ")
    word = list(inp)
    while not all(letter in player2 for letter in word):
        print("Please use only letters in your hand")
        letters_inhand()
    player_storage = player2
    for letter in word:
        if letter in player2:
            player2.remove(letter)
        else:
            player2 = player_storage
            letters_inhand()
    draws_to_7_2()
    print(player2)
    
    direction = input("In which direction should your word be? D R? ")
    
    if direction == "D":
        while len(word) > (16 - int(y)):
            print("Error, word colides with the border")
            inp_modifier()
    if direction == "R":
        while len(word) > (16 - int(x)):
            print("Error, word colides with the border")
            inp_modifier()
    
    if direction == "D":
        p = 0
        q = 1
        if checker_D() == True:
            for i in range(len(word)):
                arr[int(y)-1+p][int(x)-1] = word[q-1]
                p += 1
                q += 1
        else:
            print("Error, please enter different coordinations that don't colide with other words")
            y = input("Enter Y coords of the start ")
            x = input("Enter X coords of the start ")
            if checker_D() == True:
                for i in range(len(word)):
                    arr[int(y)-1+p][int(x)-1] = word[q-1]
                    p += 1
                    q += 1
            else:
                pass   
    if direction == "R":
        p = 0
        q = 1
        if checker_R() == True:
            for i in range(len(word)):
                arr[int(y)-1][int(x)-1+p] = word[q-1]
                p += 1
                q += 1
        else:
            print("Error, please enter different coordinations that don't colide with other words")
            y = input("Enter Y coords of the start ")
            x = input("Enter X coords of the start ")
            if checker_R() == True:
                for i in range(len(word)):
                    arr[int(y)-1][int(x)-1+p] = word[q-1]
                    p += 1
                    q += 1
            else:
                pass
            
    score = 0
    for i in word:
        value = letter_scores[i]
        score += value
    main_func() 
    #main_scoreboard()
    print_score_2()