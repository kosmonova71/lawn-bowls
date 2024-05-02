from tkinter import Tk, Button, Label, StringVar, Entry
root = Tk()

root.score = 0
root.score2 = 0
root.score3 = 0
player1 = StringVar()
player2 = StringVar()
ends2 = StringVar()

def save_info():
     player1_info = player1.get()
     player2_info = player2.get()
     ends2_info = ends2.get()
     file = open("scP1.txt", "w")
     file.write(player1_info)    
     file = open("scP2.txt", "w")
     file.write(player2_info)

def save2_info():
     file = open("Endsset.txt", "w")
     file.write(ends2_info)
     file.close()

def clicked():
    root.score += 1
    L['text'] = ' ' + str(root.score)
    file = open("P1.txt", "w")
    file.write(str(root.score))
    file.close()

def clicked2():
    root.score2 += 1
    K['text'] = ' ' + str(root.score2)
    file = open("P2.txt", "w")
    file.write(str(root.score2))
    file.close()
    
def clicked3():
    root.score3 += 1
    J['text'] = ' ' + str(root.score3)
    file = open("E1.txt", "w")
    file.write(str(root.score3))
    file.close()
    
def clicked4():
    root.score -= 1
    L['text'] = ' ' + str(root.score)
    file = open("P1.txt", "w")
    file.write(str(root.score))
    file.close()
    
def clicked5():
    root.score2 -= 1
    K['text'] = ' ' + str(root.score2)
    file = open("P2.txt", "w")
    file.write(str(root.score2))
    file.close()
    
def clicked6():
    root.score3 -= 1
    J['text'] = ' ' + str(root.score3)
    file = open("E1.txt", "w")
    file.write(str(root.score3))
    file.close()
    
def clear():
    root.score = 0
    root.score2 = 0
    root.score3 = 0
    L['text'] = ' ' + str(root.score)
    K['text'] = ' ' + str(root.score2)
    J['text'] = ' ' + str(root.score3)
    file = open("P1.txt", "w")
    file.write(str(root.score))
    file = open("P2.txt", "w")
    file.write(str(root.score2))    
    file = open("E1.txt", "w")
    file.write(str(root.score3))
    file.close()
    
root.geometry("300x250")
root.title("Lawn Bowls Scoreboard")
single = Label(root, text = "Scoreboard", font="none 14 bold").place(x = 95,y = 10)
name = Label(root, text = "Player 1", font="none 10 bold").place(x = 20,y = 50)  
name1 = Label(root, text = "Player 2", font="none 10 bold").place(x = 20, y = 90)
Home = Label(root, text = "Home", font="none 10 bold").place(x = 30, y = 120)
Away = Label(root, text = "Aways", font="none 10 bold").place(x = 130, y = 120)
Ends = Label(root, text = "Ends", font="none 10 bold").place(x = 230, y = 120)
Set = Label(root, text = "Set Ends", font="none 10 bold").place(x = 145, y = 50)
L = Label(root, text = root.score, font="Aria 14 bold")
L.place(x = 30, y = 140)
K = Label(root, text = root.score2, font="Aria 14 bold")
K.place(x = 130, y = 140)
J = Label(root, text = root.score3, font="Aria 14 bold")
J.place(x = 230, y = 140)
player1_entry = Entry(root, textvariable = player1, width = "10").place(x = 80, y = 50)
player2_entry = Entry(root, textvariable = player2, width = "10").place(x = 80, y = 90)
ends2_entry = Entry(root, textvariable = ends2, width = "10").place(x = 210, y = 50)
btn1 = Button(root, text="Save", command=save_info).place(x = 160, y = 85)
btn2 = Button(root, text="Save", command=save2_info).place(x = 240, y = 85)  
b = Button(root, text="+", command=clicked).place(x = 50, y = 170)
b2 = Button(root, text="+", command=clicked2).place(x = 150, y = 170)
b3 = Button(root, text="+", command=clicked3).place(x = 250, y = 170)
b4 = Button(root, text="-", command=clicked4).place(x = 30, y = 170)
b5 = Button(root, text="-", command=clicked5).place(x = 130, y = 170)
b6 = Button(root, text="-", command=clicked6).place(x = 230, y = 170)
b1 = Button(root, text="Score Reset", command=clear).place(x = 110, y = 210)
root.wm_attributes("-topmost", 1)
root.resizable(0, 0)
root.mainloop()
