from tkinter import *


def click(event):
    text = event.widget.cget("text")  # cget --> how to get text from widget
    # print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                value = "Error"

        scvalue.set(value)
        screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


root = Tk()
root.geometry("300x420")
root.minsize(300, 415)
root.maxsize(300, 415)
root.title("Codsoft Calculator")
root.wm_iconbitmap("calculator-simple.ico")

scvalue = StringVar()
scvalue.set(" ")
screen = (Entry(root, textvariable=scvalue, font="lucida 39 bold"))
screen.pack(fill=X, ipadx=10, pady=30, padx=10)

f = Frame(root, bg="grey")
b = Button(f, text="C", padx=10, font="lucida 20 italic")
b.pack(side=LEFT, padx=3, pady=2)
b.bind("<Button-1>", click)
b = Button(f, text="(", padx=10, font="lucida 20 italic")
b.pack(side=LEFT, padx=3, pady=2)
b.bind("<Button-1>", click)
b = Button(f, text=")", padx=10, font="lucida 20 italic")
b.pack(side=LEFT, padx=3, pady=2)
b.bind("<Button-1>", click)
b = Button(f, text="/", padx=10,font="lucida 20 italic")
b.pack(side=LEFT, padx=3, pady=2)
b.bind("<Button-1>", click)
b = Button(f, text="%", padx=10, font="lucida 20 italic")
b.pack(side=LEFT, padx=3, pady=2)
b.bind("<Button-1>", click)
f.pack(anchor="w")

f = Frame(root, bg="grey")
b = Button(f, text="7", padx=16, font="lucida 20 italic")
b.pack(side=LEFT, padx=3, pady=2)
b.bind("<Button-1>", click)
b = Button(f, text="8", padx=16, font="lucida 20 italic")
b.pack(side=LEFT, padx=3, pady=2)
b.bind("<Button-1>", click)
b = Button(f, text="9", padx=16, font="lucida 20 italic")
b.pack(side=LEFT, padx=3, pady=2)
b.bind("<Button-1>", click)
b = Button(f, text="*", padx=18, font="lucida 20 italic")
b.pack(side=LEFT, padx=3, pady=2)
b.bind("<Button-1>", click)
f.pack(anchor="w")

f = Frame(root, bg="grey")
b = Button(f, text="4", padx=16, font="lucida 20 italic")
b.pack(side=LEFT, padx=3, pady=2)
b.bind("<Button-1>", click)
b = Button(f, text="5", padx=16, font="lucida 20 italic")
b.pack(side=LEFT, padx=3, pady=2)
b.bind("<Button-1>", click)
b = Button(f, text="6", padx=16, font="lucida 20 italic")
b.pack(side=LEFT, padx=3, pady=2)
b.bind("<Button-1>", click)
b = Button(f, text="-", padx=19, font="lucida 20 italic")
b.pack(side=LEFT, padx=3, pady=2)
b.bind("<Button-1>", click)
f.pack(anchor="w")

f = Frame(root, bg="grey")
b = Button(f, text="1", padx=16, font="lucida 20 italic")
b.pack(side=LEFT, padx=3, pady=2)
b.bind("<Button-1>", click)
b = Button(f, text="2", padx=16, font="lucida 20 italic")
b.pack(side=LEFT, padx=3, pady=2)
b.bind("<Button-1>", click)
b = Button(f, text="3", padx=16, font="lucida 20 italic")
b.pack(side=LEFT, padx=3, pady=2)
b.bind("<Button-1>", click)
b = Button(f, text="+", padx=18, font="lucida 20 italic")
b.pack(side=LEFT, padx=3, pady=2)
b.bind("<Button-1>", click)
f.pack(anchor="w")

f = Frame(root, bg="grey")
b = Button(f, text="0",  padx=13, font="lucida 20 italic")
b.pack(side=LEFT, padx=3, pady=2)
b.bind("<Button-1>", click)
b = Button(f, text=".", padx=13, font="lucida 20 italic")
b.pack(side=LEFT, padx=3, pady=2)
b.bind("<Button-1>", click)
b = Button(f, text="00", padx=14, font="lucida 20 italic")
b.pack(side=LEFT, padx=3, pady=2)
b.bind("<Button-1>", click)
b = Button(f, text="=", padx=20, font="lucida 20 italic")
b.pack(side=LEFT, padx=3, pady=2)
b.bind("<Button-1>", click)
f.pack(anchor="w")

root.mainloop()
