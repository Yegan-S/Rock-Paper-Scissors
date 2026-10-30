class RockPaperScissors:
    def __init__(self,name):
     self.choices = ['rock', 'paper', 'scissors']
     self.player_name = name
     
    def get_player_choice(self):
        user_choice = input(f'Enter your choice ({self.choices}): ')
        if user_choice in self.choices:
            return user_choice
        
        print (f'Invalid choice, you must select from {self.choices}.')
        return self.get_player_choice()
    
    def play(self):
     user_choice = self.get_player_choice()
     

game = RockPaperScissors('Ali')
game.play()