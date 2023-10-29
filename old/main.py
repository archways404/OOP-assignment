import random

class RouletteWheel:
    def __init__(self):
        self.pockets = list(range(37))  # 0 to 36
        self.pocket_colors = {
            0: "green",
            32: "red",
            15: "black",
            19: "red",
            4: "black",
            21: "red",
            2: "black",
            25: "red",
            17: "black",
            34: "red",
            6: "black",
            27: "red",
            13: "black",
            36: "red",
            11: "black",
            30: "red",
            8: "black",
            23: "red",
            10: "black",
            5: "red",
            24: "black",
            16: "red",
            33: "black",
            1: "red",
            20: "black",
            14: "red",
            31: "black",
            9: "red",
            22: "black",
            18: "red",
            29: "black",
            7: "red",
            28: "black",
            12: "red",
            35: "black",
            3: "red",
            26: "black"
        }

    def spin(self):
        return random.choice(self.pockets)

    def get_color(self, pocket):
        return self.pocket_colors.get(pocket, 'unknown')

class Player:
    def __init__(self, name, initial_balance=100):
        self.name = name
        self.balance = initial_balance
        self.bet = 0
        self.bet_color = None

    def place_bet(self, amount, color):
        if amount <= self.balance and color in ["red", "black"]:
            self.bet = amount
            self.bet_color = color
            self.balance -= amount
            return True
        else:
            return False

    def win(self, amount):
        self.balance += amount

    def lose(self):
        self.bet = 0
        self.bet_color = None

class RouletteGame:
    def __init__(self):
        self.players = []

    def add_player(self, player):
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
        self.wheel = RouletteWheel()
        print("Welcome to Roulette!")
        num_players = int(input("Enter the number of players: "))

        for _ in range(num_players):
            name = input(f"Enter player {_ + 1}'s name: ")
            player = Player(name)
            self.add_player(player)

        while True:
            self.play_round()
            continue_playing = input("Do you want to play another round? (yes/no): ").lower()
            if continue_playing != 'yes':
                break

if __name__ == "__main__":
    game = RouletteGame()
    game.start_game()