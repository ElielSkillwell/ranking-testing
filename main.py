import random

from utils.sim_ranked import SimulatedPlayer, sim_battle
from utils.print_best import print_best, scatter_results

def main(contestant_amount):
    contestants = []
    for i in range(contestant_amount):
        contestants.append(SimulatedPlayer(f'player-{i}', i))

    for i in range(contestant_amount * 100):
        temp_contestant1 = contestants.pop(random.randint(0, len(contestants)-1))
        temp_contestant2 = contestants.pop(random.randint(0, len(contestants)-1))
        sim_battle(temp_contestant1, temp_contestant2)
        contestants.extend([temp_contestant1, temp_contestant2])

    print_best(contestants)
    scatter_results(contestants)

if __name__ == '__main__':
    main(1000)