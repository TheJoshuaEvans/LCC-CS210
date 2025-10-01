import random

class Die:
    """A rollable die"""
    def __init__(self, sides: int = 6):
        self.sides = sides
        """The number of sides the die has"""

        self.value = self.roll()
        """The current value of the die"""

    def roll(self):
        """Roll the die!"""
        return random.randint(1, self.sides)

class Player:
    """A player of the dice game"""
    def __init__(self, name: str):
        self.name = name
        """The player's name"""

        self.roll_value = 0
        """The player's latest roll"""

    def roll_die(self, die: Die):
        """Roll the provided die and announce the value

        Parameters:
            die (Die): The die the player will roll
        """
        self.roll_value = die.roll()
        print(f"{self.name} rolled a {self.roll_value}")

class DiceBattle:
    """Manages a two player game of the "Dice Battle"!"""
    def __init__(self, p1_name: str, p2_name: str):
        """
        Parameters:
            p1_name (str): The name of the first player
            p2_name (str): The name of the second player
        """

        self.die = Die()
        """The game die"""

        self.player_1 = Player(p1_name)
        """Player 1"""

        self.player_2 = Player(p2_name)
        """Player 2"""

    def play(self):
        """Play a game of "Dice Battle"! Two players roll a die,
        and the player with the highest roll wins!"""

        print("\n--- Dice Battle Start (Python) ---")

        # Players take turns rolling the die...
        self.player_1.roll_die(self.die)
        self.player_2.roll_die(self.die)

        # Find the winner!
        if self.player_1.roll_value > self.player_2.roll_value:
            print(f"{self.player_1.name} wins! (High Roll)")
        elif self.player_1.roll_value < self.player_2.roll_value:
            print(f"{self.player_2.name} wins! (High Roll)")
        else:
            print("It's a draw!")

        print("-----------------------------------")


game = DiceBattle("PlayerA", "PlayerB")
game.play()
