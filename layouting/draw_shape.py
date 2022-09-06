from dataclasses import dataclass
from dataclasses_json import dataclass_json
import tkinter

@dataclass_json
@dataclass
class Position:
    x: int
    y: int

    @property
    def xy(self):
        return (self.x, self.y)

@dataclass_json
@dataclass
class Rectangle:
    w: int
    h: int
    pos: Position

    @property
    def bottom_right(self):
        return Position(self.pos.x + self.w, self.h + self.pos.y)

with open("layout.json") as f:
    rect_values = Rectangle.from_json(f.read())

root = tkinter.Tk()
canvas = tkinter.Canvas(root, bg = "white", height = 720, width = 1080)
position = rect_values.pos.xy
rect = canvas.create_rectangle(position, rect_values.bottom_right.xy, fill = 'red')

canvas.pack()
root.mainloop()

#rect = Rectangle(layout["w"], layout["h"], Position(layout["pos"]["x"], layout["pos"]["y"]))
