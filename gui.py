import os 
from tkinter import *
from tkinter import Tk, Text, BOTH, W, N, E, S
from tkinter.ttk import Frame, Button, Label, Style
from tkinter import filedialog
from PIL import ImageTk,Image  

def open_image():
    file = filedialog.askopenfilename()
    img = ImageTk.PhotoImage(Image.open(file))
    canvas = Canvas(window, bg="white", height=400) 
    canvas.grid(row=1, column=0, columnspan=4, rowspan=2, padx=5, sticky=E+W+S+N)     
    canvas.create_image(20,20, anchor=NW, image=img)    
    canvas.image = img

def rule_editor():
    os.system('python D:/Documents/Akademik/"Teknik Informatika"/"Semester 5"/"Inteligensi Buatan"/Tugas/"Tubes 2"/geometri-kbs/rule_editor.py')

def show_rules():
    os.system('python D:/Documents/Akademik/"Teknik Informatika"/"Semester 5"/"Inteligensi Buatan"/Tugas/"Tubes 2"/geometri-kbs/show_rules.py')

def show_facts():
    os.system('python D:/Documents/Akademik/"Teknik Informatika"/"Semester 5"/"Inteligensi Buatan"/Tugas/"Tubes 2"/geometri-kbs/show_facts.py')

window = Tk()
window.attributes("-fullscreen", True)
    
window.title("Windows")

lbl = Label(window, text="Source Image")
lbl.grid(sticky=W, row=0, column=0, pady=4, padx=5)
canvas = Canvas(window, bg="white", height=400) 
canvas.grid(row=1, column=0, columnspan=4, rowspan=2, padx=5, sticky=E+W+S+N)

lbl2 = Label(window, text="Detection Image")
lbl2.grid(sticky=W, row=0, column=4, pady=4, padx=5)
canvas2 = Canvas(window, bg="white", height=400) 
canvas2.grid(row=1, column=4, columnspan=4, rowspan=2, padx=5, sticky=E+W+S+N)

lbl3 = Label(window, text="Detection Result")
lbl3.grid(sticky=W, row=3, column=0, pady=4, padx=5)
canvas3 = Canvas(window, bg="white") 
canvas3.grid(row=4, column=0, columnspan=2, padx=5, sticky=E+W+S+N)

lbl4 = Label(window, text="Matched Fact")
lbl4.grid(sticky=W, row=3, column=3, pady=4, padx=5)
canvas4 = Canvas(window, bg="white") 
canvas4.grid(row=4, column=3, columnspan=2, padx=5, sticky=E+W+S+N)

lbl5 = Label(window, text="Hit Rules")
lbl5.grid(sticky=W, row=3, column=6, pady=4, padx=5)
canvas5 = Canvas(window, bg="white") 
canvas5.grid(row=4, column=6, columnspan=2, padx=5, sticky=E+W+S+N)

abtn = Button(window, text="Open Image", width=20, command=open_image)
abtn.place(x=1180,y=30)

bbtn = Button(window, text="Open Rule Editor", width=20, command=rule_editor)
bbtn.place(x=1180,y=70)

cbtn = Button(window, text="Show Rules", width=20, command=show_rules)
cbtn.place(x=1180,y=110)

dbtn = Button(window, text="Show Facts", width=20, command=show_facts)
dbtn.place(x=1180,y=150) 

window.mainloop()