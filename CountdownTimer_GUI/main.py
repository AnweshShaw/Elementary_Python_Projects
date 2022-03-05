from tkinter import *
from tkinter import messagebox
import math

FONT_NAME = "Courier"
timer = None
RED = "#e7305b"
GREEN = "#006400"

# Resetting Timer
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    checkmark.config(text="")

# Working of Countdown
def countdown(count):
    min_count = math.floor(count / 60)
    sec_count = count % 60
    if min_count < 10:
        min_count = f"0{min_count}"
    if sec_count < 10:
        sec_count = f"0{sec_count}"
    canvas.itemconfig(timer_text, text=f"{min_count}:{sec_count}")
    print(count)
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        messagebox.showinfo(title="Message", message="Time is up!!!")
        checkmark.config(text="Time Up ✔", fg=GREEN)
        checkmark.place(x=110, y=300)


# Creating UI
window = Tk()
window.title("Countdown Timer ")
title_label = Label(text="Timer", fg=RED, font=(FONT_NAME, 20, "bold"))
title_label.place(x=100, y=0)

canvas = Canvas(width=400, height=450, bg="cyan")
clock_img = PhotoImage(file="image__3_-removebg-preview.png")
canvas.create_image(200, 200, image=clock_img)
timer_text = canvas.create_text(200, 190, text="00:00", fill="red2", font=(FONT_NAME, 60, "bold"))
canvas.pack()

label = Label(text="MIN: ",bg="cyan",font="bold")
label.place(x=40, y=38)
label2 = Label(text="SEC: ",bg="cyan",font="bold")
label2.place(x=180, y=38)
label3 = Label(text="SET TIME :",bg="cyan",font="bold")
label3.place(x=150,y=1)
start_button = Button(text="Start ", highlightthickness=0,bd=5)
start_button.place(x=100, y=370)
spin = Spinbox(window,from_=0,to_=60,width=10)
spin.place(x=95, y=43)
spin2 = Spinbox(window, from_=0, to_=60, width=10)
spin2.place(x=235, y=43)

def click():
    MIN = int(spin.get())
    SEC = int(spin2.get())

    # Timer functioning
    def start_timer():
        countdown(int(MIN * 60)+SEC)
        checkmark.config(text="")

    start_button = Button(text="Start ", highlightthickness=0, command=start_timer, bd=5)
    start_button.place(x=100, y=370)

submit_button = Button(text="Submit", highlightthickness=0, command=click)
submit_button.place(x=320, y=40)
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer, bd=5)
reset_button.place(x=250, y=370)
checkmark = Label(text="Time Up ✔", fg=GREEN, font=("Algerian", 30, "bold"))

window.mainloop()
