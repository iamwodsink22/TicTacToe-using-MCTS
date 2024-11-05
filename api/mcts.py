import copy
import random
import numpy as np
from env import Env


class Node:
    def __init__(self, player, prevNode=None, action=None):
        self.player = player
        self.action = action
        self.prevNode = prevNode
        self.isExpanded = False
        self.outcome = False
        self.children = dict()
        self.w = 0
        self.n = 0
        self.state = None
        
        
    def is_terminal(self,):
        
        return self.state.game_end()

    def eval(self, training: bool):

        return self.w/self.n if self.n > 0 else float("inf") if training else 0

    def choose_best_action(self, training: bool) -> int:
        return max(self.children, key=lambda action: self.children[action].eval(training))

    def choose_random_action(self) -> int:
        return random.sample(list(self.children.keys()), 1)[0]

    def expand(self, state, player):
        self.state = state
        for action in self.state.get_moves():
            if action not in self.children:
                self.children[action] = Node(
                    player*-1, prevNode=self, action=action)

    def expanded(self):
        return len(self.children) > 0


class MCTS:
    def __init__(self, state, training: bool = True):
        self.game = state
        self.cop_game = copy.deepcopy(state)
        self.training = training
    

    def simulate(self, player):
        root = Node(1)

        root.expand(self.cop_game, player)
        for i in range(1000):
        
            node = root
            while not node.is_terminal():
                    
                    search_path = [node]

                    # SELECT
                    if node.expanded():
                        
                        action = node.choose_random_action()
                        node=node.children[action]
                        
                        search_path.append(node)
                    parent = search_path[-2]
                    state = parent.state
                    next_state, _ = state.next_state(
                        action=action, player=state.player)
                   
                    # next_state = state.get_cboard(next_state, player=-1)
                    node.state=Env(next_state, player=_)
                    value = Env(next_state, player=_).get_reward(_)
                    
                    
                    if value == 0:
                        node.expand(Env(next_state, _), _)

                    self.backpropagation(search_path, value,1)

        return root.choose_best_action(False)

    def backpropagation(self, search_path, value, to_play):
        for node in reversed(search_path):
            node.w += value if node.player == to_play else -value
            node.n += 1
