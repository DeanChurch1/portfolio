 ##age=int(input("How old are you"))
##
##if age > 50:
##    print("you are old")
##else:
##    print("you need to grow up a bit")


from tkinter import *
from tkinter import ttk
from tkinter import font
import calendar
import time
import datetime
print(calendar.timegm(time.gmtime()))
def current_time():
    seconds = calendar.timegm(time.gmtime())
    curent_seconds = seconds % 60
    minutes = seconds // 60
    curent_minutes= minutes % 60
    hours = minutes // 60
    current_hour = hours % 24
    if current_hour >=12:
        tag=" PM"
    else:
        tag=" AM"
#set the time zone
    current_hour = current_hour - 6
#format the output
    timex= str(current_hour)+":"+str(curent_minutes)+":"+str(curent_seconds)+tag
#return the output
    return timex

def quit(*args):
    root.destroy()

def show_time():
    time=current_time()
#show the time
    txt.set(time)
#trigger the tick after 1000ms    
    root.after(1000, show_time)


root = Tk()
root.attributes("-fullscreen", False)
root.configure(background='Green')
root.bind("x", quit)
root.after(1000, show_time)

fnt = font.Font(family='Helvetica', size = 60, weight='bold')
txt = StringVar()
lbl = ttk.Label(root, textvariable=txt, font=fnt, foreground="yellow", background="red")
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()
