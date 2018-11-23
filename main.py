import matplotlib.pyplot as plt
import matplotlib.animation as animation

from gol_functions import *

# main() function
def main():

	arguments = input_arguments()

	gridsize = int(arguments.gridsize)

	interval = int(arguments.interval)

	# use for different starting forms

	grid = randomgrid(gridsize)

	fig, ax = plt.subplots()
	# colormap: black -> alive, white -> dead
	img = ax.imshow(grid, cmap='binary', interpolation='nearest')

	ani = animation.FuncAnimation(fig, update, fargs=(img, grid, gridsize,),
	                              frames=10,
	                              interval=interval,
	                              save_count=50)

	# remove x and y - axis labels, numbers and ticks
	ax.axes.xaxis.set_ticklabels([])
	ax.axes.yaxis.set_ticklabels([])
	plt.xticks([])
	plt.yticks([])

	plt.show()  # call main


if __name__ == '__main__':
	main()