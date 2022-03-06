from tkinter import *
import math

window = Tk()
window.title("Calculator ")

canvas = Canvas(height=420, width=300, bg="black")
canvas.pack()
value = StringVar()
value.set("")
entry = Entry(textvar=value, font=("Arial", 15, "bold"), width=23, borderwidth=4)
entry.place(x=20, y=70)

# Click Numbers Button
def click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))

# Clear Button
def clear():
    entry.delete(0, END)

# Add Button
def add():
    num = entry.get()
    global num1, calculation
    calculation = "add"
    num1 = int(num)
    clear()

# Subtract Button
def subtract():
    num = entry.get()
    global num1, calculation
    calculation = "sub"
    num1 = int(num)
    clear()

# Multiply Button
def multiply():
    num = entry.get()
    global num1, calculation
    calculation = "mul"
    num1 = int(num)
    clear()

# Divide Button
def divide():
    num = entry.get()
    global num1, calculation
    calculation = "div"
    num1 = int(num)
    clear()

# Modulus Button
def modulus():
    num = entry.get()
    global num1, calculation
    calculation = "mod"
    num1 = int(num)
    clear()

# Square Root Button
def square_root():
    num = entry.get()
    global num1, calculation
    calculation = "root"
    num1 = float(num)
    clear()
    num1 = math.sqrt(num1)
    entry.insert(0, num1)

# Equal to Button
def equal():
    sec_no = entry.get()
    clear()
    num2 = int(sec_no)
    if calculation == "add":
        entry.insert(0, num1 + num2)
    if calculation == "sub":
        entry.insert(0, num1 - num2)
    if calculation == "mul":
        entry.insert(0, num1 * num2)
    if calculation == "div":
        entry.insert(0, int(num1 / num2))
    if calculation == "mod":
        entry.insert(0, num1 % num2)


clear_button = Button(text=" C ", highlightthickness=0, bd=5, height=1, width=4, font="bold", command=clear)
clear_button.place(x=20, y=120)
plusminus_button = Button(text=" √ ", highlightthickness=0, bd=5, height=1, width=4, font="bold"
                          ,command=square_root)
plusminus_button.place(x=90, y=120)
modulus_button = Button(text=" % ", highlightthickness=0, bd=5, height=1, width=4, font="bold"
                        ,command=modulus)
modulus_button.place(x=160, y=120)
divide_button = Button(text=" / ", highlightthickness=0, bd=5, height=1, width=4, bg="orange", font="bold"
                       , command=divide)
divide_button.place(x=230, y=120)

# Remember the lambda function which allows us to pass parameters as args which are not allowed generally.

button_7 = Button(text=" 7 ", highlightthickness=0, bd=5, height=1, width=4, font="bold", command=lambda: click(7))
button_7.place(x=20, y=180)
button_8 = Button(text=" 8 ", highlightthickness=0, bd=5, height=1, width=4, font="bold", command=lambda: click(8))
button_8.place(x=90, y=180)
button_9 = Button(text=" 9 ", highlightthickness=0, bd=5, height=1, width=4, font="bold", command=lambda: click(9))
button_9.place(x=160, y=180)
multiply_button = Button(text=" X ", highlightthickness=0, bd=5, height=1, width=4, bg="orange", font="bold"
                         , command=multiply)
multiply_button.place(x=230, y=180)
button_4 = Button(text=" 4 ", highlightthickness=0, bd=5, height=1, width=4, font="bold", command=lambda: click(4))
button_4.place(x=20, y=240)
button_5 = Button(text=" 5 ", highlightthickness=0, bd=5, height=1, width=4, font="bold", command=lambda: click(5))
button_5.place(x=90, y=240)
button_6 = Button(text=" 6 ", highlightthickness=0, bd=5, height=1, width=4, font="bold", command=lambda: click(6))
button_6.place(x=160, y=240)
subtract_button = Button(text=" - ", highlightthickness=0, bd=5, height=1, width=4, bg="orange", font="bold",
                         command=subtract)
subtract_button.place(x=230, y=240)
button_1 = Button(text=" 1 ", highlightthickness=0, bd=5, height=1, width=4, font="bold", command=lambda: click(1))
button_1.place(x=20, y=300)
button_2 = Button(text=" 2 ", highlightthickness=0, bd=5, height=1, width=4, font="bold", command=lambda: click(2))
button_2.place(x=90, y=300)
button_3 = Button(text=" 3 ", highlightthickness=0, bd=5, height=1, width=4, font="bold", command=lambda: click(3))
button_3.place(x=160, y=300)
add_button = Button(text=" + ", highlightthickness=0, bd=5, height=1, width=4, bg="orange", font="bold", command=add)
add_button.place(x=230, y=300)
button_0 = Button(text=" 0 ", highlightthickness=0, bd=5, height=1, width=8, font="bold", command=lambda: click(0))
button_0.place(x=20, y=360)
decimal_button = Button(text=" . ", highlightthickness=0, bd=5, height=1, width=6, font="bold")
decimal_button.place(x=135, y=360)
equal_button = Button(text=" = ", highlightthickness=0, bd=5, height=1, width=4, bg="orange", font="bold",
                      command=equal)
equal_button.place(x=230, y=360)

window.mainloop()
