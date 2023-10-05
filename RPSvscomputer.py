from random import randint
#needed in order to randomise the input of computer each time 

print("Welcome to the Ultimate Rock, Paper, Scissors Game \n I hope you are ready \n...ROCK...\n...PAPER...\n...SCISSORS...")
Player1 = input("(enter Player 1's choice):")
Computer = randint(1,3)
print("Shoot!!!!")
if randint == 1:
    Computer = "rock"
elif randint == 2:
    Computer = "paper" 
else:
    Computer = "scissors"
#f string allows you to write a string that contains a value/str
print(f"Computer plays {Computer}" )
#
if Player1 == Computer: 
        print("You are as smart as a computer , Its a tie")
elif Player1 == "rock": 
    if Computer == "scissors":
        print("You win")
    elif Computer == "paper":
        print("Computer wins")
elif Player1 == "paper": 
    if Computer == "scissors":
        print("Computer wins")
    elif Computer == "rock":
        print("Player 1 wins")  
elif Player1 == "paper": 
    if Computer == "scissors":
        print("Computer wins")
    elif Computer == "rock":
        print("Player 1 wins") 

else: print("Something went wrong")
