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

    # Doing some goofing around...
    rules = []
    with open('units/week_02/test.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            rules.append(row)
            app_id = 2529820
            locals = {f'metacritic_score': 81, 'r': None}
            exec(f'r = {row["IF"]}', {}, locals)
            print(locals['r'])
    print(rules)


if __name__ == "__main__":
    # This is fucking bonkers OuO
    locals = {'x': 5, 'r': 0}
    in_val = 'metacritic_score >= 80'
    print(exec(f'r = {in_val}', {'metacritic_score': 78}, locals))
    print(locals)

    main()
