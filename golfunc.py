import numpy as np
import argparse
from collections import namedtuple

ON = 255
OFF = 0
values = (ON, OFF)

def randomgrid(gridsize):
	"""create a symmetrical grid of the size of gridsize"""
	return np.random.choice(values, gridsize*gridsize, p=[0.2, 0.8]).reshape(gridsize, gridsize)


def update(frames, img, grid, gridsize):
    """updates the grid every time it is refreshed"""
    # create a new grid through copying the passed grid
    # frames seems unused here but is necessary for funcAnimation to work.
    newgrid = grid.copy()

    for i in range(gridsize):
        for j in range(gridsize):
            # this formula considers the edge/boundary conditions that appear
            # every cell has to have 8 neighbouring cells
            # to implement this in a grid of size n we simply fold the 4 edges to each parallel edge
            # we'll end up with a cylinder first, then with a geometric shape called torus (google it.)
            total = int((grid[i, (j - 1) % gridsize] + grid[i, (j + 1) % gridsize] +
                         grid[(i - 1) % gridsize, j] + grid[(i + 1) % gridsize, j] +
                         grid[(i - 1) % gridsize, (j - 1) % gridsize] +
                         grid[(i - 1) % gridsize, (j + 1) % gridsize] +
                         grid[(i + 1) % gridsize, (j - 1) % gridsize] + grid[
                         (i + 1) % gridsize, (j + 1) % gridsize]) / 255)

        # apply conway's basic rules of the game of life for each cell
            if grid[i, j] == ON:
                if (total < 2) or (total > 3):
                    newgrid[i, j] = OFF
            else:
                if total == 3:
                    newgrid[i, j] = ON
    # update data
    grid[:] = newgrid[:]
    img.set_data(newgrid)
    return img,


def add_glider(i, j, grid):
    """displays a glider for demonstration purposes"""
    glider = np.array([[0, 0, 255],
                       [255, 0, 255],
                       [0, 255, 255]])

    grid[i:i+3, j:j+3] = glider


def add_beacon(i, j, grid):
	"""adds a beacon for demonstration purposes"""
	beacon = np.array([[0,  0,   0,  0, 0, 0],
                       [0, 255, 255, 0, 0, 0],
                       [0, 255, 255, 0, 0, 0],
	                   [0, 0, 0, 255, 255, 0]
	                   [0, 0, 0, 255, 255, 0]
	                   [0, 0, 0,  0,   0, 0]
	                   ])

	grid[i:i+6, j:j+6] = beacon


def argument_parser():
	"""enables console parsing for the program"""
	parser = argparse.ArgumentParser(description="Conway's game of life in Python 3")
	parser.add_argument('gridsize', type=int, help='Dimension of grid.')
	parser.add_argument('interval', type=int, help='Interval.')
	parser.add_argument('formationflag', type=bool, help='Predefined formation.')
	# parser.add_argument('frame', type=int, help='How many frames to animate.')

	# get arguments from input function
	arguments = parser.parse_args()

	return arguments


def input_arguments():
	"""offers user friendly input of the arguments and returns them as a named tuple"""
	choice = ""
	arguments = namedtuple("arguments", ["gridsize", "interval", "formationflag"])

	while choice != 'y' and choice != 'n':
		print("\t\tWelcome to Conways Game of life!")
		choice = input("\t\tDo you wish to input parameters (y/n) : ")

		if choice == 'y':
			while True:
				gridsize = input("\n\t\t Grid size in squares (9 - 270): ")

				if gridsize.isdigit() is False or int(gridsize) < 9 or int(gridsize) > 270:
					print(gridsize.isdigit())
					print("Error! Please input a valid number (9 - 270):")

				else:
					break

			while True:
				interval = input("\n\t\t Interval in miliseconds (1 - 10000): ")

				if interval.isdigit() is False or int(interval) < 1 or int(interval) > 10000:
					print("Error! Please input a valid number (1 - 10000)")

				else:
					break

			# add switch - case like scenario here
			while True:
				tmp = input("\n\t\t Add a formation(glider)? (y/n):")

				if tmp == 'y':
					glider = True
					break

				if tmp == 'n':
					glider = False
					break

				else:
					print("ERROR! Please input again")

			# return namedtupel
			return arguments(int(gridsize), int(interval), glider)

		# if no manual input is wanted - return default values
		print("Okay! Returning default parameters(grid=30squares, interval=250ms, no glider)")
		return arguments(30, 250, False)
		break
