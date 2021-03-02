from tkinter import *
from tkinter.ttk import *

from time import strftime
import datetime as dt
import time

while True:
    now = dt.datetime.now()
    target = dt.datetime.combine(dt.date.today(), dt.time(minute=16))
    if target < now:
        target += dt.timedelta(days=1)

    time.sleep((target-now).total_seconds())
    print("finished")
    window = Tk()
    window.title("Clock")


    def time():
        string = strftime("%H:%M:%S %p")
        label.config(text=string)
        label.after(500, time)


    label = Label(window, font=("ds-digital", 300), background="Black", foreground="cyan")
    label.pack(anchor="center")
    time()
    mainloop()
