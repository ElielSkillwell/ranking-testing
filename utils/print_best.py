from utils.sim_ranked import SimulatedPlayer

def get_ELO(obj: SimulatedPlayer) -> int:
    return obj.get_ELO()


def print_best(contestants: list[SimulatedPlayer]):
    sorted_contestants = sorted(contestants, key=get_ELO, reverse=True)

    print(f'\n\n\nBest scores achieved: \n\n')

    for i in range(10):
        constentant = sorted_contestants[i]
        print(f'{i}. {constentant.get_name()} - ELO {constentant.get_ELO()} | (Power: {constentant.player_strength})')