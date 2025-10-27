from dataclasses import dataclass

@dataclass
class Panel:
    name: str
    function: str
    absorption: float
    surface: float
    length: float
    width: float

PANELS = [
    Panel("ecophon_wall", "wall", 1.0, 1.62, 2.7, 0.6),
    Panel("mega_wall", "wall", 0.85, 0.9, 2.0, 0.45),
    Panel("ecophon_solo", "ceilling", 2.6, 1.44, 1.2, 1.2), #2.6 ABSORPTION IS COEFFICIENT FOR ONE PANEL!
    Panel("ecophon_master", "ceilling", 1.0, 1.44, 1.2, 1.2)
    ]

@dataclass
class Covering:
    name: str
    function: str
    absortion: float

COVERINGS = [
    Covering("carpet", "floor", 0.15)
    ]

@dataclass
class Room:
    name: str
    multiplier: float

ROOMS = [Room("open_space", 1.1)]