from tkinter import *
import tkinter.messagebox
tk = Tk()
tk.title("Tic Tac Toe")

turn = True #boolean variable to indicate player turn

def checker(buttons):
    global turn
    if buttons["text"] == " " and turn == True:
        buttons["text"] = "X"
        turn = False
    elif buttons["text"] == " " and turn == False:
        buttons["text"] = "O"
        turn = True
    winner()
    
def winner():
    if(button11["text"] == "X" and button12["text"] == "X" and button13["text"] == "X" or
         button21["text"] == "X" and button22["text"] == "X" and button23["text"] == "X" or
         button31["text"] == "X" and button32["text"] == "X" and button33["text"] == "X" or
         button11["text"] == "X" and button21["text"] == "X" and button31["text"] == "X" or
         button12["text"] == "X" and button22["text"] == "X" and button32["text"] == "X" or
         button13["text"] == "X" and button23["text"] == "X" and button23["text"] == "X" or
         button11["text"] == "X" and button22["text"] == "X" and button33["text"] == "X" or
         button13["text"] == "X" and button12["text"] == "X" and button31["text"] == "X"):
        tkinter.messagebox.showinfo("Game Over", "Winner is X!")

    elif(button11["text"] == "O" and button12["text"] == "O" and button13["text"] == "O" or
         button21["text"] == "O" and button22["text"] == "O" and button23["text"] == "O" or
         button31["text"] == "O" and button32["text"] == "O" and button33["text"] == "O" or
         button11["text"] == "O" and button21["text"] == "O" and button31["text"] == "O" or
         button12["text"] == "O" and button22["text"] == "O" and button32["text"] == "O" or
         button13["text"] == "O" and button23["text"] == "O" and button23["text"] == "O" or
         button11["text"] == "O" and button22["text"] == "O" and button33["text"] == "O" or
         button13["text"] == "O" and button12["text"] == "O" and button31["text"] == "O"):
        tkinter.messagebox.showinfo("Game Over", "Winner is O!")

button11 = Button(tk, text = " ", font = ('Times 26 bold'), height = 4, width = 8, command = lambda:checker(button11))
button11.grid(row = 0, column = 0, sticky = S+N+E+W)

button12 = Button(tk, text = " ", font = ('Times 26 bold'), height = 4, width = 8, command = lambda:checker(button12))
button12.grid(row = 0, column = 1, sticky = S+N+E+W)

button13 = Button(tk, text = " ", font = ('Times 26 bold'), height = 4, width = 8, command = lambda:checker(button13))
button13.grid(row = 0, column = 2, sticky = S+N+E+W)                                     

button21 = Button(tk, text = " ", font = ('Times 26 bold'), height = 4, width = 8, command = lambda:checker(button21))
button21.grid(row = 1, column = 0, sticky = S+N+E+W)

button22 = Button(tk, text = " ", font = ('Times 26 bold'), height = 4, width = 8, command = lambda:checker(button22))
button22.grid(row = 1, column = 1, sticky = S+N+E+W)                                    
         
button23 = Button(tk, text = " ", font = ('Times 26 bold'), height = 4, width = 8, command = lambda:checker(button23))
button23.grid(row = 1, column = 2, sticky = S+N+E+W)

button31 = Button(tk, text = " ", font = ('Times 26 bold'), height = 4, width = 8, command = lambda:checker(button31))
button31.grid(row = 2, column = 0, sticky = S+N+E+W)

button32 = Button(tk, text = " ", font = ('Times 26 bold'), height = 4, width = 8, command = lambda:checker(button32))
button32.grid(row = 2, column = 1, sticky = S+N+E+W)

button33 = Button(tk, text = " ", font = ('Times 26 bold'), height = 4, width = 8, command = lambda:checker(button33))
button33.grid(row = 2, column = 2, sticky = S+N+E+W)

tk.mainloop()
