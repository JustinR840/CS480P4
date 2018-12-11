Authors:
    Elias Mote
    Justin Ramos


How to Run:
    The main file for this program in main.py.
    This program was created with Python 3.6, however it should work
    with any version of Python 3. Python 3.6 is on blue and can be run with
    "python3.6 main.py".


What Doesn't Work:
    In both MinMax and AlphaBeta the program will terminate with an incorrect result.
    Based on examples given in class, it appears as though the program is incorrectly
    finding an ending result. This is indicated by the program not exploring the same
    amount of nodes as examples given in class (with a margin by as much as 50% less).
    The current suspect for this problem is that some logic with the Eval function (in
    Helpers.py) is incorrect.


Example Input:
    Below are some examples of input the program accepts. The program
    will accept a file of Xs, Os, and -s representing standard
    tic-tac-toe characters. The program will also accept input in the
    form of 1s, 2s, and 0s where each value respectively corresponds
    with X, O, and -.
    An example file called "test.input" has also been provided with the program.

Example Input 1:
O - O -
X - - X
X O - -
- - - X

Example Input 2:
2 0 2 0
1 0 0 1
1 2 0 0
0 0 0 1