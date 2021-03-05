import sqlite3
import time
import sys
import tkinter as tk
from tkinter import *
import random
from HighScore import *
def generalQuiz():
        
    def counter():
            curr = 0
            for i in range(20, 0, -1):
                
                if i == 1:
                    curr = -1
                try:
                    timer.configure(text=i)
                    genFrame.update()
                    time.sleep(1)
                except:
                    print("")
                    
                    
            try:
                timer.configure(text="Times is up!")
            except:
                print("")
                
            if curr==-1:
                return (-1)
            else:
                
                return 0

    def calc():
            global points
            if (chosen.get() == genQs[x][2] ):
                points = points + 1
            showQ()

    def showQ():
        
        if len(l) == 1:
            gen.destroy()
            showScore(points)
        if len(l) == 2:
            nextQuestion.configure(text='End',command=calc)
                
        if l:
            a.deselect()
            b.deselect()
            c.deselect()
            d.deselect()

            x = random.choice(l[1:])
            ques.configure(text =genQs[x][0])
        
            a.configure(text=genQs[x][1][0][0])
            b.configure(text=genQs[x][1][1][0])
            c.configure(text=genQs[x][1][2][0])
            d.configure(text=genQs[x][1][3][0])
            
            
            l.remove(x)
            #print(l)
            y = counter()
            if y == -1:
                showQ()


    global gen
    gen = Tk()
    global points
    points = 0
    
    generalCanvas = Canvas(gen,width=730, height=440,bg = '#173F5F')
    generalCanvas.pack()

    genFrame = Frame(generalCanvas,bg = '#173F5F')
    genFrame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
    

    genQs = [
                [
                    "1. In which scenario does DevOps not apply?",
                    [("A. Application scenarios with high security and stability requirements", "a"),
                    ("B. Application scenarios with high time requirements", "b"),
                    ("C. Application scenarios with high human resource requirements", "c"),
                    ("D. Application scenarios with high security and stability requirements.", "d")], 
                    "a"
                ] ,
                [
                    "2. Which of the following is not the advantage of DevOps?",
                    [("A. Predictability", "a"),
                    ("B. Reproducibility", "b"),
                    ("C. Maintainability", "c"), 
                    ("D. Strict access control", "d")],
                    "d"
                ] ,
                [
                    "3. Which of the following tools can help automate deployment?",
                    [("A. AWS", "a"),
                    ("B. Git", "b"),
                    ("C. Chef", "c"),
                    ("D. Jenkins", "d")],
                    "d"
                ],
                [
                    "4. Which of the following functions can Nagios help implement? ",
                    [("A. Code management", "a"),
                    ("B. Configuration management", "b"),
                    ("C. Monitoring", "c"),
                    ("D. Log management", "d")],
                    "c"
                ],
                [
                    "5. Which of the following skills does DevOps engineer not need?",
                    [("A. Familiar with git, subversion and other source code management tools", "a"),
                    ("B. Familiar with virtual machine, such as VMware Workstation and VirtualBox.", "b"),
                    ("C. Learn about major cloud service providers, such as AWS", "c"),
                    ("D. Familiar with automation tools such as Jenkins", "d")],
                    "b"
                ],
                [
                    "6. Which of the following option is NOT the advantage of container, compared\nto virtualization?",
                    [("A. Containers provide real-time configuration and scalability", "a"),
                    ("B. Containers are lightweight", "b"),
                    ("C. Containers have better resource utilization", "c"),
                    ("D. Containers can run different operating systems", "d")],
                    "d"
                ],
                [
                    "7. Which of the following is NOT the advantage of NoSQL database over RDBMS?",
                    [("A. Support unstructured text", "a"),
                    ("B. Ability to process changes over time", "b"),
                    ("C. The simplicity of building database", "c"),
                    ("D. Support multiple data structures", "d")],
                    "c"
                ],
                [
                    "8. Which of the following is the start of flow time?",
                    [("A. The idea is put forward", "a"),
                    ("B. The request is approved", "b"),
                    ("C. The analysis is done", "c"),
                    ("D. The start of development", "d")],
                    "c"
                ],
                [
                    "19. Which of the following is the end of flow time?",
                    [("A. Run in production environment", "a"),
                    ("B. Build", "b"),
                    ("C. Integrate", "c"),
                    ("D. Test", "d")],
                    "a"
                ],

            ]
    
    l = list(range(0, len(genQs)))
    
    x = random.choice(l[0:])   
    l.remove(x) 
    ques = Label(genFrame,text =genQs[x][0], justify = LEFT,bg="#173F5F", fg="white")
    ques.place(relx=0.1,rely=0.2,anchor=W)
    global chosen
    chosen = StringVar()
    
    a = Radiobutton(genFrame,text=genQs[x][1][0][0],font="calibri 10",value="a",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue="x")
    a.place(relx=0.1,rely=0.35,anchor=W)

    b = Radiobutton(genFrame,text=genQs[x][1][1][0],font="calibri 10",value="b",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue="x")
    b.place(relx=0.1,rely=0.45,anchor=W)

    c = Radiobutton(genFrame,text=genQs[x][1][2][0],font="calibri 10",value="c",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue="x")
    c.place(relx=0.1,rely=0.55,anchor=W)

    d = Radiobutton(genFrame,text=genQs[x][1][3][0],font="calibri 10",value="d",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue="x")
    d.place(relx=0.1,rely=0.65,anchor=W)

    
    timer = Label(gen)
    timer.place(relx=0.8,rely=0.93,anchor=CENTER)
    
    submit = Button(genFrame,command=calc,text="Submit")
    submit.place(relx=0.5,rely=0.90,anchor=CENTER)
    
    nextQuestion = Button(genFrame,command=showQ,text="Next")
    nextQuestion.place(relx=0.87,rely=0.90,anchor=CENTER)

    y = counter()
    if y == -1:
        showQ()
    gen.mainloop()

def showScore(p):
    def end():
        scores.destroy()

    scores = Tk()
        
    sc = Canvas(scores, width=730, height=440,bg='#173F5F')
    sc.pack()
    
    scFrame = Frame(sc, bg = '#173F5F')
    scFrame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
    
    head = Label(scFrame,text="Your Score: \t" + str(p),fg='white',bg='#173F5F', font = "Calibri 30 bold")
    head.place(relx = 0.5, rely = 0.5, anchor = CENTER)

    submit = Button(scFrame,command=end,text="EXIT")
    submit.place(relx=0.5,rely=0.90,anchor=CENTER)



