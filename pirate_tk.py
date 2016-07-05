import tkinter as tk
import pirate_generator

class Application:
    def __init__(self, master):
        self.pigen = pirate_generator.pirateGenerator()
        frame = tk.Frame(master)
        self.frame = frame
        frame.pack(pady=10, padx=10)
        button_frame = tk.Frame(master)
        self.button_frame = button_frame
        button_frame.pack(side=tk.RIGHT, padx=5, pady=5)
        self.ref_input = tk.Entry(frame)
        self.ref_input.grid(row=1, column=1, columnspan=2)
        self.square_label = tk.Label(frame, text="", font=("Helvetica, 34"))
        self.square_label.grid(row=0, columnspan=3)
        self.choose_label = tk.Label(frame, text="Choose next square:")
        self.choose_label.grid(row=1, column=0)
        self.quit_button = tk.Button(
                    button_frame, text="Quit", command=frame.quit)
        self.quit_button.grid(row=2, column=2)
        self.next_button = tk.Button(
                    button_frame, text="Next Square", command=self.next_square)
        self.next_button.grid(row=2, column=1)
        self.history_button = tk.Button(button_frame, text="Show history", command=self.history_window)
        self.history_button.grid(row=2, column=0)
    def next_square(self):
        ref = self.ref_input.get()
        self.ref_input.delete(0, tk.END)
        if ref.upper() in self.pigen:
            square = ref
        elif len(ref) == 0 or ref == "Not available, choose another":
            square = None
        else:
            self.ref_input.insert(0, "Not available, choose another")
            return
        try:
            self.square_label["text"] = self.pigen.next_item(ref=square)
        except:
            self.square_label["text"] = "Game Over!"
            self.next_button.destroy()
    def history_window(self):
        his_window = tk.Toplevel(self.frame)
        his_window.minsize(width=150, height=150)
        his_window.wm_title("History")
        his_text = [""] * 5
        count = 0
        while count < len(self.pigen.history):
            his_text[count // 10] += self.pigen.history[count] + "\n"
            count += 1
        his_labels = [his for his in his_text if len(his) > 0]
        for label in his_labels:
            his_label = tk.Label(his_window, text=label)
            his_label.pack(side=tk.LEFT)


root = tk.Tk()
app = Application(root)
root.mainloop()
try:
    root.destroy()
except:
    pass
