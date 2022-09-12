import os
from schimpy.plot_default_formats import *
from schimpy.station import *
import matplotlib.pyplot as plt
import datetime


if __name__ == '__main__':
    os.chdir(os.path.dirname(__file__))
    time_basis = datetime.datetime(2009, 2, 10)
    set_color_cycle_dark2()

    station_fpath = '../flowlines.yaml'
    outputs_fpath = "../outputs/flux.out"
    station_name = "north_weir_upstream"

    all_ts = read_flux_out(outputs_fpath, station_fpath, time_basis)
    all_ts[station_name].plot()
    plt.show()