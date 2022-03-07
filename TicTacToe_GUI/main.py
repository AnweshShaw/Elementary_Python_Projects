from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Tic_Tac_Toe")

moves_count = 0
switch_player = True

# Reset Button:
def reset():
    reset_button = Button(text="Reset", bd=5, highlightthickness=0)
    reset_button.place(x=130, y=265)
    global square_1,square_2,square_3,square_4,square_5,square_6,square_7,square_8,square_9,moves_count,switch_player
    moves_count = 0
    switch_player = True

# Disable the button:
def disable_buttons():
    square_1.config(state=DISABLED)
    square_2.config(state=DISABLED)
    square_3.config(state=DISABLED)
    square_4.config(state=DISABLED)
    square_5.config(state=DISABLED)
    square_6.config(state=DISABLED)
    square_7.config(state=DISABLED)
    square_8.config(state=DISABLED)
    square_9.config(state=DISABLED)

# Function to see if the game has been won
def is_game_won():
    global win
    win = False
    if square_1["text"] == "X" and square_2["text"] == "X" and square_3["text"] == "X":
        win = True
        square_1.config(bg="red")
        square_2.config(bg="red")
        square_3.config(bg="red")
        disable_buttons()
        messagebox.showinfo(title="Message",message="Congratulations!!! Player 1(X) won the game.")
    elif square_4["text"] == "X" and square_5["text"] == "X" and square_6["text"] == "X":
        win = True
        square_4.config(bg="red")
        square_5.config(bg="red")
        square_6.config(bg="red")
        disable_buttons()
        reset()
        messagebox.showinfo(title="Message",message="Congratulations!!! Player 1(X) won the game.")
    elif square_7["text"] == "X" and square_8["text"] == "X" and square_9["text"] == "X":
        win = True
        square_7.config(bg="red")
        square_8.config(bg="red")
        square_9.config(bg="red")
        disable_buttons()
        reset()
        messagebox.showinfo(title="Message",message="Congratulations!!! Player 1(X) won the game.")
    elif square_1["text"] == "X" and square_4["text"] == "X" and square_7["text"] == "X":
        win = True
        square_1.config(bg="red")
        square_4.config(bg="red")
        square_7.config(bg="red")
        disable_buttons()
        reset()
        messagebox.showinfo(title="Message",message="Congratulations!!! Player 1(X) won the game.")
    elif square_2["text"] == "X" and square_5["text"] == "X" and square_8["text"] == "X":
        win = True
        square_2.config(bg="red")
        square_5.config(bg="red")
        square_8.config(bg="red")
        disable_buttons()
        reset()
        messagebox.showinfo(title="Message",message="Congratulations!!! Player 1(X) won the game.")
    elif square_3["text"] == "X" and square_6["text"] == "X" and square_9["text"] == "X":
        win = True
        square_3.config(bg="red")
        square_6.config(bg="red")
        square_9.config(bg="red")
        disable_buttons()
        reset()
        messagebox.showinfo(title="Message",message="Congratulations!!! Player 1(X) won the game.")
    elif square_1["text"] == "X" and square_5["text"] == "X" and square_9["text"] == "X":
        win = True
        square_1.config(bg="red")
        square_5.config(bg="red")
        square_9.config(bg="red")
        disable_buttons()
        reset()
        messagebox.showinfo(title="Message",message="Congratulations!!! Player 1(X) won the game.")
    elif square_3["text"] == "X" and square_5["text"] == "X" and square_7["text"] == "X":
        win = True
        square_3.config(bg="red")
        square_5.config(bg="red")
        square_7.config(bg="red")
        disable_buttons()
        reset()
        messagebox.showinfo(title="Message",message="Congratulations!!! Player 1(X) won the game.")
    elif square_1["text"] == "O" and square_2["text"] == "O" and square_3["text"] == "0":
        win = True
        square_1.config(bg="red")
        square_2.config(bg="red")
        square_3.config(bg="red")
        disable_buttons()
        reset()
        messagebox.showinfo(title="Message",message="Congratulations!!! Player 2(O) won the game.")
    elif square_4["text"] == "O" and square_5["text"] == "O" and square_6["text"] == "O":
        win = True
        square_4.config(bg="red")
        square_5.config(bg="red")
        square_6.config(bg="red")
        disable_buttons()
        reset()
        messagebox.showinfo(title="Message",message="Congratulations!!! Player 2(O) won the game.")
    elif square_7["text"] == "O" and square_8["text"] == "0" and square_9["text"] == "O":
        win = True
        square_7.config(bg="red")
        square_8.config(bg="red")
        square_9.config(bg="red")
        disable_buttons()
        reset()
        messagebox.showinfo(title="Message",message="Congratulations!!! Player 2(O) won the game.")
    elif square_1["text"] == "O" and square_4["text"] == "O" and square_7["text"] == "O":
        win = True
        square_1.config(bg="red")
        square_4.config(bg="red")
        square_7.config(bg="red")
        disable_buttons()
        reset()
        messagebox.showinfo(title="Message",message="Congratulations!!! Player 2(O) won the game.")
    elif square_2["text"] == "O" and square_5["text"] == "O" and square_8["text"] == "O":
        win = True
        square_2.config(bg="red")
        square_5.config(bg="red")
        square_8.config(bg="red")
        disable_buttons()
        reset()
        messagebox.showinfo(title="Message",message="Congratulations!!! Player 2(O) won the game.")
    elif square_3["text"] == "O" and square_6["text"] == "O" and square_9["text"] == "O":
        win = True
        square_3.config(bg="red")
        square_6.config(bg="red")
        square_9.config(bg="red")
        disable_buttons()
        reset()
        messagebox.showinfo(title="Message",message="Congratulations!!! Player 2(O) won the game.")
    elif square_1["text"] == "O" and square_5["text"] == "O" and square_9["text"] == "O":
        win = True
        square_1.config(bg="red")
        square_5.config(bg="red")
        square_9.config(bg="red")
        disable_buttons()
        reset()
        messagebox.showinfo(title="Message",message="Congratulations!!! Player 2(O) won the game.")
    elif square_3["text"] == "O" and square_5["text"] == "O" and square_7["text"] == "O":
        win = True
        square_3.config(bg="red")
        square_5.config(bg="red")
        square_7.config(bg="red")
        disable_buttons()
        reset()
        messagebox.showinfo(title="Message",message="Congratulations!!! Player 2(O) won the game.")

# Working of X and O buttons
def click_button(button):
    global switch_player,moves_count
    if button["text"] =="" and switch_player == True:
        button["text"] = "X"
        switch_player = False
        moves_count += 1
        is_game_won()
        if moves_count == 9 and win ==False:
            messagebox.showinfo(title="Message",message="Try Again!!! It is a draw")
    elif button["text"] =="" and switch_player == False:
        button["text"] = "O"
        switch_player = True
        moves_count += 1
        is_game_won()
        if moves_count == 9 and win ==False:
            messagebox.showinfo(title="Message",message="Try Again!!! It is a draw")
    else:
        messagebox.showwarning(title="Warning",message="Error!!!, The square is already filled. Select any other square.")

canvas = Canvas(height=300, width=300, bg="black")
canvas.pack()


square_1 = Button(text="", highlightthickness=1,height=2,width=5,bd=5,font="bold",command=lambda:click_button(square_1))
square_1.place(x=45,y=40)
square_2 = Button(text="", highlightthickness=1,height=2,width=5,bd=5,font="bold",command=lambda:click_button(square_2))
square_2.place(x=120,y=40)
square_3 = Button(text="", highlightthickness=1,height=2,width=5,bd=5,font="bold",command=lambda:click_button(square_3))
square_3.place(x=195,y=40)
square_4 = Button(text="", highlightthickness=1,height=2,width=5,bd=5,font="bold",command=lambda:click_button(square_4))
square_4.place(x=45,y=115)
square_5 = Button(text="", highlightthickness=1,height=2,width=5,bd=5,font="bold",command=lambda:click_button(square_5))
square_5.place(x=120,y=115)
square_6 = Button(text="", highlightthickness=1,height=2,width=5,bd=5,font="bold",command=lambda:click_button(square_6))
square_6.place(x=195,y=115)
square_7 = Button(text="", highlightthickness=1,height=2,width=5,bd=5,font="bold",command=lambda:click_button(square_7))
square_7.place(x=45,y=190)
square_8 = Button(text="", highlightthickness=1,height=2,width=5,bd=5,font="bold",command=lambda:click_button(square_8))
square_8.place(x=120,y=190)
square_9 = Button(text="", highlightthickness=1,height=2,width=5,bd=5,font="bold",command=lambda:click_button(square_9))
square_9.place(x=195,y=190)
window.mainloop()
