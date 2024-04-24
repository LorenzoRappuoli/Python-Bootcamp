from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():

    window.after_cancel(timer)
    canvas.itemconfig(canvas_label, text="start!")
    canvas.itemconfig(canvas_timer, text = "00:00")
    canvas.itemconfig(canvas_label_2, text="")

    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

# Timer Mechanism
def start_timer():
    global reps
    reps += 1

    # Work interval
    work_interval = WORK_MIN * 60

    # Short break
    short_interval = SHORT_BREAK_MIN * 60

    # Long break
    long_interval = LONG_BREAK_MIN * 60

    if reps % 8 == 0 and reps != 0:  # Long break
        count_down(long_interval)
        canvas.itemconfig(canvas_label, text="Long Pause")

    elif reps % 2 == 0:  # Short break
        count_down(short_interval)
        canvas.itemconfig(canvas_label, text="Short Pause")

    else:  # Work time
        if reps > 1:
            canvas.itemconfig(canvas_label_2, text="✓")
        count_down(work_interval)
        canvas.itemconfig(canvas_label, text="Work Time")





# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):

    canvas.itemconfig(canvas_timer, text = count)

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)

    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
FONT_NAME = "Arial"
window = Tk()
window.title("Pomodoro")
window.config(padx=10, pady=10)  # Aggiunge spaziatura intorno alla finestra
window.geometry("300x400")

# Canvas
canvas = Canvas(window, width=300, height=300)  # Aumenta le dimensioni del canvas
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(150, 150, image=tomato_img)  # Posiziona l'immagine al centro del canvas
canvas_timer = canvas.create_text(150, 150, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))  # Posiziona il testo al centro sopra l'immagine
canvas.grid(column=1, row=2, columnspan=3)  # Estende il canvas sulle tre colonne
canvas_label = canvas.create_text(150, 200, text="start!", fill="white", font=(FONT_NAME, 15, "bold"))
canvas_label_2 = canvas.create_text(150, 220, text="", fill="green", font=(FONT_NAME, 10))


# Labels
t1 = Label(window, text="Tomato timer", font=(FONT_NAME, 20, "bold"))
t1.grid(column=1, row=1, columnspan=3)  # Estende l'etichetta sulle tre colonne

# Buttons
button1 = Button(window, text="Start", command=start_timer)
button1.grid(column=1, row=3)

button3 = Button(window, text="Reset")
button3.config(command=reset_timer)  # Associa la funzione reset_timer() al pulsante
button3.grid(column=3, row=3)

window.mainloop()