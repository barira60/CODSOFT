import random
from tkinter import *

root=Tk()
root.title("Chat Bot")
root.geometry("750x400")
bots=StringVar()

hellow=["hi","hello","hi!!","anyone here","help"]
how=["how are you","whats up!!"]
age=["whats your age?","your age?","how old are you"]
bye=["bye","see you later","goodbye","byeee","good to see you","ok bye"]
name=["whats your name?","how can i call you?","what is your name?"]
doing=["how are you doing?","what are you doing?"]
weather=["What's the weather like today?","today weather","weather","forecast"]
time=["What time is it","time"]
color=["What is your favorite color?","fav color","your color"]

def chat():
    if input.get().lower() in hellow:
        bot=["Hi","Welcome","Hey! I am here to assit you."]
        bots.set(random.choice(bot))
    elif input.get().lower() in how:
        bot=["Fine!","Happy,What about you??","Yes Fine^^"]
        bots.set(random.choice(bot))
    elif input.get().lower() in age:
        bot=["I don't have a physical age, but I was created recently by Barira Babar"]
        bots.set(random.choice(bot))
    elif input.get().lower() in bye:
        bot=["Bye","Goodbye! Have a great day!"]
        bots.set(random.choice(bot))
    elif input.get().lower() in name:
        bot = ["I'm a chatbot. You can call me ChatBot.","I am ChatBot, your virtual assistant"]
        bots.set(random.choice(bot))
    elif input.get().lower() in doing:
        bot=[" I'm just a computer program, so I don't have feelings, but I'm here to help you!"]
        bots.set(random.choice(bot))
    elif input.get().lower() in time:
        bot = ["I don't have real-time data, so I can't provide the current time."]
        bots.set(random.choice(bot))
    elif input.get().lower() in color:
        bot = ["I don't have personal preferences, but I'm happy to talk about colors!"]
        bots.set(random.choice(bot))
    else:
        bots.set("Sorry,I don't understand that :(")

head=Label(root,text="Chat bot",font=("times new roman",30,"bold"))
head.place(x=300,y=20)

holder=Frame(width=20,height=100)
holder.place(x=80,y=120)

user=Label(holder,text="You: ",font=("arial",15,"bold"),padx=10)
user.grid(row=0,column=0)

input=Entry(holder,width=60,font=("garamond",15))
input.grid(row=0,column=1)

btn=Button(text="Submit",command=chat,padx=10,pady=10,width=10)
btn.place(x=280,y=180)

bot=Label(holder,text="Bot: ",font=("arial",15,"bold"),padx=10,pady=100)
bot.grid(row=3,column=0)

output=Entry(holder,width=60,font=("garamond",15),textvariable=bots)
output.grid(row=3,column=1)

root.mainloop()

