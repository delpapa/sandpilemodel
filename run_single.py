import sys
import cPickle as pickle

import numpy as np
import matplotlib.pylab as plt

from sandpile import ASM
from plot_avalanches import plot_avalanches

# params
random_neigbors = False
random_dropping = True
show_plots = False
size = (51, 51)
total_grains = 500000

# initialize model
asm = ASM(size[0], size[1])

# simulate model and save relevant variables
for grain in range(total_grains):

    # drop one grain
    if not random_dropping:
        asm.add_grain_middle()
    else:
        asm.add_grain_random()

    # topple
    asm.topple()

    # print the completed percent
    if grain%((total_grains-1)//100) == 0 or grain == total_grains-1:
		sys.stdout.write('\rSimulation: %3d%%'%((int)(grain/(total_grains-1.)*100)))
		sys.stdout.flush()

    # show grid figure
    if show_plots and (grain % 10000) == 0:
        plt.imshow(asm.lattice, interpolation='none')
        plt.draw()
        plt.pause(0.01)
print '\nFinished :)'

# plot avalanche
print '\nPlotting avalanche distributions...',
plot_avalanches(asm)
plt.show()
