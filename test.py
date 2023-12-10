import random
from KuhnPokerGame import KuhnPokerGame
from KuhnPokerBot import KuhnPokerBot

def run_simulation(game, bot_player):
    '''
    Run a single simulation of the Kuhn Poker game with the given bot.

    Parameters:
    - game (KuhnPokerGame): The Kuhn Poker game instance.
    - bot_player (KuhnPokerBot): The Kuhn Poker bot instance.

    Returns:
    - tuple: A tuple containing the winner's name, final pot size, and number of rounds played.
    '''
    # Simulate a single round
    rounds_played = 0
    while not game.game_over:
        # Deal initial cards
        game.deal_initial_cards()

        # Bot's turn
        bot_bet = bot_player.make_bet()
        game.bet_round_one("Player2", bot_bet)

        # Opponent's turn (simulate opponent behavior)
        opponent_bet = random.choice([0, 1])
        game.bet_round_one("Player1", opponent_bet)

        # Observe opponent's card and action
        bot_player.observe_card(game.player1_card)
        bot_player.observe_action(opponent_bet)

        # Revealing cards and determining the winner
        game.reveal_cards()
        winner = game.get_winner()

        # Reset the game for a new round
        game.reset_game()

        rounds_played += 1

    return winner, game.pot, rounds_played

def print_scenario_results(scenario_number, results):
    '''
    Print the results of a scenario.

    Parameters:
    - scenario_number (int): The scenario number.
    - results (tuple): A tuple containing the winner's name, final pot size, and number of rounds played.
    '''
    print(f"Scenario {scenario_number} Results:")
    print("Winner:", results[0])
    print("Final Pot:", results[1])
    print("Rounds Played:", results[2])
    print("")

if __name__ == "__main__":
    # Define the number of scenarios
    num_scenarios = 5

    # Create Kuhn Poker game and bot
    game = KuhnPokerGame("Player1", "Player2")
    bot_player = KuhnPokerBot("Player2")  # Assuming the bot is player 2

    # Run simulations for different scenarios
    for scenario_number in range(1, num_scenarios + 1):
        # Set up a specific scenario (e.g., opponent always bluffs)
        # ...

        # Run the simulation for the current scenario
        scenario_results = run_simulation(game, bot_player)

        # Print results for the current scenario
        print_scenario_results(scenario_number, scenario_results)

        # Reset the game and bot for the next scenario
        game.reset_game()
        bot_player = KuhnPokerBot("Player2")  # Reset bot state
