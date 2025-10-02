import sys
import unittest
from unittest.mock import patch, call

try:
    from units.week_01.dice import Die, Player, DiceBattle
except:
    from dice import Die, Player, DiceBattle

# Since the prompt is to "replicate existing code" I think it is fair to expect that the
# function output should match the existing code's output exactly
class TestDie(unittest.TestCase):
    def test_init_die(self):
        die = Die()

        # Should have initialized with a value
        self.assertGreaterEqual(die.value, 1)
        self.assertLessEqual(die.value, 6)
        print("✅ Die initialization tests successful!")

    def test_roll_die(self):
        die = Die()

        # Roll the die a bunch of times and make sure the value is always valid
        for _ in range(100):
            value = die.roll()
            self.assertGreaterEqual(value, 1)
            self.assertLessEqual(value, 6)
        print("✅ Die rolling tests successful!")

class TestPlayer(unittest.TestCase):
    def test_init_player(self):
        player = Player("TestPlayer")
        self.assertEqual(player.name, "TestPlayer")
        self.assertEqual(player.roll_value, 0)
        print("✅ Player initialization tests successful!")

    @patch('builtins.print')
    def test_roll_die(self, mock_print):
        player = Player("TestPlayer")
        die = Die()

        player.roll_die(die)
        self.assertGreaterEqual(player.roll_value, 1)
        self.assertLessEqual(player.roll_value, 6)
        mock_print.assert_called_with(f"TestPlayer rolled a {player.roll_value}")
        print("✅ Player rolling tests successful!")

class TestDiceBattle(unittest.TestCase):
    def test_dice_battle(self):
        # Should be able to run a bunch of games and they should all complete correctly
        for _ in range(10):
            game = DiceBattle("PlayerA", "PlayerB")
            with patch('builtins.print') as mock_print:
                game.play()

                # Check that the start and end messages were printed
                mock_print.assert_any_call("\n--- Dice Battle Start (Python) ---")
                mock_print.assert_any_call("-----------------------------------")

                # Check that both players rolled
                calls = [call(f"PlayerA rolled a {game.player_1.roll_value}"),
                         call(f"PlayerB rolled a {game.player_2.roll_value}")]
                mock_print.assert_has_calls(calls, any_order=True)

                # Check that the correct winner message was printed
                if game.player_1.roll_value > game.player_2.roll_value:
                    mock_print.assert_any_call("PlayerA wins! (High Roll)")
                elif game.player_1.roll_value < game.player_2.roll_value:
                    mock_print.assert_any_call("PlayerB wins! (High Roll)")
                else:
                    mock_print.assert_any_call("It's a draw!")
        print("✅ DiceBattle game tests successful!")

# Run the tests if being called directly
if __name__ == '__main__':
    unittest.main()
