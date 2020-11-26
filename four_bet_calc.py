#!/usr/bin/python3
# four_bet_calc.py by Magal Horesh
# This is a 4Bet sizing calculator

from tkinter import *
from tkinter import ttk


class FourBetCalc(ttk.Frame):

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)

        self.three_bet_size = IntVar()

        # create frame
        self.three_bet_size_frame = ttk.Frame(self, padding=(20, 5))
        self.three_bet_size_label = ttk.Label(
            self.three_bet_size_frame, text='3-Bet Size', style='InputLabel.TLabel')
        self.three_bet_size_label.pack(side=LEFT)
        self.three_bet_size_entry = ttk.Entry(
            self.three_bet_size_frame, textvariable=self.three_bet_size)
        self.three_bet_size_entry.pack(side=LEFT)
        self.three_bet_size_frame.pack()

        self.delete_entries_text()

        # create buttons
        self.buttons_frame = ttk.Frame(self, padding=(20, 10))
        self.go_button = ttk.Button(
            self.buttons_frame, text="Go!", command=self.handle_go_button, style='Button.TButton').pack(side=LEFT)
        self.clear_button = ttk.Button(
            self.buttons_frame, text="Clear", command=self.handle_clear_button, style='Button.TButton').pack(side=LEFT)
        self.buttons_frame.pack()

        # create results labels
        self.in_position_text = StringVar()
        self.out_off_position_text = StringVar()
        self.in_position_label = ttk.Label(
            self, textvariable=self.in_position_text, style='ResultLabel.TLabel').pack()
        self.out_off_position_label = ttk.Label(
            self, textvariable=self.out_off_position_text, style='ResultLabel.TLabel').pack()

    def handle_go_button(self):
        in_position_sizing = round(self.three_bet_size.get() * 2.4)
        out_off_position_sizing = round(self.three_bet_size.get() * 2.6)

        self.in_position_text.set(f'2.4x = {in_position_sizing}')
        self.out_off_position_text.set(f'2.6x = {out_off_position_sizing}')

    def handle_clear_button(self):
        self.delete_entries_text()
        self.clear_results_labels()

    def delete_entries_text(self):
        self.three_bet_size_entry.delete(0, END)

    def clear_results_labels(self):
        self.in_position_text.set('')
        self.out_off_position_text.set('')
