
class DiceGame:
    def __init__(self, player, computer):
        self._player = player
        self._computer = computer

    def play(self):
        print("=======================================")
        print("-------Welcome to Roll the Dice-------")
        print("=======================================")
        while True:
            self.play_round()
            game_over = self.check_game_over()
            if game_over:
                break


    def play_round(self):
        self.welcome_player_round()

        player_value = self._player.roll_die()
        computer_value = self._computer.roll_die()

        # show the Die values
        self.show_dice(player_value, computer_value)

        # compare both die value
        if player_value > computer_value:
            print("You have won the round 😎")
            self.update_counters(winner=self._player, loser=self._computer)
        elif computer_value > player_value:
            print("Computer won this round 😪 try again")
            self.update_counters(winner=self._computer, loser=self._player)
        else:
            print(" Its tie ! 😐")

        self.show_counters()

    def welcome_player_round(self):
        print("\n----------- NEW ROUND -----------")
        input("🎌🎌 Press any key to Roll the dice ")

    def show_dice(self, player_value, computer_value):
        print(f"Your die {player_value}")
        print(f"Computer die {computer_value}\n")

    def update_counters(self, winner, loser):
        winner.decrement_counter()
        loser.increment_counter()

    def show_counters(self):
        print(f"\nYour counter value is {self._player.counter}")
        print(f"Computer Counter value is {self._computer.counter}")


    def check_game_over(self):
        if self._player.counter == 0:
            self.show_game_over(self._player)
            return True
        elif self._computer.counter == 0:
            self.show_game_over(self._computer)
            return True
        else:
            return False

    def show_game_over(self, winner):
        if winner.is_computer:
            print("\n ==================================")
            print("           G A M E   O V E R         ")
            print("====================================")
            print(" The Computer won the game sorry... ")
            print("======================================")
        else:
            print("\n ====================================")
            print("           G A M E   O V E R          ")
            print("=========================================")
            print(" Congratulation !! You won the game 😎😎😎")
            print("======================================")

