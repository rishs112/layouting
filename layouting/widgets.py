from abc import ABC, abstractmethod
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List

@dataclass_json
class Widget(ABC):

    @abstractmethod
    def size(self):
        pass

@dataclass
class Rectangle(Widget):
    w: int
    h: int

    def size(self):
        return (self.w, self.h)

@dataclass
class Row(Widget):
    children: List[Widget]

    def size(self):
        width = 0
        height = 0
        for child in self.children:
            child_w, child_h = child.size()

            if (height < child_h):
                height = child_h
            width += child_w

        return (width, height)
    
@dataclass
class Column(Widget):
    children: List[Widget]

    def size(self):
        width = 0
        height = 0
        for child in self.children:
            child_w, child_h = child.size()

            if (width < child_w):
                width = child_w
            height += child_h

        return (width, height)
