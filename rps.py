import random

from colorama import init

init()

from colorama import Fore

player_score = 0

cpu_score = 0

possible_cpu_pick = ['rock', 'paper', 'scissors']

while player_score < 3 and cpu_score < 3:

    cpu_pick = random.choice(possible_cpu_pick)

    player_pick = input(Fore.GREEN + '> Input rock, paper or scissors: ')

    print()

    print(f'CPU PICK: {cpu_pick} VS PLAYER PICK: {player_pick}')

    if player_pick == cpu_pick:

        print(Fore.WHITE + '> It is a tie!')

        print()

        print(f'CPU SCORE: {cpu_score} VS PLAYER SCORE: {player_score}')

        print()

    elif player_pick == 'rock':

        if cpu_pick == 'paper':

            cpu_score = cpu_score + 1

            print(Fore.RED + '> CPU has one point!')

            print()

            print(f'CPU SCORE: {cpu_score} VS PLAYER SCORE: {player_score}')

        elif cpu_pick == 'scissors':

            player_score += 1

            print(Fore.RED + '> Player has one point!')

            print()

            print(f'CPU SCORE: {cpu_score} VS PLAYER SCORE: {player_score}')

    elif player_pick == 'paper':

        if cpu_pick == 'rock':

            player_score = player_score + 1

            print(Fore.RED + '> Player has one point!')

            print()

            print(f'CPU SCORE: {cpu_score} VS PLAYER SCORE: {player_score}')

            print()

        elif cpu_pick == 'scissors':

            cpu_score += 1

            print(Fore.RED + '> CPU has one point!')

            print()

            print(f'CPU SCORE: {cpu_score} VS PLAYER SCORE: {player_score}')

            print()

    elif player_pick == 'scissors':

        if cpu_pick == 'paper':

            palyer_score = player_score + 1

            print(Fore.RED + '> Player has one point!')

            print()

            print(f'CPU SCORE: {cpu_score} VS PLAYER SCORE: {player_score}')

        elif cpu_pick == 'rock':

            cpu_score += 1

            print(Fore.RED + '> CPU has one point!')

            print()

            print(f'CPU SCORE: {cpu_score} VS PLAYER SCORE: {player_score}')

            print()

    else:

        print('> Invalid input!')

        print()

if player_score > cpu_score:

    print(Fore.YELLOW + '> Player wins!')

else:

    print(Fore.BLUE + '> CPU wins')

    

