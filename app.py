import sqlite3
import time
import sys
import tkinter as tk
from tkinter import *
import random
from HighScore import *
from genQuiz import *

def signUp():

    def addToDB():
        
        fullname = fnm.get()
        username = userr.get()
        password = pasw.get()
        department = dept.get()
        
        conn = sqlite3.connect('quiz.db')
        c = conn.cursor()

        c.execute('CREATE TABLE IF NOT EXISTS userSignUp(FULLNAME text NOT NULL, USERNAME text PRIMARY KEY, PASSWORD text NOT NULL, DEPARTMENT text)')

        c.execute("SELECT * FROM userSignUp WHERE USERNAME = (?)", (username, ))
        exists = c.fetchall()
        if exists:
            error = Label(signUpFrame,text="Username already exists! Try again!",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)
            
        else:
            c.execute("INSERT INTO userSignUp VALUES (?,?,?,?)",(fullname,username,password,department)) 
            conn.commit()
            c.execute('SELECT * FROM userSignUp')
            dat=c.fetchall()
            
            conn.close()
            login(dat)

    def login_pg():
        conn = sqlite3.connect('quiz.db')
        c = conn.cursor()
        
        c.execute('SELECT * FROM userSignUp')
        dat=c.fetchall()
        login(dat)

    starter.destroy()
    
    global signUp
    signUp = Tk()

    fullname = StringVar()
    username = StringVar()
    password = StringVar()
    department = StringVar()
    
    signUpCanvas = Canvas(signUp, width=730, height=440,bg="#173F5F")
    signUpCanvas.pack()

    signUpFrame = Frame(signUpCanvas,bg='#173F5F')
    signUpFrame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    instruct = Label(signUpFrame,text="Create an account!",fg='white',bg='#173F5F')
    instruct.config(font=('calibri 30 bold'))
    instruct.place(relx=0.28,rely=0.05)

    fnamelabel = Label(signUpFrame,text="Full Name",fg='white',bg='#173F5F')
    fnamelabel.place(relx=0.18,rely=0.3)
    fnm = Entry(signUpFrame,bg='white',textvariable = fullname)
    fnm.config(width=47)
    fnm.place(relx=0.31,rely=0.3)

    userrlabel = Label(signUpFrame,text="Username",fg='white',bg='#173F5F')
    userrlabel.place(relx=0.18,rely=0.4)
    userr = Entry(signUpFrame,bg='white',textvariable = username)
    userr.config(width=47)
    userr.place(relx=0.31,rely=0.4)

    pwdlabel = Label(signUpFrame,text="Password",fg='white',bg='#173F5F')
    pwdlabel.place(relx=0.18,rely=0.5)
    pasw = Entry(signUpFrame,bg='white',show="*",textvariable = password)
    pasw.config(width=47)
    pasw.place(relx=0.31,rely=0.5)
    
    deptlabel = Label(signUpFrame,text="Department",fg='white',bg='#173F5F')
    deptlabel.place(relx=0.18,rely=0.6)
    dept = Entry(signUpFrame,bg='white',textvariable = department)
    dept.config(width=47)
    dept.place(relx=0.31,rely=0.6)
    
    #signup BUTTON
    sp = Button(signUpFrame,text='SignUp',padx=5,pady=5,width=5,command = addToDB)
    sp.configure(width = 15,height=1, activebackground = '#173F5F', relief = RAISED)
    sp.place(relx=0.4,rely=0.8)

    log = Button(signUpFrame,text='Already have a Account?',padx=5,pady=5,width=5,command = login_pg,bg="white",fg='blue')
    log.configure(width = 16,height=1, fg='white',bg='#173F5F', relief = FLAT)
    log.place(relx=0.4,rely=0.9)

    signUp.mainloop()

def login(data):
    
    def validate():
        for x,y,z,w in data:
            if y == uname.get() and z == password.get():
                global usr
                usr = y
                choices()
                break
        else:
            error = Label(loginFrame,text="Wrong Username or Password!",fg='white',bg='#173F5F')
            error.place(relx=0.37,rely=0.7)  

    signUp.destroy()
    global l_in
    l_in = Tk()

    uname = StringVar()
    password = StringVar()

    loginCanvas = Canvas(l_in, width=730, height=440,bg='#173F5F')
    loginCanvas.pack()

    loginFrame = Frame(loginCanvas,bg='#173F5F')
    loginFrame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    instruct = Label(loginFrame,text="DevOps Game Login",fg='white',bg='#173F5F')
    instruct.config(font=('calibri 30 bold'))
    instruct.place(relx=0.2,rely=0.1)

    userrlabel = Label(loginFrame,text="Username",fg='white',bg='#173F5F')
    userrlabel.place(relx=0.18,rely=0.4)
    userr = Entry(loginFrame,fg='black',bg='white',textvariable = uname)
    userr.config(width=42)
    userr.place(relx=0.31,rely=0.4)

    pwdlabel = Label(loginFrame,text="Password",fg='white',bg='#173F5F')
    pwdlabel.place(relx=0.18,rely=0.5)
    pasw = Entry(loginFrame,fg='black',bg='white',show="*",textvariable = password)
    pasw.config(width=42)
    pasw.place(relx=0.31,rely=0.5)


    loginButton = Button(loginFrame,text='Login',padx=5,pady=5,width=5,command=validate)
    loginButton.configure(width = 15,height=1, activebackground = '#173F5F', relief = RAISED)
    loginButton.place(relx=0.4,rely=0.6)
    
    l_in.mainloop()

def choices():

    l_in.destroy()

    global choice 
    choice = Tk()
    
    
    choiceCanvas = Canvas(choice,width=730, height=440,bg="#173F5F")
    choiceCanvas.pack()

    choiceFrame = Frame(choiceCanvas,bg="#173F5F")
    choiceFrame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    
    wel = Label(choiceCanvas,text=' Welcome to the DevOps Game! ',fg="white",bg="#173F5F") 
    wel.config(font=('Broadway 22 bold '))
    wel.place(relx=0.1,rely=0.02)
    
    
    level = Label(choiceFrame,text='Select the game type.',bg="#173F5F",fg = 'white', font="calibri 18")
    level.place(relx=0.25,rely=0.3)
    
    
    ch = IntVar()
    
    genr = Radiobutton(choiceFrame,text='General DevOps Quiz',bg="#173F5F",font="calibri 16", fg="white",value=1,variable = ch, activebackground="#173F5F", selectcolor = "#173F5F", justify = LEFT )
    genr.place(relx=0.25,rely=0.5)
    
    airbnbg = Radiobutton(choiceFrame,text='Airbnb DevOps Simulation',bg="#173F5F",font="calibri 16", fg="white",value=2,variable = ch, activebackground="#173F5F", selectcolor = "#173F5F"  , justify = LEFT)
    airbnbg.place(relx=0.25,rely=0.6)
    
    
    def decide():
        
        a = ch.get()
        
        if a == 1:
            choice.destroy()
            generalQuiz()
        elif a == 2:
            choice.destroy()
            airbnbSimulation()
        else:
            pass
    
    letsgo = Button(choiceFrame,text="Let's Go",bg="#173F5F", fg="white", font="calibri 12",command=decide, relief = RAISED)
    letsgo.place(relx=0.25,rely=0.8)
    choice.mainloop()


def airbnbSimulation():
    global game
    game = Tk()

    global attributes
    #attributes: LT, MTTR, CFR, RB, SS
    attributes = [60, 30, 10, 100, 100]


    def attribUpdate(change):
        for i in range(0,len(attributes)):
            attributes[i] = attributes[i]+change[i]

            if (i==0 and attributes[i]>=100):
                game.destroy()
                gameOver(attributes, usr, 1)
            if (i==3 and attributes[i]<=0):
                game.destroy()
                gameOver(attributes, usr, 2)
            if (i==4 and attributes[i]<=0):
                game.destroy()
                gameOver(attributes, usr, 3)
        return

    def gameDetail():

        def firstPrompt():
            mlabel.configure(text = "The main features to be included in the system are:  \n \n (1) User Should Be Able To Post An Advertisement \n (2) User Should Be Able To Search For The Accommodations \n (3) User Should Be Able To Save Favorite Rental Homes And Places \n (4) In-app Messaging To The Property Owner \n (5) Ratings and Reviews \n (6) Real-time Updates And Notifications.")
            letsgo.configure(text = "Next", command=nextPrompt)
        def nextPrompt():
            mlabel.configure(text = "The system that is to be developed will entertain a big audience, \n especially during the holiday season when a lot of people are trying to book \n accommodations at the same time and the server needs to deal with multiple requests. \n \n This involves the number of visitors, traffic patterns, and features that users may access on your website. \n For instance, if your web has 10,000 concurrent users at its maximum, but 3,000 visit in the \n morning and that number gradually rises up to 10,000 in the afternoon—and these users mainly \n only search your homepage—you'll have to run a different test than if you've got 10,000 \n concurrent users on your site all day long, who continuously search several pages or access \n several features on your website. \n \n Keep this in your mind while handling the next two scenarios.")
            letsgo.configure(text = "Next", command=s1)
        firstPrompt()


    def s1():
        
        def calc():
            #attributes: LT, MTTR, CFR, RB, SS
            if (chosen.get() == "a"):
                attribUpdate([5,3,3,0,0])
            elif (chosen.get() == "b"):
                attribUpdate([-3,-2,0,-4,0])
            elif (chosen.get() == "c"):
                attribUpdate([3,1,2,-1,0])

            mlabel.place(relx=200,rely=200,anchor=CENTER)
            
            #print(attributes)
            s2()
            
        def promptAfter():
            
            a.destroy()
            b.destroy()
            c.destroy()
            qlabel.destroy()
            scoresLabel.destroy()
            
            mlabel.configure(text = "Load tests should be carried out across the software development lifecycle: \n APIs, components, microservices, and system-wide by using performance test metrics translate \n into pass/fail results to automate the Continuous Delivery pipeline, and the \n ‘Load Goals’ need to be defined as early as possible!")
            mlabel.place(relx=0.5,rely=0.5,anchor=CENTER)
            letsgo.configure(text = "Next", command=calc)
            
        mlabel.place(relx=200,rely=200,anchor=CENTER)

        
        promptq = "You need to get a common view of application reliability and speed at every stage \n of the development to identify and fix performance bottlenecks. \n In this situation, which one of the following actions to take?"
        qlabel = Label(gameCanvas,justify = LEFT,text=promptq,bg="#173F5F", fg = 'white')
        qlabel.place(relx=0.5,rely=0.3,anchor=CENTER)

        chosen = StringVar()
    
        a = Radiobutton(gameFrame,text="It is too early to consider or establish goals to carry out load tests. \n If needed, these can be carried out in the later stages of deployment.",font="calibri 10",value="a",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue="x")
        a.place(relx=0.5,rely=0.4,anchor=CENTER)

        b = Radiobutton(gameFrame,text="‘Load Goals’ should be established from the very start (through direct engagement \n with business colleagues and key stakeholders), and you should \n search tools to help you with the process.",font="calibri 10",value="b",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue="x")
        b.place(relx=0.5,rely=0.55,anchor=CENTER)

        c = Radiobutton(gameFrame,text="Load tests should be carried out across the software development lifecycle, \n but ‘Load Goals’ do not need to be at such an early stage.",font="calibri 10",value="c",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue="x")
        c.place(relx=0.5,rely=0.7,anchor=CENTER)

        letsgo.configure(text = "Submit", command=promptAfter)

        scores = "LT = " + str(attributes[0]) + "     MTTR = " + str(attributes[1]) + "     CFR = " + str(attributes[2]) + "     RB = " + str(attributes[3]) + "     SS = " + str(attributes[4])
        scoresLabel = Label(gameCanvas,text=scores,fg="white", bg = '#173F5F')
        scoresLabel.place(relx=0.5,rely=0.95,anchor=CENTER)


    def s2():
        
        def calcS2():
           #attributes: LT, MTTR, CFR, RB, SS
            if (chosen.get() == "a"):
                attribUpdate([-5,-2,0,-1,0])
            elif (chosen.get() == "b"):
                attribUpdate([3,4,6,-2,0])
            
            a.destroy()
            b.destroy()
            qlabel.destroy()
            scoresLabel.destroy()
            
            mlabel.configure(text = "")
            print(attributes)
            s3()

        
        scores = "LT = " + str(attributes[0]) + "     MTTR = " + str(attributes[1]) + "     CFR = " + str(attributes[2]) + "     RB = " + str(attributes[3]) + "     SS = " + str(attributes[4])
        scoresLabel = Label(gameCanvas,text=scores,fg="white", bg = '#173F5F')
        scoresLabel.place(relx=0.5,rely=0.95,anchor=CENTER)
        
            
        promptq = "Now, what would you do to ensure that the CPU stays \n low and you do not experience any memory leaks?"
        qlabel = Label(gameCanvas,justify = LEFT,text=promptq,bg="#173F5F", fg="white")
        qlabel.place(relx=0.5,rely=0.3,anchor=CENTER)
        
        chosen = StringVar()

        a = Radiobutton(gameFrame,text="To make sure you stand up to your load goals, you need a buffer; \n specifically, you need to make sure that your system can handle heavier loads; \n also, take your system to the limit and see when and how it fails.",font="calibri 10",value="a",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue=0)
        a.place(relx=0.5,rely=0.5,anchor=CENTER)

        b = Radiobutton(gameFrame,text="A buffer is not needed as the ‘Load Goals’ that are set are \n pretty strict. Hence, just testing the system to its limits \n and seeing when and how it fails is enough.",font="calibri 10",value="b",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue=0)
        b.place(relx=0.5,rely=0.65,anchor=CENTER)

        letsgo.configure(text = "Submit", command=calcS2)
            
        
    def s3():

        def calcS3():
            #attributes: LT, MTTR, CFR, RB, SS
            if (chosen.get() == "a"):
                attribUpdate([2,5,5,0,0])
            elif (chosen.get() == "b"):
                attribUpdate([-1,-1,0,0,0])
            elif (chosen.get() == "c"):
                attribUpdate([3,3,4,0,0])
            
            a.destroy()
            b.destroy()
            c.destroy()
            qlabel.destroy()
            scoresLabel.destroy()
            
            #mlabel.configure(text = "")
            print(attributes)

            s4()

            
        scores = "LT = " + str(attributes[0]) + "     MTTR = " + str(attributes[1]) + "     CFR = " + str(attributes[2]) + "     RB = " + str(attributes[3]) + "     SS = " + str(attributes[4])
        scoresLabel = Label(gameCanvas,text=scores,fg="white", bg = '#173F5F')
        scoresLabel.place(relx=0.5,rely=0.95,anchor=CENTER)

        promptq = "The project has started. Your team is using Git to collaborate \n on the project. You are noticing inconsistent repositories and you are \n not able to see the change history. What do you \n think is the issue here that you will need to fix?"
        qlabel = Label(gameCanvas,justify = LEFT,text=promptq,fg="white", bg = '#173F5F')
        qlabel.place(relx=0.5,rely=0.3,anchor=CENTER)
        
        chosen = StringVar()

        a = Radiobutton(gameFrame,text="A developer is not integrating the contents of the feature branch \n to the master branch.",font="calibri 10",value="a",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue=0)
        a.place(relx=0.5,rely=0.41,anchor=CENTER)

        b = Radiobutton(gameFrame,text="A developer is using ‘git rebase’ instead of ‘git merge’.",font="calibri 10",value="b",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue=0)
        b.place(relx=0.5,rely=0.51,anchor=CENTER)

        c = Radiobutton(gameFrame,text="A developer is using ‘git merge’ instead of ‘git rebase’.",font="calibri 10",value="c",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue=0)
        c.place(relx=0.5,rely=0.61,anchor=CENTER)
        

        letsgo.configure(text = "Submit", command=calcS3)
        

    def s4():
        def Prompt():
            mlabel.configure(text = '''Uh oh! You made the sponsors angry. Now they've agreed to raise
the budget. Proceede to the next scenario ''')
            mlabel.place(relx=0.5,rely=0.5,anchor=CENTER)
            letsgo.configure(text = "Next", command=s9)


        def calcS4():
            
            a.destroy()
            b.destroy()
            c.destroy()
            d.destroy()
            qlabel.destroy()
            scoresLabel.destroy()
            
            #attributes: LT, MTTR, CFR, RB, SS
            if (chosen.get() == "a"):
                attribUpdate([0,0,0,0,-10])
                Prompt()
            elif (chosen.get() == "b"):
                attribUpdate([3,0,5,-10,0])
                s5()
            elif (chosen.get() == "c"):
                attribUpdate([-5,0,0,0,-5])
                s9()
            elif (chosen.get() == "d"):
                attribUpdate([0,0,0,-30,5])
                s9()

        mlabel.place(relx=200,rely=200,anchor=CENTER)  
        scores = "LT = " + str(attributes[0]) + "     MTTR = " + str(attributes[1]) + "     CFR = " + str(attributes[2]) + "     RB = " + str(attributes[3]) + "     SS = " + str(attributes[4])
        scoresLabel = Label(gameCanvas,text=scores,fg="white", bg = '#173F5F')
        scoresLabel.place(relx=0.5,rely=0.95,anchor=CENTER)

        promptq = "Let me remind you of a function that we said we would deploy: \n (4) in-app messaging to the property owner \n The project seemed to have an ample budget before the CEO requested \n to add a feature where you can connect with your friends and send \n them accommodation details in-app to plan a trip together. \n While this is an extension of feature (4), the issue is that the \n extension still requires extra manpower and resources, so it \n probably is going to exceed the budget. \n What do you think we should do now?"
        qlabel = Label(gameCanvas,justify = LEFT,text=promptq, bg="#173F5F", fg = 'white')
        qlabel.place(relx=0.5,rely=0.3,anchor=CENTER)
        
        chosen = StringVar()

        a = Radiobutton(gameFrame,text="Tell the stakeholder that this feature cannot be implemented.",font="calibri 10",value="a",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue=0)
        a.place(relx=0.5,rely=0.5,anchor=CENTER)

        b = Radiobutton(gameFrame,text="You make a trade-off by not implementing some small components of a few \n features that may not be that important and implement this extra \n feature without asking for a raise in budget.",font="calibri 10",value="b",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue=0)
        b.place(relx=0.5,rely=0.6,anchor=CENTER)

        c = Radiobutton(gameFrame,text="Ask for a raise in budget to make up for the extra resources required.",font="calibri 10",value="c",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue=0)
        c.place(relx=0.5,rely=0.7,anchor=CENTER)

        d = Radiobutton(gameFrame,text="As you fear that this may lead to dissatisfaction of the stakeholders, \n you go a little over budget to accommodate their needs.",font="calibri 10",value="d",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F',  tristatevalue=0)
        d.place(relx=0.5,rely=0.8,anchor=CENTER)
        

        letsgo.configure(text = "Submit", command=calcS4)
########################################3
#option b s5 - s6
#option c 
    def s5():

        def calc():
            a.destroy()
            b.destroy()
            qlabel.destroy()
            scoresLabel.destroy()
            #attributes: LT, MTTR, CFR, RB, SS
            if (chosen.get() == "a"):
                attribUpdate([0,0,0,-5,-10])
            elif (chosen.get() == "b"):
                attribUpdate([0,0,0,-5,-5])
            mlabel.place(relx=200,rely=200,anchor=CENTER)
            promptAfter()

        def promptAfter():    
            a.destroy()
            b.destroy()
            qlabel.destroy()
            scoresLabel.destroy()
            
            mlabel.configure(text = "While compromising on (b), the user still has the ability to view \n the promotions in the app, whereas if we chose to drop \n the feature described in (a), the user will not have the ability to search \n the accommodation by its id. Hence, it is better to drop the \n feature described in (b).")
            mlabel.place(relx=0.5,rely=0.5,anchor=CENTER)
            letsgo.configure(text = "Next", command=s6)
                
        mlabel.place(relx=200,rely=200,anchor=CENTER)
        scores = "LT = " + str(attributes[0]) + "     MTTR = " + str(attributes[1]) + "     CFR = " + str(attributes[2]) + "     RB = " + str(attributes[3]) + "     SS = " + str(attributes[4])
        scoresLabel = Label(gameCanvas,text=scores,fg="white", bg = '#173F5F')
        scoresLabel.place(relx=0.5,rely=0.95,anchor=CENTER)

        promptq = "While considering the trade-offs, you have arrived at a dilemma. \n You must drop one of the following sub-features (because they \n are not explicitly stated in the requirements document) \n to implement the new feature that the CEO has asked you to. \n Which one would you choose?"
        qlabel = Label(gameCanvas,justify = LEFT,text=promptq,fg="white", bg = '#173F5F')
        qlabel.place(relx=0.5,rely=0.3,anchor=CENTER)
        
        chosen = StringVar()

        a = Radiobutton(gameFrame,text="The user may search the accommodation by the accommodation id.",font="calibri 10",value="a",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue=0)
        a.place(relx=0.5,rely=0.5,anchor=CENTER)

        b = Radiobutton(gameFrame,text="The user may see the promotions going on in the app but will \n not get notifications.",font="calibri 10",value="b",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue=0)
        b.place(relx=0.5,rely=0.6,anchor=CENTER)
        

        letsgo.configure(text = "Submit", command=calc)
######################
# Q6   
    def s6():
        def calc():
            a.destroy()
            b.destroy()
            c.destroy()
            qlabel.destroy()
            scoresLabel.destroy()
           #attributes: LT, MTTR, CFR, RB, SS
            if (chosen.get() == "a"):
                attribUpdate([2,0,0,-2,5])
                s7()
            elif (chosen.get() == "b"):
                attribUpdate([1,0,0,-1,-10])
                s8()
            elif (chosen.get() == "c"):
                attribUpdate([5,0,0,0,-5])
                s12()

        mlabel.place(relx=200,rely=200,anchor=CENTER)
        scores = "LT = " + str(attributes[0]) + "     MTTR = " + str(attributes[1]) + "     CFR = " + str(attributes[2]) + "     RB = " + str(attributes[3]) + "     SS = " + str(attributes[4])
        scoresLabel = Label(gameCanvas,text=scores,fg="white", bg = '#173F5F')
        scoresLabel.place(relx=0.5,rely=0.95,anchor=CENTER)

        promptq = '''You may have noticed that we did not involve the sponsors of the project in
making the decision to exclude this feature. Was it a good decision to not
include the decision of sponsors?'''
        qlabel = Label(gameCanvas,justify = LEFT,text=promptq,fg="white", bg = '#173F5F')
        qlabel.place(relx=0.5,rely=0.3,anchor=CENTER)
        
        chosen = StringVar()

        a = Radiobutton(gameFrame,text='''The sponsors should be kept informed of such decisions, so it was
not a very good practice.''',font="calibri 10",value="a",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue=0)
        a.place(relx=0.5,rely=0.4,anchor=CENTER)


        b = Radiobutton(gameFrame,text='''Since the feature was not explicitly stated in the requirements
document, it was okay to play smart and exclude it even if the
stakeholders were expecting to have it in the final deliverables.''',font="calibri 10",value="b",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue=0)
        b.place(relx=0.5,rely=0.55,anchor=CENTER)        

        c = Radiobutton(gameFrame,text='''The team working in a DevOps environment already has a lot on
their plate, so whether stakeholders are satisfied or not shouldn’t
bother them.''',font="calibri 10",value="c",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue=0)
        c.place(relx=0.5,rely=0.7,anchor=CENTER)

        letsgo.configure(text = "Submit", command=calc)
##################################
#option a Q7, b Q8


    def s7():
        def calc():
            a.destroy()
            b.destroy()
            c.destroy()
            qlabel.destroy()
            scoresLabel.destroy()
            #attributes: LT, MTTR, CFR, RB, SS
            if (chosen.get() == "a"):
                attribUpdate([5,5,10,0,-15])
            elif (chosen.get() == "b"):
                attribUpdate([-2,-2,-1,-3,0])
            elif (chosen.get() == "c"):
                attribUpdate([4,3,7,0,-10])
            s12()

        mlabel.place(relx=200,rely=200,anchor=CENTER)
        scores = "LT = " + str(attributes[0]) + "     MTTR = " + str(attributes[1]) + "     CFR = " + str(attributes[2]) + "     RB = " + str(attributes[3]) + "     SS = " + str(attributes[4])
        scoresLabel = Label(gameCanvas,text=scores,fg="white", bg = '#173F5F')
        scoresLabel.place(relx=0.5,rely=0.95,anchor=CENTER)

        promptq = '''As per your suggestion, the sponsors were informed of this decision. This
led to serious dissatisfaction. Now, they are demanding that you implement
both features. This has sparked anger amongst the developers. They have
started to hastily code, are ignoring the error messages they get while
coding and are deploying buggy code. What should you do in such a
scenario?'''
        qlabel = Label(gameCanvas,justify = LEFT,text=promptq,fg="white", bg = '#173F5F')
        qlabel.place(relx=0.5,rely=0.3,anchor=CENTER)
        
        chosen = StringVar()

        a = Radiobutton(gameFrame,text='''Communicate the significance of not having bugs in the code in the
first place and encourage the team members to perform their best.
There is no need to have a developer dedicated to fixing bugs
before deployment.''',font="calibri 10",value="a",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue=0)
        a.place(relx=0.5,rely=0.5,anchor=CENTER)


        b = Radiobutton(gameFrame,text='''Keep a team member on the call for every single day that the
development process is being performed. Ask him/her to react to
error notifications in the code and try to fix these bugs.''',font="calibri 10",value="b",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue=0)
        b.place(relx=0.5,rely=0.6,anchor=CENTER)        

        c = Radiobutton(gameFrame,text='''Even if it lowers work satisfaction, ask all the members to be
responsible for the bugs in their own codes and fix them as soon
as they encounter them.''',font="calibri 10",value="c",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue=0)
        c.place(relx=0.5,rely=0.7,anchor=CENTER)

        letsgo.configure(text = "Submit", command=calc)

    def s8():
        def Prompt():
            mlabel.configure(text = '''Add extensibility and heightened control to your blockchain network by optionally
integrating a node with native AWS and Azure services, all managed and configured
within your own organizationally-controlled cloud suite. Services include key
management, log streaming, backups and private data routing.''')
            mlabel.place(relx=0.5,rely=0.5,anchor=CENTER)
            letsgo.configure(text = "Next", command=s12)

        def calc():
            a.destroy()
            b.destroy()
            qlabel.destroy()
            scoresLabel.destroy()
            #attributes: LT, MTTR, CFR, RB, SS
            if (chosen.get() == "a"):
                attribUpdate([-2,-3,0,-2,0])
            elif (chosen.get() == "b"):
                attribUpdate([2,4,0,-5,0])
            Prompt()
            
        mlabel.place(relx=200,rely=200,anchor=CENTER)
        scores = "LT = " + str(attributes[0]) + "     MTTR = " + str(attributes[1]) + "     CFR = " + str(attributes[2]) + "     RB = " + str(attributes[3]) + "     SS = " + str(attributes[4])
        scoresLabel = Label(gameCanvas,text=scores,fg="white", bg = '#173F5F')
        scoresLabel.place(relx=0.5,rely=0.95,anchor=CENTER)

        promptq = '''Because you did not involve the key sponsors in this critical decision, your
superior fears that they might be dissatisfied when they see that this
feature is not implemented. He asks you to design the code such that this
sub-feature, if necessary, can be implemented by extending the main
feature. What approach would make the feature more extensible?'''
        qlabel = Label(gameCanvas,justify = LEFT,text=promptq,fg="white", bg = '#173F5F')
        qlabel.place(relx=0.5,rely=0.3,anchor=CENTER)
        
        chosen = StringVar()

        a = Radiobutton(gameFrame,text='''Visualize and understand critical details about your network and
deployed resources. Integrate nodes with your own
organizational-controlled cloud resources.''',font="calibri 10",value="a",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue=0)
        a.place(relx=0.5,rely=0.5,anchor=CENTER)


        b = Radiobutton(gameFrame,text='''Node integration with the organizational-controlled cloud resources
is not essential to making the feature more extensible.''',font="calibri 10",value="b",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue=0)
        b.place(relx=0.5,rely=0.6,anchor=CENTER)        

        

        letsgo.configure(text = "Submit", command=calc)

    def s9():
        
        def calc():
            a.destroy()
            b.destroy()
            qlabel.destroy()
            scoresLabel.destroy()
            #attributes: LT, MTTR, CFR, RB, SS
            if (chosen.get() == "a"):
                attribUpdate([-2,-1,0,0,0])
            elif (chosen.get() == "b"):
                attribUpdate([2,3,0,0,0])
            s10()

        mlabel.place(relx=200,rely=200,anchor=CENTER)
        scores = "LT = " + str(attributes[0]) + "     MTTR = " + str(attributes[1]) + "     CFR = " + str(attributes[2]) + "     RB = " + str(attributes[3]) + "     SS = " + str(attributes[4])
        scoresLabel = Label(gameCanvas,text=scores,fg="white", bg = '#173F5F')
        scoresLabel.place(relx=0.5,rely=0.95,anchor=CENTER)

        promptq = '''The stakeholder agrees to extend the budget. After the programming team
deploys the extension of feature (4), you find that there are scalability
issues as after the extension, the load tests keep failing. What caused this
issue of scalability in the first place?'''
        qlabel = Label(gameCanvas,justify = LEFT,text=promptq,fg="white", bg = '#173F5F')
        qlabel.place(relx=0.5,rely=0.3,anchor=CENTER)
        
        chosen = StringVar()

        a = Radiobutton(gameFrame,text='''Lack of observability and forecasting, or''',font="calibri 10",value="a",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue=0)
        a.place(relx=0.5,rely=0.5,anchor=CENTER)

        b = Radiobutton(gameFrame,text='''Lack of a clear understanding of feature requirements?''',font="calibri 10",value="b",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue=0)
        b.place(relx=0.5,rely=0.6,anchor=CENTER)        
        letsgo.configure(text = "Submit", command=calc)
        
    def s10():
        def calc():
            a.destroy()
            b.destroy()
            c.destroy()
            d.destroy()
            qlabel.destroy()
            scoresLabel.destroy()
            #attributes: LT, MTTR, CFR, RB, SS
            if (chosen.get() == "a"):
                attribUpdate([-1,-1,0,-2,0])
            elif (chosen.get() == "b"):
                attribUpdate([-1,-2,0,-2,0])
            elif (chosen.get() == "c"):
                attribUpdate([-2,-1,0,-2,0])
            elif (chosen.get() == "d"):
                attribUpdate([-2,-2,0,-3,0])    
            
            s11()

        mlabel.place(relx=200,rely=200,anchor=CENTER)
        scores = "LT = " + str(attributes[0]) + "     MTTR = " + str(attributes[1]) + "     CFR = " + str(attributes[2]) + "     RB = " + str(attributes[3]) + "     SS = " + str(attributes[4])
        scoresLabel = Label(gameCanvas,text=scores,fg="white", bg = '#173F5F')
        scoresLabel.place(relx=0.5,rely=0.95,anchor=CENTER)

        promptq = '''You suspect that the issue exists within software scaling. Your team has
suggested these approaches to improve the scalability of the code:
1. using RUM (real-user monitoring)
2. user-facing metrics such as HTTP error rates
3. understanding system behavior during load tests
Which of these processes are relevant and should be carried to enhance the
software scalability?'''
        qlabel = Label(gameCanvas,justify = LEFT,text=promptq,fg="white", bg = '#173F5F')
        qlabel.place(relx=0.5,rely=0.3,anchor=CENTER)
        
        chosen = StringVar()

        a = Radiobutton(gameFrame,text='''1 and 2 only;''',font="calibri 10",value="a",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue=0)
        a.place(relx=0.5,rely=0.5,anchor=CENTER)

        b = Radiobutton(gameFrame,text='''1 and 3 only;''',font="calibri 10",value="b",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue=0)
        b.place(relx=0.5,rely=0.6,anchor=CENTER)

        c = Radiobutton(gameFrame,text='''2 and 3 only;''',font="calibri 10",value="c",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue=0)
        c.place(relx=0.5,rely=0.7,anchor=CENTER)

        d = Radiobutton(gameFrame,text='''1, 2 and 3.;''',font="calibri 10",value="d",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue=0)
        d.place(relx=0.5,rely=0.8,anchor=CENTER)        
        letsgo.configure(text = "Submit", command=calc)

######################################
#Q11

    def s11():
        def Prompt():
            mlabel.configure(text = '''After upgrading some hardware components, the issue was resolved.''')
            mlabel.place(relx=0.5,rely=0.5,anchor=CENTER)
            letsgo.configure(text = "Next", command=s12)

        def calc():
            a.destroy()
            b.destroy()
            qlabel.destroy()
            scoresLabel.destroy()
            #attributes: LT, MTTR, CFR, RB, SS
            if (chosen.get() == "a"):
                attribUpdate([2,3,3,-2,0])
                s12()
            elif (chosen.get() == "b"):
                attribUpdate([-1,-2,-2,-3,0])
                Prompt()
               

        mlabel.place(relx=200,rely=200,anchor=CENTER)
        scores = "LT = " + str(attributes[0]) + "     MTTR = " + str(attributes[1]) + "     CFR = " + str(attributes[2]) + "     RB = " + str(attributes[3]) + "     SS = " + str(attributes[4])
        scoresLabel = Label(gameCanvas,text=scores,fg="white", bg = '#173F5F')
        scoresLabel.place(relx=0.5,rely=0.95,anchor=CENTER)

        promptq = '''After employing these techniques, it turned out that the scaling issues were
encountered because a 3 rd party software was involved in the development
of the feature. What should be the next step in this situation?'''
        qlabel = Label(gameCanvas,justify = LEFT,text=promptq,fg="white", bg = '#173F5F')
        qlabel.place(relx=0.5,rely=0.3,anchor=CENTER)
        
        chosen = StringVar()

        a = Radiobutton(gameFrame,text='''Perform load tests again with larger load limits;''',font="calibri 10",value="a",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue=0)
        a.place(relx=0.5,rely=0.5,anchor=CENTER)

        b = Radiobutton(gameFrame,text='''Explore hardware scalability issues rather than software scalability
issues.''',font="calibri 10",value="b",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue=0)
        b.place(relx=0.5,rely=0.6,anchor=CENTER)

               
        letsgo.configure(text = "Submit", command=calc)

#####################################
#Q12
    def s12():
        def calc():
            a.destroy()
            b.destroy()
            c.destroy()
            qlabel.destroy()
            scoresLabel.destroy()
            #attributes: LT, MTTR, CFR, RB, SS
            if (chosen.get() == "a"):
                attribUpdate([3,2,1,-3,-15])
                s14()
            elif (chosen.get() == "b"):
                attribUpdate([-2,-1,-1,-1,5])
                s13()
            elif (chosen.get() == "c"):
                attribUpdate([3,2,1,-3,-10])
                s14()
              

        mlabel.place(relx=200,rely=200,anchor=CENTER)
        scores = "LT = " + str(attributes[0]) + "     MTTR = " + str(attributes[1]) + "     CFR = " + str(attributes[2]) + "     RB = " + str(attributes[3]) + "     SS = " + str(attributes[4])
        scoresLabel = Label(gameCanvas,text=scores,fg="white", bg = '#173F5F')
        scoresLabel.place(relx=0.5,rely=0.95,anchor=CENTER)

        promptq = '''It has come to your attention that during the testing phase, several code
efficiency issues have emerged. A staff member suggests limiting the batch
size of the continuous DevOps deliveries. What would you do?'''
        qlabel = Label(gameCanvas,justify = LEFT,text=promptq,fg="white", bg = '#173F5F')
        qlabel.place(relx=0.5,rely=0.3,anchor=CENTER)
        
        chosen = StringVar()

        a = Radiobutton(gameFrame,text='''You will refute his suggestion as you think it is not the right approach to
deal with the issue.''',font="calibri 10",value="a",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue=0)
        a.place(relx=0.5,rely=0.5,anchor=CENTER)

        b = Radiobutton(gameFrame,text='''You think it is a good idea and you would suggest implementing it as soon
as possible to make the process smoother.''',font="calibri 10",value="b",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue=0)
        b.place(relx=0.5,rely=0.6,anchor=CENTER)

        c = Radiobutton(gameFrame,text='''You nod in agreement not to be rude, but you think that limiting the batch
size of the continuous DevOps deliveries is not the way to go.''',font="calibri 10",value="c",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue=0)
        c.place(relx=0.5,rely=0.7,anchor=CENTER)

        letsgo.configure(text = "Submit", command=calc)

#####################################
#Q13
    def s13():
        def calc():
            a.destroy()
            b.destroy()
            c.destroy()
            d.destroy()
            qlabel.destroy()
            scoresLabel.destroy()
            #attributes: LT, MTTR, CFR, RB, SS
            if (chosen.get() == "a"):
                attribUpdate([-1,-1,-1,-2,0])
            elif (chosen.get() == "b"):
                attribUpdate([-1,0,-1,-2,0])
            elif (chosen.get() == "c"):
                attribUpdate([-1,-1,0,-2,0])
            elif(chosen.get() == "d"):
                attribUpdate([-3,-2,-2,-4,0])
            cq1()

        mlabel.place(relx=200,rely=200,anchor=CENTER)
        scores = "LT = " + str(attributes[0]) + "     MTTR = " + str(attributes[1]) + "     CFR = " + str(attributes[2]) + "     RB = " + str(attributes[3]) + "     SS = " + str(attributes[4])
        scoresLabel = Label(gameCanvas,text=scores,fg="white", bg = '#173F5F')
        scoresLabel.place(relx=0.5,rely=0.95,anchor=CENTER)

        promptq = '''Seems like you are in favor of limiting the batch size. Smart move! Your
superior asks you what would be the benefit of limiting the batch size of the
continuous DevOps deliveries?'''
        qlabel = Label(gameCanvas,justify = LEFT,text=promptq,fg="white", bg = '#173F5F')
        qlabel.place(relx=0.5,rely=0.3,anchor=CENTER)
        
        chosen = StringVar()

        a = Radiobutton(gameFrame,text='''Potentially required rollbacks from your production systems will be less
cumbersome.''',font="calibri 10",value="a",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue=0)
        a.place(relx=0.5,rely=0.5,anchor=CENTER)

        b = Radiobutton(gameFrame,text='''By continuously delivering in production, your team will have the constant
pride of contributing your organizational mission.''',font="calibri 10",value="b",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue=0)
        b.place(relx=0.5,rely=0.6,anchor=CENTER)

        c = Radiobutton(gameFrame,text='''You will be quicker to identify root causes of issues and resolve them.''',font="calibri 10",value="c",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue=0)
        c.place(relx=0.5,rely=0.7,anchor=CENTER)

        d = Radiobutton(gameFrame,text='''All above choices.''',font="calibri 10",value="d",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue=0)
        d.place(relx=0.5,rely=0.8,anchor=CENTER)

        letsgo.configure(text = "Submit", command=calc)


#####################################
#Q14
    def s14():

        def Prompt1():
            mlabel.configure(text = '''Hurrah! You made a wise decision. The bug has been fixed.''')
            mlabel.place(relx=0.5,rely=0.5,anchor=CENTER)
            letsgo.configure(text = "Next", command=cq1)

        def Prompt():
            mlabel.configure(text = '''No! You should’ve gone with anything except this option. MTTR has
increased. Lead time has increased. Stakeholder satisfaction has decreased.''')
            mlabel.place(relx=0.5,rely=0.5,anchor=CENTER)
            letsgo.configure(text = "Next", command=cq1)

        
        def calc():
            a.destroy()
            b.destroy()
            c.destroy()
            qlabel.destroy()
            scoresLabel.destroy()
            #attributes: LT, MTTR, CFR, RB, SS
            if (chosen.get() == "a"):
                attribUpdate([-3,-2,-2,-3,0])
                Prompt1()
            elif (chosen.get() == "b"):
                attribUpdate([-2,-1,-1,0,5])
                Prompt1()
            elif (chosen.get() == "c"):
                attribUpdate([25,10,12,-4,0])
                Prompt()


        mlabel.place(relx=200,rely=200,anchor=CENTER)
        scores = "LT = " + str(attributes[0]) + "     MTTR = " + str(attributes[1]) + "     CFR = " + str(attributes[2]) + "     RB = " + str(attributes[3]) + "     SS = " + str(attributes[4])
        scoresLabel = Label(gameCanvas,text=scores,fg="white", bg = '#173F5F')
        scoresLabel.place(relx=0.5,rely=0.95,anchor=CENTER)

        promptq = '''Uh Oh! You should’ve chosen to limit the batch size! Since you didn’t, a
major has appeared at a later stage in testing. When a user applies multiple
filters to search for an accommodation, the code times out. Now that you’re
very close to developing the application, you’ve got to make a careful
decision on how to resolve this bug. What would you do?'''
        qlabel = Label(gameCanvas,justify = LEFT,text=promptq,fg="white", bg = '#173F5F')
        qlabel.place(relx=0.5,rely=0.3,anchor=CENTER)
        
        chosen = StringVar()

        a = Radiobutton(gameFrame,text='''Dedicate a senior developer to work on fixing this bug.''',font="calibri 10",value="a",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue=0)
        a.place(relx=0.5,rely=0.5,anchor=CENTER)

        b = Radiobutton(gameFrame,text='''Take all developers on board and ask for their suggestion.''',font="calibri 10",value="b",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue=0)
        b.place(relx=0.5,rely=0.6,anchor=CENTER)

        c = Radiobutton(gameFrame,text='''Ignore this bug for now and put it into the backlog.''',font="calibri 10",value="c",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue=0)
        c.place(relx=0.5,rely=0.7,anchor=CENTER)

        letsgo.configure(text = "Submit", command=calc)



#################################
# CI Qs
#Q1

    def cq1():
        def q():
            def calc():
                a.destroy()
                b.destroy()
                c.destroy()
                qlabel.destroy()
                scoresLabel.destroy()
                #attributes: LT, MTTR, CFR, RB, SS
                if (chosen.get() == "a"):
                    attribUpdate([1,2,0,0,-5])
                    cq2()
                elif (chosen.get() == "b"):
                    attribUpdate([1,-1,-1,0,-5])
                    cq3()
                elif (chosen.get() == "c"):
                    attribUpdate([0,-1,-1,0,0])
                    cq5()
                
            mlabel.place(relx=200,rely=200,anchor=CENTER)

            scores = "LT = " + str(attributes[0]) + "     MTTR = " + str(attributes[1]) + "     CFR = " + str(attributes[2]) + "     RB = " + str(attributes[3]) + "     SS = " + str(attributes[4])
            scoresLabel = Label(gameCanvas,text=scores,fg="white", bg = '#173F5F')
            scoresLabel.place(relx=0.5,rely=0.95,anchor=CENTER)
            
            promptq = '''This scenario displays the lack of understanding from the developers and
project manager. Which member of the team is right in this scenario?'''
            qlabel = Label(gameCanvas,justify = LEFT,text=promptq,fg="white", bg = '#173F5F', )
            qlabel.place(relx=0.5,rely=0.3,anchor=CENTER)

            chosen = StringVar()

            a = Radiobutton(gameFrame,text='''Software developers. It is better to deploy the feature without bug fixes and
resolve them later.''',font="calibri 10",value="a",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue=0)
            a.place(relx=0.5,rely=0.5,anchor=CENTER)

            b = Radiobutton(gameFrame,text='''Project Manager. The development team needs to work harder to maintain
the quality of the program.''',font="calibri 10",value="b",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue=0)
            b.place(relx=0.5,rely=0.6,anchor=CENTER)

            c = Radiobutton(gameFrame,text='''neither. As the project manager needs to meet the deadline but the
development process may also be affected due to the continuous bug fixing.''',font="calibri 10",value="c",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue=0)
            c.place(relx=0.5,rely=0.7,anchor=CENTER)

            letsgo.configure(text = "Submit", command=calc)

        def Prompt():
            mlabel.configure(text = '''Continuous Integration (CI) is a development practice where developers integrate
code into a shared repository frequently, preferably several times a day. Each
integration can then be verified by an automated build and automated tests. Among
several key benefits, continuous testing helps with quick error detection and
resolution.

While implementing Continuous integration, the team has run into conflict due to
difference in roles and priorities of individuals making CI counterproductive.

The project manager, while doing his job is focused on meeting the deadline for a
new feature that was planned to be launched soon putting pressure on software
developers. Developers, however, think slowing down to fix minor bugs during the
development process is slowing them down.''')
            mlabel.place(relx=0.5,rely=0.5,anchor=CENTER)
            letsgo.configure(text = "Next", command=q)

        Prompt()



##############################
# Q2 - Q4 for option a
#Q3 and Q4 for option b
############################
##########################
#Q2
    def cq2():
        def Prompt():
            mlabel.configure(text = '''Deployment cannot be restricted by minor bugs. It may slow down
future debugging processes because of accumulating issues leading
to severe issues.''')
            mlabel.place(relx=0.5,rely=0.5,anchor=CENTER)
            letsgo.configure(text = "Next", command=cq3)

        def calc():
                a.destroy()
                b.destroy()
                qlabel.destroy()
                scoresLabel.destroy()
                #attributes: LT, MTTR, CFR, RB, SS
                if (chosen.get() == "a"):
                    attribUpdate([2,2,2,0,0])
                    Prompt()
                elif (chosen.get() == "b"):
                    attribUpdate([-5,-5,-5,0,0])
                    cq3()
                               

        mlabel.place(relx=200,rely=200,anchor=CENTER)

        scores = "LT = " + str(attributes[0]) + "     MTTR = " + str(attributes[1]) + "     CFR = " + str(attributes[2]) + "     RB = " + str(attributes[3]) + "     SS = " + str(attributes[4])
        scoresLabel = Label(gameCanvas,text=scores,fg="white", bg = '#173F5F')
        scoresLabel.place(relx=0.5,rely=0.95,anchor=CENTER)
        
        promptq = '''The software developers are partially correct in their concern. What
part of continuous integration are they missing?'''
        qlabel = Label(gameCanvas,justify = LEFT,text=promptq,fg="white", bg = '#173F5F', )
        qlabel.place(relx=0.5,rely=0.3,anchor=CENTER)

        chosen = StringVar()

        a = Radiobutton(gameFrame,text='''Features cannot be deployed with minor bugs as it may cause merge
problems.''',font="calibri 10",value="a",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue=0)
        a.place(relx=0.5,rely=0.5,anchor=CENTER)

        b = Radiobutton(gameFrame,text='''Deployment is possible but minor bugs may lead to severe system crashes
making it difficult to debug.''',font="calibri 10",value="b",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue=0)
        b.place(relx=0.5,rely=0.6,anchor=CENTER)

        letsgo.configure(text = "Submit", command=calc)



##########################
#Q3
    def cq3():
        def calc():
                a.destroy()
                b.destroy()
                c.destroy()
                qlabel.destroy()
                scoresLabel.destroy()
                #attributes: LT, MTTR, CFR, RB, SS
                if (chosen.get() == "a"):
                    attribUpdate([2,0,0,0,5])
                elif (chosen.get() == "b"):
                    attribUpdate([-3,-4,-4,-5,10])
                elif (chosen.get() == "c"):
                    attribUpdate([-5,-4,-4,-5,10])
                cq4()
        mlabel.place(relx=200,rely=200,anchor=CENTER)

        scores = "LT = " + str(attributes[0]) + "     MTTR = " + str(attributes[1]) + "     CFR = " + str(attributes[2]) + "     RB = " + str(attributes[3]) + "     SS = " + str(attributes[4])
        scoresLabel = Label(gameCanvas,text=scores,fg="white", bg = '#173F5F')
        scoresLabel.place(relx=0.5,rely=0.95,anchor=CENTER)
        
        promptq = '''Which of the following is the best way to resolve this conflict and
keep the development process running?'''
        qlabel = Label(gameCanvas,justify = LEFT,text=promptq,fg="white", bg = '#173F5F', )
        qlabel.place(relx=0.5,rely=0.3,anchor=CENTER)

        chosen = StringVar()

        a = Radiobutton(gameFrame,text='''Call a team meeting and make them understand the benefits of Continuous
integration.''',font="calibri 10",value="a",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue=0)
        a.place(relx=0.5,rely=0.5,anchor=CENTER)

        b = Radiobutton(gameFrame,text='''Highlight some incentive developers can gain from putting in more effort.''',font="calibri 10",value="b",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue=0)
        b.place(relx=0.5,rely=0.6,anchor=CENTER)

        c = Radiobutton(gameFrame,text='''Both a and b.''',font="calibri 10",value="c",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue=0)
        c.place(relx=0.5,rely=0.7,anchor=CENTER)

        letsgo.configure(text = "Submit", command=calc)




#################################
#Q4
    def cq4():
        def q():
            def calc():
                a.destroy()
                b.destroy()
                c.destroy()
                qlabel.destroy()
                scoresLabel.destroy()
                #attributes: LT, MTTR, CFR, RB, SS
                if (chosen.get() == "a"):
                    attribUpdate([10,-5,-5,-10,-10])
                    cq7()
                elif (chosen.get() == "b"):
                    attribUpdate([15,10,10,0,2])
                    ran()
                elif (chosen.get() == "c"):
                    attribUpdate([2,2,5,-5,-10])
                    ran()
            mlabel.place(relx=200,rely=200,anchor=CENTER)

            scores = "LT = " + str(attributes[0]) + "     MTTR = " + str(attributes[1]) + "     CFR = " + str(attributes[2]) + "     RB = " + str(attributes[3]) + "     SS = " + str(attributes[4])
            scoresLabel = Label(gameCanvas,text=scores,fg="white", bg = '#173F5F')
            scoresLabel.place(relx=0.5,rely=0.95,anchor=CENTER)
            
            promptq = '''You need to help the team decide between delaying bug fixes and
feature deployment with minor bugs. What would you choose
considering that each option may slow down or speed up the
development process?'''
            qlabel = Label(gameCanvas,justify = LEFT,text=promptq,fg="white", bg = '#173F5F', )
            qlabel.place(relx=0.5,rely=0.3,anchor=CENTER)

            chosen = StringVar()

            a = Radiobutton(gameFrame,text='''Insist on regular bug fixes by developers.''',font="calibri 10",value="a",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue=0)
            a.place(relx=0.5,rely=0.5,anchor=CENTER)

            b = Radiobutton(gameFrame,text='''Add the bugs to the backlog for future resolution and deploy the feature.''',font="calibri 10",value="b",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue=0)
            b.place(relx=0.5,rely=0.6,anchor=CENTER)

            c = Radiobutton(gameFrame,text='''pass the issue to another DevOps engineer.''',font="calibri 10",value="c",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue=0)
            c.place(relx=0.5,rely=0.7,anchor=CENTER)

            letsgo.configure(text = "Submit", command=calc)

        def Prompt():
            mlabel.configure(text = '''Project managers may be partially correct about the need to keep up with
minor bug fixes. Adapting to Continuous integration can be difficult for many
organizations due to the organizational culture and structure. And it needs to
be a gradual process, if imposed onto the employees may restrict the
organizations potential. DevOps teams need to understand the benefits of CI
to not just the organization but themselves.''')
            mlabel.place(relx=0.5,rely=0.5,anchor=CENTER)
            letsgo.configure(text = "Next", command=q)

        Prompt()

#############################
#Q5
    def cq5():
        def calc():
                a.destroy()
                b.destroy()
                c.destroy()
                qlabel.destroy()
                scoresLabel.destroy()
                #attributes: LT, MTTR, CFR, RB, SS
                if (chosen.get() == "a"):
                    attribUpdate([2,0,0,0,5])
                elif (chosen.get() == "b"):
                    attribUpdate([-3,-4,-4,-5,10])
                elif (chosen.get() == "c"):
                    attribUpdate([-5,-4,-4,-5,10])
                cq6()

        mlabel.place(relx=200,rely=200,anchor=CENTER)

        scores = "LT = " + str(attributes[0]) + "     MTTR = " + str(attributes[1]) + "     CFR = " + str(attributes[2]) + "     RB = " + str(attributes[3]) + "     SS = " + str(attributes[4])
        scoresLabel = Label(gameCanvas,text=scores,fg="white", bg = '#173F5F')
        scoresLabel.place(relx=0.5,rely=0.95,anchor=CENTER)
        
        promptq = '''Which of the following is the best way to resolve this conflict and
keep the development process running?'''
        qlabel = Label(gameCanvas,justify = LEFT,text=promptq,fg="white", bg = '#173F5F', )
        qlabel.place(relx=0.5,rely=0.3,anchor=CENTER)

        chosen = StringVar()

        a = Radiobutton(gameFrame,text='''Call a team meeting and make them understand the benefits of Continuous
integration.''',font="calibri 10",value="a",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue=0)
        a.place(relx=0.5,rely=0.5,anchor=CENTER)

        b = Radiobutton(gameFrame,text='''Highlight some incentive developers can gain from putting in more effort.''',font="calibri 10",value="b",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue=0)
        b.place(relx=0.5,rely=0.6,anchor=CENTER)

        c = Radiobutton(gameFrame,text='''Both a and b.''',font="calibri 10",value="c",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue=0)
        c.place(relx=0.5,rely=0.7,anchor=CENTER)

        letsgo.configure(text = "Submit", command=calc)

#################################
#Q6
    def cq6():
        def q():
            
            def prompt1():
                mlabel.configure(text = '''Adapting to Continuous integration can be difficult for many organizations due
to the organizational culture and structure. And it needs to be a gradual
process, if imposed onto the employees may restrict the organizations
potential. DevOps teams need to understand the benefits of CI to not just the
organization but themselves.
A good CI setup speeds up your workflow and encourages the team to push
every change without being afraid of breaking anything. There are more
benefits to it than just working with a better software release process.
Continuous Integration brings great business benefits as well.''')
                mlabel.place(relx=0.5,rely=0.5,anchor=CENTER)
                letsgo.configure(text = "Next", command=ran)  

            def prompt2():
                mlabel.configure(text = '''As you chose to provide monetary incentive to the developers, your
remaining budget has decreased. Although, Automated tests help in
the long run by reducing the mean time to repair during continuous
integration. It makes it easier to find bugs without manually testing all
parts of code every time a batch is deployed.''')
                mlabel.place(relx=0.5,rely=0.5,anchor=CENTER)
                letsgo.configure(text = "Next", command=cq7)  

            def calc():
                a.destroy()
                b.destroy()
                c.destroy()
                qlabel.destroy()
                scoresLabel.destroy()
                #attributes: LT, MTTR, CFR, RB, SS
                if (chosen.get() == "a"):
                    attribUpdate([5,5,10,0,5])
                    prompt1()
                elif (chosen.get() == "b"):
                    attribUpdate([2,-5,-5,-7,5])
                    prompt2()
                elif (chosen.get() == "c"):
                    attribUpdate([2,-5,0,-10,5])
                    ran()
            mlabel.place(relx=200,rely=200,anchor=CENTER)

            scores = "LT = " + str(attributes[0]) + "     MTTR = " + str(attributes[1]) + "     CFR = " + str(attributes[2]) + "     RB = " + str(attributes[3]) + "     SS = " + str(attributes[4])
            scoresLabel = Label(gameCanvas,text=scores,fg="white", bg = '#173F5F')
            scoresLabel.place(relx=0.5,rely=0.95,anchor=CENTER)
            
            promptq = '''Now that you understood the conflict and understood the benefits of
CI. Despite the benefits of CI, adapting to CI is not a piece of cake. Your
development team is having a hard time keeping up with writing
automated test cases. You have to make a critical decision and each
option has its own downsides. What would you choose?'''
            qlabel = Label(gameCanvas,justify = LEFT,text=promptq,fg="white", bg = '#173F5F', )
            qlabel.place(relx=0.5,rely=0.3,anchor=CENTER)

            chosen = StringVar()

            a = Radiobutton(gameFrame,text='''Step back to traditional manual testing and delay automated testing.''',font="calibri 10",value="a",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue=0)
            a.place(relx=0.5,rely=0.5,anchor=CENTER)

            b = Radiobutton(gameFrame,text='''Provide some incentive to the developer’s team to work harder on
automated test cases.''',font="calibri 10",value="b",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue=0)
            b.place(relx=0.5,rely=0.6,anchor=CENTER)

            c = Radiobutton(gameFrame,text='''Hire third party developers/freelancers to create automated test cases.''',font="calibri 10",value="c",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue=0)
            c.place(relx=0.5,rely=0.7,anchor=CENTER)

            letsgo.configure(text = "Submit", command=calc)

        def Prompt():
            mlabel.configure(text = '''Adapting to Continuous integration can be difficult for many organizations due
to the organizational culture and structure. And it needs to be a gradual
process, if imposed onto the employees may restrict the organizations
potential. DevOps teams need to understand the benefits of CI to not just the
organization but themselves.
A good CI setup speeds up your workflow and encourages the team to push
every change without being afraid of breaking anything. There are more
benefits to it than just working with a better software release process.
Continuous Integration brings great business benefits as well.''')
            mlabel.place(relx=0.5,rely=0.5,anchor=CENTER)
            letsgo.configure(text = "Next", command=q)

        Prompt()

#################################
#Q7
    def cq7():
        def q():
            def calc():
                a.destroy()
                b.destroy()
                c.destroy()
                d.destroy()
                qlabel.destroy()
                scoresLabel.destroy()
                #attributes: LT, MTTR, CFR, RB, SS
                if (chosen.get() == "a"):
                    attribUpdate([-2,-5,-5,0,5])
                elif (chosen.get() == "b"):
                    attribUpdate([-2,-5,-5,5,5])
                elif (chosen.get() == "c"):
                    attribUpdate([-2,-2,-2,0,-10])
                elif (chosen.get() == "b"):
                    attribUpdate([-2,-5,-5,5,5])
                ran()
            mlabel.place(relx=200,rely=200,anchor=CENTER)

            scores = "LT = " + str(attributes[0]) + "     MTTR = " + str(attributes[1]) + "     CFR = " + str(attributes[2]) + "     RB = " + str(attributes[3]) + "     SS = " + str(attributes[4])
            scoresLabel = Label(gameCanvas,text=scores,fg="white", bg = '#173F5F')
            scoresLabel.place(relx=0.5,rely=0.95,anchor=CENTER)
            
            promptq = '''Increased workload and divided attention increase the chance
of errors. Testers raised an issue with exceptions that were
ignored in the development process. Developers have been
ignoring error messages due to the increased number of
notifications from multiple submissions. As a devOps engineer,
which of the following decisions would you like to make?'''
            qlabel = Label(gameCanvas,justify = LEFT,text=promptq,fg="white", bg = '#173F5F', )
            qlabel.place(relx=0.5,rely=0.3,anchor=CENTER)

            chosen = StringVar()

            a = Radiobutton(gameFrame,text='''Only allow necessary notifications to the concerned members of the
development team and avoid unnecessary pop ups.''',font="calibri 10",value="a",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue=0)
            a.place(relx=0.5,rely=0.5,anchor=CENTER)

            b = Radiobutton(gameFrame,text='''Assign a person in charge for reacting to CI notifications and the
whole team may take turns.''',font="calibri 10",value="b",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue=0)
            b.place(relx=0.5,rely=0.6,anchor=CENTER)

            c = Radiobutton(gameFrame,text='''Request developers to not mute notifications and keep an eye on
daily notifications otherwise they may face serious consequences.''',font="calibri 10",value="c",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue=0)
            c.place(relx=0.5,rely=0.7,anchor=CENTER)

            d = Radiobutton(gameFrame,text='''Both a and b.''',font="calibri 10",value="d",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue=0)
            d.place(relx=0.5,rely=0.8,anchor=CENTER)

            letsgo.configure(text = "Submit", command=calc)

        q()


#################################
#Ran
    def ran():

        def prompt1():
                mlabel.configure(text = '''You have been entrusted with a lot of important responsibilities throughout the
process. Now, since we’re almost about to finish developing the platform, you have to
perform one last task.''')
                mlabel.place(relx=0.5,rely=0.5,anchor=CENTER)
                letsgo.configure(text = "Next", command=next) 
        x = random.choice(list(range(1,4))) 
        
        def next():
            if (attributes[1] > 90 and attributes[4] < 30 ):
                se1()
            elif (attributes[3] < 30 and attributes[4] < 30 ):
                se2()
            elif (attributes[1] > 90 or attributes[2] > 80 ):
                se3()
            else:
                if(x == 1):
                    se1()
                elif(x == 2):
                    se2()
                else:
                    se3()
        

        prompt1()



#################################
# QLast 1
    def se1():

        def calc():
            a.destroy()
            b.destroy()
            c.destroy()
            qlabel.destroy()
            scoresLabel.destroy()
            #attributes: LT, CFR, MTTR, SS, RB
            if (chosen.get() == "a"):
                attribUpdate([5,-2,3,-1,-10])
            elif (chosen.get() == "b"):
                attribUpdate([3,-4,-1,-3,5])
            elif (chosen.get() == "c"):
                attribUpdate([3,-2,-2,2,5])
            game.destroy()
            score(attributes, usr)
            
        mlabel.place(relx=200,rely=200,anchor=CENTER)

        scores = "LT = " + str(attributes[0]) + "     MTTR = " + str(attributes[1]) + "     CFR = " + str(attributes[2]) + "     RB = " + str(attributes[3]) + "     SS = " + str(attributes[4])
        scoresLabel = Label(gameCanvas,text=scores,fg="white", bg = '#173F5F')
        scoresLabel.place(relx=0.5,rely=0.95,anchor=CENTER)
        
        promptq9 = '''Due to inadequate automation of configuration checks and vulnerability
scanning, the DevOps output has been shown to have a lack of security
while handling privileged inputs (API access tokens and passwords).
What should we do in this scenario?'''
        qlabel = Label(gameCanvas,justify = LEFT,text=promptq9,fg="white", bg = '#173F5F', )
        qlabel.place(relx=0.5,rely=0.3,anchor=CENTER)

        chosen = StringVar()

        a = Radiobutton(gameFrame,text='''Cross-functional collaboration is the key to effectively integrating security
into the entire DevOps lifecycle. Hence, it is not too late to implement
DevSecOps instead of DevOps.''',font="calibri 10",value="a",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue=0)
        a.place(relx=0.5,rely=0.45,anchor=CENTER)

        b = Radiobutton(gameFrame,text='''Carry out penetration testing and ask security teams to identify
vulnerabilities. Then, they should work closely with the developers to fix
these issues.''',font="calibri 10",value="b",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue=0)
        b.place(relx=0.5,rely=0.6,anchor=CENTER)

        c = Radiobutton(gameFrame,text='''Limit privilege access rights to reduce the avenues for attack, even if it
means to restrict some of the essential access required by users to
perform certain actions or use certain features on the website.''',font="calibri 10",value="c",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue=0)
        c.place(relx=0.5,rely=0.75,anchor=CENTER)

        letsgo.configure(text = "Submit", command=calc)

#################################
# QLast 2
    def se2():

        def calc():
            a.destroy()
            b.destroy()
            c.destroy()
            qlabel.destroy()
            scoresLabel.destroy()
            #attributes: LT, CFR, MTTR, SS, RB
            if (chosen.get() == "a"):
                attribUpdate([2,0,0,-3,5])
            elif (chosen.get() == "b"):
                attribUpdate([2,2,4,0,0])
            elif (chosen.get() == "c"):
                attribUpdate([3,0,0,-5,5])
            game.destroy()
            score(attributes, usr)
            
        mlabel.place(relx=200,rely=200,anchor=CENTER)

        scores = "LT = " + str(attributes[0]) + "     MTTR = " + str(attributes[1]) + "     CFR = " + str(attributes[2]) + "     RB = " + str(attributes[3]) + "     SS = " + str(attributes[4])
        scoresLabel = Label(gameCanvas,text=scores,fg="white", bg = '#173F5F')
        scoresLabel.place(relx=0.5,rely=0.95,anchor=CENTER)
        
        promptq = '''Documentation is created in a waterfall fashion, rarely updated, highly prone
to human error and lacking consistency. The DevOps team, while trying to
code, test and deploy features was just too busy to finish documentation
that inevitably was abandoned altogether. How do you plan to deal with this
situation?'''
        qlabel = Label(gameCanvas,justify = LEFT,text=promptq,fg="white", bg = '#173F5F', )
        qlabel.place(relx=0.5,rely=0.3,anchor=CENTER)

        chosen = StringVar()

        a = Radiobutton(gameFrame,text='''Dedicate a developer to review the documentation. Ask the developer to
review and formulate the documentation in a detailed manner even if
there is a need to hire extra help.''',font="calibri 10",value="a",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue=0)
        a.place(relx=0.5,rely=0.45,anchor=CENTER)

        b = Radiobutton(gameFrame,text='''Ignore the documentation as it is not that important. The timely delivery of
the system is necessary and should be focused upon. Documentation
quality is not the main deliverable so is not that critical.''',font="calibri 10",value="b",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue=0)
        b.place(relx=0.5,rely=0.6,anchor=CENTER)

        c = Radiobutton(gameFrame,text='''Dedicate a developer to review the documentation. If it lacks in quality, ask
him/her to replace the detailed documentation with condensed demos that
are critical for the understanding of the functionalities of the system.''',font="calibri 10",value="c",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue=0)
        c.place(relx=0.5,rely=0.75,anchor=CENTER)

        letsgo.configure(text = "Submit", command=calc)


#################################
# QLast 3
    def se3():

        def calc():
            a.destroy()
            b.destroy()
            qlabel.destroy()
            scoresLabel.destroy()
            #attributes: LT, CFR, MTTR, SS, RB
            if (chosen.get() == "a"):
                attribUpdate([3,-1,2,-2,-5])
            elif (chosen.get() == "b"):
                attribUpdate([1,-3,-2,0,5])
            game.destroy()
            score(attributes, usr)
            
        mlabel.place(relx=200,rely=200,anchor=CENTER)

        scores = "LT = " + str(attributes[0]) + "     MTTR = " + str(attributes[1]) + "     CFR = " + str(attributes[2]) + "     RB = " + str(attributes[3]) + "     SS = " + str(attributes[4])
        scoresLabel = Label(gameCanvas,text=scores,fg="white", bg = '#173F5F')
        scoresLabel.place(relx=0.5,rely=0.95,anchor=CENTER)
        
        promptq = '''During the project, we were faced with several technical issues and bugs.
Another thing that was very prominent was the lack of collaboration
between teams, which led to a rather impeding and thwarting Agile
environment. What would you suggest, for future teams, to reduce the
impact of this issue?'''
        qlabel = Label(gameCanvas,justify = LEFT,text=promptq,fg="white", bg = '#173F5F', )
        qlabel.place(relx=0.5,rely=0.3,anchor=CENTER)

        chosen = StringVar()

        a = Radiobutton(gameFrame,text='''Design audit-based control frameworks to improve quality, assurance,
security, compliance, and risk mitigation via checklists and audits of
activity.''',font="calibri 10",value="a",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue=0)
        a.place(relx=0.5,rely=0.5,anchor=CENTER)

        b = Radiobutton(gameFrame,text='''Implement organizational changes at smaller units for better
understanding of agile development, helping them build trust with more
autonomous control frameworks, to make collaboration easier.''',font="calibri 10",value="b",variable = chosen, justify = LEFT, activebackground="#173F5F", selectcolor = "#173F5F" ,fg="white", bg = '#173F5F', tristatevalue=0)
        b.place(relx=0.5,rely=0.65,anchor=CENTER)

        letsgo.configure(text = "Submit", command=calc)


####################################
# Main window


    gameCanvas = Canvas(game,width=730, height=440, bg = '#173F5F')
    gameCanvas.pack()

    gameFrame = Frame(gameCanvas,bg="#173F5F")
    gameFrame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    prompt = "Welcome to the DevOps Game! \n The game is designed to help you learn various techniques and judge the best choices \n to make the project a success. You are asked to make different choices, as the key \n decision maker of the DevOps team (the DevOps Engineer), aiming to develop \n a vacation rental online marketplace platform. You will be provided with different \n scenarios and dilemmas, and will have to choose between them. \n \n You should, according to your understanding, choose the best possible \n option for every given scenario. \n Your choices will affect some specific indicators, including \n lead time, change failure rate, MTTR, budget and stakeholder satisfaction. \n At the same time, your choices may lead to different pathways in the game. \n \n Let's Start!"
    mlabel = Label(gameCanvas,justify = LEFT,text=prompt,bg="#173F5F", fg = 'white' )
    mlabel.place(relx=0.5,rely=0.5,anchor=CENTER)

    letsgo = Button(gameFrame,text="Let's Go",bg="#173F5F", fg = 'white',font="calibri 12",command=gameDetail)
    letsgo.place(relx=0.8,rely=0.85)

    
    
    game.mainloop()
 



def start():
    
    global starter 
    starter = Tk()

    introCanvas = Canvas(starter, width = 725, height = 433)
    img = PhotoImage(file="back.png")
    introCanvas.grid(column = 0 , row = 0)
    introCanvas.create_image(70, 0, image = img, anchor = NW)

    button = Button(starter, text='Start the DevOps Game!',command = signUp,) 
    button.grid(column = 0 , row = 2)
    button.configure(width=105, height=4, activebackground = "#33B5E5", bg ='sky blue', relief = RAISED)
    
    starter.mainloop()
    
    
if __name__=='__main__':
    start()
