import random

number = random.randint(0,3)

words = ["dog","cat","danny devito","toe"]
hint1 = ["bark","Meow","Short","on a foot"]
hint2 = ["bork","Kitty"," extreamly short"," has a nail"]

secretword = words[number]
guess = ""
counter = 1

while True:
    print("Guess my secret word!")
    print("Type 'hint1', 'hint2', 'first letter', or 'give up' for answer.")
    guess = input()

    if guess == secretword:
        print("You win?")
        print("It took you " + str(counter)+ " guesses.")
        break

    elif guess == "hint1":
        print( hint1[number] )

    elif guess == "hint2":
        print( hint2[number] )

    elif guess == "first letter":
        print( secretword[0] )

    elif guess == "give up":
        print("jeez I had faith in you but you let me down.")
        print("You failed " + str(counter) + " times.")
        break

    else:
        print("Try again or not it is your choice.")
        counter += 1

