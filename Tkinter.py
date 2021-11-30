from tkinter import *

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

aken = Tk()
aken.title("Название окна")
aken.geometry("600x400")

btn = Button(aken, text = "Нажми", font = "Arial 20", fg = "blue", bg = "lightblue", width = 20, height = 3)

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