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

    TODO Integrate custom time for timer, change break timer to be its own thing, Implement reset button, add File location box.

    """
    def __init__(self, master):
        self.master = master

        # Time now Label
        self.clock = tk.Label(master, text="")
        self.clock.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
        self.update_clock()

        # Close button (REPLACE WITH CHECKMARKS)
        # self.close_button = tk.Button(master, text="Close", command=master.quit)
        # self.close_button.grid(row=0, column=1, sticky=tk.N+tk.S+tk.E+tk.W)

        # Checkmarks
        self.marks = 0
        self.checkmark = tk.Label(master, image=CHECKMARK0)
        self.checkmark.photo = CHECKMARK0
        self.checkmark.grid(row=0, column=1, sticky=tk.N+tk.S+tk.E+tk.W)

        # Start timer (DUMMY)
        self.switch = False
        self.run_button = tk.Button(master, text="Run Timer", command=self.run_timer)
        self.run_button.grid(row=1, column=0, sticky=tk.N+tk.S+tk.E+tk.W)

        # Custom Timer Entry
        self.custom_timer = tk.Text(root, width=3, height=1)
        self.custom_timer.insert(tk.END, "0")
        self.custom_timer.grid(row=1, column=1, sticky=tk.N+tk.S+tk.E+tk.W)

        # Break Timer (Start Timer Copy)
        self.switch = False
        self.break_button = tk.Button(master, text="Break Timer", command=self.run_timer)
        self.break_button.grid(row=2, column=0, sticky=tk.N + tk.S + tk.E + tk.W)

        # Break Custom Time
        self.break_timer = tk.Text(root, width=3, height=1)
        self.break_timer.insert(tk.END, "0")
        self.break_timer.grid(row=2, column=1, sticky=tk.N + tk.S + tk.E + tk.W)

        # Text entry
        self.submit_button = tk.Button(master, text="Submit", command=self.submit)
        self.submit_button.grid(row=3, column=1,  sticky=tk.E+tk.W)
        self.text = ScrolledText(root, width=32, height=8)
        self.text.grid(row=0, column=2, rowspan=3, sticky=tk.N+tk.S+tk.E+tk.W)

        # Reset Button
        self.reset_button = tk.Button(master, text="Reset")
        self.reset_button.grid(row=3, column=0, sticky=tk.N+tk.S+tk.E+tk.W)

    def update_clock(self):
        # Update clock label every second
        now = time.strftime("%H:%M:%S")
        self.clock.configure(text=now)
        root.after(1000, self.update_clock)

    def run_timer(self):
        if self.run_button["state"] == tk.DISABLED:
            print("Time is up")
            self.run_button.config(state=tk.NORMAL)
            self.update_marks()
        else:
            root.after(5000, self.run_timer)
            self.run_button.config(state=tk.DISABLED)

    def update_marks(self):
        if self.marks is 0:
            self.marks = 1
            self.checkmark.configure(image=CHECKMARK1)
            self.checkmark.image = CHECKMARK1
        elif self.marks is 1:
            self.marks = 2
            self.checkmark.configure(image=CHECKMARK2)
            self.checkmark.image = CHECKMARK2
        elif self.marks is 2:
            self.marks = 3
            self.checkmark.configure(image=CHECKMARK3)
            self.checkmark.image = CHECKMARK3
        elif self.marks is 3:
            self.marks = 4
            self.checkmark.configure(image=CHECKMARK4)
            self.checkmark.image = CHECKMARK4
        else:                                           # Replace with Reset Button
            self.marks = 0
            self.checkmark.configure(image=CHECKMARK0)
            self.checkmark.image = CHECKMARK0

    def submit(self):
        #
        # TODO write to text file instead of printing, add timestamp
        text = self.text.get("1.0", tk.END)
        self.text.delete("1.0", tk.END)
        print(text)


# Start Tk
root = tk.Tk()
root.geometry("480x320+32+32")



# Global Resources
DEBUG = False

CHECKMARK0 = tk.PhotoImage(file="icon_0.png")
CHECKMARK1 = tk.PhotoImage(file="icon_1.png")
CHECKMARK2 = tk.PhotoImage(file="icon_2.png")
CHECKMARK3 = tk.PhotoImage(file="icon_3.png")
CHECKMARK4 = tk.PhotoImage(file="icon_4.png")

# Class initialization
gui = Pomodoro(root)

# Main loop
root.mainloop()
