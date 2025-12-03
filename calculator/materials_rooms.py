from dataclasses import dataclass

@dataclass
class Panel:
    number: int
    name: str
    function: str
    absorption: float
    surface: float
    length: float
    width: float

PANELS = [
    Panel(1, "ecophon_wall", "wall", 1.0, 1.62, 2.7, 0.6),
    Panel(2, "mega_wall", "wall", 0.85, 0.9, 2.0, 0.45),
    Panel(3, "ecophon_solo", "ceilling", 2.6, 1.44, 1.2, 1.2), #2.6 ABSORPTION IS COEFFICIENT FOR ONE PANEL!
    Panel(4, "ecophon_master", "ceilling", 1.0, 1.44, 1.2, 1.2)
    ]

@dataclass
class Covering:
    number: int
    name: str
    function: str
    absortion: float

COVERINGS = [
    Covering(1, "carpet", "floor", 0.15)
    ]

@dataclass
class Room:
    number: 1
    name: str
    multiplier: float

ROOMS = [Room(1, "open_space", 1.1)]