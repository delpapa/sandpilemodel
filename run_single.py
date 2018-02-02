import sys
import os
import cPickle as pickle

import numpy as np
import matplotlib.pylab as plt

from sandpile import ASM
from plot_avalanches import plot_avalanches, plot_pile

################################################################################
#                                Parameters                                    #
################################################################################
size = (101, 101)           # lattice size
total_grains = 500000       # number of grains to drop

random_neigbors = False     # if True, grains topple to random neighbors
random_dropping = False     # drop grains randomly instead of in the middle

draw_plots = True           # draw plots during the simulation
avalanches = True           # plot avalanche events distributions

################################################################################
#                            Sandpile simulation                               #
################################################################################
# 1. initialization
asm = ASM(size[0], size[1])

# 2. rrun simulation and save relevant variables
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
    if draw_plots and (grain % 100) == 0:
        plt.imshow(asm.lattice, interpolation='none', cmap='Blues')
        plt.draw()
        plt.pause(0.01)

plot_pile(asm.lattice)
print '\nDone :)'

# 3. pickle relevant variables
# create results directory
for n_sim in xrange(1, 1000):
    results_dir = 'results/ASM' + '_' + str(n_sim) + '/'
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)
        break
# pickle variables
with open(results_dir+'avalanche_times.p', 'wb') as f:
    pickle.dump(asm.aval_time, f)
with open(results_dir+'avalanche_sizes.p', 'wb') as f:
    pickle.dump(asm.aval_size, f)

# 4. plot avalanches
if plot_avalanches:
    print '\nPlotting avalanche distributions...',
    plot_avalanches(asm.aval_time, asm.aval_size)
