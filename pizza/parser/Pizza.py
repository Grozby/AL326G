import os
import numpy as np


class Pizza:

    def __init__(self, r, c, l, h, data, slices=None):
        self.r = r
        self.c = c
        self.l = l
        self.h = h
        self.data = data
        self.slices = slices
        self.dir = os.path.dirname(os.path.realpath(__file__))

    def to_submission(self, name):
        file = open(os.path.join(self.dir, "..", "submissions", name), "w")
        file.write(str(len(self.slices)))
        for sl in self.slices:
            file.write(str(sl.r1) + " " + str(sl.c1) + " " + str(sl.r2) + str(sl.c2))
        file.close()

    def add_slice(self, slice_to_add):
        if self.slices is None:
            self.slices = [slice_to_add]
        else:
            self.slices.append(slice_to_add)

    def is_feasible(self, sl):
        dim = (sl.r2 - sl.r1 + 1) * (sl.c2 - sl.c1 + 1)
        s = np.sum(self.data[sl.r1:sl.r2+1, sl.c1:sl.c2+1])
        return dim <= self.h and s >= self.l and dim - s >= self.l