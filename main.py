import random

# Define the Card class
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

# Define the Deck class
class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

# Define the Hand class
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0

    def add_card(self, card):
        self.cards.append(card)
        self.calculate_value()

    def calculate_value(self):
      self.value = 0
      num_aces = 0
      for card in self.cards:
          if card.rank == "Ace":
              num_aces += 1
          elif card.rank in ["King", "Queen", "Jack"]:
              self.value += 10
          else:
              self.value += int(card.rank) if card.rank.isnumeric() else 10  # Use 10 for non-numeric ranks
      for _ in range(num_aces):
          if self.value + 11 <= 21:
              self.value += 11
          else:
              self.value += 1


# Define the Person class
class Person:
    def __init__(self, name, money=1000):
        self.name = name
        self.hand = Hand()
        self.wallet = Wallet(money)

# Define the Wallet class
class Wallet:
    def __init__(self, money):
        self.money = money

    def add_money(self, amount):
        self.money += amount

    def spend_money(self, amount):
        if self.money >= amount:
            self.money -= amount
            return True
        else:
            return False

# Define the Player class, inheriting from Person
class Player(Person):
    pass

# Define the Dealer class, inheriting from Person
class Dealer(Person):
    pass

# Define the Store class
class Store:
    def __init__(self):
        self.items = {"Chips": 10, "Beer": 5, "Cigars": 20}

    def list_items(self):
        print("Store Items:")
        for item, price in self.items.items():
            print(f"{item}: ${price}")

    def buy_item(self, player, item_name):
        if item_name in self.items:
            price = self.items[item_name]
            if player.wallet.spend_money(price):
                print(f"{player.name} bought {item_name} for ${price}.")
                return True
            else:
                print(f"{player.name} doesn't have enough money to buy {item_name}.")
        else:
            print(f"{item_name} is not available in the store.")
        return False

# Define the BlackjackGame class
class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.player = Player("Player")
        self.dealer = Dealer("Dealer")
        self.store = Store()

    def play(self):
        print("Welcome to Blackjack!")

        # Deal initial cards
        for _ in range(2):
            self.player.hand.add_card(self.deck.deal_card())
            self.dealer.hand.add_card(self.deck.deal_card())

        # Player's turn
        while self.player.hand.value < 21:
            print("\nPlayer's Hand:")
            for card in self.player.hand.cards:
                print(card)
            print(f"Total Value: {self.player.hand.value}")
            action = input("Do you want to 'hit', 'stand', or 'buy'? ").lower()
            if action == "hit":
                self.player.hand.add_card(self.deck.deal_card())
            elif action == "stand":
                break
            elif action == "buy":
                self.store.list_items()
                item_name = input("Enter the item you want to buy: ")
                self.store.buy_item(self.player, item_name)

        # Dealer's turn
        while self.dealer.hand.value < 17:
            self.dealer.hand.add_card(self.deck.deal_card())

        # Display final hands
        print("\nPlayer's Hand:")
        for card in self.player.hand.cards:
            print(card)
        print(f"Total Value: {self.player.hand.value}")
        print("\nDealer's Hand:")
        for card in self.dealer.hand.cards:
            print(card)
        print(f"Total Value: {self.dealer.hand.value}")

        # Determine the winner
        if self.player.hand.value > 21:
            print("Player busts! Dealer wins.")
        elif self.dealer.hand.value > 21:
            print("Dealer busts! Player wins.")
        elif self.player.hand.value > self.dealer.hand.value:
            print("Player wins!")
        elif self.player.hand.value < self.dealer.hand.value:
            print("Dealer wins.")
        else:
            print("It's a tie!")

if __name__ == "__main__":
    game = BlackjackGame()
    game.play()
