from random import *
import pandas

FONT_NAME = "Courier"
Green = '#B1DDC6'
from tkinter import *

# --------DataBase_--------
try:
    word_to_learn_data = pandas.read_csv('word_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv('database.csv',)
    word_to_learn_data_dic = original_data.to_dict(orient='records')
else:
    word_to_learn_data_dic = word_to_learn_data.to_dict(orient='records')




def next_card():
    global number, flip, current
    myscreen.after_cancel(flip)
    current = choice(word_to_learn_data_dic)
    card_canvas.itemconfig(card_display, image=card_front)
    card_canvas.itemconfig(title, fill=Green, text='Arabic')
    card_canvas.itemconfig(word, text=current['arabic'], fill=Green)
    card_canvas.itemconfig(pronunciation, text=current['pronunciate'])
    flip = myscreen.after(3000, translation)


def translation():
    card_canvas.itemconfig(title, fill='white', text='English')
    card_canvas.itemconfig(card_display, image=card_back)
    card_canvas.itemconfig(word, text=current['english'], fill='white')
    card_canvas.itemconfig(pronunciation, text='')


def remove():

    word_to_learn_data_dic.remove(current)
    data = pandas.DataFrame(word_to_learn_data_dic)
    data.to_csv('word_to_learn.csv',index = False)
    next_card()

# -----------UI-------------
myscreen = Tk()
myscreen.title('Learning Arabic Flash Card')
flip = myscreen.after(3000, translation)
myscreen.config(pady=30, padx=30, bg=Green)
card_canvas = Canvas(width=800, height=526, bg=Green, highlightthickness=0)
card_front = PhotoImage(file='images/card_front.png')
card_back = PhotoImage(file='images/card_back.png')
card_display = card_canvas.create_image(400, 262, image=card_front, )
title = card_canvas.create_text(400, 100, text='', fill=Green, font=(FONT_NAME, 35, 'italic'))
word = card_canvas.create_text(400, 300, text='', fill=Green, font=(FONT_NAME, 60, 'bold'))
pronunciation = card_canvas.create_text(400, 430, text='Arabic', fill=Green, font=(FONT_NAME, 60, 'italic'))
card_canvas.grid(column=0, row=0, columnspan=3)
# alternatively you could create an empty dictionary and use random.choice(list_data) to get the random dictionary
# in the list_data ...

current = {}
check_image = PhotoImage(file='images/right.png')
check_button = Button(image=check_image, highlightthickness=0, command=remove, )
check_button.grid(column=2, row=2)
cancel_image = PhotoImage(file='images/wrong.png', )
cancel_button = Button(image=cancel_image, highlightthickness=0, command=next_card)
cancel_button.grid(column=0, row=2)
next_card()

myscreen.mainloop()
