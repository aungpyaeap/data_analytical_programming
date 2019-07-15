import functions

from tkinter import *
from tkinter import messagebox

background_color = "lightblue"

window = Tk()
window.title("Natural Processed English Spelling Check")
window.configure(background=background_color)

FullScreenApp(window)


Label(window, text="STEP 1: SENTENCE CONFIGURATION", font="arial 12", fg = "black", bg = background_color).grid(columnspan = 1, sticky='W')
textbox1 = Text(window, height = 7, width = 80, wrap="word")
textbox1.config(font='arial')
textbox1.grid(row=1, column=0)

for i in range(1):
    gridframe = Frame(window)
    #Label(gridframe, text="Only English characters are allowed.", font='times 12', fg="blue4").pack(side=LEFT)
    Button(gridframe, text='START', font='arial', background='Orange', width = 10, command=start).pack(side=LEFT)
    Label(gridframe, text="-", font='arial 12', fg="blue4").pack(side=LEFT)
    Button(gridframe, text='CLEAR', font='arial', background='Orange', width = 10, command=exit).pack(side=LEFT)
    Label(gridframe, text="-", font='arial 12', fg="blue4").pack(side=LEFT)
    Button(gridframe, text='RESET', font='arial', background='Orange', width = 10, command=donothing).pack(side=LEFT)
    gridframe.grid(row=2, column=0, sticky= E)

Label(window, text="STEP 2: ERROR DETECTION ANALYSIS", font="arial 12", fg = "black", bg = background_color).grid(columnspan = 1, sticky='W')
textbox2 = Text(window, height = 7, width = 80, wrap="word")
#textbox2.insert('end', 'new material to insert', ('highlightline', 'recent', 'warning'))
#textbox2.tag_configure('highlightline', background='yellow', relief='raised')
textbox2.config(font='arial')

textbox2.grid(row=4, column=0)

for i in range(1):
    gridframe = Frame(window)
    Button(gridframe, text='AUTO NLP', font='arial', background='Orange', width = 10, command=auto_nlp).pack(side=LEFT)
    Label(gridframe, text="-", font='arial 12', fg="blue4").pack(side=LEFT)
    Button(gridframe, text='COPY', font='arial', background='Orange', width = 10, command=donothing).pack(side=LEFT)
    Label(gridframe, text="-", font='arial 12', fg="blue4").pack(side=LEFT)
    Button(gridframe, text='CLEAR', font='arial', background='Orange', width = 10, command=donothing).pack(side=LEFT)
    gridframe.grid(row=5, column=0, sticky= E)

Label(window, text="STEP 3: AUTO CORRECTION", font="arial 12", fg = "black", bg = background_color).grid(columnspan = 1, sticky='W')
textbox3 = Text(window, height = 7, width = 80, wrap="word")
textbox3.config(font='arial')
textbox3.grid(row=7, column=0)

for i in range(1):
    gridframe = Frame(window)
    Button(gridframe, text='BIGRAM', font='arial', background='Orange', width = 10, command=show_bigram).pack(side=LEFT)
    Label(gridframe, text="-", font='arial 12', fg="blue4").pack(side=LEFT)
    Button(gridframe, text='RESET', font='arial', background='Orange', width = 10, command=donothing).pack(side=LEFT)
    gridframe.grid(row=8, column=0, sticky= E)

################################################# RIGHT PANEL

Label(window, text=" ", bg=background_color).grid(row=2, column=1)

for i in range(1):
    gridframe = Frame(window)
    Label(gridframe, text="TOKEN LENGTH\n0", font='arial 12', fg="blue4").pack(side=TOP)
    Label(gridframe, text="WORD LENGTH\n0", font='arial 12', fg="blue4").pack(side=TOP)
    gridframe.grid(row=1, column=2, sticky= E)

Label(window, text="FALSE & SINGLE WORDS", font='arial 12', bg=background_color).grid(row=3, column=2)
Listbox(window, width=30, height=8, font='arial 10', fg='black', bg='white').grid(row=4, column=2, sticky=E)

Label(window, text=" ", bg=background_color).grid(row=2, column=3)

Label(window, text="SUGGESTION WORDS", font='arial 12', bg=background_color).grid(row=3, column=4)
Listbox(window, width=30, height=8, font='arial 10', fg='black', bg='white').grid(row=4, column=4)

Label(window, text="AUTO NLP RESULT", font='arial 12', bg=background_color).grid(row=6, column=2)
Listbox(window, width=30, height=8, font='arial 10', fg='black', bg='white').grid(row=7, column=2)

Listbox(window, width=30, height=8, font='arial 10', fg='black', bg='white').grid(row=7, column=4)

window.mainloop()