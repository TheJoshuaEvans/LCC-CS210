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

# Unit Testing
This project uses the `unittest` Python framework for unit testing. To run all tests in the project, use the following command:
```sh
uv run -m unittest
```

To run a specific unit test suite, just run the test file directly, like so:
```sh
uv run units/week_01/test_coffee.py
uv run units/week_01/test_dice.py
uv run units/week_01/test_med.py
```
