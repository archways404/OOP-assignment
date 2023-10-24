import random

# Define the Card class
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank}"

# Define the Deck class
class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
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

    def reset(self):
        self.cards = []
        self.value = 0

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
    def __init__(self, players):
        self.deck = Deck()
        self.players = players
        self.store = Store()

    def play(self):
        print("Welcome to Blackjack!")

        # Player selection
        if not self.players:
            print("No players available. Add a person to play Blackjack.")
            return
        
        print("Available Players:")
        for player in self.players:
          print(player.name)
        player_name = input("Enter the name of the player who wants to play: ")
        player = next((p for p in self.players if p.name == player_name), None)
        if player is None:
          print("Player not found.")
          return

        # Place a bet
        while True:
            try:
                bet = int(input(f"Enter your bet (1-{player.wallet.money}): "))
                if 1 <= bet <= player.wallet.money:
                    player.wallet.spend_money(bet)
                    break
                else:
                    print("Invalid bet amount. Please enter a valid bet.")
            except ValueError:
                print("Invalid input. Please enter a valid bet.")

        # Deal initial cards
        player.hand.add_card(self.deck.deal_card())
        dealer_hidden_card = self.deck.deal_card()
        player.hand.add_card(self.deck.deal_card())
        dealer_hand = [self.deck.deal_card(), dealer_hidden_card]

        # Player's turn
        while player.hand.value < 21:
            print("\nPlayer's Hand:")
            for card in player.hand.cards:
                print(card)
            print(f"Total Value: {player.hand.value}")

            # Reveal the hidden dealer card
            dealer_hand[1] = dealer_hidden_card
            self.calculate_hand_value(dealer_hand)

            action = input("Do you want to 'hit' or 'stand'? ").lower()
            if action == "hit":
                player.hand.add_card(self.deck.deal_card())
            elif action == "stand":
                break

        # Dealer's turn
        while self.calculate_hand_value(dealer_hand) < 17:
            dealer_hand.append(self.deck.deal_card())

        # Display final hands
        print("\nPlayer's Hand:")
        for card in player.hand.cards:
            print(card)
        print(f"Total Value: {player.hand.value}")
        print("\nDealer's Hand:")
        for card in dealer_hand:
            print(card)
        print(f"Total Value: {self.calculate_hand_value(dealer_hand)}")

        # Determine the winner and update the wallet
        player_value = player.hand.value
        dealer_value = self.calculate_hand_value(dealer_hand)

        if player_value > 21:
            print(f"{player.name} busts! Dealer wins.")
        elif dealer_value > 21:
            print("Dealer busts! Player wins.")
            player.wallet.add_money(bet * 2)
        elif player_value > dealer_value:
            print(f"{player.name} wins!")
            player.wallet.add_money(bet * 2)
        elif player_value < dealer_value:
            print("Dealer wins.")
        else:
            print("It's a tie!")
            player.wallet.add_money(bet)
        
        player.hand.reset()
        dealer_hand = []
            
    @staticmethod
    def calculate_hand_value(hand):
        value = 0
        num_aces = 0
        for card in hand:
            if card.rank == "Ace":
                num_aces += 1
            elif card.rank in ["King", "Queen", "Jack"]:
                value += 10
            else:
                value += int(card.rank) if card.rank.isnumeric() else 10  # Use 10 for non-numeric ranks
        for _ in range(num_aces):
            if value + 11 <= 21:
                value += 11
            else:
                value += 1
        return value

# Define the Menu class for creating a text-based menu
class Menu:
    def __init__(self):
        self.players = []
    
    def display(self):
        while True:
            print("\nMain Menu:")
            print("1. Play Blackjack")
            print("2. View Credits")
            print("3. Add Credits")
            print("4. Go to the Store")
            print("5. Add Dealer")
            print("6. Add Person")
            print("7. Select Person")
            print("8. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.play()
            elif choice == '2':
                self.view_credits()
            elif choice == '3':
                self.add_credits()
            elif choice == '4':
                self.go_to_store()
            elif choice == '5':
                self.add_dealer()
            elif choice == '6':
                self.add_person()
            elif choice == '7':
                self.select_person()
            elif choice == '8':
                break
            else:
                print("Invalid choice. Please select a valid option.")
    
    def play(self):
        if not self.players:
            print("No players available. Add a person to play Blackjack.")
            return
        game = BlackjackGame(self.players)
        game.play()


    def view_credits(self):
        for player in self.players:
            print(f"{player.name}'s Credits: ${player.wallet.money}")
    
    def add_credits(self):
        player_name = input("Enter the name of the player to add credits: ")
        amount = int(input("Enter the amount to add: "))
        player = next((p for p in self.players if p.name == player_name), None)
        if player:
            player.wallet.add_money(amount)
            print(f"Added ${amount} credits to {player.name}'s wallet.")
        else:
            print("Player not found.")
    
    def go_to_store(self):
        if not self.players:
            print("No players available. Add a person to access the store.")
            return
        store = Store()
        store.list_items()
        player_name = input("Enter the name of the player to access the store: ")
        player = next((p for p in self.players if player.name == player_name), None)
        if player:
            item_name = input("Enter the item you want to buy: ")
            store.buy_item(player, item_name)
        else:
            print("Player not found.")

    def add_dealer(self):
        dealer = Dealer("Dealer")
        self.players.append(dealer)
        print("Dealer added to the list of players.")

    def add_person(self):
        name = input("Enter the name of the person: ")
        money = int(input("Enter the initial money for the person: "))
        person = Player(name, money)
        self.players.append(person)
        print(f"{name} added to the list of players with ${money} credits.")

    def select_person(self):
        if not self.players:
            print("No players available. Add a person to select.")
            return
        print("\nAvailable Players:")
        for player in self.players:
            print(player.name)
        player_name = input("Enter the name of the player you want to select: ")
        player = next((p for p in self.players if p.name == player_name), None)
        if player:
            print(f"Selected: {player.name}")
        else:
            print("Player not found.")

if __name__ == "__main__":
    menu = Menu()
    menu.display()