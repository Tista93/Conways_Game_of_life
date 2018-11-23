from collections import namedtuple
import numpy as np

ON = 255
OFF = 0
vals = [ON, OFF]

def input_arguments():
	"""offers input for settings before the game of life starts"""
	choice = ""
	arguments = namedtuple("arguments", ["gridsize", "interval"])

	while choice != 'y' and choice != 'n':
		print("\t\tWelcome to Conways Game of life!")
		choice = input("\t\tDo you wish to input parameters (y/n) : ")

		if choice == 'y':
			while True:
				gridsize = input("\n\t\t Grid size (9 - 1000): ")

				if int(gridsize) < 9 or int(gridsize) > 1000 or gridsize.isdigit() is False:
					print("Error! Please input a valid number (9 - 1000):")

				else:
					break

			while True:
				interval = input("\n\t\t Interval (1 - 1000): ")

				if int(interval) < 1 or int (interval) > 1000 or interval.isdigit() is False:
					print("Error! Please input a valid number (1 - 1000)")

				else:
					break
			break

	return arguments(int(gridsize), int(interval))


def randomgrid(n):
    """returns a grid of NxN random values"""
    return np.random.choice(vals, n*n, p=[0.2, 0.8]).reshape(n, n)


def addglider(i, j, grid):
    """adds a glider with top-left cell at (i, j)"""
    glider = np.array([[0,    0, 255],
                       [255,  0, 255],
                       [0,  255, 255]])
    grid[i:i+3, j:j+3] = glider



def update(frameNum, img, grid, n):
    # copy grid since we require 8 neighbors for calculation
    # and we go line by line
    newgrid = grid.copy()
    for i in range(n):
        for j in range(n):
            # compute 8-neghbor sum using toroidal boundary conditions
            # x and y wrap around so that the simulation
            # takes place on a toroidal surface
            total = int((grid[i, (j-1)%n] + grid[i, (j+1)%n] +
                         grid[(i-1)%n, j] + grid[(i+1)%n, j] +
                         grid[(i-1)%n, (j-1)%n] + grid[(i-1)%n, (j+1)%n] +
                         grid[(i+1)%n, (j-1)%n] + grid[(i+1)%n, (j+1)%n])/255)
            # apply Conway's rules
            if grid[i, j] == ON:
                if (total < 2) or (total > 3):
                    newgrid[i, j] = OFF
            else:
                if total == 3:
                    newgrid[i, j] = ON
                    # update data
                    img.set_data(newgrid)
                    grid[:] = newgrid[:]
                    return img,



