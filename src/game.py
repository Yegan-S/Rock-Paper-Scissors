import random 


class RockPaperScissors:
    def __init__(self,name):
     self.choices = ['rock', 'paper', 'scissors']
     self.player_name = name
     
    def get_player_choice(self):
        user_choice = input(f'Enter your choice ({self.choices}): ')
        if user_choice.lower() in self.choices:
            return user_choice.lower()
        
        print (f'Invalid choice, you must select from {self.choices}.')
        return self.get_player_choice()

    def get_computer_choice(self):
        return random.choice(self.choices)

    
    def play(self):
        user_choice = self.get_player_choice()
        computer_choice = self.get_computer_choice()
        print(user_choice, computer_choice)

game = RockPaperScissors('Ali')
game.play()