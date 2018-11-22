import matplotlib.pyplot as plt
import matplotlib.animation as animation

from gol_functions import *

# main() function
def main():
	args = input_arguments()
	n = 100
	interval = 50

	if args.n and int(args.n) > 8:
		n = int(args.n)

	if args.interval:
		interval = int(args.interval)

	# use for different starting forms
	# grid = np.array([])

	grid = randomGrid(n)

	fig, ax = plt.subplots()
	# colormap: black -> alive, white -> dead
	img = ax.imshow(grid, cmap='binary', interpolation='nearest')

	ani = animation.FuncAnimation(fig, update, fargs=(img, grid, n,),
	                              frames=10,
	                              interval=interval,
	                              save_count=50)

	plt.show()  # call main


if __name__ == '__main__':
	main()