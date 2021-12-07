from tkinter import *
from tkinter import ttk

klik = 0

def klikker(event):
    global klik
    klik+=1
    lbl.configure(text=klik)

def klikker2(event):
    global klik
    if klik > 0:
        klik -=1
    else:
        klik = 0
    lbl.configure(text=klik)

def text_to_lbl(event):
    text = ent.get()
    lbl.configure(text=text)
    ent.delete(0, END)

def valik():
    val = var.get() #value 1, 2, 3
    ent.insert(END, str(val)+", ")

def uus_aken(ind: int):
    uusaken = Toplevel()
    tabs = ttk.Notebook(uusaken)
    texts = ["1.gif", "2.gif", "3.gif", "4.gif", "5.gif",]
    
    tab1= Frame(tabs)
    img1 = PhotoImage(file = texts[0])
    tabs.add(tab1, text=texts[0])
    can1=Canvas(tab1, height = 800, width = 800)
    can1.create_image(0,0,image = img1, anchor=NW)
    can1.pack()

    tab2= Frame(tabs)
    img2 = PhotoImage(file = texts[1])
    tabs.add(tab2, text=texts[1])
    can2=Canvas(tab2, height = 700, width = 700)
    can2.create_image(0,0,image = img2, anchor=NW)
    can2.pack()
    
    tab3= Frame(tabs)
    img3 = PhotoImage(file = texts[2])
    tabs.add(tab3, text=texts[2])
    can3=Canvas(tab3, height = 2000, width = 2000)
    can3.create_image(0,0,image = img3, anchor=NW)
    can3.pack()
    
    tab4= Frame(tabs)
    img4 = PhotoImage(file = texts[3])
    tabs.add(tab4, text=texts[3])
    can4=Canvas(tab4, height = 2000, width = 2000)
    can4.create_image(0,0,image = img4, anchor=NW)
    can4.pack()
    
    tab5= Frame(tabs)
    img5 = PhotoImage(file = texts[4])
    tabs.add(tab1, text=texts[4])
    can5=Canvas(tab5, height = 1000, width = 1000)
    can5.create_image(0,0,image = img5, anchor=NW)
    can5.pack()

    tabs.add(tab1, text = texts[0])
    tabs.add(tab2, text = texts[1])
    tabs.add(tab3, text = texts[2])
    tabs.add(tab4, text = texts[3])
    tabs.add(tab5, text = texts[4])
    tabs.grid(row = 0, column = 0)

    tabs.select(int)
    uusaken.mainloop()

aken = Tk()
aken.title("Название окна")
aken.geometry("600x400")
menu = Menu(aken)
aken.config(menu=menu)
m1 = Menu(menu)
menu.add_cascade(label = "Tabs", menu=m1)
m1.add_command(label = "Tab1", accelerator = "Command+A", command = lambda: uus_aken(0))
m1.add_command(label = "Tab2", command = lambda: uus_aken(1))
m1.add_command(label = "Tab3", command = lambda: uus_aken(2))
m1.add_separator()

btn = Button(aken, text = "Нажми", font = "Arial 20", fg = "blue", bg = "lightblue", width = 20, height = 3)
btn2 = Button(aken, text = "Новое окно", font = "Arial 20", fg = "blue", bg = "lightblue", command =lambda: uus_aken(0))

lbl = Label(aken, text = "...")
ent = Entry(aken, fg = "blue", width = 20, font="Arial 20")
var = IntVar() #StrngVar()
var.set(0)
r1=Radiobutton(aken, text = "Первый", variable = var, value = 1, command = valik)
r2=Radiobutton(aken, text = "Второй", variable = var, value = 2, command = valik)
r3=Radiobutton(aken, text = "Третий", variable = var, value = 3, command = valik)

btn.bind("<Button-1>", klikker) #1 - ЛКМ 2 - СКМ 3 - ПКМ
btn.bind("<Button-3>", klikker2)
ent.bind("<Return>", text_to_lbl) #Return - нажатие на Enter

lbl.pack()
btn.pack()
ent.pack()
r1.pack(side = LEFT)
r2.pack(side = LEFT)
r3.pack(side = LEFT)
aken.mainloop()