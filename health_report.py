from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Healt Report")
root.geometry("600x600")

def get_report():
    score = 0
    
    print(question1_radiobutton.get())
    if(question1_radiobutton.get() == "Yes"):
        score = score + 20
    if(question2_radiobutton.get() == "Yes"):
        score = score + 20
    if(question3_radiobutton.get() == "Yes"):
        score = score + 20
        
    if(score <= 20):
        messagebox.showinfo(title="Report", message="You don't need to visit a doctor")
    elif(score == 40):
        messagebox.showinfo(title="Report", message="You might perhaps have to visit a doctor")
    else:
        messagebox.showinfo(title="Report", message="I strongly advise you to visit doctor")

question1_label = Label(root, text="Do you have headache and sore throat?")
question1_label.pack()

question1_radiobutton = StringVar(value="0")
question1_r1 = Radiobutton(root, text='Yes', variable=question1_radiobutton, value="Yes")
question1_r1.pack()
question1_r2 = Radiobutton(root, text="No", variable=question1_radiobutton, value="No")
question1_r2.pack()

question2_label = Label(root, text="Is your body tempreture high?")
question2_label.pack()

question2_radiobutton = StringVar(value="0")
question2_r1 = Radiobutton(root, text='Yes', variable=question2_radiobutton, value="Yes")
question2_r1.pack()
question2_r2 = Radiobutton(root, text="No", variable=question2_radiobutton, value="No")
question2_r2.pack()

question3_label = Label(root, text="Are there any symptoms of eye redness?")
question3_label.pack()

question3_radiobutton = StringVar(value="0")
question3_r1 = Radiobutton(root, text='Yes', variable=question3_radiobutton, value="Yes")
question3_r1.pack()
question3_r2 = Radiobutton(root, text="No", variable=question3_radiobutton, value="No")
question3_r2.pack()


button = Button(root, text="Get Report", command=get_report)
button.pack()

root.mainloop()