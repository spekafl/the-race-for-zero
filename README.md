# The Race For Zero

## Video Demo:  <https://www.youtube.com/watch?v=PCt-VrIfNwc>

## Description

The Race For Zero is a Python text-based game that simulates a simple dice-rolling tournament. The game is designed to be played by a single player against a randomly generated list of opponents. The goal of the game is to reach **zero points** before all opponents do.

### How the Game Works

- The game begins with the player entering their name, selecting their country of origin, and choosing the tournament size.
- Each round, the player and opponents roll a six-sided dice. The player’s score starts at **30 points** and decreases by the number rolled. If the subtraction results in a negative number, the score is increased by the roll instead.
- The game ends when a player reaches zero points, at which point is declared the winner.

## Running the Game

To run **The Race For Zero**, ensure you have **Python 3.11** or later installed. Follow these steps:

1. Clone or download the project repository.
2. Open a terminal or command prompt and navigate to the project directory.
3. Install the required packages by running `pip install -r requirements.txt`.
4. Run the game by executing `python project.py`.

## Project Structure

### Files

- `project.py`: Contains the game logic, user interface, and tournament management.
- `requirements.txt`: Lists the required Python packages for running the game.
- `test_project.py`: Basic tests for the main game script using `pytest`.

### Class: Player

Defines the player character and includes methods for participating in the tournament.

#### Attributes

- `name` The player's name.
- `country` The player's country of origin.
- `rounds` A list storing the scores of each round (defaults to an empty list).
- `score` The player's current score (defaults to 30).
- `status` The player's current status. Used to tag the winner

#### Methods

- `play_round()` Rolls a six-sided die and adjusts the player's score based on the roll.
- `__str__()`: Provides a string representation of the player.

## Functions

- `main()` Main function that controls the game flow.
- `get_name()` Retrieves and formats the player's name.
- `get_country()` Validates the player's country input and returns the ISO 3166-1 name.
 Accepts as input the country name, 2 or 3 letters country code and the numeric code.
- `get_opponents()` Generates a list of opponents by fetching data from an external API.
- `tournament_presentation()` Presents the tournament details.
- `get_scoreboard()` Displays the current scoreboard after each round.

## Required Packages

- `pycountry`: Validates the player's country using ISO codes.
- `pyfiglet`: Creates ASCII art fonts for visual enhancement.
- `random`: Randomly generates opponent lists and dice rolls.
- `requests`: Fetches random users for opponents from the API <https://randomuser.me/>.
- `tabulate`: Formats the tournament presentation and scoreboard.

Install these packages via the `requirements.txt` file.

## Key Features

1. Randomly generated opponents: Each tournament features a unique set of opponents, providing a new experience with each playthrough.
2. User interface: The game offers an intuitive interface for entering player details, rolling dice, and viewing scores.
3. Tournament management: The game tracks player scores, rounds, and automatically determines the winner.

## Design Choices

This project prioritizes simplicity and ease of use. The game runs directly in the terminal, with minimalistic but effective design elements for a smooth user experience.
