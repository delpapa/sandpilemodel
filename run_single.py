import sys
import os
import cPickle as pickle

import numpy as np
import matplotlib.pylab as plt

from sandpile import ASM
from plot_avalanches import plot_avalanches

################################################################################
#                                Parameters                                    #
################################################################################
size = (51, 51)
total_grains = 50000

random_neigbors = False
random_dropping = True
show_plots = True
plot_avalanches = False

################################################################################
#                            Sandpile simulation                               #
################################################################################
# 1. initialize model
asm = ASM(size[0], size[1])

# 2. simulate model and save relevant variables
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
print '\nFinished :)'

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
    plt.show()
