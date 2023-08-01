import tkinter as tk


class App(tk.Tk):

    def __init__(self):
        super().__init__()

        # Color settings
        self.bg_color = "white"
        self.txt_color = "black"
        # Result var
        self.result = 0
        self.ch = tk.IntVar()
        self.ch.set(0)
        # MoneyGet Frame
        self.entry_get = []

        self.geometry("400x600")
        self.resizable(False, False)
        self.title("MoneyREsult")

        # Change theme
        self.scale = tk.Scale(self, from_=0, to=1, orient=tk.HORIZONTAL, showvalue=False, command=self.theme_change)
        self.scale.grid(row=0, column=0, sticky="wn")

        # RadioButton Frame
        # Make Frame of RadioButton
        self.radio_btn_frame = tk.Frame(bg=self.bg_color)
        self.radio_btn_frame.grid(row=1, column=0, sticky="wesn")
        # Money Enter Frame
        self.money_get_frame = tk.Frame(bg=self.bg_color)
        self.money_get_frame.grid(row=2, column=0, sticky="wesn")

        self.draw_screen()
        self.draw_entry_get()

        self.grid_rowconfigure(3, minsize=130)
        self.grid_columnconfigure(0, minsize=400)
        self.money_get_frame.grid_columnconfigure(0, minsize=135)
        self.money_get_frame.grid_columnconfigure(2, minsize=135)

    def frame_color(self):
        """
        Changes the color of frames.
        :return: nothing
        """
        self.money_get_frame["bg"] = self.bg_color
        self.radio_btn_frame["bg"] = self.bg_color

    def draw_radio_btn(self):
        """
        Draws buttons for switching modes.
        :return: nothing
        """
        tk.Label(self.radio_btn_frame, text="Settings!", font=("Arial", 16), bg=self.bg_color, fg=self.txt_color)\
            .grid(row=0, column=0)
        for i, j in zip(["Only coins!", "Only bill!", "All!"], [2, 1, 0]):
            tk.Radiobutton(self.radio_btn_frame, text=i, variable=self.ch, activebackground=self.bg_color, command=self.change_mode, value=j, bg=self.bg_color, fg="grey", padx=30, font=("Arial", 12)).grid(row=1, column=j)

        self.radio_btn_frame.grid_rowconfigure(1, minsize=40)

    def draw_entry_get(self):
        """
        Initializes and displays input fields.
        :return: nothing
        """
        for rows_index in range(1, 8, 2):
            for column_index in range(3):
                ent = tk.Entry(self.money_get_frame, state=tk.NORMAL, borderwidth=2)
                self.entry_get.append(ent)
                ent.grid(row=rows_index, column=column_index)
                ent.insert(0, "0")

    def draw_entry(self):
        """
        Draw input fields.
        :return: nothing
        """
        bill_cost = [1, 3, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000]

        for rows_index in range(12):
            if self.ch.get() == 2 and bill_cost[rows_index] > 10:
                self.entry_get[rows_index]["state"] = tk.DISABLED
            elif self.ch.get() == 1 and bill_cost[rows_index] <= 10:
                self.entry_get[rows_index]["state"] = tk.DISABLED
            else:
                self.entry_get[rows_index]["state"] = tk.NORMAL

    def draw_money_get_label(self):
        """
        Displays labels with cost names.
        :return: nothing
        """
        # Selection of lines on which labels will be placed
        rows_index_list = [i for i in range(0, 7, 2)]
        # Texts for labels.
        bill_cost = [[1, 3, 5], [10, 20, 50], [100, 200, 500], [1000, 2000, 5000]]

        for rows_index, bill_text in zip(rows_index_list, bill_cost):
            for column_index in range(len(bill_text)):
                if self.ch.get() == 2 and bill_text[column_index] > 10:
                    tk.Label(self.money_get_frame, text=str(bill_text[column_index]), bg=self.bg_color, fg="grey", font=("Arial", 16)). \
                        grid(row=rows_index, column=column_index)
                elif self.ch.get() == 1 and bill_text[column_index] <= 10:
                    tk.Label(self.money_get_frame, text=str(bill_text[column_index]), bg=self.bg_color, fg="grey", font=("Arial", 16)). \
                        grid(row=rows_index, column=column_index)
                else:
                    tk.Label(self.money_get_frame, text=str(bill_text[column_index]), bg=self.bg_color, fg=self.txt_color, font=("Arial", 16)). \
                        grid(row=rows_index, column=column_index)

            self.money_get_frame.grid_rowconfigure(rows_index, minsize=50)

    def make_zero(self):
        """
        Resets all input fields on zero.
        :return: nothing
        """
        for i in range(12):
            self.entry_get[i].delete(0, tk.END)
            self.entry_get[i].insert(0, "0")

    def count_result(self):
        """
        Counting summ from fields.
        :return: nothing
        """
        count_money = 0
        bill_cost = [1, 3, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000]
        for i in range(12):
            try:
                count_money += int(self.entry_get[i].get()) * bill_cost[i]
            except:
                break

        return count_money

    def get_result(self):
        """
        Print result.
        :return: nothing
        """
        self.result = self.count_result()
        tk.Label(self, text=str(self.result), font=("Arial", 50), bg=self.bg_color, fg=self.txt_color).\
            grid(row=3, column=0, sticky="wesn")

    def theme_change(self, mode):
        """
        Changes app them. Has two modes light and dark.
        int :param mode: It's the Integer number from scale for changed theme of app.
        :return:
        """
        if int(mode) == 1:
            self.bg_color = "black"
            self.txt_color = "white"
        if int(mode) == 0:
            self.bg_color = "white"
            self.txt_color = "black"

        self.draw_screen()

    def draw_result_lbl(self):
        tk.Label(self, text=str(self.result), font=("Arial", 50), bg=self.bg_color, fg=self.txt_color). \
            grid(row=3, column=0, sticky="wesn")

    def draw_result_btn(self):
        tk.Button(self, text="Result!", command=self.get_result, font=("Arial", 36), bg=self.bg_color, fg=self.txt_color).\
            grid(row=4, column=0, sticky="wesn")

    def draw_screen(self):
        """
        Draws main screen
        :return: nothing
        """
        # Radiobutton
        self.draw_radio_btn()
        # Frames
        self.frame_color()
        self.draw_money_get_label()
        # Result
        self.draw_result_lbl()
        self.draw_result_btn()
        # Them changer
        self["bg"] = self.bg_color
        self.scale["troughcolor"] = self.bg_color

    def change_mode(self):
        """
        Draws changed mode.
        :return: nothing
        """
        self.draw_radio_btn()
        self.make_zero()
        self.draw_money_get_label()
        self.draw_entry()


if __name__ == "__main__":
    app = App()
    app.mainloop()
