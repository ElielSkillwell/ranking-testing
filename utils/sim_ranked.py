import random

import utils._global as _global

class SimulatedPlayer:
    def __init__(self, model, index) -> None:
        self.player_strength = random.random()
        self.model_name = model
        self.ELO = 400
        self.index = index

    def get_battle_vars(self):
        return self.player_strength
    
    def set_ELO(self, result_elo):
        self.ELO = result_elo
    
    def get_ELO(self):
        return self.ELO
    
    def get_name(self):
        return self.model_name
    


def battle_two(sim_player1: SimulatedPlayer, sim_player2: SimulatedPlayer) -> dict[SimulatedPlayer]:
    total_strength = sim_player1.get_battle_vars() + sim_player2.get_battle_vars()
    ratio_strength1 = sim_player1.get_battle_vars() / total_strength
    random_num = random.random()

    if random_num <= ratio_strength1:
        return sim_player1
    else:
        return sim_player2

def new_elo(player_obj: SimulatedPlayer, past_elo, won_or_lost, expected_outcome):
    if past_elo < _global.MAX_CHANGE_IN_ELO_UNDER_1000:
        max_change = _global.MAX_CHANGE_IN_ELO_UNDER_1000
    elif past_elo < _global.MAX_CHANGE_IN_ELO_UNDER_1500:
        max_change = _global.MAX_CHANGE_IN_ELO_UNDER_1500
    else:
        max_change = _global.MAX_CHANGE_IN_ELO_OVER_1500
    player_new_ELO = past_elo + max_change * (1 - expected_outcome)
    if player_new_ELO <= _global.MIN_ELO:
        player_new_ELO = _global.MIN_ELO
    player_obj.set_ELO(int(player_new_ELO))

def calc_elo(player_won: SimulatedPlayer, player_lost: SimulatedPlayer):
    won_elo = player_won.get_ELO()
    lost_elo = player_lost.get_ELO()
    expected_outcome_won = (10 ** (won_elo / _global.ELO_MAGIC_C)) / ((10 ** (won_elo / _global.ELO_MAGIC_C)) + (10 ** (lost_elo / _global.ELO_MAGIC_C)))
    expected_outcome_lost = (10 ** (lost_elo / _global.ELO_MAGIC_C)) / ((10 ** (lost_elo / _global.ELO_MAGIC_C)) + (10 ** (won_elo / _global.ELO_MAGIC_C)))

    new_elo(player_obj=player_won, past_elo=won_elo, won_or_lost=1, expected_outcome=expected_outcome_won)
    new_elo(player_obj=player_lost, past_elo=lost_elo, won_or_lost=0, expected_outcome=expected_outcome_lost)


def sim_battle(sim_player1: SimulatedPlayer, sim_player2: SimulatedPlayer, logs=False):
    player1_old_elo = sim_player1.get_ELO()
    player2_old_elo = sim_player2.get_ELO()
    player_won = battle_two(sim_player1, sim_player2)
    if player_won == sim_player1:
        calc_elo(sim_player1, sim_player2)
        winner = sim_player1.get_name()
    else:
        calc_elo(sim_player2, sim_player1)
        winner = sim_player2.get_name()

    if logs:
        print(f"""{sim_player1.get_name()}-{sim_player2.get_name()}: Player {winner} won. 
New Elo:
{sim_player1.get_name()}: {player1_old_elo} -> {sim_player1.get_ELO()}
{sim_player2.get_name()}: {player2_old_elo} -> {sim_player2.get_ELO()}""")
