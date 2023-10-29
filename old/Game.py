# GAME
from typing import List
from Wheel import RouletteWheel
from Player import Player

class RouletteGame:
    def __init__(self):
        self.players: List[Player] = []

    def add_player(self, player: Player):
        self.players.append(player)

    def play_round(self):
        for player in self.players:
            print(f"{player.name}'s balance: ${player.balance}")
            pocket = self.wheel.spin()
            color = self.wheel.get_color(pocket)
            print(f"Pocket: {pocket} ({color})")

            bet_color = input(f"{player.name}, enter the color you want to bet on (red/black): ").lower()
            bet = int(input(f"Enter your bet (1-{player.balance}): "))

            if player.place_bet(bet, bet_color):
                if pocket == 0:
                    print("Green zero! You lose.")
                elif color == player.bet_color:
                    player.win(bet * 2)
                    print(f"Congratulations, {player.name}! You won ${bet * 2}.")
                else:
                    print(f"Sorry, {player.name}. You lose ${bet}.")
                    player.lose()
            else:
                print("Invalid bet. Please try again.")
                continue

    def start_game(self):
        self.wheel: RouletteWheel = RouletteWheel()
        print("Welcome to Roulette!")
        num_players: int = int(input("Enter the number of players: "))

        for _ in range(num_players):
            name: str = input(f"Enter player {_ + 1}'s name: ")
            player: Player = Player(name)
            self.add_player(player)

        while True:
            self.play_round()
            continue_playing: str = input("Do you want to play another round? (yes/no): ").lower()
            if continue_playing != 'yes':
                break

if __name__ == "__main__":
    game: RouletteGame = RouletteGame()
    game.start_game()
