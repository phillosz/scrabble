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
main_func()

print("PLAYER 1")
#PLAYER INPUTS           
y = input("Enter Y coords of the start ")
x = input("Enter X coords of the start ")

def coords_y_modifier():
    global y
    y = input("Enter Y coords of the start ")
def coords_x_modifier():
    global x 
    x = input("Enter X coords of the start ")

while int(y) not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]:
    print("Error, please enter number between 1 and 15")
    coords_y_modifier()
    
while int(x) not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]:
    print("Error, please enter number between 1 and 15")
    coords_x_modifier()

word = []
inp = input("Enter your word in CAPITALS ")
for letter in inp:
    word.append(letter)
direction = input("In which direction should your word be? D R? ")


#CHECKS IF THE WORD FITS INSIDE THE BORDERS
def inp_modifier():
    global inp, word
    inp = input("Enter your word in CAPITALS ")
    word = list(inp)

if direction == "D":
    while len(word) > (16 - int(y)):
        print("Error, word colides with the border")
        inp_modifier()
if direction == "R":
    while len(word) > (16 - int(x)):
        print("Error, word colides with the border")
        inp_modifier()
        
        
#WRITES PLAYERS WORD
def word_word_coll():
    print("Error, please enter different coordinations that don't colide with other words")
    y = input("Enter Y coords of the start ")
    x = input("Enter X coords of the start ")

if direction == "D":
    p = 0
    q = 1
    for i in str(inp):
            arr[int(y)-1+p][int(x)-1] = word[q-1]
            p += 1
            q += 1
if direction == "R":
    p = 0
    q = 1
    for i in str(inp):
        while arr[int(y)-1][int(x)-1+p] in ["A", "B", "C", "D", "E", "F", "G", "H", "CH", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "X", "Y", "Z"]:
            word_word_coll()
        else:
            arr[int(y)-1][int(x)-1+p] = word[q-1]
            p += 1
            q += 1
                   
main_func()        







print("PLAYER 2")

y = input("Enter Y coords of the start ")
x = input("Enter X coords of the start ")

def coords_y_modifier():
    global y
    y = input("Enter Y coords of the start ")
def coords_x_modifier():
    global x 
    x = input("Enter X coords of the start ")

while int(y) not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]:
    print("Error, please enter number between 1 and 15")
    coords_y_modifier()
    
while int(x) not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]:
    print("Error, please enter number between 1 and 15")
    coords_x_modifier()

word = []
inp = input("Enter your word in CAPITALS ")
for letter in inp:
    word.append(letter)
direction = input("In which direction should your word be? D R? ")


#CHECKS IF THE WORD FITS INSIDE THE BORDERS
def inp_modifier():
    global inp, word
    inp = input("Enter your word in CAPITALS ")
    word = list(inp)

if direction == "D":
    while len(word) > (16 - int(y)):
        print("Error, word colides with the border")
        inp_modifier()
if direction == "R":
    while len(word) > (16 - int(x)):
        print("Error, word colides with the border")
        inp_modifier()


#WRITES PLAYERS WORD
if direction == "D":
    p = 0
    q = 1
    for i in str(inp):
            arr[int(y)-1+p][int(x)-1] = word[q-1]
            p += 1
            q += 1
if direction == "R":
    p = 0
    q = 1
    for i in str(inp):
        while arr[int(y)-1][int(x)-1+p] in ["A", "B", "C", "D", "E", "F", "G", "H", "CH", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "X", "Y", "Z"]:
            word_word_coll()
        else:
            arr[int(y)-1][int(x)-1+p] = word[q-1]
            p += 1
            q += 1
                   
main_func()        

    