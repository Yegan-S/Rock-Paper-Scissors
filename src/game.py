class RockPaperScissors:
    def __init__(self,name):
     self.choices = ['rock', 'paper', 'scissors']
     self.player_name = name
     
    def get_player_choice(self):
        user_choice = input(f'Enter your choice ({self.choices}): ')
        print(user_choice)
    
    def play(self):
     user_choice = self.get_player_choice()
     

game = RockPaperScissors('Ali')
game.play()