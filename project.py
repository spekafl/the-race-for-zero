import pycountry
from pyfiglet import Figlet
import random
import requests
import tabulate


class Player:
    def __init__(self, name, country, rounds=None, score=30, status=''):
        if rounds is None:
            rounds = []
        self.name = name
        self.country = country
        self.rounds = rounds
        self.score = score
        self.status = status

    def __str__(self):
        return f'''⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⠿⣿⡿⠉⠀⢤⣤⣴⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣦⣤⡤⠀⠉⢻⣿⠿⣿⣿
⣿⣿⠀⠘⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠃⠀⣿⣿
⣿⣿⠀⢰⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⡆⠀⣿⣿
⣿⣿⡄⠘⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⠃⢰⣿⣿
⣿⣿⣧⠀⢻⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡏⠀⣼⣿⣿
⣿⣿⣿⣆⠈⢿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⡟⠀⢰⣿⣿⣿
⣿⣿⣿⣿⡄⠀⠻⡿⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⠟⠀⢠⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣦⠀⠁⢀⣴⣄⠀⠀⠀⠀⠀⠀⠀⠀⣠⣦⡀⠀⠀⣰⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣷⣄⣠⣿⣿⣿⡆⠀⠀⠀⠀⢰⣿⣿⣿⣄⣠⣾⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⢠⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠀⠀⠀⠀⠀⠀⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣶⣤⣤⣤⣤⣶⣶⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿\nFrom {self.country}, after {len(self.rounds)} rounds, the winner of The Race For Zero is {self.name}!!!!\n'''

    @property
    def rounds(self):
        return self._rounds
    
    @rounds.setter
    def rounds(self, value):
        self._rounds = value

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if value != 0:
            self._score = value
        else:
            self._score = value
            self.status = 'winner'

    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, value):
        self._status = value

    def play_round(self):
        score = random.randint(1, 6)
        if self.score > 0:
            self.score -= score
        elif self.score < 0:
            self.score += score
        self.rounds.append(score)


def main():
    # ASCII art for The Race For Zero title
    figlet = Figlet()
    figlet.setFont(font='doom')
    print(figlet.renderText('The Race For Zero'))

    # Create user player
    # Name
    while True:
        name = input('Enter Player Name: ')
        if len(name) > 0:
            player_name = get_name(name)
            break
        else:
            print('Invalid player name. Please enter a non-empty string.')

    # Country
    while True:
        player_country = input('From: ').strip().capitalize()
        validate = get_country(player_country)
        if validate:
            player_country = validate
            break
        else:
            print('Invalid country. Please try again.')

    player = Player(player_name, player_country)

    # Create tournament
    while True:
        # Reset player attributes if playing again
        if len(player.rounds) > 0:
            player.rounds = []
            player.score = 30
            player.status = ''

        participants = []
        # Append user player to tournament
        participants.append(player)

        # Create opponents
        # Select number of players
        while True:
            user_input = input('Number of players (2-8): ').strip()
            if user_input.isdigit():
                num_players = int(user_input)
                if 2 <= num_players <= 8:
                    break
                else:
                    print('Invalid number of players. Please enter a number between 2 and 8.')
            else:
                print('Invalid input. Please enter a valid number.')

        # Create opponent's list
        opponents = get_opponents(num_players)
        for opponent in opponents:
            participants.append(opponent)

        print(tournament_presentation(participants))

        # Starting next round
        round = 1
        tournament_finished = False

        while not tournament_finished:
            next_round = input(f'Ready for round {round}? (y/n) (default = y): ').strip().lower() or 'y'
            match next_round:
                case 'y':
                    for participant in participants:
                        participant.play_round()
                        if participant.status == 'winner':
                            print(get_scoreboard(participants))
                            print(participant)
                            tournament_finished = True
                            break
                    
                    if tournament_finished:
                        break

                    print(get_scoreboard(participants))
                    round += 1
                case 'n':
                    print(f'The participant {player.name} leaves the tournament')
                    tournament_finished = True
                    break
                case _:
                    print('Invalid option. Please enter "y" or "n".')
                    continue

        # Ask for play again or exit
        while True:
            play_again = input('Play again? (y/n) (default = y): ').strip().lower() or 'y'
            match play_again:
                case 'y':
                    break
                case 'n':
                    print('Thank for participate!\nSee you soon!')
                    exit()
                case _:
                    print('Invalid option. Please enter "y" or "n".')
                    continue


def get_name(name):
    '''
    Return the name from the provided input.
    '''
    return name.strip().capitalize()


def get_country(country):
    '''
    Validate and return the country name from the provided input.
    '''
    try:
        country_data = pycountry.countries.lookup(country)
        return country_data.name
    except LookupError:
        return False


def get_opponents(total_players):
    '''
    Generate a list of opponents for the tournament.
    '''
    # Get 100 candidates from API and populate the list of opponents
    response = requests.get(r'https://randomuser.me/api/?seed=player_name&results=100')
    data = response.json()

    opponents_all = []

    for _ in range(100):
        # name = data['results'][_]['login']['username']
        name = data['results'][_]['name']['first']
        country = data['results'][_]['location']['country']
        opponent = Player(name, country)
        opponents_all.append(opponent)

    # Get a random sample of opponents for the tournament
    opponents_sample = random.sample(opponents_all, total_players-1)
    
    oppenents_selected = []

    for opponent in opponents_sample:
        oppenents_selected.append(opponent)

    return oppenents_selected


def tournament_presentation(players):
    '''
    Generate a presentation for the current tournament.
    '''
    headers = ['Player', 'From', 'Score']
    data = [(player.name, player.country, player.score) for _, player in enumerate(players)]

    return tabulate.tabulate(data, headers=headers, tablefmt='fancy_grid')


def get_scoreboard(players):
    '''
    Generate a scoreboard for the current tournament.
    '''
    headers = ['Player', 'From', 'Rounds', 'Score']
    data = [(player.name, player.country, player.rounds, player.score) for _, player in enumerate(players)]

    return tabulate.tabulate(data, headers=headers, tablefmt='fancy_grid')


if __name__ == "__main__":
    main()