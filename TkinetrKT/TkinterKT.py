#9. Kilomeetrid
from tkinter import *
import math
aken = Tk()
aken.title("Kilomeetrid")
aken.iconbitmap("favicon.ico")
aken.geometry("400x350")

tekst = Label(aken, text = "Sisesta kilomeetrid: ")
tekst.grid(row = 0, column = 0)
e1 = Entry(aken)
e1.grid(row = 0, column = 1)


tekst = Label(aken, text = "Sisesta miilid: ")
tekst.grid(row = 1, column = 0)
e2 = Entry(aken)
e2.grid(row = 1, column = 1)

def arv_miilides():
    pik1 = int(e1.get())
    mile = (pik1*0.6214)
    lyh1 = round(mile, 4)
    print(lyh1)
    vastus1.config(text=lyh1)


def arv_kilomeetrites():
    pik2 = int(e2.get())
    km = (pik2/0.62137)
    lyh2 = round(km, 2)
    print(lyh2)
    vastus2.config(text=lyh2)

#nupp
nupp1 = Button(aken, text="Convert", command=lambda:[arv_miilides(), arv_kilomeetrites()])
nupp1.grid(row = 7, column = 2)


tekst = Label(aken, text = "Miilides: " )
tekst.grid(row = 4)
vastus1 = Label(aken, text = "0 ")
vastus1.grid(column=1, row= 4)
tekst = Label(aken, text = "Kilomeetrites: " )
tekst.grid(row = 5)
vastus2 = Label(aken, text = "0 ")
vastus2.grid(column=1, row= 5)

aken.mainloop()