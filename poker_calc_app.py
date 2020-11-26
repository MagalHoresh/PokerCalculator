#!/usr/bin/python3
# main_app.py by Magal Horesh
# This is a poker calculator

from tkinter import *
from tkinter import ttk
from e_calc import eCalc
from four_bet_calc import FourBetCalc


class PokerCalcApp(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        parent.title('PokerCalc')
        parent.geometry('300x250+500+300')
        parent.resizable(False, False)

        self.notebook = ttk.Notebook(self)
        self.notebook.pack()
        self.e_calc_tab = eCalc(self.notebook)
        self.four_bet_calc_tab = FourBetCalc(self.notebook)
        self.notebook.add(self.e_calc_tab, text='eCalc')
        self.notebook.add(self.four_bet_calc_tab, text='4BetCalc')

        # define dictionaries
        self.enter_key_dict = {
            0: self.e_calc_tab.handle_go_button,
            1: self.four_bet_calc_tab.handle_go_button
        }
        self.c_key_dict = {
            0: self.e_calc_tab.handle_clear_button,
            1: self.four_bet_calc_tab.handle_clear_button
        }

        # define styles
        self.style = ttk.Style()
        self.style.configure('InputLabel.TLabel', foreground='blue',
                             font=('Ariel', 12, 'bold'))
        self.style.configure('ResultLabel.TLabel', foreground='blue',
                             font=('Ariel', 18, 'bold'))
        self.style.configure('Button.TButton', foreground='green',
                             font=('Ariel', 10, 'bold'))
        self.style.configure('TEntry', width=20)

        # handle keyboard events
        parent.bind('<Return>', lambda e: self.handle_enter_key_pressed())
        parent.bind('c', lambda e: self.handle_c_key_pressed())

    def get_notebook_index(self):
        return self.notebook.index(self.notebook.select())

    def handle_enter_key_pressed(self):
        self.enter_key_dict[self.get_notebook_index()]()

    def handle_c_key_pressed(self):
        self.c_key_dict[self.get_notebook_index()]()


if __name__ == "__main__":
    root = Tk()
    PokerCalcApp(root).pack()
    root.mainloop()
