from tkinter import *
from functools import partial
from functools import partial  # To prevent unwanted windows
import all_constants as c
import conversion_rounding as cr
from datetime import date



class Converter:
    """
    Temperature conversion tool (°C to °F or °F to °C)
    Temperature conversion tool (C to F or F to C
    """

def __init__(self):
    """
    Temperature converter GUI
    """
    def __init__(self):
        """
        Temperature converter GUI
        """

    self.all_calculations_list = []
<<<<<<< Updated upstream
        self.all_calculations_list = []

<<<<<<< Updated upstream
        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()
=======
    self.temp_frame = Frame(padx=10, pady=10)
    self.temp_frame.grid()

    self.temp_heading = Label(self.temp_frame,
                              text="Temperature Converter",
                              font=("Arial", "16", "bold"))
    self.temp_heading.grid(row=0)
>>>>>>> Stashed changes

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

<<<<<<< Updated upstream
        # Button list (button text | bg color | command | row | column)

        self.temp_heading = Label(self.temp_frame,
                                  text="Temperature Converter",
                                  font=("Arial", "16", "bold")
                                  )
        self.temp_heading.grid(row=0)

        instructions = ("Please enter the temperature below then press "
                        "one of the buttons to convert it from celsius "
                        "to fahrenheit or vice versa.")
        self.temp_instructions = Label(self.temp_frame,
                                       text=instructions,
                                       wraplength=245, width=40,
                                       justify="left")
        self.temp_instructions.grid(row=1)

        self.temp_entry = Entry(self.temp_frame,
                                font=("Arial", "14")
                                )
        self.temp_entry.grid(row=2, padx=10, pady=10)

        error = "Please enter a number"
        self.answer_error = Label(self.temp_frame, text=error,
                                  fg="#004C99", font=("Arial", "12", "bold"))
        self.answer_error.grid(row=3)

        # Conversion, help and history / export buttons
        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)

        # button list (button text | bg colour | command | row| column)
        button_details_list = [
            ["To Celsius", "#990099", lambda: self.check_temp(c.ABS_ZERO_FAHRENHEIT), 0, 0],
            ["To Fahrenheit", "#009900", lambda: self.check_temp(c.ABS_ZERO_CELSIUS), 0, 1],
            ["Help / Info", "#CC6600", self.to_help, 1, 0],  # Fixed row and column
            ["History / Export", "#004C99", self.to_history, 1, 1],  # Fixed row and column
            ["Help / Info", "#CC6600", self.help_info, 1, 0],  # Fixed: Changed to self.help_info
            ["History / Export", "#004C99", self.to_history, 1, 1]
        ]
=======
    # List to hold buttons once they have been made
    self.button_ref_list = []
>>>>>>> Stashed changes
=======

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
>>>>>>> Stashed changes

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

<<<<<<< Updated upstream
<<<<<<< Updated upstream

        # List to hold buttons once they have been made
        self.button_ref_list = []

        for item in button_details_list:
            self.make_button = Button(self.button_frame,
                                      text=item[0], bg=item[1],
                                      fg="#ffffff", font=("Arial", "12", "bold"),
                                      width=12, command=item[2])
            self.make_button.grid(row=item[3], column=item[4], padx=5, pady=5)

            self.button_ref_list.append(self.make_button)

        # Retrieve to_help button
        self.to_help_button = self.button_ref_list[2]

        # Retrieve 'history / export' button and disable it at the start
        self.to_history_button = self.button_ref_list[3]
        self.to_history_button.config(state=DISABLED)

    def check_temp(self, min_temp):
        """
        Check temperature is valid and either invokes calculation
        function or shows a custom number
        Check if the temperature is above the absolute zero and
        either calculates the answer or displays an error message
        """

        # Retrieve temperature to be converted
        to_convert = self.temp_entry.get()

        # Reset label and entry box (if we had an error)
        self.answer_error.config(fg="#004C99", font=("Arial", "13", "bold"))
        self.temp_entry.config(bg="#FFFFFF")
        self.temp_entry.config(bg="#ffffff")

        error = f"Enter a number more than / equal to {min_temp}"
        error = f"Enter a number more then / equal to {min_temp}"
        has_errors = "no"

        # Checks that amount to be converted is a number above absolute zero
        try:
            to_convert = float(to_convert)
            if to_convert >= min_temp:
                error = ""
                self.convert(min_temp, to_convert)
            else:
                error = "Too Low"
                error = f"Enter a number more then / equal to {min_temp}"
                has_errors = "no"

        except ValueError:
            error = "Please enter a number"

        # Display the error if necessary
        if error != "":
            self.answer_error.config(text=error, fg="#9C0000")
            self.temp_entry.config(bg="#F4CCCC")
            self.answer_error.config(text=error, fg="#9C0000", font=("Arial", "13", "bold"))
            self.temp_entry.config(bg="#FFCCCC")
            self.temp_entry.delete(0, END)

    def convert(self, min_temp, to_convert):
        """
        Convert temperature and update answer label
        Converts temperatures and updates answer label. Also stores
        calculations for Export / History feature
        """

        if min_temp == c.ABS_ZERO_CELSIUS:
            answer = cr.to_fahrenheit(to_convert)
            answer_statement = f"{to_convert}°C is {answer} °F"
=======
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
>>>>>>> Stashed changes
            answer_statement = f"{to_convert}°C is °F: {answer}°F"
        else:
            error = "Too Low"
    except ValueError:
        error = "Please enter a number"
            answer = cr.to_celsius(to_convert)
            answer_statement = f"{to_convert}°F is °C: {answer}°C"

<<<<<<< Updated upstream
        # Enable history export button
        # Enable history export button as soon as we have a valid calculation
        self.to_history_button.config(state=NORMAL)

        # Update answer label
        self.answer_error.config(text=answer_statement)
        self.all_calculations_list.append(answer_statement)
        print(self.all_calculations_list)

    def to_help(self):
        """
        Open help dialogue box and display help button
        (so that users can't create multiple help box).
        """
    def help_info(self):
        DisplayHelp(self)


    def to_history(self):
         """
        Placeholder for history export function.
        """
        HistoryExport(self)



=======
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
        Opens history dialog box and disables history button
        (so that users can't create multiple history boxes).
        """
        HistoryExport(self, self.all_calculations_list)  # Corrected variable name

    # Update answer label
    self.answer_error.config(text=answer_statement)
    self.all_calculations_list.append(answer_statement)

def to_help(self):
    """
    Open help dialogue box and display help button
    (so that users can't create multiple help box).
    """
    DisplayHelp(self)
>>>>>>> Stashed changes
class DisplayHelp:
    """
    Display help information in a new window
    """

<<<<<<< Updated upstream
    def __init__(self, partner):
        # setup dialog box and background colour
        background = "#ffe6cc"
        self.help_box = Toplevel()

        # Disable help button
        # disable help button
        partner.to_help_button.config(state=DISABLED)

        # If users press cross at top, closes help and release help button
        # If user press cross at top, closes help and
        # 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_help, partner))
=======
def __init__(self, partner):
    background = "#ffe6cc"
    self.help_box = Toplevel()

    # Disable help button
    partner.to_help_button.config(state=DISABLED)

    # If users press cross at top, closes help and release help button
    self.help_box.protocol('WM_DELETE_WINDOW',
                           partial(self.close_help, partner))
>>>>>>> Stashed changes

    self.help_frame = Frame(self.help_box, width=300,
                            height=200)
    self.help_frame.grid()

    self.help_heading_label = Label(self.help_frame, text="Help / Info",
                                    font=("Arial", "14", "bold"))
    self.help_heading_label.grid(row=0)

<<<<<<< Updated upstream
        help_text = "To use this program simply enter a temperature  " \
                    "you wish to convert and then press the button " \
                    "to either convert from Celsius (centigrade) or Fahrenheit. \n\n" \
                    "Note that -273 degree C " \
                    "is the absolute zero and -459.67 degree F is the (coldest temperature as possible). " \
                    "If you try to convert temperatures below this limit you will receive an error. \n\n" \
                    "To see your calculation history and export it to a text file, press the 'History / Export' button."

        self.help_text_label = Label(self.help_frame, text=help_text, wraplength=350,

        self.help_frame = Frame(self.help_box, width=400,
                                height=200)
        self.help_frame.grid()

        self.help_heading_label = Label(self.help_frame,
                                         text="Help / Info",
                                         font=("Arial", "14", "bold"))
        self.help_heading_label.grid(row=0)

        help_text = "To use the program, simply enter the temperature " \
                    "you wish to convert, and then choose to convert " \
                    "to either degrees celsius or " \
                    "fahrenheit.. \n\n" \
                    "Note that -273 degrees C " \
                    "(-459 F) is absolute zero (the coldest possible " \
                    "temperature). If you try to convert a " \
                    "temperature that is less than -273 degrees C, " \
                    "you will get an error message. \n\n" \
                    "To see your " \
                    "calculations history and export it to a text " \
                    "file, press the 'History / Export' button."

        self.help_text_label = Label(self.help_frame,
                                     text=help_text, wraplength=350,
                                     justify="left")
        self.help_text_label.grid(row=1, padx=10)

        self.dismiss_button = Button(self.help_frame,
                                    font=("Arial", "12", "bold"),
                                    text="Dismiss", bg="#CC6600",
                                    fg="#FFFFFF",
                                    command=partial(self.close_help, partner))
                                     font=("Arial", "12", "bold"),
                                     text="Dismiss", bg="#CC6600",
                                     fg="#FFFFFF",
                                     command=partial(self.close_help, partner))
        self.dismiss_button.grid(row=2, padx=10, pady=10)

        # Set background colour for all widgets
        recolour_list = [self.help_frame, self.help_heading_label, self.help_text_label]
        # List and loop to set background colour on
        # everything except the button
        recolour_list = [self.help_frame, self.help_heading_label,
                         self.help_text_label]

        for item in recolour_list:
            item.config(bg=background)

    def close_help(self, partner):
        """
        Close help dialogue box and re-enable help button.
        Closes help dialog box (and enables help button)
        """
        # Put help button back to normal
        partner.to_help_button.config(state=NORMAL)
        self.help_box.destroy()
=======
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
>>>>>>> Stashed changes

=======
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

>>>>>>> Stashed changes
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
        self.help_box.destroy()