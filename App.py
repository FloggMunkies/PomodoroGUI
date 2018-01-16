import tkinter as tk
import time


class App:
    def __init__(self, master):
        self.master = master

        # Tomato
        tomato_icon = tk.PhotoImage(file="tomato.png")
        tomato_label = tk.Label(self.master, image=tomato_icon)
        tomato_label.photo = tomato_icon
        # tomato_label.pack()

        # Time
        self.time = time.strftime("%M:%S", time.strptime("25 0", "%M %S"))
        self.time_text = tk.Label(self.master, image=tomato_icon, text=self.time, font=("Helvetica", 16), compound=tk.CENTER)
        self.time_text.pack()
        self.time_text.bind("<Button-1>", self.foo)

    def foo(self, event):
        popup = tk.Tk()
        popup.geometry("128x64+32+32")
        window = Timer(popup)
        popup.mainloop()
        print("test")

    def update_timer(self, new_time):
        print(new_time)
        self.time = time.strftime("%M:%S", time.strptime(new_time, "%M:%S"))
        self.time_text.config(text=self.time)


class Timer:
    def __init__(self, master):
        self.master = master
        self.master.bind("<Return>", self.update_timer)

        # Text Entry
        self.label = tk.Label(self.master, text="Enter new time:")
        self.text = tk.Text(self.master, width=5, height=1)
        self.label.grid(row=0)
        self.text.grid(row=1)

        self.temp = tk.Button(self.master, text="Foobar", command=self.update_timer)
        self.temp.grid(row=2)

    def update_timer(self, event=""):
        print(event)
        new_time = self.text.get("1.0", "end-1c")  # grabs text from line 1 to end - 1 char to avoid grabbing \n
        App.update_timer(gui, new_time)
        self.master.destroy()


# Start Tk
root = tk.Tk()
root.geometry("256x256+32+32")


# Global Resources
DEBUG = False


# Class initialization
gui = App(root)

# Main loop
root.mainloop()
