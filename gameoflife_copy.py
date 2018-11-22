import sys, argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def randomGrid(N):
    """returns a grid of NxN random values"""
    return np.random.choice(vals, N*N, p=[0.2, 0.8]).reshape(N, N)

def addGlider(i, j, grid):
    """adds a glider with top-left cell at (i, j)"""
    glider = np.array([[0,    0, 255],
                       [255,  0, 255],
                       [0,  255, 255]])
    grid[i:i+3, j:j+3] = glider

def update(frameNum, img, grid, N):
    # copy grid since we require 8 neighbors for calculation
    # and we go line by line
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):
            # compute 8-neghbor sum using toroidal boundary conditions
            # x and y wrap around so that the simulation
            # takes place on a toroidal surface
            total = int((grid[i, (j-1)%N] + grid[i, (j+1)%N] +
                         grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                         grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] +
                         grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N])/255)
            # apply Conway's rules
            if grid[i, j] == ON:
                if (total < 2) or (total > 3):
                    newGrid[i, j] = OFF
            else:
                if total == 3:
                    newGrid[i, j] = ON
                    # update data
                    img.set_data(newGrid)
                    grid[:] = newGrid[:]
                    return img,

def input_arguments():
	"""offers input for settings before the game of life starts"""
	choice = ""

	parser = argparse.ArgumentParser(description="Runs Conway's game of life simulation")
	parser.add_argument('--grid-size', dest='N', required=False)
	parser.add_argument('--mov-file', dest='movfile', required=False)
	parser.add_argument('--interval', dest='interval', required=False)
	args = parser.parse_args()

	while choice != 'y' and choice != 'n':
		print("\t\tWelcome to Conways Game of life!")
		choice = input("\t\tDo you wish to input parameters (y/n) : ")

		if choice == 'y':
			args.N = input("\n\t\t Grid size: ")
			args.interval = input("\n\t\t Interval: ")
			#args.movfile = input("\n\t\t Tape the whole thing (y/n): ")
			break

	return args




# main() function
def main():

	args = input_arguments()

	N = 50
	if args.N and int(args.N) > 8:
		N = int(args.N)

	updateInterval = 300
	if args.interval:
		updateInterval = int(args.interval)

	grid = np.array([])

	grid = randomGrid(N)

	fig, ax = plt.subplots()
	img = ax.imshow(grid, cmap='PiYG', interpolation='nearest')
	ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N,),
	                              frames=10,
	                              interval=updateInterval,
	                              save_count=50)

	# if args.movfile:
	#	ani.save(args.movfile, fps=30, extra_args=['-vcodec', 'libx264'])

	plt.show()

# call main
if __name__ == '__main__':
    main()