from tkinter import *

#Creating the main window
mainPanel = Tk()
mainPanel.title("Rock Paper Scissors")
mainPanel.geometry("275x125")
var = IntVar()

#setting the choice
def sel():
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
    # Send the choice to server and recive results


    #send choice to server

    #Creates Panel
    top= Toplevel(mainPanel)
    top.geometry("275x125")
    top.title("Results")

    # getGameResults = playerResult 
    playerResults = 1

    if (playerResults == 1):
        result = "You won!"
    else:
        result = "You lost!"
    Label(top, text= result).pack()


#Rock button
R1 = Radiobutton(mainPanel, text="Rock", variable=var, value=1, command=sel)
R1.pack( anchor = W )

#Paper button
R2 = Radiobutton(mainPanel, text="Paper", variable=var, value=2, command=sel)
R2.pack( anchor = W )

#Scissors button
R3 = Radiobutton(mainPanel, text="Scissors", variable=var, value=3, command=sel)
R3.pack( anchor = W)

#Submit button
B = Button(text ="Submit", command = buttonPush)

#packing panels to the main window
label = Label(mainPanel)
label.pack()
B.pack()
mainPanel.mainloop()