import os
import argparse
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

from golfunc import *

def main():

	# uncommend this to make the program work via console argument parsing
    # arguments = argument_parser()
    # set the arguments

	# u
    arguments = input_arguments()
    gridsize = int(arguments.gridsize)
    interval = int(arguments.interval)
    formation = arguments.formationflag

    # if you want to start with a formation:
    if formation:
        grid = np.zeros(gridsize*gridsize).reshape(gridsize, gridsize)
        add_glider(1, 1, grid)

    # else display a randopm grid
    else:
        grid = randomgrid(gridsize)

    fig, ax = plt.subplots()

    # colormap: black -> alive, white -> dead
    img = ax.imshow(grid, cmap='binary', interpolation='nearest')

    # # this will be used to save the animation in a later version
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, gridsize,),
                                  frames=50,
                                  interval=interval,
                                  save_count=50)

    # remove x and y - axis labels, numbers and ticks
    ax.axes.xaxis.set_ticklabels([])
    ax.axes.yaxis.set_ticklabels([])
    plt.xticks([])
    plt.yticks([])

    # plot the animated output
    plt.show()

if __name__ == '__main__':
    main()
    print("DONE")