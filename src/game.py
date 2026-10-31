import random
from typing import List, Tuple


class RockPaperScissors:
    """Main class for Rock Paper Scissors."""
    def __init__(self,name: str):
        self.choices: List[str] = ['rock', 'paper', 'scissors']
        self.player_name: str = name
     
    def get_player_choice(self):
        user_choice: str = input(f'Enter your choice ({self.choices}): ')
        if user_choice.lower() in self.choices:
            return user_choice.lower()
        
        print (f'Invalid choice, you must select from {self.choices}.')
        return self.get_player_choice()

    def get_computer_choice(self):
        """Get computer choice randomly from choices: rock, paper, scissors."""
        return random.choice(self.choices)
    
    def decide_winner(self, user_choice: str, computer_choice: str) -> str:
        """Decied the winner of the game, based on user and computer choices.

        :param user_choice: The choice of the user.
        :param computer_choice: The choice of the computer.
        :return: The result of the game.

        """

        if user_choice == computer_choice:
            return "It's a Tie."
        


        win_combinations: List[Tuple(str, str)] = [('rock', 'scissors'), ('paper', 'rock'), ('scissors', 'paper')]
        for win_comb in win_combinations:
                if (user_choice == win_comb[0]) & (computer_choice == win_comb[1]):
                    return "Congratulations! You won!"

        return "Oh no! The computer won!"

    def play(self):
        """Play the game.
        - Get user choice.
        - Get computer choice.
        - Decide the winner.
        - Print the result.
        """
        user_choice = self.get_player_choice()
        computer_choice = self.get_computer_choice()
        print(f'computer_choices: {computer_choice}')
        print(self.decide_winner(user_choice, computer_choice))



if __name__ == '__main__':
    game = RockPaperScissors('Yegane')

    while True:
        game.play()

        continue_game = input('Do you want to play again? (Enter any key to play agin, enter q/Q to exit!)')
        if continue_game.lower() == 'q':
            break

