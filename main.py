import matplotlib.pyplot as plt
from matplotlib import animation
from golfunc import *


# main function
def main():

    # uncomment this to make the program work via console argument parsing
    # ####arguments = argument_parser()

    # comment this out if you want to run the program via command line argument parsing
    arguments = input_arguments()

    # set arguments
    gridsize = int(arguments.gridsize)
    interval = int(arguments.interval)
    formation = arguments.formationflag

    # if you want to display a glider for demonstration:
    # will later implement all the other different shapes.
    if formation:
        grid = np.zeros(gridsize*gridsize).reshape(gridsize, gridsize)
        add_glider(1, 1, grid)

    # else display a random grid
    else:
        grid = randomgrid(gridsize)

    # prepare the plots
    fig, ax = plt.subplots()

    # colormap: black -> alive, white -> dead
    img = ax.imshow(grid, cmap='binary', interpolation='nearest')

    # create animation ('ani' will later be used for saving the animation)
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, gridsize,),
                                  frames=60,
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
