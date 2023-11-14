from tkinter import*
from PIL import Image,ImageTk
from random import randint

#main window
root = Tk()
root.title("Rock Scissor Paper")
root.configure(background="light blue")

#picture
rock_img = ImageTk.PhotoImage(Image.open("rock-user.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper-user.png"))
scissor_img = ImageTk.PhotoImage(Image.open("scissors-user.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("scissors.png"))

#insert picture

user_label = Label(root, image=scissor_img, bg="light blue")
comp_label = Label(root, image=scissor_img_comp, bg="light blue")
user_label.grid(row=1, column=4)
comp_label.grid(row=1, column=0)


#scores
playerScore = Label(root, text=0, font=100, bg="light blue", fg="red")
computerScore = Label(root, text=0, font=100, bg="light blue", fg="red")
playerScore.grid(row=1, column=3)
computerScore.grid(row=1, column=1) 

#buttons
rock = Button(root,width=20,height=2,text="ROCK",bg="red",fg="white", command = lambda: updateChoice("rock"))
paper = Button(root,width=20,height=2,text="PAPER",bg="green",fg="white", command = lambda: updateChoice("paper"))
scissor = Button(root,width=20,height=2,text="SCISSOR",bg="blue",fg="white", command = lambda: updateChoice("scissor"))
rock.grid(row=2,column=1)
paper.grid(row=2,column=2)
scissor.grid(row=2,column=3)

#indicators
user_indicator = Label(root, font=50,text="USER",bg="black", fg="red")
computer_indicator = Label(root, font=50,text="COMPUTER",bg="black", fg="red")
user_indicator.grid(row=0, column=3)
computer_indicator.grid(row=0, column=1)

#messages
msg = Label(root, font=50,bg="red",fg="white")
msg.grid(row=3, column=2)

#update message
def updateMessage(x):
    msg['text'] = x

#update user score
def updateUserScore():
    score = int(playerScore["text"])
    score += 1
    playerScore["text"] = str(score)

#update computer score
def updateCompScore():
    score = int(computerScore["text"])
    score += 1
    computerScore["text"] = str(score) 

#check winner
def checkWin(player,computer):
    if player == computer:
        updateMessage("Its a tie!!!")
    elif player == "rock":
        if computer == "paper":
            updateMessage("You lose")
            updateCompScore()
        else:
            updateMessage("You win")
            updateUserScore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("You lose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    elif player == "scissor":
        if computer == "rock":
            updateMessage("You lose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    else:
        pass
   
#updates choices
choices = ["rock","paper","scissor"]
def updateChoice(x):
    
 #for computer
    compChoice = choices[randint(0,2)]
    if compChoice == "rock":
        comp_label.configure(image=rock_img_comp) 
    elif compChoice == "paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)
    
#for user
    if x=="rock":
        user_label.configure(image=rock_img)
    elif x=="paper":
         user_label.configure(image=paper_img)
    else:
         user_label.configure(image=scissor_img)
         
    checkWin(x,compChoice)


root.mainloop()
