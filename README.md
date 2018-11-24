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
  
  
**Explaination of the theoretical background of Conways Game of Life**

The Game of Life, also known simply as Life, is a cellular automaton 
devised by the British mathematician John Horton Conway in 1970.

The game is a zero-player game, meaning that its evolution is determined 
by its initial state, requiring no further input. One interacts with the 
Game of Life by creating an initial configuration and observing how it 
evolves, or, for advanced players, by creating patterns with particular
properties.

The universe of the Game of Life is an infinite, two-dimensional 
orthogonal grid of square cells, each of which is in one of two 
possible states, alive or dead, (or populated and unpopulated, respectively).
Every cell interacts with its eight neighbours, which are the cells that 
are horizontally, vertically, or diagonally adjacent. At each step in time, 
the following transitions occur:

1. *Any live cell with fewer than two live neighbors dies, as if by underpopulation.*
2. *Any live cell with two or three live neighbors lives on to the next generation.*
3. *Any live cell with more than three live neighbors dies, as if by overpopulation.*
4. *Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.*



**The base grid:**

   ![game-of-life-diagram](https://user-images.githubusercontent.com/43903037/48967944-6756e800-efe8-11e8-8fe4-a49b99b05d89.png)


**Approach:**
1. Initialize the cells in the grid.
2. At each time step in the simulation, for each 
   cell (i, j) in the grid, do the following:
   
   a. Update the value of cell (i, j) based on 
      its neighbors, taking into account the 
      ***boundary conditions***.
      
   b. Update the display of grid values.
   
   
   

***"Boundary conditions? What are you talking about?"***

To get the boundary coniditions to create a grid of the size n made up of smaller "base grits" we simply need to "fold"
each side to the side parallel to it.
If we fold the side D to the side B well end up with a cylinder.
If we then connect the ends of the cylinder (thus connecting side A to C) to each other, 
we'll end up with a torus.

![torus](https://user-images.githubusercontent.com/43903037/48967966-a5eca280-efe8-11e8-9703-5863b38b340b.png)

It's kinda like Pac-Man - the top is connected to the bottom and the left is connected to the right.
Conwey's rules also apply to those connected edges and thus creating the boundary conditions.
These conditions make the whole thing scaleable.
If you still have some problems understanding this then I'd suggest you have a look at the *update* function in *golfunc.py*

Have fun!

Sources: 
www.wikipedia.org
www.geeksforgeeks.org
