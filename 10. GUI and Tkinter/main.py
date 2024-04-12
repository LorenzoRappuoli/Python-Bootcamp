from tkinter import *

def button_pressed():
    nt = inp.get()
    cal = float(nt)*1.6
    t4.config(text=str(cal))

window = Tk()
window.title("Miles to km")
window.minsize(250, 150)
window.config(padx=10, pady=10)


inp = Entry(window)
inp.grid(column = 2, row = 1)

t = Label(window, text="Miles", font=("Arial", 15, "bold"))
t.grid(column = 3, row = 1)

t2 = Label(window, text="Is equal to", font=("Arial", 15, "bold"))
t2.grid(column = 1, row = 2)

t3 = Label(window, text="KM", font=("Arial", 15, "bold"))
t3.grid(column = 3, row = 2)

t4 = Label(window, text="", font=("Arial", 15, "bold"))
t4.grid(column = 2, row = 2)

# Button
button = Button(window, text="Calculate", command=button_pressed)
button.grid(column = 2, row = 3)

mainloop()