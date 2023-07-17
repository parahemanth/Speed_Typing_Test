from tkinter import *
from random import *
import time

wind=Tk()
wind.title("Speed Typing Test")
wind.geometry("370x425")
wind.configure(bg="skyblue")

def reset():
    text1.delete("1.0",END)
    global sample
    sample=choice(sentences)
    text1.insert(END,sample)
    text2.delete("1.0",END)
    text3.delete("1.0",END)
    global start
    start=time.time()


def calculate(end):
    text3.delete("1.0",END)
    time_taken=end-start
    text=text2.get("1.0",END)
    n=len(text)-1
    correct_count=0
    for i in range(n):
        if(i+1>len(sample)):
            break
        if(sample[i]==text[i]):
            correct_count+=1
    time_in_min=time_taken/60
    GWPM=(n/5)/time_in_min
    NWPM=(correct_count/5)/time_in_min
    Accuracy=(NWPM*100)/GWPM
    result="Total typed characters: "+str(n)+"\nCorrect typed characters: "+str(correct_count)+"\nIncorrect typed characters: "+str(n-correct_count)+"\nTime taken: "+str(round(time_taken,2))+"sec\nAccuracy:"+str(round(Accuracy,2))+"%\nTyping speed of the candidate: "+str(round(NWPM,2))+" WPM"
    text3.insert("1.0",result)


sentences=["The quick red fox jumps over the lazy dog showcasing its agility and speed in a timeless display of nature's prowess.",
           "Pack my box with seven dozen liquor jugs, carefully arranging each item to maximize space and ensure safe transport.",
           "Six big devils from Greece quickly forgot how to fox-trot, their once-refined skill devolving into chaos and confusion."]

label1=Label(master=wind,text="Here is your Sentence:",bg="skyblue",font=("Times", "12", "bold italic"))
label1.place(x=15,y=10)

text1=Text(master=wind,height=4,width=42,)
text1.place(x=15,y=40)

label2=Label(master=wind,text="Type the above Sentence:",bg="skyblue",font=("Times", "12", "bold italic"))
label2.place(x=15,y=120)

text2=Text(master=wind,height=4,width=42,)
text2.place(x=15,y=150)

button=Button(master=wind,text="Check Result",bg="lightgreen",font=("Times", "10", "bold italic"),relief="raised",command=lambda:calculate(time.time()))
button.place(x=140,y=230)

label3=Label(master=wind,text="Results:",bg="skyblue",font=("Times", "12", "bold italic"))
label3.place(x=15,y=260)

text3=Text(master=wind,height=6,width=42,)
text3.place(x=15,y=285)

reset_button=Button(master=wind,text=" RESET ",width=10,bg="orange",font=("Times", "10", "bold italic"),relief="raised",command=lambda:reset())
reset_button.place(x=140,y=390)

reset()

wind.mainloop()