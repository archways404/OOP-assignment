# WHEEL

import random
from typing import List, Dict

class RouletteWheel:
    def __init__(self):
        self.pockets: List[int] = list(range(37))  # 0 to 36
        self.pocket_colors: Dict[int, str] = {
            0: "green",
            32: "red",
            15: "black",
            # Define pocket colors for the remaining numbers
        }

    def spin(self) -> int:
        return random.choice(self.pockets)

    def get_color(self, pocket: int) -> str:
        return self.pocket_colors.get(pocket, 'unknown')
