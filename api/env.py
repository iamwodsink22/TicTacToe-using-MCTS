import numpy as np
import copy


class Env:
    def __init__(self, states, player):
        self.states = states
        self.player = player


    def get_moves(self):
        return list(zip(*np.where(self.states == 0)))

    def get_next_player(self):
        return self.player*-1
    

    def next_state(self, action,player):
        prime_state = copy.deepcopy(self.states)
        
        prime_state[action] = player

        return (prime_state, -player)


    def get_cboard(self, state, player):
        return player*state

    def winner(self,  player):
        seqs = np.array([self.states[0, :], self.states[1, :], self.states[2, :],
                        self.states[:, 0], self.states[:, 1],
                        self.states[:, 2], self.states[(0, 1, 2), (0, 1, 2)], self.states[(2, 1, 0), (0, 1, 2)]], dtype='object')
        seq = seqs.tolist()

        if [player, player, player] in seq:
            return True
        else:
            return False

    def get_reward(self,player):
        if self.winner(player):
            return -10
        if self.winner(-player):
            return 10
        else:
            return 0

    def game_end(self):  
        if 0 not in self.states or self.game_over():
            return True
        else:
            return False

    def game_over(self):  
        if self.winner(1) or self.winner(-1) is True:
            return True
        else:
            return False

