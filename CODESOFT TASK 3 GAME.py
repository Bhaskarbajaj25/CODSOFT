import random

def computer():
    L=['rock','paper','scissor']
    a=str(random.choice(L))
    return(a)

def user():
    a=input("Enter your choice : 1. Rock  2. Paper  3. Scissor  4. Quit:  ")
    if a.lower() not in ["rock","paper","scissor","quit"]:
        return "Invalid"
    else:
        return (a.lower())

def game():
    c,u=0,0
    while True:
        
        m=computer()
        n=user()
        if m==n:
            print("COMPUTER: ", m)
            print("YOUR:", n)
            print("It's a tie")
        elif (n == "rock" and m == "scissor") or(n == "scissor" and m == "paper") or(n == "paper" and m == "rock"):
            print("COMPUTER: ", m)
            print("YOUR:", n)
            print("You win!")
            u+= 1
        elif n=='quit':
            break
        else:
            print("COMPUTER: ", m)
            print("YOUR:", n)
            print("Sorry Computer wins this time!")
            c+= 1
        
        print("Your Score: ",u,", Computer Score: ",c)
    
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

    print("Thanks for playing")

game()    
