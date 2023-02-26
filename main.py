from die import Die
from player import Player
from dice_game import DiceGame


# creating 2 die instance
player_die = Die()
computer_die = Die()

# create 2 player instance using respective die instance
my_player = Player(player_die, is_computer=False)
computer_player = Player(computer_die, is_computer=True)

game = DiceGame(my_player, computer_player)
game.play()
