from tkinter import *
from functools import partial
import all_constants as c
import conversion_rounding as cr


class Converter:
    """
    Temperature conversion tool (°C to °F or °F to °C)
    """

    def __init__(self):
        """
        Temperature converter GUI
        """

        self.all_calculations_list = []

        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.temp_heading = Label(self.temp_frame,
                                  text="Temperature Converter",
                                  font=("Arial", "16", "bold"))
        self.temp_heading.grid(row=0)

        instructions = ("Please enter a temperature below and then press "
                        "one of the buttons to convert it from centigrade to "
                        "Fahrenheit.")
        self.temp_instructions = Label(self.temp_frame,
                                       text=instructions,
                                       wraplength=150, width=40,
                                       justify="left")
        self.temp_instructions.grid(row=1)

        self.temp_entry = Entry(self.temp_frame,
                                font=("Arial", "14"))
        self.temp_entry.grid(row=2, padx=10, pady=10)

        error = "Please enter a number"
        self.answer_error = Label(self.temp_frame, text=error, fg="#004C99",
                                  font=("Arial", "14", "bold"))
        self.answer_error.grid(row=3)

        # Conversion, help and history/export buttons
        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)

        # Button list (button text | bg color | command | row | column)
        button_details_list = [
            ["To Celsius", "#990099", lambda: self.check_temp(c.ABS_ZERO_FAHRENHEIT), 0, 0],
            ["To Fahrenheit", "#009900", lambda: self.check_temp(c.ABS_ZERO_CELSIUS), 0, 1],
            ["Help / Info", "#CC6600", self.to_help, 1, 0],  # Fixed row and column
            ["History / Export", "#004C99", None, 1, 1],  # Fixed row and column
        ]

        # List to hold buttons once they have been made
        self.button_ref_list = []

        for item in button_details_list:
            make_button = Button(self.button_frame,
                                 text=item[0], bg=item[1],
                                 fg="#FFFFFF", font=("Arial", "12", "bold"),
                                 width=12, command=item[2])
            make_button.grid(row=item[3], column=item[4], padx=5, pady=5)
            self.button_ref_list.append(make_button)

        self.to_help_button = self.button_ref_list[2]

        # Retrieve 'history / export' button and disable it at the start
        self.to_history_button = self.button_ref_list[3]
        self.to_history_button.config(state=DISABLED)

    def check_temp(self, min_temp):
        """
        Check temperature is valid and either invokes calculation
        function or shows a custom number
        """
        to_convert = self.temp_entry.get()

        self.answer_error.config(fg="#004C99", font=("Arial", "13", "bold"))
        self.temp_entry.config(bg="#FFFFFF")

        error = f"Enter a number more than / equal to {min_temp}"
        has_errors = "no"

        try:
            to_convert = float(to_convert)
            if to_convert >= min_temp:
                error = ""
                self.convert(min_temp, to_convert)
            else:
                error = "Too Low"
        except ValueError:
            error = "Please enter a number"

        # Display the error if necessary
        if error != "":
            self.answer_error.config(text=error, fg="#9C0000")
            self.temp_entry.config(bg="#F4CCCC")
            self.temp_entry.delete(0, END)

    def convert(self, min_temp, to_convert):
        """
        Convert temperature and update answer label
        """
        if min_temp == c.ABS_ZERO_CELSIUS:
            answer = cr.to_fahrenheit(to_convert)
            answer_statement = f"{to_convert}°C is {answer} °F"
        else:
            answer = cr.to_celsius(to_convert)
            answer_statement = f"{to_convert}°F is {answer} °C"

        # Enable history export button
        self.to_history_button.config(state=NORMAL)

        # Update answer label
        self.answer_error.config(text=answer_statement)
        self.all_calculations_list.append(answer_statement)

    def to_help(self):
        """
        Open help dialogue box and display help button
        (so that users can't create multiple help box).
        """
        DisplayHelp(self)


class DisplayHelp:
    """
    Display help information in a new window
    """

    def __init__(self, partner):
        background = "#ffe6cc"
        self.help_box = Toplevel()

        # Disable help button
        partner.to_help_button.config(state=DISABLED)

        # If users press cross at top, closes help and release help button
        self.help_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_help, partner))

        self.help_frame = Frame(self.help_box, width=300,
                                height=200)
        self.help_frame.grid()

        self.help_heading_label = Label(self.help_frame, text="Help / Info",
                                        font=("Arial", "14", "bold"))
        self.help_heading_label.grid(row=0)

        help_text = "To use this program simply enter a temperature  " \
                    "you wish to convert and then press the button " \
                    "to either convert from Celsius (centigrade) or Fahrenheit. \n\n" \
                    "Note that -273 degree C " \
                    "is the absolute zero and -459.67 degree F is the (coldest temperature as possible). " \
                    "If you try to convert temperatures below this limit you will receive an error. \n\n" \
                    "To see your calculation history and export it to a text file, press the 'History / Export' button."

        self.help_text_label = Label(self.help_frame, text=help_text, wraplength=350,
                                     justify="left")
        self.help_text_label.grid(row=1, padx=10)

        self.dismiss_button = Button(self.help_frame,
                                    font=("Arial", "12", "bold"),
                                    text="Dismiss", bg="#CC6600",
                                    fg="#FFFFFF",
                                    command=partial(self.close_help, partner))
        self.dismiss_button.grid(row=2, padx=10, pady=10)

        # Set background colour for all widgets
        recolour_list = [self.help_frame, self.help_heading_label, self.help_text_label]
        for item in recolour_list:
            item.config(bg=background)

    def close_help(self, partner):
        """
        Close help dialogue box and re-enable help button.
        """
        # Put help button back to normal
        partner.to_help_button.config(state=NORMAL)
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()