import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import time


class Pomodoro:
    """Pomodoro GUI timer for time management and workflow

    6 Parts to Pomodoro technique:
        1) Decide task to be done
        2) Set timer (25 mins)
        3) Work until timer goes off
        4) Add checkmark after timer goes off
        5) if # of checkmarks is < 4 then take short 3-5 min break and go back to step 1
        6 if # of checkmarks is >= 4 then take a longer break, 15-30 mins, and erase all checkmarks and start over at 1

    This App allows for you to easily set and start your timer and keep track of checkmarks, with the added bonus of
    keeping a log of your work related to step 1 in a text file.

    TODO Finish the timer button, Checkmarks, break timers, final reset, Make pretty, unit test

    """
    def __init__(self, master):
        self.master = master

        # Time now Label
        self.clock = tk.Label(master, text="")
        self.clock.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
        self.update_clock()

        # Close button (REPLACE WITH CHECKMARKS)
        self.close_button = tk.Button(master, text="Close", command=master.quit)
        self.close_button.grid(row=0, column=1, sticky=tk.N+tk.S+tk.E+tk.W)

        # Start timer (DUMMY)
        self.switch = False
        self.run_button = tk.Button(master, text="Run Timer", command=self.run_timer)
        self.run_button.grid(row=1, column=0, sticky=tk.N+tk.S+tk.E+tk.W)

        # Custom Timer Entry
        self.custom_timer = tk.Text(root, width=3, height=1)
        self.custom_timer.insert(tk.END, "0")
        self.custom_timer.grid(row=1, column=1, sticky=tk.N+tk.S+tk.E+tk.W)

        # Text entry
        self.submit_button = tk.Button(master, text="Submit", command=self.submit)
        self.submit_button.grid(row=4, column=1,  sticky=tk.N+tk.S+tk.E+tk.W)
        self.text = ScrolledText(root, width=56, height=8)
        self.text.grid(row=3, columnspan=2, sticky=tk.N+tk.S+tk.E+tk.W)

    def update_clock(self):
        # Update clock label every second
        now = time.strftime("%H:%M:%S")
        self.clock.configure(text=now)
        root.after(1000, self.update_clock)

    def run_timer(self):
        # Self referential function to wait 5 seconds and switching modes to indicate time is up
        print("Switch is set to", self.switch)
        if self.switch:
            print("Timer is up!")
            self.switch = False
            return
        root.after(5000, self.run_timer)
        self.switch = not self.switch

    def submit(self):
        #
        # TODO write to text file instead of printing, add timestamp
        text = self.text.get("1.0", tk.END)
        self.text.delete("1.0", tk.END)
        print(text)


root = tk.Tk()
root.geometry("480x320+32+32")
gui = Pomodoro(root)
root.mainloop()
