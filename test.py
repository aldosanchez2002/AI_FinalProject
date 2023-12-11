import random
import numpy as np
from KuhnPokerGame import KuhnPokerGame
from KuhnPokerBot import KuhnPokerBot

# Simulation Test
if __name__ == "__main__":
    # Initialize the bot
    bot = KuhnPokerBot("Player2")

    # Simulate multiple rounds of the game
    for _ in range(10):
        # Simulate opponent's card and action observation
        observed_card = np.random.choice([0, 1, 2], p=bot.prior_opponent_card)
        observed_action = np.random.choice([0, 1], p=bot.prior_opponent_action)

        # Observe opponent's card and action
        bot.observe_card(observed_card)
        bot.observe_action(observed_action)

        # Make a betting decision and evaluate hand strength
        bet_decision = bot.make_bet()
        hand_strength = bot.evaluate_hand_strength()

        # Print results for each round
        print(f"{bot.player_name} observed opponent's card: {observed_card}")
        print(f"{bot.player_name} observed opponent's action: {'bet' if observed_action else 'check/fold'}")
        print(f"{bot.player_name} decided to {'bet' if bet_decision else 'check/fold'}.")
        print(f"{bot.player_name}'s estimated hand strength: {hand_strength:.2f}")
        print("-" * 30)