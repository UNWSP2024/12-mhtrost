#Micah Trost
#4/21/2026

import tkinter

class GUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.gallon_frame = tkinter.Frame()
        self.miles_frame = tkinter.Frame()
        self.button_frame = tkinter.Frame()
        self.result_frame = tkinter.Frame()

        self.gallon_label = tkinter.Label(self.gallon_frame, text="Gallons of gas the car holds: ")
        self.gallon_entry = tkinter.Entry(self.gallon_frame, width=10)

        self.miles_label = tkinter.Label(self.miles_frame, text="Miles the car can be driven on a full tank: ")
        self.miles_entry = tkinter.Entry(self.miles_frame, width=10)

        self.calc_button = tkinter.Button(self.button_frame, text="Calculate MPG", command=self.calculate_mpg)

        self.result_label = tkinter.Label(self.result_frame, text="Miles per gallon: ")

        self.gallon_label.pack(side="left")
        self.gallon_entry.pack(side="left")

        self.miles_label.pack(side="left")
        self.miles_entry.pack(side="left")

        self.calc_button.pack()

        self.result_label.pack()

        self.gallon_frame.pack()
        self.miles_frame.pack()
        self.button_frame.pack()
        self.result_frame.pack()

        tkinter.mainloop()
    def calculate_mpg(self):
        gallons = float(self.gallon_entry.get())
        miles = float(self.miles_entry.get())
        mpg = miles / gallons
        self.result_label.config(text="Miles per gallon: " + str(mpg))
if __name__ == "__main__":    
    gui = GUI()
