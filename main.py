import tkinter as tk


class App(tk.Tk):

    def __init__(self):
        super().__init__()

        # Color settings
        self.bg_color = "white"
        self.txt_color = "black"


        self.geometry("400x600")
        self.resizable(False, False)
        self.title("MoneyREsult")

        # Change theme
        self.scale = tk.Scale(self, from_=0, to=1, orient=tk.HORIZONTAL, showvalue=False, command=self.theme_change)
        self.scale.grid(row=0, column=0, sticky="wn")

        # RadioButton Frame
        # Make Frame of RadioButton
        self.radio_btn_frame = tk.Frame(borderwidth=1, relief=tk.SOLID, bg=self.bg_color)
        self.radio_btn_frame.grid(row=1, column=0, sticky="wesn")

        self.ch = tk.IntVar()
        self.ch.set(0)
        # Draw visual radiobutton
        self.draw_radio_btn()

        # MoneyGet Frame
        self.entry_get = []
        self.money_get_frame = tk.Frame(borderwidth=1, relief=tk.SOLID)
        self.money_get_frame.grid(row=2, column=0, sticky="wesn")

        self.draw_money_get_label()
        self.draw_entry_get()

        # Result
        # Result var
        self.result = 0
        tk.Label(self, text=str(self.result), font=("Arial", 50), bg=self.bg_color, fg=self.txt_color).\
            grid(row=3, column=0, sticky="wesn")

        tk.Button(self, text="Result!", command=self.get_result, font=("Arial", 36), bg=self.bg_color, fg=self.txt_color).\
            grid(row=5, column=0, sticky="wesn")

        self.grid_rowconfigure(3, minsize=154)
        self.grid_columnconfigure(0, minsize=400)
        self.money_get_frame.grid_columnconfigure(0, minsize=135)
        self.money_get_frame.grid_columnconfigure(2, minsize=135)

    def frame_color(self):
        self.money_get_frame["bg"] = self.bg_color
        self.radio_btn_frame["bg"] = self.bg_color

    def draw_radio_btn(self):

        tk.Label(self.radio_btn_frame, text="Settings!", font=("Arial", 16), bg=self.bg_color, fg=self.txt_color)\
            .grid(row=0, column=0)
        for i, j in zip(["Only coins!", "Only bill!", "All!"], [2, 1, 0]):
            tk.Radiobutton(self.radio_btn_frame, text=i, variable=self.ch, activebackground=self.bg_color, command=self.change_mode, value=j, bg=self.bg_color, fg="grey", padx=30, font=("Arial", 12)).grid(row=1, column=j)

        self.radio_btn_frame.grid_rowconfigure(1, minsize=40)

    def draw_entry_get(self):

        for rows_index in range(1, 8, 2):
            for column_index in range(3):
                ent = tk.Entry(self.money_get_frame, state=tk.NORMAL)
                self.entry_get.append(ent)
                ent.grid(row=rows_index, column=column_index)
                ent.insert(0, "0")

    def draw_entry(self):

        bill_cost = [1, 3, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000]

        for rows_index in range(12):
            if self.ch.get() == 2 and bill_cost[rows_index] > 10:
                self.entry_get[rows_index]["state"] = tk.DISABLED
            elif self.ch.get() == 1 and bill_cost[rows_index] <= 10:
                self.entry_get[rows_index]["state"] = tk.DISABLED
            else:
                self.entry_get[rows_index]["state"] = tk.NORMAL

    def draw_money_get_label(self):

        rows_index_list = [i for i in range(0, 7, 2)]
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
        for i in range(12):
            self.entry_get[i].delete(0, tk.END)
            self.entry_get[i].insert(0, "0")

    def count_result(self):
        count_money = 0
        bill_cost = [1, 3, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000]
        for i in range(12):
            try:
                count_money += int(self.entry_get[i].get()) * bill_cost[i]
            except:
                break

        return count_money

    def get_result(self):
        self.result = self.count_result()
        for i in range(12):
            print(self.entry_get[i].get())
        tk.Label(self, text=str(self.result), font=("Arial", 50), bg=self.bg_color, fg=self.txt_color).\
            grid(row=3, column=0, sticky="wesn")

    def theme_change(self, mode):
        if int(mode) == 1:
            self.bg_color = "black"
            self.txt_color = "white"
        if int(mode) == 0:
            self.bg_color = "white"
            self.txt_color = "black"

        self.draw_radio_btn()
        self.frame_color()
        self.draw_money_get_label()

        tk.Label(self, text=str(self.result), font=("Arial", 50), bg=self.bg_color, fg=self.txt_color). \
            grid(row=3, column=0, sticky="wesn")
        self["bg"] = self.bg_color


    def change_mode(self):
        print(self.ch.get())
        self.draw_radio_btn()
        self.make_zero()
        self.draw_money_get_label()
        self.draw_entry()




if __name__ == "__main__":
    app = App()
    app.mainloop()
