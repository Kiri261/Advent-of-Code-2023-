#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 17:34:39 2023

@author: kirishanakiritharan
"""

import io
import re
from dataclasses import dataclass
from typing import List

@dataclass
class ColorDraw:
    red: int = 0
    green: int = 0
    blue: int = 0

    @classmethod
    def parse(cls, datastring: str = "2233 green, 4 blue, 1 red"):
        cmd = {}
        for tpl in re.findall(r"(\d*) (green|blue|red)", datastring):
            cmd[tpl[1]] = int(tpl[0])
        return cls(**cmd)

    def calculate_power(self):
        return self.red * self.green * self.blue

@dataclass
class GameDraw:
    game_id: int
    draws: List[ColorDraw]

    @classmethod
    def parse(cls, datastring: str = "Game 11: 3 blue, 4 red; 1 red, 2 green, 6 blue"):
        m = re.match(r"^Game (\d*): (.*)$", datastring)
        if m is None:
            raise ValueError(f"{datastring=}")
        draws = []
        for draw in m.group(2).split(";"):
            draws.append(ColorDraw.parse(draw))
        game = cls(game_id=int(m.group(1)), draws=draws)
        return game

    def is_possible(self, draw: ColorDraw):
        for d in self.draws:
            if draw.red < d.red or draw.green < d.green or draw.blue < d.blue:
                return False
        return True

    def get_color_list(self, rgb: str):
        res = []
        for d in self.draws:
            res.append(getattr(d, rgb))
        return res

    def get_max_draw(self):
        colors = ["red", "green", "blue"]
        max_draw = ColorDraw()
        for c in colors:
            setattr(max_draw, c, max(self.get_color_list(c)))
        return max_draw

with io.open("/Users/kirishanakiritharan/Desktop/input2", "r") as file:
    lines = file.readlines()

result = 0
for line in lines:
    game_draw = GameDraw.parse(line)
    result += game_draw.get_max_draw().calculate_power()

print(result)
