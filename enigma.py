from tkinter import *
from tkinter.messagebox import *

frame = Tk()
frame.title("enigma machine simulator")
frame.geometry('800x400')



alefba = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "

def rot():
    f = open("setting.txt", "r")
    r1 = f.readline()
    r2 = f.readline()
    r3 = f.readline()
    f.close()
    return (r1 , r2 , r3)

r1,r2,r3 = rot()
r1 = r1.replace("\n", "")
r2 = r2.replace("\n", "")
r3 = r3.replace("\n", "")


def reflector(x):
    for i in range(0 , len(alefba)):
        if alefba[i] == x:
            s = i
    return(alefba[52 - s])


def enigma(c):
    
    for i in range(0 , len(alefba)):
        if alefba[i] == c:
            s = i
    c1 = r1[s]
    for i in range(0 , len(alefba)):
        if alefba[i] == c1:
            s = i
    c2 = r2[s]
    for i in range(0 , len(alefba)):
        if alefba[i] == c2:
            s = i
    c3 = r3[s]

    ref = reflector(c3)

    for i in range(0 , len(r3)):
        if r3[i] == ref:
            s = i
    c3 = alefba[s]
    for i in range(0 , len(r2)):
        if r2[i] == c3:
            s = i
    c2 = alefba[s]
    for i in range(0 , len(r1)):
        if r1[i] == c2:
            s = i
    
    c1 = alefba[s]

    return(c1)

def charkhesh():
    global r1 , r2 , r3
    r1 = r1[1:] + r1[0]
    if a % 53 == 0:
        r2 = r2[1:] + r2[0]
    if a % (53*53) == 0:
        r3 = r3[1:] = r3[0]
    

cipher_text = ""
a = 0
def nahaii():
    global a , cipher_text , var1 , r1 , r2 , r3
    for i in var.get():
        cipher_text += enigma(i)
        a += 1
        charkhesh()
    
    var1.set(cipher_text)
    cipher_text=""
    
    r1,r2,r3 = rot()
    r1 = r1.replace("\n", "")
    r2 = r2.replace("\n", "")
    r3 = r3.replace("\n", "")

var = StringVar()
entry = Entry(frame, textvariable = var, width=50)
entry.pack(padx=10, pady=10)

var1 = StringVar()
entry1 = Entry(frame, textvariable = var1, width=50)
entry1.pack(padx=20, pady=20)
printButton = Button(frame,
						text = "convert",
						command = nahaii)



printButton.pack()





frame.mainloop()