import sqlite3
import pprint
import tkinter as tk
import sys
from tkinter import *

def gameOver(attributes, usr, r):
    def next():
        scores.destroy()
        score(attributes, usr)
    
    scores = Tk()
        
    sc = Canvas(scores, width=730, height=440,bg='#173F5F')
    sc.pack()
    
    scFrame = Frame(sc, bg = '#173F5F')
    scFrame.place(relwidth=0.9,relheight=0.8,relx=0.05,rely=0.1)
    l = Label(scFrame,text="GAME OVER!",fg='white',bg='#173F5F', font = "Calibri 30 bold")
    l.place(relx = 0.5, rely = 0.1, anchor = CENTER)

    if(r == 1):
        head = Label(scFrame,text='''Your Lead time has exceeded the maximum. 
Your project has no time left to complete the required tasks.

To improve lead time, try to go for automation and have a better 
working environment.''' ,fg='white',bg='#173F5F', font = "Calibri 16", justify = LEFT, relief="solid", width = 600, height = 6)
        head.place(relx = 0.5, rely = 0.5, anchor = CENTER)
    elif(r == 2):
        if(attributes[0] > 85):
            head = Label(scFrame,text='''You have run out the budget that was assigned to the project.
Your project was launched with limited functionality.

Try to use existing staff and working capacity to keep budget in control.''',fg='white',bg='#173F5F', font = "Calibri 16", justify = LEFT, relief="solid", width = 600, height = 5)
            head.place(relx = 0.5, rely = 0.5, anchor = CENTER)
        else:
            head = Label(scFrame,text='''You have run out the budget that was assigned to the project at an 
early stage. Your project failed to Launch.

Try to use existing staff and working capacity to keep budget in control.''',fg='white',bg='#173F5F', font = "Calibri 16", justify = LEFT, relief="solid", width = 600, height = 5)
            head.place(relx = 0.5, rely = 0.5, anchor = CENTER)

    elif(r == 3):
        head = Label(scFrame,text='''The Stakeholders of the project are disatisfied with the progress 
and have decided to shut down this project.

Try to have all stakeholders onboard before making any decision that 
may affect the course of the project.''' ,fg='white',bg='#173F5F', font = "Calibri 16", justify = LEFT, relief="solid", width = 600, height = 6)
        head.place(relx = 0.5, rely = 0.5, anchor = CENTER)
    
    

    submit = Button(scFrame, bg = "white", command = next,text="Next", width = 40, height = 1)
    submit.place(relx=0.5,rely=0.9,anchor=CENTER)
    
    scores.mainloop()

def score(attributes, usr):
    #attributes: LT,MTTR,CFR,RB,SS
    TS = ((100 - attributes[0]) * 6) + ((100 - attributes[1]) * 4) + ((100 - attributes[2]) * 3) + (attributes[3] * 5) + (attributes[4] * 5)
    
    def next():
        scores.destroy()
        writeHighScore(TS, usr)
        
    scores = Tk()
        
    sc = Canvas(scores, width=730, height=440,bg='#173F5F')
    sc.pack()
    
    scFrame = Frame(sc, bg = '#173F5F')
    scFrame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
    
    head = Label(scFrame,text="Your Score: \t" + str(TS),fg='white',bg='#173F5F', font = "Calibri 16 bold")
    head.place(relx = 0.5, rely = 0.1, anchor = CENTER)

    head = Label(scFrame,text="Your Score Breakdown" ,fg='white',bg='#173F5F', font = "Calibri 10 bold")
    head.place(relx = 0.5, rely = 0.2, anchor = CENTER)
    
    a1 = Label(scFrame,text="Lead Time: " + str(attributes[0]),fg='white',bg='#173F5F', borderwidth=1, relief="solid", width = 600, height = 2)
    a1.place(relx = 0.5, rely = 0.3, anchor = CENTER)

    a2 = Label(scFrame,text="Mean Time To Repair: " + str(attributes[1]),fg='white',bg='#173F5F', borderwidth=1, relief="solid", width = 600, height = 2)
    a2.place(relx = 0.5, rely = 0.4, anchor = CENTER)

    a3 = Label(scFrame,text="Change Failure Rate: " + str(attributes[2]),fg='white',bg='#173F5F', borderwidth=1, relief="solid", width = 600, height = 2)
    a3.place(relx = 0.5, rely = 0.5, anchor = CENTER)

    a4 = Label(scFrame,text="Remianing Budget: " + str(attributes[3]),fg='white',bg='#173F5F', borderwidth=1, relief="solid", width = 600, height = 2)
    a4.place(relx = 0.5, rely = 0.6, anchor = CENTER)

    a5 = Label(scFrame,text="Stakeholders' Satisfaction: " + str(attributes[4]),fg='white',bg='#173F5F', borderwidth=1, relief="solid", width = 300, height = 2)
    a5.place(relx = 0.5, rely = 0.7, anchor = CENTER)

    submit = Button(scFrame, bg = "white", command = next,text="Next", width = 40, height = 1)
    submit.place(relx=0.5,rely=0.90,anchor=CENTER)
    
    scores.mainloop()
    
def writeHighScore(score, usr):
    conn = sqlite3.connect('quiz.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS HighScores(USERNAME text, HIGHSCORE int,
                CONSTRAINT fk_column FOREIGN KEY (USERNAME)
                REFERENCES userSignUp (USERNAME)) ''')

    
    c.execute('''SELECT EXISTS(SELECT 1 FROM HighScores WHERE USERNAME = ?)''', (usr,))
    exists = c.fetchone()
    if(exists[0] == 1):
        c.execute('''SELECT HIGHSCORE FROM HighScores Where USERNAME = (?)''', (usr,))
        scores = c.fetchall()
        if(score > scores[0][0]):            
            c.execute('''UPDATE HighScores
                    SET HIGHSCORE = (?)
                    WHERE USERNAME = (?)
                    ''', (score, usr))
        else:
            print("Old score is higher")
            conn.commit()
            dispHighScore(usr)
    else:
        print("New High Score")
        c.execute("""INSERT INTO HighScores
                    (USERNAME, HIGHSCORE)
                    VALUES(?,?)""", (usr, score))
    conn.commit()   
    conn.close()
    dispHighScore(usr)
    
def dispHighScore(usr):
    def end():
        LB.destroy()
        try:
            sys.exit()
        except:
            print("END")
    LB = Tk()
    conn = sqlite3.connect('quiz.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM HighScores ORDER BY HIGHSCORE DESC''')
    scores = c.fetchall()

    LBCanvas = Canvas(LB, width=730, height=440,bg='#173F5F')
    LBCanvas.pack()
    LBFrame = Frame(LBCanvas, bg = '#173F5F')
    LBFrame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
    
    l = Label(LBFrame,text="Leader Board",fg='white',bg='#173F5F')
    l.place(relx = 0.5, rely = 0.05, anchor = CENTER)
    l.config(font=('Calibri 30 bold'))

    head = Label(LBFrame,text="Rank \t\t\t User Name \t\t\t Score",fg='white',bg='#173F5F', font = "Calibri 9 bold")
    head.place(relx = 0.5, rely = 0.2, anchor = CENTER)
    
    s1 = "1 \t\t\t "  + scores[0][0]  + " \t\t\t\t " + str(scores[0][1])  
    score1 = Label(LBFrame,text=s1,fg='white',bg='#173F5F', borderwidth=1, relief="sunken", width = 600, height = 2)
    score1.place(relx = 0.5, rely = 0.3, anchor = CENTER)
    if (len(scores) > 1):
        s2 = "2 \t\t\t "  + scores[1][0]  + " \t\t\t\t " + str(scores[1][1]) 
        score2 = Label(LBFrame,text=s2,fg='white',bg='#173F5F', borderwidth=1, relief="sunken", width = 600, height = 2)
        score2.place(relx = 0.5, rely = 0.4, anchor = CENTER)
    if (len(scores) > 2):
        s3 = "3 \t\t\t "  + scores[2][0]  + " \t\t\t\t " + str(scores[2][1]) 
        score3 = Label(LBFrame,text=s3,fg='white',bg='#173F5F', borderwidth=1, relief="sunken", width = 600, height = 2)
        score3.place(relx = 0.5, rely = 0.5, anchor = CENTER)
    if (len(scores) > 3):
        s4 = "4 \t\t\t "  + scores[3][0]  + " \t\t\t\t " + str(scores[3][1]) 
        score4 = Label(LBFrame,text=s4,fg='white',bg='#173F5F', borderwidth=1, relief="sunken", width = 600, height = 2)
        score4.place(relx = 0.5, rely = 0.6, anchor = CENTER)
    if (len(scores) > 4):
        s5 = "5 \t\t\t "  + scores[4][0]  + " \t\t\t\t " + str(scores[4][1]) 
        score5 = Label(LBFrame,text=s5,fg='white',bg='#173F5F', borderwidth=1, relief="sunken", width = 600, height = 2)
        score5.place(relx = 0.5, rely = 0.7, anchor = CENTER)

    submit = Button(LBFrame, bg = "white", command = end ,text="EXIT", width = 40, height = 1)
    submit.place(relx=0.5,rely=0.90,anchor=CENTER)
    
    #print(scores)
    LB.mainloop()
    return
    

#gameOver([99,54,60,50,30], "Hairs", 2)