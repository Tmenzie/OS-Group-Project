from tkinter import *
from PIL import Image, ImageTk

#Creating the main window
mainPanel = Tk()
mainPanel.title("Rock Paper Scissors")
mainPanel.geometry("500x400")
var = IntVar()

#Loading the images

#setting the choice
def select():
    if var.get() == 1:
        choice = "rock"
    elif var.get() == 2:
        choice = "paper"
    elif var.get() == 3:
        choice = "scissors"

    #Displaying choice on screen
    selection = "You choose " + choice
    label.config(text = selection)

#Send choice to server
def buttonPush():
    
    #send choice to server
    top= Toplevel(mainPanel)
    top.geometry("275x125")
    top.title("Results")

    playerResults = 1

    if (playerResults == "Winner"):
        result = "You won!"
    else:
        result = "You lost!"
    Label(top, text= result).pack()


#Rock button
rock_pic = PhotoImage("/Rock.png")
R1 = Radiobutton(mainPanel, image=rock_pic, variable=var, value=1, command=select)
R1.image = rock_pic
R1.pack()

#Paper button
paper_pic = PhotoImage("/Scissors.png")
R2 = Radiobutton(mainPanel, image=paper_pic, variable=var, value=2, command=select)
R2.image = paper_pic
R2.pack()


#Scissors button
scissor_pic = PhotoImage("/Scissors.png")
R3 = Radiobutton(mainPanel, image=scissor_pic, variable=var, value=3, command=select)
R3.image = scissor_pic
R3.pack()

#Submit button
B = Button(text ="Submit", command = buttonPush)



#packing panels to the main window
label = Label(mainPanel)
label.pack()
B.pack()
mainPanel.mainloop()