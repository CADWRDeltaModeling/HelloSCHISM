import os
from schimpy.plot_default_formats import *
from schimpy.station import *
import matplotlib.pyplot as plt
import datetime


if __name__ == '__main__':
    os.chdir(os.path.dirname(__file__))
    time_basis = datetime.datetime(2000, 1, 1)
    set_color_cycle_dark2()
