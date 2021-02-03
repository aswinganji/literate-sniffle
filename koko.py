from tkinter import*
root = Tk()
root.geometry("600x600")
root.title("TitleUsed416thtime")


question1radiobutton = StringVar(value = "0")
ques1 = Label(root,text = "44 6f 20 79 6f 75 20 48 61 76 65 20 42 72 65 61 74 68 69 6e 67 20 50 72 6f 62 6c 65 6d 3f")
ques1.pack()

q1r1 = Radiobutton(root,text = "yes", variable = question1radiobutton,value = "yes")
q1r1.pack()

q1r2 = Radiobutton(root,text = "no", variable = question1radiobutton,value = "no")
q1r2.pack()



question2radiobutton = StringVar(value = "0")
ques2 = Label(root,text = "44 6f 20 79 6f 75 20 48 61 76 65 20 53 77 65 6c 6c 69 6e 67 3f")
ques2.pack()

q2r1 = Radiobutton(root,text = "yes", variable = question2radiobutton,value = "yes")
q2r1.pack()

q2r2 = Radiobutton(root,text = "no", variable = question2radiobutton,value = "no")
q2r2.pack()




question3radiobutton = StringVar(value = "0")
ques3 = Label(root,text = "44 6f 20 79 6f 75 20 48 61 76 65 20 6c 6f 73 73 20 6f 66 20 6d 65 6d 6f 72 79 20 61 6e 64 20 64 69 73 6f 72 69 65 6e 74 61 74 69 6f 6e 3f")
ques3.pack()

q3r1 = Radiobutton(root,text = "yes", variable = question3radiobutton,value = "yes")
q3r1.pack()

q3r2 = Radiobutton(root,text = "no", variable = question3radiobutton,value = "no")
q3r2.pack()








question4radiobutton = StringVar(value = "0")
ques4 = Label(root,text = "44 6f 20 79 6f 75 20 48 61 76 65 20 73 68 6f 72 74 6e 65 73 73 20 6f 66 20 42 72 65 61 74 68 3f")
ques4.pack()

q4r1 = Radiobutton(root,text = "yes", variable = question4radiobutton,value = "yes")
q4r1.pack()

q4r2 = Radiobutton(root,text = "no", variable = question4radiobutton,value = "no")
q4r2.pack()





question5radiobutton = StringVar(value = "0")
ques5 = Label(root,text = "44 6f 20 79 6f 75 20 45 78 70 65 72 69 65 6e 63 65 20 77 68 65 65 7a 69 6e 67 20 6f 72 20 63 6f 75 67 68 69 6e 67 3f")
ques5.pack()

q5r1 = Radiobutton(root,text = "yes", variable = question5radiobutton,value = "yes")
q5r1.pack()

q5r2 = Radiobutton(root,text = "no", variable = question5radiobutton,value = "no")
q5r2.pack()






















def fvr():
    score = 0
    if question1radiobutton.get()== "yes" :
        score = score + 10
        print(score)
    
    if question2radiobutton.get()== "yes" :
        score = score + 10
        print(score)
    
    if question3radiobutton.get()== "yes" :
        score = score + 10
        print(score)
        
    if question4radiobutton.get()== "yes" :
        score = score + 10
        print(score)
        
        
    if question5radiobutton.get()== "yes" :
        score = score + 10
        print(score)
    
    if score <= 10:
        messagebox.showinfo("rprt","You dnt hv t mt te doktr")
        
    elif score >= 20 and score <=30: 
        messagebox.showinfo("rprt","You mw hv t mt te doktr")
     
    else:
        messagebox.showinfo("rprt","You hv t mt te doktr")

bright = Button(root,text = "yu hv t hv bd report",command = fvr)
bright.pack()


root.mainloop()









