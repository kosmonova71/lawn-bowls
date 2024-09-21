import os
from tkinter import Tk, Button, Label, StringVar, Entry, Canvas
from tkinter import colorchooser, PhotoImage, NW, ttk, messagebox, Frame
from PIL import Image, ImageDraw, ImageFont, ImageTk
import matplotlib.font_manager as fm
import configparser
config = configparser.ConfigParser()
config1 = configparser.ConfigParser()
config2 = configparser.ConfigParser()
config3 = configparser.ConfigParser()
config4 = configparser.ConfigParser()
config5 = configparser.ConfigParser()
config6 = configparser.ConfigParser()
config7 = configparser.ConfigParser()
config.add_section("Score")
config1.add_section("Score")
config2.add_section("Score")
config3.add_section("Score")
config4.add_section("Score")
config5.add_section("Score")
config6.add_section("Score")
config7.add_section("Score")
def raise_frame(frame):
    frame.tkraise()
root = Tk()
root.score = 0
root.score2 = 0
root.score3 = 0
root.score4 = 0
root.score5 = 0
root.score6 = 0
player1 = StringVar()
player2 = StringVar()
ends2 = StringVar()
root.scorea = 0
root.score2a = 0
root.score3a = 0
player1a = StringVar()
player2a = StringVar()
ends2a = StringVar()
root.scoreb = 0
root.score2b = 0
root.score3b = 0
player1b = StringVar()
player2b = StringVar()
ends2b = StringVar()
team1_entry_var = StringVar()
team2_entry_var = StringVar()
total_score_team1 = 0
total_score_team2 = 0
total_score_team3 = 0

f0 = Frame(root)
f1 = Frame(root)
def clear_interface():
    root.score = 0
    root.score2 = 0
    root.score3 = 0
    root.score4 = 0
    root.score5 = 0
    root.score6 = 0
    root.scorea = 0
    root.score2a = 0
    root.score3a = 0
    root.scoreb = 0
    root.score2b = 0
    root.score3b = 0
    total_score_team1 = 0
    total_score_team2 = 0
    total_score_team3 = 0
    player1.set('')
    player2.set('')
    ends2.set('')
    player1a.set('')
    player2a.set('')
    ends2a.set('')
    player1b.set('')
    player2b.set('')
    ends2b.set('')
    team1_entry_var.set('')
    team2_entry_var.set('')    
def sum_numbers(file_paths):
    global total_score_team1, total_score_team2, total_score_team3
    total_score_team1 = 0
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            numbers = [int(line.strip()) for line in file]
            total_score_team1 += sum(numbers)
    return total_score_team1
def write_total_score(file_paths, output_file):
    total_score = sum_numbers(file_paths)
    with open(output_file, 'w') as file:
        file.write(str(total_score))
root.geometry("1200x250")
root.title("Lawn Bowls")
fonts = list(set([f.name for f in fm.fontManager.ttflist]))
fonts.sort()
combo = ttk.Combobox(f1, width = 20,value=fonts)
combo.place(x = 92, y = 30)
read_config = configparser.ConfigParser()
read_config1 = configparser.ConfigParser()
read_config2 = configparser.ConfigParser()
read_config3 = configparser.ConfigParser()
font_style1, font_style2, font_style3 = None, None, None
def set_font_styles():
    global font_style1, font_style2, font_style3
    read_config.read("configp/Config.ini")
    na = read_config.get("Score", "1")
    read_config1.read("configp/Config1.ini")
    a = read_config1.get("Score", "1")
    read_config2.read("configp/Config2.ini")
    b = read_config2.get("Score", "1")
    read_config3.read("configp/Config3.ini")
    c = read_config3.get("Score", "1")
    a = int(a) if a.isdigit() else 12
    b = int(b) if b.isdigit() else 12
    c = int(c) if c.isdigit() else 12
    font_style1 = ImageFont.truetype(na, a)
    font_style2 = ImageFont.truetype(na, b)
    font_style3 = ImageFont.truetype(na, c)
set_font_styles()
def clickee():
    config.set("Score", "1", fm.findfont(fm.FontProperties(family=combo.get())))
    with open('configp/Config.ini', 'w') as configfile:
        config.write(configfile)
def increase1():
     root.score4 += 1
     L1['text'] = ' ' + str(root.score4)
     config1.set("Score", "1", str(root.score4))
     with open('configp/Config1.ini', 'w') as configfile:
         config1.write(configfile)
def decrease1():
     root.score4 -= 1
     L1['text'] = ' ' + str(root.score4)
     config1.set("Score", "1", str(root.score4))
     with open('configp/Config1.ini', 'w') as configfile:
        config1.write(configfile)
def increase2():
     root.score5 += 1
     L2['text'] = ' ' + str(root.score5)
     config2.set("Score", "1", str(root.score5))
     with open('configp/Config2.ini', 'w') as configfile:
         config2.write(configfile)
def decrease2():
     root.score5 -= 1
     L2['text'] = ' ' + str(root.score5)
     config2.set("Score", "1", str(root.score5))
     with open('configp/Config2.ini', 'w') as configfile:
        config2.write(configfile)
def increase3():
     root.score6 += 1
     L3['text'] = ' ' + str(root.score6)
     config2.set("Score", "1", str(root.score6))
     with open('configp/Config3.ini', 'w') as configfile:
         config2.write(configfile)
def decrease3():
     root.score6 -= 1
     L3['text'] = ' ' + str(root.score6)
     config2.set("Score", "1", str(root.score6))
     with open('configp/Config3.ini', 'w') as configfile:
        config2.write(configfile)
def save():
     color = colorchooser.askcolor()
     label = Label(root, text="Colour", bg=color[1]).place(x = 225, y = 125)
     n1 = color[1]
     config3.set("Score", "1", n1)
     with open('configp/Config4.ini', 'w') as configfile:
        config3.write(configfile)
def save2():
     color = colorchooser.askcolor()
     label = Label(root, text="Colour", bg=color[1]).place(x = 225, y = 150)
     n2 = color[1]
     config4.set("Score", "1", n2)
     with open('configp/Config5.ini', 'w') as configfile:
        config4.write(configfile)
def save3():
     color = colorchooser.askcolor()
     label = Label(root, text="Colour", bg=color[1]).place(x = 225, y = 180)
     n3 = color[1]
     config5.set("Score", "1", n3)
     with open('configp/Config6.ini', 'w') as configfile:
        config5.write(configfile)
def save4():
     color = colorchooser.askcolor()
     label = Label(root, text="Colour", bg=color[1]).place(x = 225, y = 210)
     n4 = color[1]
     config6.set("Score", "1", n4)
     with open('configp/Config7.ini', 'w') as configfile:
        config6.write(configfile)
cs1 = Canvas(f0, width = 290, height = 130)
cs1.place(x = 900, y = 35)
pil_image = Image.open("barsp/master.png")
img1 = ImageTk.PhotoImage(pil_image)
cs1.create_image(0, 0, anchor=NW, image=img1)
mb = Label(f0, text = "Master Board", font="Aria 12 bold").place(x = 990,y = 0)
mb1 = Label(f0, text = "Home", font="Aria 12 bold").place(x = 950,y = 70)
mb2 = Label(f0, text = "Away", font="Aria 12 bold").place(x = 1102,y = 70)
mb3 = Label(f0, text = "Ends", font="Aria 12 bold").place(x = 1030,y = 30)
team1 = Label(f0, text = "Club 1", font="Aria 10 bold", fg="blue").place(x = 890, y = 180)
team2 = Label(f0, text = "Club 2", font="Aria 10 bold", fg="red").place(x = 890, y = 220)
team1_entrya = Entry(f0, textvariable=team1_entry_var, width="25")
team1_entrya.place(x=940, y=180)
team2_entrya = Entry(f0, textvariable=team2_entry_var, width="25")
team2_entrya.place(x=940, y=220)
Lc = Label(f0, text=total_score_team1, font="Aria 14 bold")
Lc.place(x=968, y=110)
Kc = Label(f0, text=total_score_team2, font="Aria 14 bold")
Kc.place(x=1121, y=110)
Jc = Label(f0, text=total_score_team3, font="Aria 14 bold")
Jc.place(x=1045, y=60)
def save_info():
    player1_info = player1.get()
    player2_info = player2.get()
    with open("text/scP1.txt", "w") as file:
        file.write(player1_info)
    with open("text/scP2.txt", "w") as file:
        file.write(player2_info)
    img = Image.open("barsp/scorebar1.png")
    draw = ImageDraw.Draw(img)
    draw.text((10, 47),(player1_info),(255,255,255),font=(font_style1))
    draw.text((10, 95),(player2_info),(255,255,255),font=(font_style1))
    draw = ImageDraw.Draw(img)
    img.save("barsp/scorebar2.png")
    img = Image.open("barsp/scorebar4.png")
    draw = ImageDraw.Draw(img)
    draw.text((10, 47),(player1_info),(255,255,255),font=(font_style1))
    draw.text((10, 95),(player2_info),(255,255,255),font=(font_style1))
    draw = ImageDraw.Draw(img)
    img.save("barsp/scorebar5.png")
def save_info2():
    team1_entrya_value = team1_entry_var.get()
    team2_entrya_value = team2_entry_var.get()
    with open("text/team1.txt", "w") as file:
        file.write(team1_entrya_value)
    with open("text/team2.txt", "w") as file:
        file.write(team2_entrya_value)
    img = Image.open("barsp/master.png")
    draw = ImageDraw.Draw(img)
    draw.text((10, 5), (team1_entrya_value), (255, 255, 255), font=(font_style1))
    draw.text((200, 5), (team2_entrya_value), (255, 255, 255), font=(font_style1))
    draw = ImageDraw.Draw(img)
    img.save("barsp/master2.png")
    img = Image.open("barsp/master2.png")
    draw = ImageDraw.Draw(img)
    draw.text((10, 5), (team1_entrya_value), (255, 255, 255), font=(font_style1))
    draw.text((200, 5), (team2_entrya_value), (255, 255, 255), font=(font_style1))
    draw = ImageDraw.Draw(img)
    img.save("barsp/master3.png")
def clicked():
    global total_score_team1, total_score_team2, total_score_team3
    total_score_team1 += 1
    root.score += 1
    L['text'] = ' ' + str(root.score)
    Lc['text'] = ' ' + str(total_score_team1)
    Kc['text'] = ' ' + str(total_score_team2)
    Jc['text'] = ' ' + str(total_score_team3)
    with open("text/P1.txt", "w") as file:
        file.write(str(root.score))
    with open("text/T1.txt", "w") as file:
        file.write(str(total_score_team1))
    with open("text/P1.txt", "r") as f:
        F1 =f.read()
    with open("text/P2.txt", "r") as g:
        F2 =g.read()
    with open("text/E1.txt", "r") as e:
        F3 =e.read()        
    with open("text/T1.txt", "r") as x:
        G1 =x.read()
    with open("text/T2.txt", "r") as y:
        G2 =y.read()
    with open("text/T3.txt", "r") as z:
        G3 =z.read()  
    img = Image.open("barsp/scorebar2.png")
    draw = ImageDraw.Draw(img)
    draw.text((250, 8), (F1), (0, 0, 0), font=(font_style3))
    draw.text((250, 56),(F2),(0,0,0),font=(font_style3))
    draw.text((150, 105),(F3),(255,255,255),font=(font_style2))
    draw = ImageDraw.Draw(img)
    img.save("barsp/scorebar3.png")
    img = Image.open("barsp/scorebar5.png")
    draw = ImageDraw.Draw(img)
    draw.text((250, 47),(F1),(0,0,0),font=(font_style3))
    draw.text((250, 92),(F2),(0,0,0),font=(font_style3))
    draw.text((150, 5),(F3),(255,255,255),font=(font_style2))
    draw = ImageDraw.Draw(img)
    img.save("barsp/scorebar6.png")    
    img = Image.open("barsp/master3.png")
    draw = ImageDraw.Draw(img)
    draw.text((60, 75),(G1),(0,0,0),font=(font_style3))
    draw.text((210, 75),(G2),(0,0,0),font=(font_style3))
    draw.text((140, 15),(G3),(255,255,255),font=(font_style2))
    draw = ImageDraw.Draw(img)
    img.save("barsp/master4.png")
def clicked2():
    global total_score_team1, total_score_team2, total_score_team3
    total_score_team2 += 1
    root.score2 += 1
    K['text'] = ' ' + str(root.score2)
    Lc['text'] = ' ' + str(total_score_team1)
    Kc['text'] = ' ' + str(total_score_team2)
    Jc['text'] = ' ' + str(total_score_team3)
    with open("text/P2.txt", "w") as file:
        file.write(str(root.score2))
    with open("text/T2.txt", "w") as file:
        file.write(str(total_score_team2))
    with open("text/P1.txt", "r") as f:
        F1 =f.read()
    with open("text/P2.txt", "r") as g:
        F2 =g.read()
    with open("text/E1.txt", "r") as e:
        F3 =e.read()        
    with open("text/T1.txt", "r") as x:
        G1 =x.read()
    with open("text/T2.txt", "r") as y:
        G2 =y.read()
    with open("text/T3.txt", "r") as z:
        G3 =z.read()       
    img = Image.open("barsp/scorebar2.png")
    draw = ImageDraw.Draw(img)
    draw.text((250, 8),(F1),(0,0,0),font=(font_style3))
    draw.text((150, 105),(F3),(255,255,255),font=(font_style2))
    draw = ImageDraw.Draw(img)
    img.save("barsp/scorebar3.png")
    img = Image.open("bars/scorebar5.png")
    draw = ImageDraw.Draw(img)
    draw.text((250, 47),(F1),(0,0,0),font=(font_style3))
    draw.text((250, 92),(F2),(0,0,0),font=(font_style3))
    draw.text((150, 5),(F3),(255,255,255),font=(font_style2))
    draw = ImageDraw.Draw(img)
    img.save("barsp/scorebar6.png")
    img = Image.open("barsp/master3.png")
    draw = ImageDraw.Draw(img)
    draw.text((60, 75),(G1),(0,0,0),font=(font_style3))
    draw.text((210, 75),(G2),(0,0,0),font=(font_style3))
    draw.text((140, 15),(G3),(255,255,255),font=(font_style2))
    draw = ImageDraw.Draw(img)
    img.save("barsp/master4.png")
def clicked3():
    global total_score_team1, total_score_team2, total_score_team3   
    total_score_team3 += 1
    root.score3 += 1
    J['text'] = ' ' + str(root.score3)
    Lc['text'] = ' ' + str(total_score_team1)
    Kc['text'] = ' ' + str(total_score_team2)
    Jc['text'] = ' ' + str(total_score_team3)
    with open("text/E1.txt", "w") as file:
        file.write(str(root.score3))
    with open("text/T3.txt", "w") as file:
        file.write(str(total_score_team3))       
    with open("text/P1.txt", "r") as f:
        F1 =f.read()
    with open("text/P2.txt", "r") as g:
        F2 =g.read()
    with open("text/E1.txt", "r") as e:
        F3 =e.read()
    with open("text/T1.txt", "r") as x:
        G1 =x.read()
    with open("text/T2.txt", "r") as y:
        G2 =y.read()
    with open("text/T3.txt", "r") as z:
        G3 =z.read()         
    img = Image.open("barsp/scorebar2.png")
    draw = ImageDraw.Draw(img)
    draw.text((250, 8),(F1),(0,0,0),font=(font_style3))
    draw.text((250, 56),(F2),(0,0,0),font=(font_style3))
    draw.text((150, 105),(F3),(255,255,255),font=(font_style2))
    draw = ImageDraw.Draw(img)
    img.save("barsp/scorebar3.png")
    img = Image.open("bars/scorebar5.png")
    draw = ImageDraw.Draw(img)
    draw.text((250, 47),(F1),(0,0,0),font=(font_style3))
    draw.text((250, 92),(F2),(0,0,0),font=(font_style3))
    draw.text((150, 5),(F3),(255,255,255),font=(font_style2))
    draw = ImageDraw.Draw(img)
    img.save("barsp/scorebar6.png")
    img = Image.open("barsp/master3.png")
    draw = ImageDraw.Draw(img)
    draw.text((60, 75),(G1),(0,0,0),font=(font_style3))
    draw.text((210, 75),(G2),(0,0,0),font=(font_style3))
    draw.text((140, 15),(G3),(255,255,255),font=(font_style2))
    draw = ImageDraw.Draw(img)
    img.save("barsp/master4.png")
def clicked4():
    global total_score_team1, total_score_team2, total_score_team3
    if root.score > 0:
        root.score -= 1
    total_score_team1 -= 1
    L['text'] = ' ' + str(root.score)
    Lc['text'] = ' ' + str(total_score_team1)
    Kc['text'] = ' ' + str(total_score_team2)
    Jc['text'] = ' ' + str(total_score_team3)
    with open("text/P1.txt", "w") as file:
        file.write(str(root.score))
    with open("text/T1.txt", "w") as file:
        file.write(str(total_score_team1))        
    with open("text/P1.txt", "r") as f:
        F1 =f.read()
    with open("text/P2.txt", "r") as g:
        F2 =g.read()
    with open("text/E1.txt", "r") as e:
        F3 =e.read()
    with open("text/T1.txt", "r") as x:
        G1 =x.read()
    with open("text/T2.txt", "r") as y:
        G2 =y.read()
    with open("text/T3.txt", "r") as z:
        G3 =z.read()          
    img = Image.open("barsp/scorebar2.png")
    draw = ImageDraw.Draw(img)
    draw.text((250, 8),(F1),(0,0,0),font=(font_style3))
    draw.text((250, 56),(F2),(0,0,0),font=(font_style3))
    draw.text((150, 105),(F3),(255,255,255),font=(font_style2))
    draw = ImageDraw.Draw(img)
    img.save("barsp/scorebar3.png")
    img = Image.open("barsp/scorebar5.png")
    draw = ImageDraw.Draw(img)
    draw.text((250, 47),(F1),(0,0,0),font=(font_style3))
    draw.text((250, 92),(F2),(0,0,0),font=(font_style3))
    draw.text((150, 5),(F3),(255,255,255),font=(font_style2))
    draw = ImageDraw.Draw(img)
    img.save("barsp/scorebar6.png")
    img = Image.open("barsp/master3.png")
    draw = ImageDraw.Draw(img)
    draw.text((60, 75),(G1),(0,0,0),font=(font_style3))
    draw.text((210, 75),(G2),(0,0,0),font=(font_style3))
    draw.text((140, 15),(G3),(255,255,255),font=(font_style2))
    draw = ImageDraw.Draw(img)
    img.save("barsp/master4.png")
def clicked5():
    global total_score_team1, total_score_team2, total_score_team3
    if root.score2 > 0:
        root.score2 -= 1
    total_score_team2 -= 1
    K['text'] = ' ' + str(root.score2)
    Lc['text'] = ' ' + str(total_score_team1)
    Kc['text'] = ' ' + str(total_score_team2)
    Jc['text'] = ' ' + str(total_score_team3)
    file = open("text/P2.txt", "w")
    file.write(str(root.score2))
    with open("text/T2.txt", "w") as file:
        file.write(str(total_score_team2))
    with open("text/P1.txt", "r") as f:
        F1 =f.read()
    with open("text/P2.txt", "r") as g:
        F2 =g.read()
    with open("text/E1.txt", "r") as e:
        F3 =e.read()
    with open("text/T1.txt", "r") as x:
        G1 =x.read()
    with open("text/T2.txt", "r") as y:
        G2 =y.read()
    with open("text/T3.txt", "r") as z:
        G3 =z.read()         
    img = Image.open("barsp/scorebar2.png")
    draw = ImageDraw.Draw(img)
    draw.text((250, 8),(F1),(0,0,0),font=(font_style3))
    draw.text((250, 56),(F2),(0,0,0),font=(font_style3))
    draw.text((150, 105),(F3),(255,255,255),font=(font_style2))
    draw = ImageDraw.Draw(img)
    img.save("barsp/scorebar3.png")
    img = Image.open("barsp/scorebar5.png")
    draw = ImageDraw.Draw(img)
    draw.text((250, 47),(F1),(0,0,0),font=(font_style3))
    draw.text((250, 92),(F2),(0,0,0),font=(font_style3))
    draw.text((150, 5),(F3),(255,255,255),font=(font_style2))
    draw = ImageDraw.Draw(img)
    img.save("barsp/scorebar6.png")
    img = Image.open("barsp/master3.png")
    draw = ImageDraw.Draw(img)
    draw.text((60, 75),(G1),(0,0,0),font=(font_style3))
    draw.text((210, 75),(G2),(0,0,0),font=(font_style3))
    draw.text((140, 15),(G3),(255,255,255),font=(font_style2))
    draw = ImageDraw.Draw(img)
    img.save("barsp/master4.png")
def clicked6():
    global total_score_team1, total_score_team2, total_score_team3
    if root.score3 > 0:
        root.score3 -= 1
    total_score_team3 -= 1
    J['text'] = ' ' + str(root.score3)
    Lc['text'] = ' ' + str(total_score_team1)
    Kc['text'] = ' ' + str(total_score_team2)
    Jc['text'] = ' ' + str(total_score_team3)
    file = open("text/E1.txt", "w")
    file.write(str(root.score3))
    with open("text/T3.txt", "w") as file:
        file.write(str(total_score_team3))   
    with open("text/P1.txt", "r") as f:
        F1 =f.read()
    with open("text/P2.txt", "r") as g:
        F2 =g.read()
    with open("text/E1.txt", "r") as e:
        F3 =e.read()
    with open("text/T1.txt", "r") as x:
        G1 =x.read()
    with open("text/T2.txt", "r") as y:
        G2 =y.read()
    with open("text/T3.txt", "r") as z:
        G3 =z.read()
    img = Image.open("barsp/scorebar2.png")
    draw = ImageDraw.Draw(img)
    draw.text((250, 8),(F1),(0,0,0),font=(font_style3))
    draw.text((250, 56),(F2),(0,0,0),font=(font_style3))
    draw.text((150, 105),(F3),(255,255,255),font=(font_style2))
    draw = ImageDraw.Draw(img)
    img.save("barsp/scorebar3.png")
    img = Image.open("barsp/scorebar5.png")
    draw = ImageDraw.Draw(img)
    draw.text((250, 47),(F1),(0,0,0),font=(font_style3))
    draw.text((250, 92),(F2),(0,0,0),font=(font_style3))
    draw.text((150, 5),(F3),(255,255,255),font=(font_style2))
    draw = ImageDraw.Draw(img)
    img.save("barsp/scorebar6.png")
    img = Image.open("barsp/master3.png")
    draw = ImageDraw.Draw(img)
    draw.text((60, 75),(G1),(0,0,0),font=(font_style3))
    draw.text((210, 75),(G2),(0,0,0),font=(font_style3))
    draw.text((140, 15),(G3),(255,255,255),font=(font_style2))
    draw = ImageDraw.Draw(img)
    img.save("barsp/master4.png")
def clear():
    global total_score_team1, total_score_team2, total_score_team3
    root.score = 0
    root.score2 = 0
    root.score3 = 0
    root.scorea = 0
    root.score2a = 0
    root.score3a = 0
    root.scoreb = 0
    root.score2b = 0
    root.score3b = 0
    total_score_team1 = 0
    total_score_team2 = 0
    total_score_team3 = 0
    L['text'] = ' ' + str(root.score)
    K['text'] = ' ' + str(root.score2)
    J['text'] = ' ' + str(root.score3)
    Lc['text'] = ' ' + str(total_score_team1)
    Kc['text'] = ' ' + str(total_score_team2)
    Jc['text'] = ' ' + str(total_score_team3)
    La['text'] = ' ' + str(root.scorea)
    Ka['text'] = ' ' + str(root.score2a)
    Ja['text'] = ' ' + str(root.score3a)
    Lb['text'] = ' ' + str(root.scoreb)
    Kb['text'] = ' ' + str(root.score2b)
    Jb['text'] = ' ' + str(root.score3b)   
    with open("text/P1.txt", "w") as file:
        file.write(str(root.score))
    with open("text/P2.txt", "w") as file:
        file.write(str(root.score2))
    with open("text/E1.txt", "w") as file:
        file.write(str(root.score3))
    with open("text/P1a.txt", "w") as file:
        file.write(str(root.scorea))
    with open("text/P2a.txt", "w") as file:
        file.write(str(root.score2a))
    with open("text/E1a.txt", "w") as file:
        file.write(str(root.score3a))
    with open("text/P1b.txt", "w") as file:
        file.write(str(root.scoreb))
    with open("text/P2b.txt", "w") as file:
        file.write(str(root.score2b))
    with open("text/E1b.txt", "w") as file:
        file.write(str(root.score3b))
    with open("text/T1.txt", "w") as file:
        file.write(str(total_score_team1))
    with open("text/T2.txt", "w") as file:
        file.write(str(total_score_team2))
    with open("text/T3.txt", "w") as file:
        file.write(str(total_score_team3))        
    with open("text/P1.txt", "r") as f:
        F1 =f.read()
    with open("text/P2.txt", "r") as g:
        F2 =g.read()
    with open("text/E1.txt", "r") as e:
        F3 =e.read()
    with open("text/T1.txt", "r") as x:
        G1 =x.read()
    with open("text/T2.txt", "r") as y:
        G2 =y.read()
    with open("text/T3.txt", "r") as z:
        G3 =z.read()         
    with open("text/P1a.txt", "r") as fa:
        F1a = fa.read()
    with open("text/P2a.txt", "r") as ga:
        F2a = ga.read()
    with open("text/E1a.txt", "r") as ea:
        F3a = ea.read()
    with open("text/P1b.txt", "r") as fb:
        F1b = fb.read()
    with open("text/P2b.txt", "r") as gb:
        F2b = gb.read()
    with open("text/E1b.txt", "r") as eb:
        F3b = eb.read()   
    img = Image.open("barsp/scorebar2.png")
    draw = ImageDraw.Draw(img)
    draw.text((250, 8),(F1),(0,0,0),font=(font_style3))
    draw.text((250, 56),(F2),(0,0,0),font=(font_style3))
    draw = ImageDraw.Draw(img)
    draw.text((150, 105),(F3),(255,255,255),font=(font_style2))
    draw = ImageDraw.Draw(img)
    img.save("barsp/scorebar3.png")
    img = Image.open("barsp/scorebar5.png")
    draw = ImageDraw.Draw(img)
    draw.text((250, 47),(F1),(0,0,0),font=(font_style3))
    draw.text((250, 92),(F2),(0,0,0),font=(font_style3))
    draw.text((150, 5),(F3),(255,255,255),font=(font_style2))
    draw = ImageDraw.Draw(img)
    img.save("barsp/scorebar6.png")
    img = Image.open("barsp/scorebar2a.png")
    draw = ImageDraw.Draw(img)
    draw.text((250, 8),(F1a),(0,0,0),font=(font_style3))
    draw.text((250, 56),(F2a),(0,0,0),font=(font_style3))
    draw = ImageDraw.Draw(img)
    draw.text((150, 105),(F3a),(255,255,255),font=(font_style2))
    draw = ImageDraw.Draw(img)
    img.save("barsp/scorebar3a.png")
    img = Image.open("barsp/scorebar5a.png")
    draw = ImageDraw.Draw(img)
    draw.text((250, 47),(F1a),(0,0,0),font=(font_style3))
    draw.text((250, 92),(F2a),(0,0,0),font=(font_style3))
    draw.text((150, 5),(F3a),(255,255,255),font=(font_style2))
    draw = ImageDraw.Draw(img)
    img.save("barsp/scorebar6a.png")
    img = Image.open("barsp/scorebar2b.png")
    draw = ImageDraw.Draw(img)
    draw.text((250, 8),(F1b),(0,0,0),font=(font_style3))
    draw.text((250, 56),(F2b),(0,0,0),font=(font_style3))
    draw = ImageDraw.Draw(img)
    draw.text((150, 105),(F3b),(255,255,255),font=(font_style2))
    draw = ImageDraw.Draw(img)
    img.save("barsp/scorebar3b.png")
    img = Image.open("barsp/scorebar5b.png")
    draw = ImageDraw.Draw(img)
    draw.text((250, 47),(F1b),(0,0,0),font=(font_style3))
    draw.text((250, 92),(F2b),(0,0,0),font=(font_style3))
    draw.text((150, 5),(F3b),(255,255,255),font=(font_style2))
    draw = ImageDraw.Draw(img)
    img.save("barsp/scorebar6b.png")
    img = Image.open("barsp/master3.png")
    draw = ImageDraw.Draw(img)
    draw.text((60, 75),(G1),(0,0,0),font=(font_style3))
    draw.text((210, 75),(G2),(0,0,0),font=(font_style3))
    draw.text((140, 15),(G3),(255,255,255),font=(font_style2))
    draw = ImageDraw.Draw(img)
    img.save("barsp/master4.png")   
for frame in (f0, f1):
    frame.place(x = 0,y = 0, width=1200, height=310)
single = Label(f0, text = "Rink 1", font="Aria 12 bold").place(x = 90,y = 0)
name = Label(f0, text = "Team 1", font="Aria 10 bold", fg="blue").place(x = 20, y = 40)
name1 = Label(f0, text = "Team 2", font="Aria 10 bold", fg="red").place(x = 20, y = 80)
Home = Label(f0, text = "Home", font="Aria 10 bold", fg="blue").place(x = 30, y = 120)
Away = Label(f0, text = "Aways", font="Aria 10 bold", fg="green").place(x = 130, y = 120)
Ends = Label(f0, text = "Ends", font="Aria 10 bold", fg="red").place(x = 230, y = 120)
L = Label(f0, text = root.score, font="Aria 14 bold")
L.place(x = 30, y = 140)
K = Label(f0, text = root.score2, font="Aria 14 bold")
K.place(x = 130, y = 140)
J = Label(f0, text = root.score3, font="Aria 14 bold")
J.place(x = 230, y = 140)
player1_entry = Entry(f0, textvariable = player1, width = "25")
player1_entry.place(x = 80, y = 50)
player2_entry = Entry(f0, textvariable = player2, width = "25")
player2_entry.place(x = 80, y = 90)
btn1 = Button(f0, text="Save", font="Aria 8 bold", relief="solid", command=save_info, fg="blue", bg="white").place(x = 240, y = 90)
b = Button(f0, text="+", font="Aria 8 bold", relief="solid", command=clicked).place(x = 50, y = 170)
b2 = Button(f0, text="+", font="Aria 8 bold", relief="solid", command=clicked2).place(x = 150, y = 170)
b3 = Button(f0, text="+", font="Aria 8 bold", relief="solid", command=clicked3).place(x = 250, y = 170)
b4 = Button(f0, text="-", font="Aria 8 bold", relief="solid", command=clicked4).place(x = 30, y = 170)
b5 = Button(f0, text="-", font="Aria 8 bold", relief="solid", command=clicked5).place(x = 130, y = 170)
b6 = Button(f0, text="-", font="Aria 8 bold", relief="solid", command=clicked6).place(x = 230, y = 170)
b1 = Button(f0, text="Score Reset", font="Aria 8 bold", fg="blue", bg="white", relief="solid", command=clear).place(x = 410, y = 210)
btntm = Button(f0, text="Save", font="Aria 8 bold", relief="solid", command=save_info2, fg="blue", bg="white")
btntm.place(x=1140, y=220)
def save_infoa():
    player1_infoa = player1a.get()
    player2_infoa = player2a.get()
    with open("text/scP1a.txt", "w") as file:
        file.write(player1_infoa)
    with open("text/scP2a.txt", "w") as file:
        file.write(player2_infoa)
    img = Image.open("barsp/scorebar1a.png")
    draw = ImageDraw.Draw(img)
    draw.text((10, 12),(player1_infoa),(255,255,255),font=(font_style1))
    draw.text((10, 61),(player2_infoa),(255,255,255),font=(font_style1))
    draw = ImageDraw.Draw(img)
    img.save("barsp/scorebar2a.png")
    img = Image.open("barsp/scorebar4a.png")
    draw = ImageDraw.Draw(img)
    draw.text((10, 47),(player1_infoa),(255,255,255),font=(font_style1))
    draw.text((10, 95),(player2_infoa),(255,255,255),font=(font_style1))
    draw = ImageDraw.Draw(img)
    img.save("barsp/scorebar5a.png")
def clickeda():
    global total_score_team1, total_score_team2, total_score_team3
    total_score_team1 += 1
    root.scorea += 1
    La['text'] = ' ' + str(root.scorea)
    Lc['text'] = ' ' + str(total_score_team1)
    Kc['text'] = ' ' + str(total_score_team2)
    Jc['text'] = ' ' + str(total_score_team3)
    with open("text/P1a.txt", "w") as file:
        file.write(str(root.scorea))
    with open("text/T1.txt", "w") as file:
        file.write(str(total_score_team1))        
    with open("text/P1a.txt", "r") as fa:
        F1a = fa.read()
    with open("text/P2a.txt", "r") as ga:
        F2a = ga.read()
    with open("text/E1a.txt", "r") as ea:
        F3a = ea.read()
    with open("text/T1.txt", "r") as x:
        G1 =x.read()
    with open("text/T2.txt", "r") as y:
        G2 =y.read()
    with open("text/T3.txt", "r") as z:
        G3 =z.read()  
    img = Image.open("barsp/scorebar2a.png")
    draw = ImageDraw.Draw(img)
    draw.text((250, 8),(F1a),(0,0,0),font=(font_style3))
    draw.text((250, 56),(F2a),(0,0,0),font=(font_style3))
    draw.text((150, 105),(F3a),(255,255,255),font=(font_style2))
    draw = ImageDraw.Draw(img)
    img.save("barsp/scorebar3a.png")
    img = Image.open("barsp/scorebar5a.png")
    draw = ImageDraw.Draw(img)
    draw.text((250, 47),(F1a),(0,0,0),font=(font_style3))
    draw.text((250, 92),(F2a),(0,0,0),font=(font_style3))
    draw.text((150, 5),(F3a),(255,255,255),font=(font_style2))
    draw = ImageDraw.Draw(img)
    img.save("barsp/scorebar6a.png")
    img = Image.open("barsp/master3.png")
    draw = ImageDraw.Draw(img)
    draw.text((60, 75),(G1),(0,0,0),font=(font_style3))
    draw.text((210, 75),(G2),(0,0,0),font=(font_style3))
    draw.text((140, 15),(G3),(255,255,255),font=(font_style2))
    draw = ImageDraw.Draw(img)
    img.save("barsp/master4.png")
def clicked2a():
    global total_score_team1, total_score_team2, total_score_team3
    total_score_team2 += 1
    root.score2a += 1
    Ka['text'] = ' ' + str(root.score2a)
    Lc['text'] = ' ' + str(total_score_team1)
    Kc['text'] = ' ' + str(total_score_team2)
    Jc['text'] = ' ' + str(total_score_team3)
    with open("text/P2a.txt", "w") as file:
        file.write(str(root.score2a))
    with open("text/T2.txt", "w") as file:
        file.write(str(total_score_team2))      
    with open("text/P1a.txt", "r") as fa:
        F1a = fa.read()
    with open("text/P2a.txt", "r") as ga:
        F2a = ga.read()
    with open("text/E1a.txt", "r") as ea:
        F3a = ea.read()
    with open("text/T1.txt", "r") as x:
        G1 =x.read()
    with open("text/T2.txt", "r") as y:
        G2 =y.read()
    with open("text/T3.txt", "r") as z:
        G3 =z.read()       
    img = Image.open("barsp/scorebar2a.png")
    draw = ImageDraw.Draw(img)
    draw.text((250, 8),(F1a),(0,0,0),font=(font_style3))
    draw.text((250, 56),(F2a),(0,0,0),font=(font_style3))
    draw.text((150, 105),(F3a),(255,255,255),font=(font_style2))
    draw = ImageDraw.Draw(img)
    img.save("barsp/scorebar3a.png")
    img = Image.open("barsp/scorebar5a.png")
    draw = ImageDraw.Draw(img)
    draw.text((250, 47),(F1a),(0,0,0),font=(font_style3))
    draw.text((250, 92),(F2a),(0,0,0),font=(font_style3))
    draw.text((150, 5),(F3a),(255,255,255),font=(font_style2))
    draw = ImageDraw.Draw(img)
    img.save("barsp/scorebar6a.png")
    img = Image.open("barsp/master3.png")
    draw = ImageDraw.Draw(img)
    draw.text((60, 75),(G1),(0,0,0),font=(font_style3))
    draw.text((210, 75),(G2),(0,0,0),font=(font_style3))
    draw.text((140, 15),(G3),(255,255,255),font=(font_style2))
    draw = ImageDraw.Draw(img)
    img.save("barsp/master4.png") 
def clicked3a():
    global total_score_team1, total_score_team2, total_score_team3
    total_score_team3 += 1
    root.score3a += 1
    Ja['text'] = ' ' + str(root.score3a)
    Lc['text'] = ' ' + str(total_score_team1)
    Kc['text'] = ' ' + str(total_score_team2)
    Jc['text'] = ' ' + str(total_score_team3)
    with open("text/E1a.txt", "w") as file:
        file.write(str(root.score3a))
    with open("text/T3.txt", "w") as file:
        file.write(str(total_score_team3))     
    with open("text/P1a.txt", "r") as fa:
        F1a = fa.read()
    with open("text/P2a.txt", "r") as ga:
        F2a = ga.read()
    with open("text/E1a.txt", "r") as ea:
        F3a = ea.read()
    with open("text/T1.txt", "r") as x:
        G1 =x.read()
    with open("text/T2.txt", "r") as y:
        G2 =y.read()
    with open("text/T3.txt", "r") as z:
        G3 =z.read()   
    img = Image.open("barsp/scorebar2a.png")
    draw = ImageDraw.Draw(img)
    draw.text((250, 8),(F1a),(0,0,0),font=(font_style3))
    draw.text((250, 56),(F2a),(0,0,0),font=(font_style3))
    draw.text((150, 105),(F3a),(255,255,255),font=(font_style2))
    draw = ImageDraw.Draw(img)
    img.save("barsp/scorebar3a.png")
    img = Image.open("barsp/scorebar5a.png")
    draw = ImageDraw.Draw(img)
    draw.text((250, 47),(F1a),(0,0,0),font=(font_style3))
    draw.text((250, 92),(F2a),(0,0,0),font=(font_style3))
    draw.text((150, 5),(F3a),(255,255,255),font=(font_style2))
    draw = ImageDraw.Draw(img)
    img.save("barsp/scorebar6a.png")
    img = Image.open("barsp/master3.png")
    draw = ImageDraw.Draw(img)
    draw.text((60, 75),(G1),(0,0,0),font=(font_style3))
    draw.text((210, 75),(G2),(0,0,0),font=(font_style3))
    draw.text((140, 15),(G3),(255,255,255),font=(font_style2))
    draw = ImageDraw.Draw(img)
    img.save("barsp/master4.png")
def clicked4a():
    global total_score_team1, total_score_team2, total_score_team3
    if root.scorea > 0:
        root.scorea -= 1
    total_score_team1 -= 1
    La['text'] = ' ' + str(root.scorea)
    Lc['text'] = ' ' + str(total_score_team1)
    Kc['text'] = ' ' + str(total_score_team2)
    Jc['text'] = ' ' + str(total_score_team3)
    with open("text/P1a.txt", "w") as file:
        file.write(str(root.scorea))
    with open("text/T1.txt", "w") as file:
        file.write(str(total_score_team1))       
    with open("text/P1a.txt", "r") as fa:
        F1a = fa.read()
    with open("text/P2a.txt", "r") as ga:
        F2a = ga.read()
    with open("text/E1a.txt", "r") as ea:
        F3a = ea.read()
    with open("text/T1.txt", "r") as x:
        G1 =x.read()
    with open("text/T2.txt", "r") as y:
        G2 =y.read()
    with open("text/T3.txt", "r") as z:
        G3 =z.read()    
    img = Image.open("barsp/scorebar2a.png")
    draw = ImageDraw.Draw(img)
    draw.text((250, 8),(F1a),(0,0,0),font=(font_style3))
    draw.text((250, 56),(F2a),(0,0,0),font=(font_style3))
    draw.text((150, 105),(F3a),(255,255,255),font=(font_style2))
    draw = ImageDraw.Draw(img)
    img.save("barsp/scorebar3a.png")
    img = Image.open("barsp/scorebar5a.png")
    draw = ImageDraw.Draw(img)
    draw.text((250, 47),(F1a),(0,0,0),font=(font_style3))
    draw.text((250, 92),(F2a),(0,0,0),font=(font_style3))
    draw.text((150, 5),(F3a),(255,255,255),font=(font_style2))
    draw = ImageDraw.Draw(img)
    img.save("barsp/scorebar6a.png")
    img = Image.open("barsp/master3.png")
    draw = ImageDraw.Draw(img)
    draw.text((60, 75),(G1),(0,0,0),font=(font_style3))
    draw.text((210, 75),(G2),(0,0,0),font=(font_style3))
    draw.text((140, 15),(G3),(255,255,255),font=(font_style2))
    draw = ImageDraw.Draw(img)
    img.save("barsp/master4.png")
def clicked5a():
    global total_score_team1, total_score_team2, total_score_team3
    if root.score2a > 0:
        root.score2a -= 1
    total_score_team2 -= 1
    Ka['text'] = ' ' + str(root.score2a)
    Lc['text'] = ' ' + str(total_score_team1)
    Kc['text'] = ' ' + str(total_score_team2)
    Jc['text'] = ' ' + str(total_score_team3)
    with open("text/P2a.txt", "w") as file:
        file.write(str(root.score2a))
    with open("text/T2.txt", "w") as file:
        file.write(str(total_score_team2))      
    with open("text/P1a.txt", "r") as fa:
        F1a = fa.read()
    with open("text/P2a.txt", "r") as ga:
        F2a = ga.read()
    with open("text/E1a.txt", "r") as ea:
        F3a = ea.read()
    with open("text/T1.txt", "r") as x:
        G1 =x.read()
    with open("text/T2.txt", "r") as y:
        G2 =y.read()
    with open("text/T3.txt", "r") as z:
        G3 =z.read()  
    img = Image.open("barsp/scorebar2a.png")
    draw = ImageDraw.Draw(img)
    draw.text((250, 8),(F1a),(0,0,0),font=(font_style3))
    draw.text((250, 56),(F2a),(0,0,0),font=(font_style2))
    draw.text((150, 105),(F3a),(255,255,255),font=(font_style2))
    draw = ImageDraw.Draw(img)
    img.save("barsp/scorebar3a.png")
    img = Image.open("barsp/scorebar5a.png")
    draw = ImageDraw.Draw(img)
    draw.text((250, 47),(F1a),(0,0,0),font=(font_style3))
    draw.text((250, 92),(F2a),(0,0,0),font=(font_style3))
    draw.text((150, 5),(F3a),(255,255,255),font=(font_style2))
    draw = ImageDraw.Draw(img)
    img.save("barsp/scorebar6a.png")
    img = Image.open("barsp/master3.png")
    draw = ImageDraw.Draw(img)
    draw.text((60, 75),(G1),(0,0,0),font=(font_style3))
    draw.text((210, 75),(G2),(0,0,0),font=(font_style3))
    draw.text((140, 15),(G3),(255,255,255),font=(font_style2))
    draw = ImageDraw.Draw(img)
    img.save("barsp/master4.png")
def clicked6a():
    global total_score_team1, total_score_team2, total_score_team3
    if root.score3a > 0:
        root.score3a -= 1
    total_score_team3 -= 1    
    Ja['text'] = ' ' + str(root.score3a)
    Lc['text'] = ' ' + str(total_score_team1)
    Kc['text'] = ' ' + str(total_score_team2)
    Jc['text'] = ' ' + str(total_score_team3)
    with open("text/E1a.txt", "w") as file:
        file.write(str(root.score3a))
    with open("text/T3.txt", "w") as file:
        file.write(str(total_score_team3))      
    with open("text/P1a.txt", "r") as fa:
        F1a = fa.read()
    with open("text/P2a.txt", "r") as ga:
        F2a = ga.read()
    with open("text/E1a.txt", "r") as ea:
        F3a = ea.read()
    with open("text/T1.txt", "r") as x:
        G1 =x.read()
    with open("text/T2.txt", "r") as y:
        G2 =y.read()
    with open("text/T3.txt", "r") as z:
        G3 =z.read()         
    img = Image.open("barsp/scorebar2a.png")
    draw = ImageDraw.Draw(img)
    draw.text((250, 8),(F1a),(0,0,0),font=(font_style3))
    draw.text((250, 56),(F2a),(0,0,0),font=(font_style3))
    draw.text((150, 105),(F3a),(255,255,255),font=(font_style2))
    draw = ImageDraw.Draw(img)
    img.save("barsp/scorebar3a.png")
    img = Image.open("barsp/scorebar5a.png")
    draw = ImageDraw.Draw(img)
    draw.text((250, 47),(F1a),(0,0,0),font=(font_style3))
    draw.text((250, 92),(F2a),(0,0,0),font=(font_style3))
    draw.text((150, 5),(F3a),(255,255,255),font=(font_style2))
    draw = ImageDraw.Draw(img)
    img.save("barsp/scorebar6a.png")
    img = Image.open("barsp/master3.png")
    draw = ImageDraw.Draw(img)
    draw.text((60, 75),(G1),(0,0,0),font=(font_style3))
    draw.text((210, 75),(G2),(0,0,0),font=(font_style3))
    draw.text((140, 15),(G3),(255,255,255),font=(font_style2))
    draw = ImageDraw.Draw(img)
    img.save("barsp/master4.png")
singlea = Label(f0, text = "Rink 2", font="Aria 12 bold").place(x = 390,y = 0)
namea = Label(f0, text = "Team 1", font="Aria 10 bold", fg="blue").place(x = 320, y = 40)
name1a = Label(f0, text = "Team 2", font="Aria 10 bold", fg="red").place(x = 320, y = 80)
Homea = Label(f0, text = "Home", font="Aria 10 bold", fg="blue").place(x = 330, y = 120)
Awaya = Label(f0, text = "Aways", font="Aria 10 bold", fg="green").place(x = 430, y = 120)
Endsa = Label(f0, text = "Ends", font="Aria 10 bold", fg="red").place(x = 530, y = 120)
La = Label(f0, text = root.scorea, font="Aria 14 bold")
La.place(x = 330, y = 140)
Ka = Label(f0, text = root.score2a, font="Aria 14 bold")
Ka.place(x = 430, y = 140)
Ja = Label(f0, text = root.score3a, font="Aria 14 bold")
Ja.place(x = 530, y = 140)
player1_entrya = Entry(f0, textvariable = player1a, width = "25")
player1_entrya.place(x = 380, y = 40)
player2_entrya = Entry(f0, textvariable = player2a, width = "25")
player2_entrya.place(x = 380, y = 80)
btn1a = Button(f0, text="Save", font="Aria 8 bold", relief="solid", command=save_infoa, fg="blue", bg="white").place(x = 540, y = 80)
ba = Button(f0, text="+", font="Aria 8 bold", relief="solid", command=clickeda).place(x = 350, y = 170)
b2a = Button(f0, text="+", font="Aria 8 bold", relief="solid", command=clicked2a).place(x = 450, y = 170)
b3a = Button(f0, text="+", font="Aria 8 bold", relief="solid", command=clicked3a).place(x = 550, y = 170)
b4a = Button(f0, text="-", font="Aria 8 bold", relief="solid", command=clicked4a).place(x = 330, y = 170)
b5a = Button(f0, text="-", font="Aria 8 bold", relief="solid", command=clicked5a).place(x = 430, y = 170)
b6a = Button(f0, text="-", font="Aria 8 bold", relief="solid", command=clicked6a).place(x = 530, y = 170)
def save_infob():
    player1_infob = player1b.get()
    player2_infob = player2b.get()
    with open("text/scP1b.txt", "w") as file:
        file.write(player1_infob)
    with open("text/scP2b.txt", "w") as file:
        file.write(player2_infob)
    img = Image.open("barsp/scorebar1b.png")
    draw = ImageDraw.Draw(img)
    draw.text((10, 12),(player1_infob),(255,255,255),font=(font_style1))
    draw.text((10, 61),(player2_infob),(255,255,255),font=(font_style1))
    draw = ImageDraw.Draw(img)
    img.save("barsp/scorebar2b.png")
    img = Image.open("barsp/scorebar4b.png")
    draw = ImageDraw.Draw(img)
    draw.text((10, 47),(player1_infob),(255,255,255),font=(font_style1))
    draw.text((10, 95),(player2_infob),(255,255,255),font=(font_style1))
    draw = ImageDraw.Draw(img)
    img.save("barsp/scorebar5b.png")
def clickedb():
    global total_score_team1, total_score_team2, total_score_team3
    total_score_team1 += 1
    root.scoreb += 1
    Lb['text'] = ' ' + str(root.scoreb)
    Lc['text'] = ' ' + str(total_score_team1)
    Kc['text'] = ' ' + str(total_score_team2)
    Jc['text'] = ' ' + str(total_score_team3)
    with open("text/P1b.txt", "w") as file:
        file.write(str(root.scoreb))
    with open("text/T1.txt", "w") as file:
        file.write(str(total_score_team1))
    with open("text/P1b.txt", "r") as fb:
        F1b = fb.read()
    with open("text/P2b.txt", "r") as gb:
        F2b = gb.read()
    with open("text/E1b.txt", "r") as eb:
        F3b = eb.read()
    with open("text/T1.txt", "r") as x:
        G1 =x.read()
    with open("text/T2.txt", "r") as y:
        G2 =y.read()
    with open("text/T3.txt", "r") as z:
        G3 =z.read()  
    img = Image.open("barsp/scorebar2b.png")
    draw = ImageDraw.Draw(img)
    draw.text((250, 8),(F1b),(0,0,0),font=(font_style3))
    draw.text((250, 56),(F2b),(0,0,0),font=(font_style3))
    draw.text((150, 105),(F3b),(255,255,255),font=(font_style2))
    draw = ImageDraw.Draw(img)
    img.save("barsp/scorebar3b.png")
    img = Image.open("barsp/scorebar5b.png")
    draw = ImageDraw.Draw(img)
    draw.text((250, 47),(F1b),(0,0,0),font=(font_style3))
    draw.text((250, 92),(F2b),(0,0,0),font=(font_style3))
    draw.text((150, 5),(F3b),(255,255,255),font=(font_style2))
    draw = ImageDraw.Draw(img)
    img.save("barsp/scorebar6b.png")
    img = Image.open("barsp/master3.png")
    draw = ImageDraw.Draw(img)
    draw.text((60, 75),(G1),(0,0,0),font=(font_style3))
    draw.text((210, 75),(G2),(0,0,0),font=(font_style3))
    draw.text((140, 15),(G3),(255,255,255),font=(font_style2))
    draw = ImageDraw.Draw(img)
    img.save("barsp/master4.png")
def clicked2b():
    global total_score_team1, total_score_team2, total_score_team3
    total_score_team2 += 1
    root.score2b += 1
    Kb['text'] = ' ' + str(root.score2b)
    Lc['text'] = ' ' + str(total_score_team1)
    Kc['text'] = ' ' + str(total_score_team2)
    Jc['text'] = ' ' + str(total_score_team3)
    with open("text/P2b.txt", "w") as file:
        file.write(str(root.score2b))
    with open("text/T2.txt", "w") as file:
        file.write(str(total_score_team2))       
    with open("text/P1b.txt", "r") as fb:
        F1b = fb.read()
    with open("text/P2b.txt", "r") as gb:
        F2b = gb.read()
    with open("text/E1b.txt", "r") as eb:
        F3b = eb.read()
    with open("text/T1.txt", "r") as x:
        G1 =x.read()
    with open("text/T2.txt", "r") as y:
        G2 =y.read()
    with open("text/T3.txt", "r") as z:
        G3 =z.read()          
    img = Image.open("barsp/scorebar2b.png")
    draw = ImageDraw.Draw(img)
    draw.text((250, 8),(F1b),(0,0,0),font=(font_style3))
    draw.text((250, 56),(F2b),(0,0,0),font=(font_style3))
    draw.text((150, 105),(F3b),(255,255,255),font=(font_style2))
    draw = ImageDraw.Draw(img)
    img.save("barsp/scorebar3b.png")
    img = Image.open("barsp/scorebar5b.png")
    draw = ImageDraw.Draw(img)
    draw.text((250, 47),(F1b),(0,0,0),font=(font_style3))
    draw.text((250, 92),(F2b),(0,0,0),font=(font_style3))
    draw.text((150, 5),(F3b),(255,255,255),font=(font_style2))
    draw = ImageDraw.Draw(img)
    img.save("barsp/scorebar6b.png")
    img = Image.open("barsp/master3.png")
    draw = ImageDraw.Draw(img)
    draw.text((60, 75),(G1),(0,0,0),font=(font_style3))
    draw.text((210, 75),(G2),(0,0,0),font=(font_style3))
    draw.text((140, 15),(G3),(255,255,255),font=(font_style2))
    draw = ImageDraw.Draw(img)
    img.save("barsp/master4.png")
def clicked3b():
    global total_score_team1, total_score_team2, total_score_team3
    total_score_team3 += 1
    root.score3b += 1
    Jb['text'] = ' ' + str(root.score3b)
    Lc['text'] = ' ' + str(total_score_team1)
    Kc['text'] = ' ' + str(total_score_team2)
    Jc['text'] = ' ' + str(total_score_team3)
    with open("text/E1b.txt", "w") as file:
        file.write(str(root.score3b))
    with open("text/T3.txt", "w") as file:
        file.write(str(total_score_team3))      
    with open("text/P1b.txt", "r") as fb:
        F1b = fb.read()
    with open("text/P2b.txt", "r") as gb:
        F2b = gb.read()
    with open("text/E1b.txt", "r") as eb:
        F3b = eb.read()
    with open("text/T1.txt", "r") as x:
        G1 =x.read()
    with open("text/T2.txt", "r") as y:
        G2 =y.read()
    with open("text/T3.txt", "r") as z:
        G3 =z.read()  
    img = Image.open("barsp/scorebar2b.png")
    draw = ImageDraw.Draw(img)
    draw.text((250, 8),(F1b),(0,0,0),font=(font_style3))
    draw.text((250, 56),(F2b),(0,0,0),font=(font_style3))
    draw.text((150, 105),(F3b),(255,255,255),font=(font_style2))
    draw = ImageDraw.Draw(img)
    img.save("barsp/scorebar3b.png")
    img = Image.open("barsp/scorebar5b.png")
    draw = ImageDraw.Draw(img)
    draw.text((250, 47),(F1b),(0,0,0),font=(font_style3))
    draw.text((250, 92),(F2b),(0,0,0),font=(font_style3))
    draw.text((150, 5),(F3b),(255,255,255),font=(font_style2))
    draw = ImageDraw.Draw(img)
    img.save("barsp/scorebar6b.png")
    img = Image.open("barsp/master3.png")
    draw = ImageDraw.Draw(img)
    draw.text((60, 75),(G1),(0,0,0),font=(font_style3))
    draw.text((210, 75),(G2),(0,0,0),font=(font_style3))
    draw.text((140, 15),(G3),(255,255,255),font=(font_style2))
    draw = ImageDraw.Draw(img)
    img.save("barsp/master4.png")
def clicked4b():
    global total_score_team1, total_score_team2, total_score_team3
    if root.scoreb > 0:
        root.scoreb -= 1
    total_score_team1 -= 1    
    Lb['text'] = ' ' + str(root.scoreb)
    Lc['text'] = ' ' + str(total_score_team1)
    Kc['text'] = ' ' + str(total_score_team2)
    Jc['text'] = ' ' + str(total_score_team3)
    with open("text/P1b.txt", "w") as file:
        file.write(str(root.scoreb))
    with open("text/T1.txt", "w") as file:
        file.write(str(total_score_team1))   
    with open("text/P1b.txt", "r") as fb:
        F1b = fb.read()
    with open("text/P2b.txt", "r") as gb:
        F2b = gb.read()
    with open("text/E1b.txt", "r") as eb:
        F3b = eb.read()
    with open("text/T1.txt", "r") as x:
        G1 =x.read()
    with open("text/T2.txt", "r") as y:
        G2 =y.read()
    with open("text/T3.txt", "r") as z:
        G3 =z.read()  
    img = Image.open("barsp/scorebar2b.png")
    draw = ImageDraw.Draw(img)
    draw.text((250, 8),(F1b),(0,0,0),font=(font_style3))
    draw.text((250, 56),(F2b),(0,0,0),font=(font_style3))
    draw.text((150, 105),(F3b),(255,255,255),font=(font_style2))
    draw = ImageDraw.Draw(img)
    img.save("barsp/scorebar3b.png")
    img = Image.open("barsp/scorebar5b.png")
    draw = ImageDraw.Draw(img)
    draw.text((250, 47),(F1b),(0,0,0),font=(font_style3))
    draw.text((250, 92),(F2b),(0,0,0),font=(font_style3))
    draw.text((150, 5),(F3b),(255,255,255),font=(font_style2))
    draw = ImageDraw.Draw(img)
    img.save("barsp/scorebar6b.png")
    img = Image.open("barsp/master3.png")
    draw = ImageDraw.Draw(img)
    draw.text((60, 75),(G1),(0,0,0),font=(font_style3))
    draw.text((210, 75),(G2),(0,0,0),font=(font_style3))
    draw.text((140, 15),(G3),(255,255,255),font=(font_style2))
    draw = ImageDraw.Draw(img)
    img.save("barsp/master4.png")
def clicked5b():
    global total_score_team1, total_score_team2, total_score_team3
    if root.score2b > 0:
        root.score2b -= 1
    total_score_team2 -= 1    
    Kb['text'] = ' ' + str(root.score2b)
    Lc['text'] = ' ' + str(total_score_team1)
    Kc['text'] = ' ' + str(total_score_team2)
    Jc['text'] = ' ' + str(total_score_team3)
    with open("text/P2b.txt", "w") as file:
        file.write(str(root.score2b))
    with open("text/T2.txt", "w") as file:
        file.write(str(total_score_team2))       
    with open("text/P1b.txt", "r") as fb:
        F1b = fb.read()
    with open("text/P2b.txt", "r") as gb:
        F2b = gb.read()
    with open("text/E1b.txt", "r") as eb:
        F3b = eb.read()
    with open("text/T1.txt", "r") as x:
        G1 =x.read()
    with open("text/T2.txt", "r") as y:
        G2 =y.read()
    with open("text/T3.txt", "r") as z:
        G3 =z.read()  
    img = Image.open("barsp/scorebar2b.png")
    draw = ImageDraw.Draw(img)
    draw.text((250, 8),(F1b),(0,0,0),font=(font_style3))
    draw.text((250, 56),(F2b),(0,0,0),font=(font_style3))
    draw.text((150, 105),(F3b),(255,255,255),font=(font_style2))
    draw = ImageDraw.Draw(img)
    img.save("barsp/scorebar3b.png")
    img = Image.open("barsp/scorebar5b.png")
    draw = ImageDraw.Draw(img)
    draw.text((250, 47),(F1b),(0,0,0),font=(font_style3))
    draw.text((250, 92),(F2b),(0,0,0),font=(font_style3))
    draw.text((150, 5),(F3b),(255,255,255),font=(font_style2))
    draw = ImageDraw.Draw(img)
    img.save("barsp/scorebar6b.png")
    img = Image.open("barsp/master3.png")
    draw = ImageDraw.Draw(img)
    draw.text((60, 75),(G1),(0,0,0),font=(font_style3))
    draw.text((210, 75),(G2),(0,0,0),font=(font_style3))
    draw.text((140, 15),(G3),(255,255,255),font=(font_style2))
    draw = ImageDraw.Draw(img)
    img.save("barsp/master4.png")
def clicked6b():
    global total_score_team1, total_score_team2, total_score_team3
    if root.score3b > 0:
        root.score3b -= 1
    total_score_team3 -= 1  
    Jb['text'] = ' ' + str(root.score3b)
    Lc['text'] = ' ' + str(total_score_team1)
    Kc['text'] = ' ' + str(total_score_team2)
    Jc['text'] = ' ' + str(total_score_team3)
    with open("text/E1b.txt", "w") as file:
        file.write(str(root.score3b))
    with open("text/T3.txt", "w") as file:
        file.write(str(total_score_team3))        
    with open("text/P1b.txt", "r") as fb:
        F1b = fb.read()
    with open("text/P2b.txt", "r") as gb:
        F2b = gb.read()
    with open("text/E1b.txt", "r") as eb:
        F3b = eb.read()
    with open("text/T1.txt", "r") as x:
        G1 =x.read()
    with open("text/T2.txt", "r") as y:
        G2 =y.read()
    with open("text/T3.txt", "r") as z:
        G3 =z.read()  
    img = Image.open("barsp/scorebar2b.png")
    draw = ImageDraw.Draw(img)
    draw.text((250, 8),(F1b),(0,0,0),font=(font_style3))
    draw.text((250, 56),(F2b),(0,0,0),font=(font_style3))
    draw.text((150, 105),(F3b),(255,255,255),font=(font_style2))
    draw = ImageDraw.Draw(img)
    img.save("barsp/scorebar3b.png")
    img = Image.open("barsp/scorebar5b.png")
    draw = ImageDraw.Draw(img)
    draw.text((250, 47),(F1b),(0,0,0),font=(font_style3))
    draw.text((250, 92),(F2b),(0,0,0),font=(font_style1))
    draw.text((150, 5),(F3b),(255,255,255),font=(font_style2))
    draw = ImageDraw.Draw(img)
    img.save("barsp/scorebar6b.png")
    img = Image.open("barsp/master3.png")
    draw = ImageDraw.Draw(img)
    draw.text((60, 75),(G1),(0,0,0),font=(font_style3))
    draw.text((210, 75),(G2),(0,0,0),font=(font_style3))
    draw.text((140, 15),(G3),(255,255,255),font=(font_style2))
    draw = ImageDraw.Draw(img)
    img.save("barsp/master4.png")
singleb = Label(f0, text = "Rink 3", font="Aria 12 bold").place(x = 690,y = 0)
nameb = Label(f0, text = "Team 1", font="Aria 10 bold", fg="blue").place(x = 620, y = 40)
nameb2 = Label(f0, text = "Team 2", font="Aria 10 bold", fg="red").place(x = 620, y = 80)
Homeb = Label(f0, text = "Home", font="Aria 10 bold", fg="blue").place(x = 630, y = 120)
Awayb = Label(f0, text = "Aways", font="Aria 10 bold", fg="green").place(x = 730, y = 120)
Endsb = Label(f0, text = "Ends", font="Aria 10 bold", fg="red").place(x = 830, y = 120)
Lb = Label(f0, text = root.scoreb, font="Aria 14 bold")
Lb.place(x = 630, y = 140)
Kb = Label(f0, text = root.score2b, font="Aria 14 bold")
Kb.place(x = 730, y = 140)
Jb = Label(f0, text = root.score3b, font="Aria 14 bold")
Jb.place(x = 830, y = 140)
player1_entryb = Entry(f0, textvariable = player1b, width = "25")
player1_entryb.place(x = 680, y = 40)
player2_entryb = Entry(f0, textvariable = player2b, width = "25")
player2_entryb.place(x = 680, y = 80)
btn1b = Button(f0, text="Save", font="Aria 8 bold", relief="solid", command=save_infob, fg="blue", bg="white").place(x = 840, y = 80)
bb = Button(f0, text="+", font="Aria 8 bold", relief="solid", command=clickedb).place(x = 650, y = 170)
b2b = Button(f0, text="+", font="Aria 8 bold", relief="solid", command=clicked2b).place(x = 750, y = 170)
b3b = Button(f0, text="+", font="Aria 8 bold", relief="solid", command=clicked3b).place(x = 850, y = 170)
b4b = Button(f0, text="-", font="Aria 8 bold", relief="solid", command=clicked4b).place(x = 630, y = 170)
b5b = Button(f0, text="-", font="Aria 8 bold", relief="solid", command=clicked5b).place(x = 730, y = 170)
b6b = Button(f0, text="-", font="Aria 8 bold", relief="solid", command=clicked6b).place(x = 830, y = 170)
Label(f1, text = "Font truetype", font = "none 8 bold").place(x = 5,y = 30)
Button(f1, text="Select", command=clickee, fg="blue", bg="white", relief="solid").place(x = 277, y = 30)
Label(f1, text = "Scorebar Customizer", font="none 12 bold").place(x = 100,y = 5)
Label(f1, text = "Name Size", font="none 8 bold").place(x = 5,y = 60)
Label(f1, text = "End Size", font="none 8 bold").place(x = 5,y = 90)
Label(f1, text = "End Size end", font="none 8 bold").place(x = 5,y = 120)
Label(f1, text = "Name1 Colour", font="none 8 bold").place(x = 375,y = 30)
Label(f1, text = "Name2 Colour", font="none 8 bold").place(x = 375,y = 60)
Label(f1, text = "S01 Colour", font="none 8 bold").place(x = 375,y = 90)
Label(f1, text = "S02 Colour", font="none 8 bold").place(x = 375,y = 120)
Button(f1, text="Select", command=clickee, fg="blue", bg="white", relief="solid").place(x = 277, y = 30)
Button(f1, text="Decrease", width=7,command=decrease1, fg="blue", bg="white", relief="solid").place(x = 95, y = 60)
Button(f1, text="Increase", width=7,command=increase1, fg="blue", bg="white", relief="solid").place(x = 185, y = 60)
Button(f1, text="Decrease", width=7,command=decrease2, fg="blue", bg="white", relief="solid").place(x = 95, y = 90)
Button(f1, text="Increase", width=7,command=increase2, fg="blue", bg="white", relief="solid").place(x = 185, y = 90)
Button(f1, text="Decrease", width=7,command=decrease3, fg="blue", bg="white", relief="solid").place(x = 95, y = 120)
Button(f1, text="Increase", width=7,command=increase3, fg="blue", bg="white", relief="solid").place(x = 185, y = 120)
Button(f1, text="Choose Colour", command=save, fg="blue", bg="white", relief="solid").place(x = 460, y = 30)
Button(f1, text="Choose Colour", command=save2, fg="blue", bg="white", relief="solid").place(x = 460, y = 60)
Button(f1, text="Choose Colour", command=save3, fg="blue", bg="white", relief="solid").place(x = 460, y = 90)
Button(f1, text="Choose Colour", command=save4, fg="blue", bg="white", relief="solid").place(x = 460, y = 120)
L1 = Label(f1, text = root.score4, font="Aria 14 bold")
L1.place(x = 280, y = 60)
L2 = Label(f1, text = root.score5, font="Aria 14 bold")
L2.place(x = 280, y = 90)
L3 = Label(f1, text = root.score6, font="Aria 14 bold")
L3.place(x = 280, y = 120)
Button(f0, text='Custom', command=lambda:raise_frame(f1), fg="blue", relief="solid").place(x = 10, y = 210)
Button(f1, text='score', command=lambda:raise_frame(f0), fg="blue", relief="solid").place(x = 250, y = 210)
raise_frame(f0)
root.wm_attributes("-topmost", 1)
root.resizable(0, 0)
root.mainloop()
