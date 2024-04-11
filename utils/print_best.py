import matplotlib.pyplot as plt
from utils.sim_ranked import SimulatedPlayer

def get_ELO(obj: SimulatedPlayer) -> int:
    return obj.get_ELO()

def get_index(obj: SimulatedPlayer) -> int:
    return obj.index


def print_best(contestants: list[SimulatedPlayer]):
    sorted_contestants = sorted(contestants, key=get_ELO, reverse=True)

    print(f'\n\n\nBest scores achieved: \n\n')

    for i in range(10):
        constentant = sorted_contestants[i]
        print(f'{i}. {constentant.get_name()} - ELO {constentant.get_ELO()} | (Power: {constentant.player_strength})')


def scatter_results(contestants: list[SimulatedPlayer]):
    sorted_contestants = sorted(contestants, key=get_index)
    indices = []
    ELOs = []
    for contestant in sorted_contestants:
        indices.append(contestant.index)
        ELOs.append(contestant.ELO)

    plt.scatter(indices, ELOs, color='blue')
    plt.xlabel('Index of Object')
    plt.ylabel('ELO of Variable')
    plt.title('Correspondence of Order and Variable Value')
    plt.grid(True)
    plt.show()