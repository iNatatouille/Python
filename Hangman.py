import random

attempts = 10

words = [
    "Hero",
    "Keyboard",
    "Silent",
    "Memory",
    "Hangman",
    "Funny",
    "Joker",
    "Inquisitive",
    "Phenomenal"
]

chosenWord = words[random.randint(0,len(words)-1)].upper()

wordLength = len(chosenWord)

current = ""

for i in range(0,wordLength):
    current += "_ "
    
print(current)

usedChars = []
answerArray = list(chosenWord)
emptyArray = []
for i in range(0,len(answerArray)):
    emptyArray.append(" ")
won = False
while not won:
    
    while True:
        
        guess = input("Guess: ").upper()
        if len(guess) != 1:
            print("Enter only 1 character.")
        elif guess in usedChars:
            print("You have already used this character.")
        else:
            break
        
    usedChars.append(guess)
    
    # Check if letter is in word
    correct = False
    while guess in answerArray:
        correct = True
        position = answerArray.index(guess)
        answerArray[position] = " "
        emptyArray[position] = guess

    if not correct:
        attempts -= 1
    
    # Convert to string
    current = ""
    for i in range(0,len(emptyArray)):
        if emptyArray[i] == " ":
            current += "_ "
        else:
            current += emptyArray[i] + " "
            
    print(current)
    print("Attempts: " + str(attempts))
    
    if attempts == 0:
        print("You lose!")
        won = True
    
    won = True
    for i in range(len(emptyArray)):
        if emptyArray[i] == " ":
            won = False
    if won:
        print("You won!")

