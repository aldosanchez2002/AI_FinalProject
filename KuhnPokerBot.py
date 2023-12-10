'''
Class Name: KuhnPokerBot
Attributes:
    Initialization:
        - The bot should be initialized with a player name.

    Observing Opponent's Card:
        - The bot should have a method `observe_card(opponent_card)` to update its internal model based on the card observed from the opponent.

    Observing Opponent's Action:
        - The bot should have a method `observe_action(opponent_action)` to update its internal model based on the action observed from the opponent (check/fold or bet).

    Making Betting Decision:
        - The bot should have a method `make_bet()` to make a betting decision based on its internal model.
        - The method should return an integer representing the betting decision (0 for check/fold, 1 for bet).

    Evaluating Hand Strength:
        - The bot should have a method `evaluate_hand_strength()` to evaluate the strength of its current hand based on the internal model.
        - The method should return a float value between 0 and 1, representing the strength of the bot's hand.
'''
import random

class KuhnPokerBot:
    def __init__(self, player_name):
        '''
        Initialize the Kuhn Poker bot.

        Parameters:
        - player_name (str): The name of the bot player.
        '''
        self.player_name = player_name
        self.opponent_card = None
        self.opponent_action = None
        self.hand_strength = None

    def observe_card(self, opponent_card):
        '''
        Observe the opponent's card.

        Parameters:
        - opponent_card (int): The card observed in the opponent's hand.
        '''
        self.opponent_card = opponent_card

    def observe_action(self, opponent_action):
        '''
        Observe the opponent's action.

        Parameters:
        - opponent_action (int): The action taken by the opponent (0 for check/fold, 1 for bet).
        '''
        self.opponent_action = opponent_action

    def make_bet(self):
        '''
        Make a betting decision based on probabilistic reasoning.

        Returns:
        - int: The bot's betting decision (0 for check/fold, 1 for bet).
        '''
        # Use probabilistic reasoning based on opponent's card and actions
        if self.opponent_card == 1:
            # Example: higher probability to bet if opponent often bluffs
            if self.opponent_action == 1 and random.random() < 0.8:
                return 1
            else:
                return 0
        else:
            # Example: higher probability to bet if opponent often bluffs
            if self.opponent_action == 1 and random.random() < 0.2:
                return 1
            else:
                return 0

    def evaluate_hand_strength(self):
        '''
        Evaluate the strength of the bot's hand based on probabilistic reasoning.

        Returns:
        - float: A value representing the estimated hand strength.
        '''
        # Use probabilistic reasoning to evaluate hand strength
        # Example: assign probabilities based on the opponent's card
        if self.opponent_card == 1:
            return random.uniform(0.7, 1.0)  # Adjust based on your strategy
        else:
            return random.uniform(0.0, 0.3)  # Adjust based on your strategy
