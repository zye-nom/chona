import tkinter as sister
from tkinter import messagebox
main_window = sister.Tk()
main_window.geometry("5000x5000")
main_window.configure(bg="white")
main_window.title("mth assignment")

def AREA():
    RADIUS = int(big.get())
    AREA = 3.14 * RADIUS**2
    messagebox.showinfo("AREA", "the area is " + str(AREA))

def CIRCUMFERENCE():
    RADIUS = int(big.get())
    CIRCUMFERENCE  = 2 * RADIUS  * 3.14
    messagebox.showinfo("CIRCUMFERENCE", "the circumference is " + str(CIRCUMFERENCE))

small = sister.Label(text="radius:", font=("Algerian", 20))
small.grid(row=0, column=0, padx=5, pady=5)
big =sister.Entry(font=("Algerian", 20))
big.grid(row=0, column=1)


calc_1 = sister.Button(text="AREA", font=("Algerian", 25), command=AREA)
calc_1.grid(row=2, column=3, padx=5, pady=5)
calc_2 = sister.Button(text="CIRCUMFERENCE", font=("Algerian", 25), command=CIRCUMFERENCE)
calc_2.grid(row=3, column=3, padx=5, pady=5)




main_window.mainloop()
