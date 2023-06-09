import numpy as np
import copy


class Env:
    def __init__(self, states, player):
        self.states = states
        self.player = player
    # get all moves in a state

    def get_moves(self):
        return list(zip(*np.where(self.states == 0)))

    def get_next_player(self):
        self.player = self.player*-1
    # state after taking an action

    def next_state(self, action, player):
        prime_state = copy.deepcopy(self.states)
        print(action)
        prime_state[action] = player

        return (prime_state, -player)

    # board from another player perspective

    def get_cboard(self, state, player):
        return player*state

    # check if the given player has won the match
    def winner(self,  player):
        seqs = np.array([self.states[0, :], self.states[1, :], self.states[2, :],
                        self.states[:, 0], self.states[:, 1],
                        self.states[:, 2], self.states[(0, 1, 2), (0, 1, 2)], self.states[(2, 1, 0), (0, 1, 2)]], dtype='object')
        seq = seqs.tolist()

        if [player, player, player] in seq:
            return True
        else:
            return False
    # reward function for players, if CPU wins it gets 10 points if player wins it gets -10 and 0 for draw

    def get_reward(self, player):
        if self.winner(player):
            return 10
        if self.winner(-player):
            return -10
        else:
            return 0

    def game_end(self):  # check if game has ended
        if 0 not in self.states or self.game_over():
            return True
        else:
            return False

    def game_over(self):  # check if someone has won
        if self.winner(1) or self.winner(-1) is True:
            return True
        else:
            return False


# a = np.zeros((3, 3))
# e = Env(a, 1)
# print(e.get_moves())
# print(e.next_state((1, 2)))
# print(e.states)
# print(e.game_end())
