from tkinter import Button, Entry, Label, StringVar, Tk
import csv
from datetime import datetime
import time

time.sleep(1500)

while True:
    starttime = time.time()
    window = Tk()
    window.geometry("450x300")
    window.title("Reminder!")
    window.configure(background="black")

    time_ans = StringVar()
    work_ans = StringVar()

    def click():
        try:
            f = open(r'data.csv', 'a')
        except:
            f = open('myfile.txt', 'w')
        writer = csv.writer(f)
        current_time = datetime.now()
        writer.writerow([current_time.day, str(current_time.hour)+":"+str(current_time.minute), int(time_ans.get()), work_ans.get()])
        window.destroy()

    time_text = Label(window, text="Enter Time", bg="white", fg="black", font="none 12 bold").place(x=120,y=0)
    time_input = Entry(window, textvariable=time_ans, width=30).place(x=120, y=30)
    work_text = Label(window, text="What work?", bg="white", fg="black", font="none 12 bold").place(x=120, y=70)
    work_input =  Entry(window, textvariable=work_ans, width=30).place(x=120, y=110)
    water_text = Label(window, text="PLEASE HAVE WATER", bg="white", fg="red").place(x=150, y=250)
    submit_button = Button(window, text="submit", command=click).place(x=180, y=160)
    window.mainloop()
    time.sleep(1500 - ((time.time() - starttime)%1500)+ int(time_ans.get())*60)

