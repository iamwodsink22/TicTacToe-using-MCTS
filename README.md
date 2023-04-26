# TicTacToe-using-MCTS
A Simple TicTacToe using MonteCarlo Tree Search Algorithm(Reinforcement Learning)

The skill of the CPU can be changed by increasing or decreasing number of simulations in the simulation method of MCTS Class.
While entering the position of your symbol, first number represents the row and second number represents the column

     0 0 0
     0 0 0
     0 0 0
If you want to enter -1 in middle of the board you need to enter '1 1' since it is at 1st row and 1st column as per python indexing.

     0  0 0
     0 -1 0
     0  0 0
Similary to enter -1 in first element you need to enter '0 0' as it is in 0th row and 0th column as per python indexing.

    -1 0 0
     0 0 0
     0 0 0

The CPU automatically plays as soon as you play.1 denotes CPU and -1 denotes Player.
You can change the denotatation to whatever you like in the main file.
