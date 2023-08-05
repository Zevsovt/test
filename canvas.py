import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Базовый canvas")

        self.canvas = tk.Canvas(self, bg="white")
        self.label = tk.Label(self)
        self.canvas.bind("", self.mouse_motion)

        self.canvas.pack()
        self.label.pack()

    def mouse_motion(self, event):
        x, y = event.x, event.y
        text = "Позиция курсора: ({}, {})".format(x, y)
        self.label.config(text=text)

if __name__ == "__main__":
    app = App()
    app.mainloop()