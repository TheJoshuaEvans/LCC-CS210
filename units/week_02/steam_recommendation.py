# Based on these instructions:
# https://lcc-cit.github.io/CS210-CourseMaterials/Labs/Lab02-RuleBasedSystems/GroupA/CS210_Lab02_Instructions_GroupA.html

#* DEV NOTE: I am abandoning this path. I learned a lot and will be reusing a ton of code, but I can't
#* figure out a decent way to actually integrate the data with the lab requirements

import csv

from init import init

def main():
    program_data = init()
    games = program_data.games
    game_details = program_data.game_details

    print('Welcome to the Steam Recommendation Expert System!')
    print('Pleas answer the following questions to get a game recommendation from your library')
    print('Leave any response blank to skip that question\n')

    # have_played = input('Do you want to play a game you have played before (y/n): ').strip().lower()
    # print(have_played == '')

    genres = set()
    for game in game_details:
        if not game:
            continue
        for genre in game.get('genres', []):
            genres.add(genre['description'])
    print(f'Available genres: {", ".join(sorted(genres))}')

    # I give up :)

if __name__ == "__main__":
    main()
