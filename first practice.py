import tkinter as mister
from tkinter import messagebox
main_window = mister.Tk()
main_window.geometry("1000x1000")
main_window.configure(bg="white")
main_window.title("toaster")

firstlabel = mister.Label(text="male", font=("arial", 40))
firstlabel.grid(row=0,  column=0)
secondlabel = mister.Label(text="female", font=("arial", 40))
secondlabel.grid(row=1, column=0)

firstentry = mister.Entry(font=("arial, 40"))
firstentry.grid(row=0, column=1)
secondentry = mister.Entry(font=("arial", 40))
secondentry.grid(row=1 ,column=1)

firstbutton = mister.Button(text="sex", font=("arial", 55))
firstbutton.grid(row=2, column=3)




main_window.mainloop()