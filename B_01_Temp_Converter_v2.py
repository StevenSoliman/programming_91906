from tkinter import *
from functools import partial
import all_constants as c
import conversion_rounding as cr
from datetime import date

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
                                       wraplength=250, width=40,
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
            ["Help / Info", "#CC6600", self.to_help, 1, 0],
            ["History / Export", "#004C99", self.to_history, 1, 1],
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

        # Retrieve to_help button
        self.to_help_button = self.button_ref_list[2]

        # Retrieve 'history / export' button and disable it at the start
        self.to_history_button = self.button_ref_list[3].config(state=DISABLED)

    def check_temp(self, min_temp):
        """
        Check temperature is valid and either invokes calculation
        function or shows a custom error message
        """
        # Retrieve temperature to be converted
        to_convert = self.temp_entry.get()

        # Reset label and entry box (if we had an error)
        self.answer_error.config(fg="#004C99", font=("Arial", "13", "bold"))
        self.temp_entry.config(bg="#FFFFFF")

        error = f"Enter a number more than / equal to {min_temp}"

        # Checks that amount to be converted is a number above absolute zero
        try:
            to_convert = float(to_convert)
            if to_convert >= min_temp:
                error = ""
                self.convert(min_temp, to_convert)
            else:
                error = f"Enter a number more than / equal to {min_temp}"
        except ValueError:
            error = "Please enter a number"

        # Display the error if necessary
        if error != "":
            self.answer_error.config(text=error, fg="#9C0000")
            self.temp_entry.config(bg="#F4CCCC")
            self.temp_entry.delete(0, END)

    def convert(self, min_temp, to_convert):
        """
        Convert temperature and update answer label. Also stores
        calculations for Export / History feature
        """
        if min_temp == c.ABS_ZERO_CELSIUS:
            answer = cr.to_fahrenheit(to_convert)
            answer_statement = f"{to_convert}°C is {answer}°F"
        else:
            answer = cr.to_celsius(to_convert)
            answer_statement = f"{to_convert}°F is {answer}°C"

        # Enable history export button as soon as we have a valid calculation
        self.to_history_button.config(state=NORMAL)

        # Update answer label
        self.answer_error.config(text=answer_statement)
        self.all_calculations_list.append(answer_statement)

    def to_help(self):
        """
        Open help dialogue box and display help button
        (so that users can't create multiple help boxes).
        """
        DisplayHelp(self)

    def to_history(self):
        """
        Opens history dialog box and disables history button
        (so that users can't create multiple history boxes).
        """
        HistoryExport(self, self.all_calculations_list)


class DisplayHelp:
    """
    Display help information in a new window
    """
    def __init__(self, partner):
        # setup dialog box and background colour
        background = "#ffe6cc"
        self.help_box = Toplevel()

        # Disable help button
        partner.to_help_button.config(state=DISABLED)

        # If users press cross at top, closes help and
        # 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_help, partner))

        self.help_frame = Frame(self.help_box, width=300,
                                height=200)
        self.help_frame.grid()

        self.help_heading_label = Label(self.help_frame, text="Help / Info",
                                        font=("Arial", "14", "bold"))
        self.help_heading_label.grid(row=0)

        help_text = "To use this program simply enter a temperature " \
                    "you wish to convert and then press the button " \
                    "to either convert from Celsius (centigrade) or Fahrenheit. \n\n" \
                    "Note that -273 degree C " \
                    "is the absolute zero and -459.67 degree F is the coldest possible temperature. " \
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

        # List and loop to set background colour on
        # everything except the button
        recolour_list = [self.help_frame, self.help_heading_label,
                         self.help_text_label]

        for item in recolour_list:
            item.config(bg=background)

    def close_help(self, partner):
        """
        Closes help dialog box and enables help button
        """
        # Put help button back to normal
        partner.to_help_button.config(state=NORMAL)
        self.help_box.destroy()


class HistoryExport:
    """
    Displays history dialog box and export button
    """

    def __init__(self, partner, calculations):
        self.history_box = Toplevel()
        partner.to_history_button.config(state=DISABLED)

        self.history_box.protocol('WM_DELETE_WINDOW', partial(self.close_history, partner))

        self.history_frame = Frame(self.history_box)
        self.history_frame.grid()

        calc_back = "#D5E8D4" if len(calculations) <= c.MAX_CALCS else "#ffe6cc"
        calc_amount = "all your" if len(
            calculations) <= c.MAX_CALCS else f"your recent calculations - showing {c.MAX_CALCS} / {len(calculations)}"

        recent_intro_txt = f"Below are {calc_amount} calculations (to the nearest degree)"

        newest_first_list = list(reversed(calculations))
        newest_first_string = "\n".join(newest_first_list[:c.MAX_CALCS])

        export_instruction_txt = (
            "Please push <Export> to save your calculations in a file. "
            "If the filename already exists, it will be overwritten."
        )

        history_labels_list = [
            ["History / Export", ("Arial", 16, "bold"), None],
            [recent_intro_txt, ("Arial", 11), None],
            [newest_first_string, ("Arial", 14), calc_back],
            [export_instruction_txt, ("Arial", 11), None],
        ]

        history_labels_ref = []
        for count, item in enumerate(history_labels_list):
            make_label = Label(
                self.history_frame, text=item[0], font=item[1],
                bg=item[2], wraplength=300, justify="left", padx=20, pady=10
            )
            make_label.grid(row=count)
            history_labels_ref.append(make_label)

        self.export_filename_label = history_labels_ref[3]

        self.history_button_frame = Frame(self.history_box)
        self.history_button_frame.grid(row=4)

        button_details_list = [
            ["Export", "#004C99", lambda: self.export_data(calculations), 0, 0],
            ["Close", "#666666", partial(self.close_history, partner), 0, 1]
        ]

        for btn in button_details_list:
            make_button = Button(
                self.history_button_frame, font=("Arial", 12, "bold"),
                text=btn[0], bg=btn[1], fg="#FFFFFF", width=12,
                command=btn[2]
            )
            make_button.grid(row=btn[3], column=btn[4], padx=20, pady=10)

    def export_data(self, calculations):
        today = date.today()

        # Get day, month and year as individual string
        day = today.strftime("%d")
        month = today.strftime("%m")
        year = today.strftime("%Y")

        file_name = f"temperature_{year}_{month}_{day}"

        success_string = ("Export successful. The file is called" 
                          f" {file_name}.txt")
        self.export_filename_label.config(fg="#009900", text=success_string ,
                                          font=("Arial", "12", "bold"))

        write_to = f"{file_name}.txt"

        with open(write_to, "w") as text_file:
            text_file.write("***** Temperature Calculations *****\n")
            text_file.write(f"Generated: {day}/{month}/{year}\n\n")
            text_file.write("Here is your calculation history (oldest to newest)...\n")

            # write the item to file
            for item in calculations:
                text_file.write(item)
                text_file.write("\n")

    def close_history(self, partner):
        partner.to_history_button.config(state=NORMAL)
        self.history_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()