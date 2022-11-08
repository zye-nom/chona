import tkinter as converter
from tkinter import messagebox
main_window = converter.Tk()

main_window.configure(bg="brown")
main_window.title("converter")
main_window.geometry("500x500")

def calculate():
   year  = int(daily.get())
   calculate = year // 365
   messagebox.showinfo("calculator", "the answer is " + str(calculate))

annual = converter.Label(text="year ", font=("algerian", 25))
annual.grid(row=0, column=0, pady=5, padx=5)
daily = converter.Entry(font=("algerian", 25))
daily.grid(row=0, column=1)

calculator = converter.Button(text="calculate", font=("algerian", 25), command=calculate)
calculator.grid(row=2, column=1)







main_window.mainloop()