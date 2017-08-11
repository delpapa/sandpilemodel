import numpy as np

class ASM(object):

    def __init__(self, x, y):

        self.x = x
        self.y = y

        # lattice is created with a border of height 0 to account for the
        # grain falling off
        self.lattice = np.zeros((self.x+2, self.y+2))
        self.lattice_middle = (self.x/2+1, self.y/2+1)

    def add_grain_middle(self):
        self.lattice[self.lattice_middle] += 1

    def add_grain_random(self):
        rand_unit = (np.random.randint(1,self.x+1),
                     np.random.randint(1,self.y+1))
        self.lattice[rand_unit] += 1 

    def topple(self, max_height = 4):

        # avalanche time and size counters
        self.avalanche_time = 0
        self.avalanche_sites = np.zeros((self.x+2, self.y+2))

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
            self.avalanche_time += 1
            self.avalanche_sites[elem_x, elem_y] += 1

        self.avalanche_size = np.count_nonzero(self.avalanche_sites)
