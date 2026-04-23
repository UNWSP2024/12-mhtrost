#Micah Trost
#4/21/2026

import tkinter
from tkinter import messagebox  

class GUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.rate_frame = tkinter.Frame()
        self.minutes_frame = tkinter.Frame()
        self.button_frame = tkinter.Frame()

        self.rate_var = tkinter.IntVar()
        self.daytime_radio = tkinter.Radiobutton(self.rate_frame, text="Daytime (6:00 A.M. through 5:59 P.M.) - $0.02 per minute", variable=self.rate_var, value=1)
        self.evening_radio = tkinter.Radiobutton(self.rate_frame, text="Evening (6:00 P.M. through 11:59 P.M.) - $0.12 per minute", variable=self.rate_var, value=2)
        self.offpeak_radio = tkinter.Radiobutton(self.rate_frame, text="Off-Peak (midnight through 5:59 A.M.) - $0.05 per minute", variable=self.rate_var, value=3)

        self.minutes_label = tkinter.Label(self.minutes_frame, text="Number of minutes of the call: ")
        self.minutes_entry = tkinter.Entry(self.minutes_frame, width=10)

        self.calc_button = tkinter.Button(self.button_frame, text="Calculate Charge", command=self.calculate_charge)

        self.daytime_radio.pack(anchor="w")
        self.evening_radio.pack(anchor="w")
        self.offpeak_radio.pack(anchor="w")

        self.minutes_label.pack(side="left")
        self.minutes_entry.pack(side="left")

        self.calc_button.pack()

        self.rate_frame.pack()
        self.minutes_frame.pack()
        self.button_frame.pack()

        tkinter.mainloop()
    def calculate_charge(self):
        minutes = float(self.minutes_entry.get())
        if self.rate_var.get() == 1:
            charge = minutes * 0.02
            messagebox.showinfo(f"Charge for the call", f"The charge for the call is: ${charge:.2f}")
        elif self.rate_var.get() == 2:
            charge = minutes * 0.12
            messagebox.showinfo(f"Charge for the call", f"The charge for the call is: ${charge:.2f}")
        elif self.rate_var.get() == 3:
            charge = minutes * 0.05
            messagebox.showinfo(f"Charge for the call", f"The charge for the call is: ${charge:.2f}")
if __name__ == "__main__":    
    gui = GUI()