from tkinter import *

class Converter():
    """
    Temperature conversion tool (°C to °F or °F to °C)
    """

    def __int__(self):
        """
        Temperatre converter GUI
        """

        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.temp_heading = Label(self.temp_frame, text="Temperature Convertor")
        self.temp_heading.grid(row=0)

# main routine
if __name__ == "--main--":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()