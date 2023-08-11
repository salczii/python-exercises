from abc import ABC, abstractmethod
from dataclasses import dataclass


class Building(ABC):
    @abstractmethod
    def area(self):
        pass


@dataclass
class Home(Building):
    rooms: int
    length: int
    width: int

    @property
    def area(self):
        return self.length * self.width

    @classmethod
    def from_area_home(cls, area, rooms):
        length = area / 2
        width = 2
        return cls(rooms, length, width)


my_home = Home(3, 10, 10)
someones_home = Home(4, 20, 20)
print(my_home == someones_home)  # thanks to @dataclass
print(my_home.area)  # thanks to @property
print(Home.from_area_home(100, 3))  # thanks to @classmethod
