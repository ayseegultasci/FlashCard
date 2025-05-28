from gettext import textdomain
from tkinter import  *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
learn = {}
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/Words - Sayfa1.csv")
    learn = original_data.to_dict(orient="records")
else:
    learn = data.to_dict(orient="records")


def next_Card():
    global current_card, timer
    window.after_cancel(timer)
    current_card = random.choice(learn)
    canvas.itemconfig(card_title, text="English", fill= "black")
    canvas.itemconfig(card_word, text=current_card["English"], fill= "black")
    canvas.itemconfig(card_bg, image=card_front_img)
    timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="Türkçe", fill= "white")
    canvas.itemconfig(card_word, text=current_card["Türkçe"],fill= "white")
    canvas.itemconfig(card_bg, image=card_back_img)

def is_known():
    learn.remove(current_card)
    next_Card()
    data = pandas.DataFrame(learn)
    data.to_csv("data/words_to_learn.csv", index=False)
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer = window.after(4000, func=flip_card)
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_bg = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"), fill="black")
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"), fill="black")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, borderwidth=0, relief="flat", command=next_Card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, borderwidth=0, relief="flat", command=is_known)
known_button.grid(row=1, column=1)
next_Card()
window.mainloop()

