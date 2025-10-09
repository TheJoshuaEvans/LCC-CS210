# LCC-CS210
Resources for LCC's Intro to AI Development
Course Link: https://classes.lanecc.edu/course/view.php?id=132172

# Run
This project is meant to be used with the "uv" python version manager: 
https://github.com/astral-sh/uv

To run a python script with uv, use the following format
```sh
uv run hello-world.py
```

> Note: If you are not using uv for python version management, replace `uv run` with `python` or `python3` or whatever the appropriate command is for your platform

# Unit Testing
This project uses the `unittest` Python framework for unit testing. To run all tests in the project, use the following command:
```sh
uv run -m unittest
```

To run a specific unit test suite, just run the test file directly:
```sh
uv run units/week_01/test_coffee.py
uv run units/week_01/test_dice.py
uv run units/week_01/test_lab_1a_finance.py
uv run units/week_01/test_lab_1a_shipping.py
uv run units/week_01/test_med.py
```
