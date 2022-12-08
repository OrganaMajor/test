from tkinter import *
import random

screen = Tk()
screen.geometry("360x250")
#x = int(E.get())

possibleAction = ['rock', 'paper', 'scissors']
computerAction = random.choice(possibleAction)
scoreUser = 0
scoreComputer = 0
#txt = "computer chose"

def rock(e):
    L1.config(text= "rock")
    L2.config(text=str(random.choice(possibleAction)))

def paper(e):
    L1.config(text= "paper")
    L2.config(text=str(random.choice(possibleAction)))

def scissors(e):
    L1.config(text= "scissors")
    L2.config(text=str(random.choice(possibleAction)))

"""def UserScore():
    global scoreUser
    scoreUser +=1
    return scoreUser"""


def game():
    for i in range (10):
        
        if l1 == l2:
            l5.config(text='Same choice, no winner')
            #text.set("Same choice, no winner")
            #print('Your score =', scoreUser, 'computer score =', scoreComputer)

        elif l1 == 'rock':
            if l2 == 'paper':
                l5.config(text='Paper covers rock. You lose')
                scoreComputer +=1
                #print('Your score =', scoreUser, 'computer score =', scoreComputer)
            elif l2 == 'scissors':
                l5.config(text='Rock smashes scissors. You win')
                scoreUser +=1
                #print('Your score =', scoreUser, 'computer score =', scoreComputer)

        elif l1 == 'paper':
            if l2 == 'rock':
                l5.config(text='Paper covers rock. You win')
                scoreUser +=1
                #print('Your score =', scoreUser, 'computer score =', scoreComputer)
            elif l2 == 'scissors':
                l5.config(text='Scissors cut paper. You lose')
                scoreComputer +=1
                #print('Your score =', scoreUser, 'computer score =', scoreComputer)

        elif l1 == 'scissors':
            if l2 == 'paper':
                l5.config(text='Scissors cut paper. You win')
                scoreUser +=1
                #print('Your score =', scoreUser, 'computer score =', scoreComputer)
            elif l2 == 'rock':
                l5.config(text='Rock smashes scissors. You lose')
                scoreComputer +=1
                #print('Your score =', scoreUser, 'computer score =', scoreComputer)


B1 = Button(text= "Rock", width= 10, font=10, pady=5, command=game)
B1.bind("<Button-1>", rock)
B1.grid(row=1, column=0)

B2 = Button(text= "Paper", width= 10, font=10, pady=5, command=game)
B2.bind("<Button-1>", paper)
B2.grid(row=1, column=1)

B3 = Button(text= "Scissors", width= 10, font=10, pady=5, command=game)
B3.bind("<Button-1>", scissors)
B3.grid(row=1, column=2)

l1= Label(screen, text="you chose" )
l1.grid(row=2, columnspan=3)
L1= Label(screen, text="")
L1.grid(row=3, columnspan=3)

l2= Label(screen, text="computer chose")
l2.grid(row=4, column=0, columnspan=3)
L2= Label(screen, text="")
L2.grid(row=5, columnspan=3)
 

L3= Label(screen, text="User Score:")
L3.grid(row=7, column=0)
l3= Label(screen, text=scoreUser)
l3.grid(row=8, column=0)

L4= Label(screen, text="Computer Score:")
L4.grid(row=7, column=2)
l4= Label(screen, text=scoreComputer)
l4.grid(row=8, column=2)


l5= Label(screen, text="")
l5.grid(row=6, columnspan=3)

screen.mainloop()


"""
if scoreUser > scoreComputer:
    print("You have won the game")
elif scoreComputer > scoreUser:
    print("Computer has won the game")
else :
    print("Same score: it's a tie lol!")
"""
