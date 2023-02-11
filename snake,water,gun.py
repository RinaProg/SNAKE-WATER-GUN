import random

option=['snake','water','gun']

player_score=0
comp_score=0
print("Choose any of them : Snake , Water , Gun")
game=True
# user=input("Enter your name->\n")
while game:
    player=None
    comp = random.choice(option)
    
    while player not in option:
        try:
            
            player = input("enter your choise :\n")
            
        except EOFError as e:
            print(e)

        if player!='snake' and player !='water' and player!='gun':
            print("Invalid choice,try again.....")
            continue
        print(f"player : {player}")
        print(f"computer : {comp}")   
        if player == comp:
            print("Game Tie!")
        elif player == "snake" and comp =="water":
            print("you win")
            player_score+=1
        elif player == "water" and comp == "gun":
            print("you win")
            player_score+=1
        elif player == "gun" and comp == "snake":
            print("you win")
            player_score+=1

        else:
            print("you lose")
            comp_score+=1

        print(f"player score is : {player_score}")
        print(f"computer score is : {comp_score}")
    

    if not input("Do you want to play again?(y/n)\n").lower()=="y":
        game=False
if player_score>comp_score:
    print(f"Your score is: {player_score}")
    print("Congratulation! You win the game..") 
elif comp_score>player_score:
    print(f"Computer score is: {comp_score}")
    print("Computer win the game..")
else:
    print("Draw Match....")    

print("Thanks for playing.")
