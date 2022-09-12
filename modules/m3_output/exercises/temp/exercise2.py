from schimpy.plot_default_formats import *
from schimpy.station import *
import matplotlib.pyplot as plt
import datetime


if __name__ == '__main__':
    station_fpath = '../flow_station_xsects.yaml'
    outputs_fpath = '../outputs/flux.out'
    time_basis = datetime.datetime(2009, 2, 10)
    station_name = 'montezuma_mouth'
    set_color_cycle_dark2()
    ts=read_flux_out(outputs_fpath,station_fpath,time_basis)
    ts[station_name].plot()
    plt.show()