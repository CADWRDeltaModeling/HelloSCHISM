
import os
from schimpy.plot_default_formats import *
from schimpy.station import *
import matplotlib.pyplot as plt
import datetime
import pdb

if __name__ == '__main__':
    os.chdir(os.path.dirname(__file__))
    station_fpath = '../station.in'
    time_basis = datetime.datetime(2009, 2, 10)
    set_color_cycle_dark2()

    outputs_fpath = "../outputs/staout_1"
    station_name = "oc_in" # Ocean Boundary Inland
    sub_loc = "default"
    all_ts = read_staout(outputs_fpath, station_fpath, time_basis)
    all_ts[station_name + "_" + sub_loc].plot()
    plt.show()

