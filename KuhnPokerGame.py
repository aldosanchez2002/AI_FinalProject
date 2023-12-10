import random
class KuhnPokerGame:
    '''
    Class Name: KuhnPokerGame
    Attributes:
        Players:
            player1: The first player.
            player2: The second player.
        Deck:
            deck: A list representing the deck of cards (1, 2, 3).
        Pot:
            pot: An integer representing the current pot.
        Player Hands:
            player1_card: The card held by player 1.
            player2_card: The card held by player 2.
        Game State:
            round: An integer representing the current betting round (1 or 2).
            game_over: A boolean indicating whether the game is over.
    '''
    def __init__(self, player1_name, player2_name):
        '''
        Initialize the Kuhn Poker game.

        Parameters:
        - player1_name (str): The name of the first player.
        - player2_name (str): The name of the second player.
        '''
        self.player1 = player1_name
        self.player2 = player2_name
        self.deck = [1, 2, 3]
        self.pot = 0
        self.player1_card = None
        self.player2_card = None
        self.round = 1
        self.game_over = False

    def deal_initial_cards(self):
        '''
        Deals one card to each player.
        '''
        self.player1_card = self.deck.pop(random.randint(0, len(self.deck) - 1))
        self.player2_card = self.deck.pop(random.randint(0, len(self.deck) - 1))

    def bet_round_one(self, bet_player, bet_amount):
        '''
        Handles the first betting round. If the bet_player is player 1, the other player must either call or fold. Updates the pot accordingly.

        Parameters:
        - bet_player (str): The player making the bet.
        - bet_amount (int): The amount of the bet (0 for check/fold, 1 for bet).
        '''
        if bet_player == self.player1:
            self.pot += bet_amount
            if bet_amount == 1:
                self.pot += 1
                self.game_over = True
        else:
            self.pot += bet_amount
            if bet_amount == 1:
                self.pot += 1
                self.game_over = True

    def reveal_cards(self):
        '''
        Reveals the cards of both players and determines the winner. Updates the pot accordingly.
        '''
        if self.player1_card > self.player2_card:
            self.pot += 2
        else:
            self.pot -= 2

    def get_winner(self):
        '''
        Determines the winner based on the revealed cards.

        Returns:
        - str: The name of the winning player.
        '''
        if self.player1_card > self.player2_card:
            return self.player1
        else:
            return self.player2

    def reset_game(self):
        '''
        Resets the game state for a new round.
        '''
        self.deck = [1, 2, 3]
        self.pot = 0
        self.player1_card = None
        self.player2_card = None
        self.round = 1
        self.game_over = False

    def print_game_state(self):
        '''
        Prints the current game state.
        '''
        print("Player 1: " + str(self.player1_card))
        print("Player 2: " + str(self.player2_card))
        print("Pot: " + str(self.pot))
        print("Round: " + str(self.round))
        print("Game Over: " + str(self.game_over))
        print("")
