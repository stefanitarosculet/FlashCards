from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
# Convert the dataframe to a dictionary using Pandas
data = pandas.read_csv("data/french_words.csv")
word= data.to_dict(orient="records")
current_card = {}

# The function will be used when called the button and will insert the random word into the canvas text field
def next_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(word)
    canvas.itemconfig(canvas_word, text = current_card["French"], fill = "black")
    canvas.itemconfig(canvas_language, text ="French", fill= "black")
    canvas.itemconfig(canvas_image, image = card_front)
    flip_timer= window.after(3000, func=flip_card)


#This function will be used to flip the card
def flip_card():
    canvas.itemconfig(canvas_word, text = current_card['English'], fill = "white")
    canvas.itemconfig(canvas_language, text = "English", fill = "white")
    canvas.itemconfig(canvas_image, image = card_back)

# def remove_word():
#     word.remove(current_card)


window = Tk()
window.title("Flash Cards")
window.config(padx =50, pady=50, bg = BACKGROUND_COLOR)
# This will introduce a 3 sec delay which will be used to flip the card
flip_timer = window.after(3000,func=flip_card)


card_front = PhotoImage(file = "images/card_front.png")
card_back = PhotoImage(file = "images/card_back.png")
correct_image = PhotoImage(file = "images/right.png")
wrong_image = PhotoImage(file= "images/wrong.png")

canvas = Canvas(width = 800, height = 560, bg = BACKGROUND_COLOR, highlightthickness = 0)
canvas_image = canvas.create_image(400, 265, image = card_front)
canvas_language = canvas.create_text(400, 150, text="", font= ("Ariel", 40, "italic"))
canvas_word = canvas.create_text(400, 263, text ="", font = ("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan = 2)


correct_button = Button(image=correct_image, highlightthickness = 0, command = next_word)
correct_button.grid(row=1, column=0)
wrong_button = Button(image= wrong_image, highlightthickness = 0, command = next_word)
wrong_button.grid(row=1, column=1)


next_word()
window.mainloop()

