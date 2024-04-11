import random
from utils.sim_ranked import SimulatedPlayer, sim_battle
from utils.print_best import print_best

def main(contestant_amount):
    contestants = []
    for i in range(contestant_amount):
        contestants.append(SimulatedPlayer(f'player-{i}'))
    
    for i in range(contestant_amount * 10):
        sim_battle(*random.sample(contestants, 2))

    print_best(contestants)

if __name__ == '__main__':
    main(1000)