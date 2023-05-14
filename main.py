import numpy as np
from env import Env
from mcts import Node
from mcts import MCTS
z = np.zeros((3, 3))
turn = 1
print(z)
# Until the game is not over, keep taking turns between CPU and Player
while Env(z, -1).game_end() is False:
    
    if turn == -1:
        '''Rows are a and columns are b i.e 1'space'2 means first row second column'''
        a, b = input("Enter Your move").split()

        if not z[int(a)][int(b)]:
            z[int(a)][int(b)] = -1
            print(z)
            turn = turn*-1
            print(turn)
    elif turn == 1:
        env = Env(z, 1)
        action = MCTS(env).simulate(1)

        z[action] = 1
        print(z)
        turn = turn*-1
        print(turn)
if Env(z, 1).winner(1) is True:
    print("CPU Wins")
elif Env(z, 1).winner(-1) is True:
    print("Player Wins")
