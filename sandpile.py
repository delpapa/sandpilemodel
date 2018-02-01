import numpy as np

class ASM(object):

    def __init__(self, x, y, h = 4, random_init = False):

        self.x = x
        self.y = y

        # lattice is created with a border of height 0 to account for the
        # grain falling off
        if random_init:
            self.lattice = np.random.randint(h, size=(self.x+2, self.y+2))
        else:
            self.lattice = np.zeros((self.x+2, self.y+2))

        self.lattice_middle = (self.x/2+1, self.y/2+1)

        # stats to save
        self.aval_time = []
        self.aval_size = []
        self.aval_size_all = []

    def add_grain_middle(self):
        self.lattice[self.lattice_middle] += 1

    def add_grain_random(self):
        rand_unit = (np.random.randint(1,self.x+1),
                     np.random.randint(1,self.y+1))
        self.lattice[rand_unit] += 1

    def topple(self, max_height = 4):

        # avalanche time and size counters
        avalanche_time = 0
        avalanche_sites = np.zeros((self.x+2, self.y+2))

        while self.lattice.max() >= max_height:

            # decrease over threshold piles
            elem_x, elem_y = np.where(self.lattice >= max_height)
            self.lattice[elem_x, elem_y] -= max_height

            # increase height of neighbor piles
            self.lattice[elem_x-1, elem_y] += 1
            self.lattice[elem_x+1, elem_y] += 1
            self.lattice[elem_x, elem_y-1] += 1
            self.lattice[elem_x, elem_y+1] += 1

            # remove grains of the border
            self.lattice[0] = self.lattice[-1] = 0
            self.lattice[:, 0] = self.lattice[:, -1] = 0

            # update counters
            avalanche_time += 1
            avalanche_sites[elem_x, elem_y] += 1

        # do not save size 0 avalanches
        if avalanche_time > 0:
            self.aval_time.append(avalanche_time)
            self.aval_size.append(np.count_nonzero(avalanche_sites))
            self.aval_size_all.append(avalanche_sites.sum())
