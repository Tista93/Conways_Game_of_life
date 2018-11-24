## A simple and straightforward implementation of Conway's GoL in Python 3.
### No complicated frameworks were used. Easy to understand for beginners/early intermediates.

**How the program works:**
- There are 2 ways you can run this program by manipulating the code: 
  1. With a simplified input prompt (DEFAULT) 
  2. Or with command line argument parsing

  Choose whichever you prefer.

- You can adjust the **size of the grid** and the **update interval** 
- You can either create a **random grid** of alive/dead cells or start
  an empty screen with a **predetermend formation** to watch its behaviour
  *(Currently there is only the glider. More formations will follow)*
  
 Enjoy.

**Explaination of the theoretical background of Conways Game of Life**

The Game of Life, also known simply as Life, is a cellular automaton 
devised by the British mathematician John Horton Conway in 1970.

The game is a zero-player game, meaning that its evolution is determined 
by its initial state, requiring no further input. One interacts with the 
Game of Life by creating an initial configuration and observing how it 
evolves, or, for advanced players, by creating patterns with particular
properties.

he universe of the Game of Life is an infinite, two-dimensional 
orthogonal grid of square cells, each of which is in one of two 
possible states, alive or dead, (or populated and unpopulated, respectively).
Every cell interacts with its eight neighbours, which are the cells that 
are horizontally, vertically, or diagonally adjacent. At each step in time, t
he following transitions occur:

1. *Any live cell with fewer than two live neighbors dies, as if by underpopulation.*
2. *Any live cell with two or three live neighbors lives on to the next generation.*
3. *Any live cell with more than three live neighbors dies, as if by overpopulation.*
4. *Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.*

The initial pattern constitutes the seed of the system. The first generation is created by 
applying the above rules simultaneously to every cell in the seed; births and deaths occur 
simultaneously, and the discrete moment at which this happens is sometimes called a tick. 
Each generation is a pure function of the preceding one.
The rules continue to be applied repeatedly to create further generations.

**The basic grid:**

[TheBasicGrid](https://cdncontribute.geeksforgeeks.org/wp-content/uploads/Game-Of-Life-Diagram.png)
