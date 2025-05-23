# graphics.py

from tkinter import *

class Canvas:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Canvas App")
        self.canvas = CanvasWidget(width, height)
        self.canvas.pack()
        self.root.update()

    def create_rectangle(self, x1, y1, x2, y2, color):
        return self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline='black')

    def moveto(self, obj, x, y):
        bbox = self.canvas.bbox(obj)
        if bbox:
            cur_x, cur_y = bbox[0], bbox[1]
            dx = x - cur_x
            dy = y - cur_y
            self.canvas.move(obj, dx, dy)
        self.root.update()

    def set_color(self, obj, color):
        self.canvas.itemconfig(obj, fill=color)
        self.root.update()

    def find_overlapping(self, x1, y1, x2, y2):
        return self.canvas.find_overlapping(x1, y1, x2, y2)

    def wait_for_click(self):
        self._click_pos = None
        self.canvas.bind("<Button-1>", self._on_click)
        while self._click_pos is None:
            self.root.update()
        self.canvas.unbind("<Button-1>")

    def get_last_click(self):
        return self._click_pos

    def get_mouse_x(self):
        return self.canvas.winfo_pointerx() - self.canvas.winfo_rootx()

    def get_mouse_y(self):
        return self.canvas.winfo_pointery() - self.canvas.winfo_rooty()

    def _on_click(self, event):
        self._click_pos = (event.x, event.y)

class CanvasWidget(Canvas):
    def __init__(self, width, height):
        super().__init__()
        self.canvas = Canvas(self.root, width=width, height=height, bg="white")
