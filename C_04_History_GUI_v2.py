from tkinter import *
from functools import partial
import all_constants as c

class Converter:
    """
        Temperature conversion tool (°C to °F or °F to °C)
        """

    def __init__(self):
        """
        Temperature converter GUI
        """

        self.all_calculations_list = ['10.0 °F is -12°C', '20.0 °F is -7°C',
                                      '30.0 °F is -1°C', '40.0 is 4°C',
                                      '50.0 °F is 10°C', '60.0 °F is 16°C']

        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.to_history_button = Button(self.temp_frame,
                                     text="Help / Export",
                                     bg="#CC6600",
                                     fg="#FFFFFF",
                                     font=("Arial", "14", "bold"), width=12,
                                     command=self.to_history)
        self.to_history_button.grid(row=1, padx=5, pady=5)


    def to_history(self):
        """
        Open help dialogue box and disable history button
        (so that users can't create multiple history box).
        """
        HistoryExport(self, self.all_calculations_list)

class HistoryExport:

    """
    Displays history dialog box and export button
    """


    def __init__(self, partner, calculations):
        # setup dialogue box and background colour

        self.history_box = Toplevel()

        partner.to_history_button.config(state=DISABLED)

        #If users press cross at top, closes history and release history button
        self.history_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_history,partner))

        self.history_frame = Frame(self.history_box)
        self.history_frame.grid()

        if len(calculations) <= c.MAX_CALCS:
            calc_back = "#D5E8D4"
            calc_amount = "all your"
        else:
            calc_back = "#ffe6cc"
            calc_amount = (f"your recent calculations - "
                           f"showing {c.MAX_CALCS} / {len(calculations)}")

        recent_intro_txt = (f"Below are {calc_amount} calculations - showing"
                            "3 / 3 calculations. All calculations are"
                            "shown to the nearest degree")

        newest_first_string = ""
        newest_first_list = list(reversed(calculations))

        if len(calculations) <= c.MAX_CALCS:
            for item in newest_first_list:
                newest_first_string += item + "\n"
        else:
            for item in newest_first_list[c.MAX_CALCS-1]:
                newest_first_string += item + "\n"

            newest_first_string += newest_first_list[-1]

        export_instruction_txt = ("Please push <Export> to save your calculations"
                                 "in file. If the filename already exists, it will be overwritten.  ")

        history_labels_list = [
            ["History / Export", ("Arial", "16", "bold"), None],
            [recent_intro_txt, ("Arial", "11"), None],
            [newest_first_list, ("Arial", "14"), calc_back],
            [export_instruction_txt, ("Arial", "11"), None],
        ]

        history_labels_ref = []
        for count, item in enumerate(history_labels_list):
            make_label = Label(self.history_frame, text=item[0], font=item[1],
                               bg=item[2],
                               wraplength=300, justify="left", padx=10, pady=20)
            make_label.grid(row=count)

            history_labels_ref.append(make_label)

        # Retrieve export instruction label so that we can
        # configure it to show the filename if the user exports the file
        self.export_filename_label = history_labels_ref[3]

        # make frame to hold buttons
        self.history_button_frame = Frame(self.history_box)
        self.history_button_frame.grid(row=4)

        button_ref_list = []

        button_details_list = [
            ["Export", "#004C99", "", 0,0],
            ["Close", "#666666", partial(self.close_history, partner), 0,1]
        ]

        for btn in button_details_list:
            self.make_button = Button(self.history_button_frame,
                                      font=("Arial", "12", "bold"),
                                      text=btn[0], bg=btn[1],
                                      fg="#FFFFFF", width=12,
                                      command=btn[2])
            self.make_button.grid(row=btn[3], column=btn[4], padx=20, pady=10)


    def close_history(self, partner):
        self.history_box.destroy()
        """
        Close history dialogue box and reenable history button.
        """
        #put history button to normal
        partner.to_history_button.config(state=NORMAL)
        self.history_box.destroy()



# Main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
