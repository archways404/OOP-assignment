# PLAYER

from typing import Optional

class Player:
    def __init__(self, name: str, initial_balance: int = 100):
        self.name: str = name
        self.balance: int = initial_balance
        self.bet: int = 0
        self.bet_color: Optional[str] = None

    def place_bet(self, amount: int, color: str) -> bool:
        if amount <= self.balance and color in ["red", "black"]:
            self.bet = amount
            self.bet_color = color
            self.balance -= amount
            return True
        else:
            return False

    def win(self, amount: int):
        self.balance += amount

    def lose(self):
        self.bet = 0
        self.bet_color = None
