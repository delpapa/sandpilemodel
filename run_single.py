import numpy as np
import matplotlib.pylab as plt

from sandpile import ASM

# params
random_neigbors = False
random_dropping = True
size = (51, 51)
total_grains = 100000

asm = ASM(size[0], size[1])

for step in range(total_grains):

    # drop one grain
    if not random_dropping:
        asm.add_grain_middle()
    else:
        asm.add_grain_random()

    asm.topple()

    # # print the completed percent
    # if step%((grains-1)//100) == 0 or step == grains-1:
	# 	sys.stdout.write('\rSimulation: %3d%%'%((int)(step/(grains-1)*100)))
	# 	sys.stdout.flush()

    if not (step % 10000):
        plt.imshow(asm.lattice, interpolation='none')
        plt.draw()
        plt.pause(0.01)

print '\nFinished :)'
plt.show()
