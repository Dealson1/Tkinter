from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *

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
    if askyesno('Вопрос','Могу я открыть?'):
        showinfo('Ответ', 'Открываю окно')
    else:
        showinfo('Ответ', 'Закрываю окно')
        aken.destroy()
    aken2 = Toplevel()
    aken2.title('Настройки')
    #aken2.geometry('300x200')
    tabs = ttk.Notebook(aken2)
    texts = ['1.gif', '2.gif', '3.gif', '4.gif', '5.gif']
    textn = ['1.gif', '2.gif', '3.gif', '4.gif', '5.gif']
    tabn = ['tab0', 'tab1', 'tab2', 'tab3', 'tab4']
    cann = ['can0', 'can1', 'can2', 'can3', 'can4']

    for i in range(len(texts)):
        tabn[i] = Frame(tabs)
        textn[i] = PhotoImage(file = texts[i]).subsample(1)
        tabs.add(tabn[i], text = texts[i])
        cann[i] = Canvas(tabn[i], height = 800, width = 1000)
        cann[i].create_image(0,0, image = textn[i], anchor = NW)
        cann[i].pack()

    tabs.grid(row = 0, column = 0)
    tabs.select(ind)
    aken2.mainloop()

aken = Tk()
aken.title("Название окна")
aken.geometry("600x400")
menu = Menu(aken)
aken.config(menu=menu)
m1 = Menu(menu)
menu.add_cascade(label = "Tabs", menu=m1)
m1.add_command(label = "Tab1", command = lambda: uus_aken(0))
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