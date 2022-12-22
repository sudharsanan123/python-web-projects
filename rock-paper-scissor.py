from random import randint
moves=["rock","paper","scissors"]
while True:
    computer=moves[randint(0,2)]
    player=input("rock, paper or scissors? (or end the game)").lower()
    if player=="end the game":
        print("The game is ended")
        break
    elif player==computer:
        print("Tie!!")
    elif player=="rock":
        if computer=="paper":
            print("You Lose!!",computer,"beats",player)
        else:
            print("you Win",player,"beats",computer)
    elif player=="paper":
        if computer=="scissors":
            print("You Lose!!",computer,"beats",player)
        else:
            print("You Win!!",player,"beasts",computer)
    elif player=="scissors":
        if computer=="rock":
            print("You lose",computer,"beasts",player)
        else:
            print("You Win!",player,"beast",computer)
    else:
        print("Check your spelling")

