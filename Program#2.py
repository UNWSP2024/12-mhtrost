#Micah Trost
#4/21/2026

import tkinter

class GUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.services_frame = tkinter.Frame()
        self.button_frame = tkinter.Frame()
        self.result_frame = tkinter.Frame()

        self.oil_var = tkinter.IntVar()
        self.lube_var = tkinter.IntVar()
        self.radiator_var = tkinter.IntVar()
        self.transmission_var = tkinter.IntVar()
        self.inspection_var = tkinter.IntVar()
        self.muffler_var = tkinter.IntVar()
        self.tire_var = tkinter.IntVar()
        self.oil_check = tkinter.Checkbutton(self.services_frame, text="Oil Change - $30.00", variable=self.oil_var)
        self.lube_check = tkinter.Checkbutton(self.services_frame, text="Lube Job - $20.00", variable=self.lube_var)
        self.radiator_check = tkinter.Checkbutton(self.services_frame, text="Radiator Flush - $40.00", variable=self.radiator_var)
        self.transmission_check = tkinter.Checkbutton(self.services_frame, text="Transmission Fluid - $100.00", variable=self.transmission_var)
        self.inspection_check = tkinter.Checkbutton(self.services_frame, text="Inspection - $35.00", variable=self.inspection_var)
        self.muffler_check = tkinter.Checkbutton(self.services_frame, text="Muffler replacement - $200.00", variable=self.muffler_var)
        self.tire_check = tkinter.Checkbutton(self.services_frame, text="Tire Rotation - $20.00", variable=self.tire_var)
        self.calc_button = tkinter.Button(self.button_frame, text="Calculate Total", command=self.calculate_total)  
        self.result_label = tkinter.Label(self.result_frame, text="Total Charges: ")    
        self.oil_check.pack(anchor="w")
        self.lube_check.pack(anchor="w")
        self.radiator_check.pack(anchor="w")
        self.transmission_check.pack(anchor="w")
        self.inspection_check.pack(anchor="w")
        self.muffler_check.pack(anchor="w")
        self.tire_check.pack(anchor="w")
        self.calc_button.pack()
        self.result_label.pack()
        self.services_frame.pack()
        self.button_frame.pack()
        self.result_frame.pack()
        tkinter.mainloop()
    def calculate_total(self):
        total = 0
        if self.oil_var.get() == 1:
            total += 30
        if self.lube_var.get() == 1:
            total += 20
        if self.radiator_var.get() == 1:
            total += 40
        if self.transmission_var.get() == 1:
            total += 100
        if self.inspection_var.get() == 1:
            total += 35
        if self.muffler_var.get() == 1:
            total += 200
        if self.tire_var.get() == 1:
            total += 20
        self.result_label.config(text="Total Charges: $" + str(total))
if __name__ == "__main__":    
    gui = GUI()