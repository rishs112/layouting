from layouting.widgets import *

with open("widgets.json") as f:
    widget_values = Rectangle.from_json(f.read())

    print(widget_values)