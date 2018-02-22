import sys
import os
import pickle

import numpy as np
import matplotlib.pylab as plt

from sandpile import ASM
from plot_avalanches import plot_avalanches, plot_pile

################################################################################
#                                Parameters                                    #
################################################################################
SIZE = (101, 101)             # lattice size
TOTAL_GRAINS = 100000        # number of grains to drop

RANDOM_DROPPING = False     # drop grains randomly instead of in the middle
RANDOM_INIT = False         # start from a random lattice state

EXP_NAME = 'test'

DRAW_PLOTS = True           # draw plots during the simulation
PLOT_AVALANCHES = True      # plot avalanche events distributions

################################################################################
#                            Sandpile simulation                               #
################################################################################
# 1. initialization
asm = ASM(SIZE[0], SIZE[1], random_init=RANDOM_INIT)

# 2. rrun simulation and save relevant variables
for grain in range(TOTAL_GRAINS):

    # drop one grain
    if not RANDOM_DROPPING:
        asm.add_grain_middle()
    else:
        asm.add_grain_random()

    # topple
    asm.topple()

    # print the completed percent
    if grain%((TOTAL_GRAINS-1)//100) == 0 or grain == TOTAL_GRAINS-1:
        sys.stdout.write('\rSimulation: %3d%%'\
                         %((int)(grain/(TOTAL_GRAINS-1.)*100)))
        sys.stdout.flush()

    # show grid figure
    if DRAW_PLOTS and (grain % 100) == 0:
        plt.imshow(asm.lattice, interpolation='none', cmap='magma')
        plt.draw()
        plt.pause(0.01)

plot_pile(asm.lattice)
print('\nDone :)')

# 3. pickle relevant variables
# create results directory
for n_sim in range(1, 1000):
    results_dir = '../results/' + EXP_NAME + '/ASM_' + str(n_sim) + '/'
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)
        break
# pickle variables
with open(results_dir+'avalanche_times.p', 'wb') as f:
    pickle.dump(asm.aval_time, f)
with open(results_dir+'avalanche_sizes.p', 'wb') as f:
    pickle.dump(asm.aval_size, f)

# 4. plot avalanches
if PLOT_AVALANCHES:
    print('\nPlotting avalanche distributions...'),
    plot_avalanches(asm.aval_time, asm.aval_size)
