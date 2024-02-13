import random
from typing import Dict


ACTIONS: Dict[int, str] = {0: "Rock", 1: "Paper", 2: "Scissors"}
VICTORIES: Dict[str, str] = {
    "Rock": "Scissors",   # Rock beats scissors
    "Paper": "Rock",      # Paper beats rock
    "Scissors": "Paper",  # Scissors beats paper
}


def get_user_selection(actions: Dict[int, str]) -> str:
    """Prompt the user to select an action and return their choice."""
    choices = [f"{actions[action]}[{action}]" for action in actions]
    choices_str = ", ".join(choices)
    selection = int(input(f"Enter a choice ({choices_str}): "))
    action = actions[selection]
    return action


def get_computer_selection(actions: Dict[int, str]) -> str:
    """Generate a random action for the computer."""
    selection = random.randint(0, len(actions) - 1)
    action = actions[selection]
    return action


def get_determine_winner(victories: Dict[str, str], user_action: str, computer_action: str) -> str:
    """Determine the winner of the game based on the user's and computer's actions."""
    defeats = victories[user_action]
    if user_action == computer_action:
        result = f"Both players selected {user_action}. It's a tie!"
    elif computer_action in defeats:
        result = f"{user_action} beats {computer_action}! You win!"
    else:
        result = f"{computer_action} beats {user_action}! You lose."
    return result


if __name__ == "__main__":
    while True:
        try:
            user_selection = get_user_selection(ACTIONS)
            print(user_selection)
            computer_selection = get_computer_selection(ACTIONS)
            print(computer_selection)
            determine_winner = get_determine_winner(
                VICTORIES, user_selection, computer_selection
            )
            print(determine_winner)
        except:
            range_str = f"[0, {len(ACTIONS) - 1}]"
            print(f"Invalid selection. Enter a value in range {range_str}")
            continue

        play_again = input("Play again? (y/n): ")
        if play_again.lower() != "y":
            break
