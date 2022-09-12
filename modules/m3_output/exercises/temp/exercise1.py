
from schimpy.plot_default_formats import *
from schimpy.station import *
import matplotlib.pyplot as plt
import datetime
import pdb

if __name__ == '__main__':
    station_fpath = '../station.in'
    outputs_fpath = '../outputs/staout_1'
    time_basis = datetime.datetime(2009, 2, 10)
    station_name = '9414290'  # San Francisco
    sub_loc="default"
    set_color_cycle_dark2()
    
    outputs_fpath = '../outputs/staout_6'
    station_name = 'MRZ'  # San Francisco
    sub_loc="upper"
    all_ts=read_staout(outputs_fpath,station_fpath,time_basis)
    all_ts[station_name+"_"+sub_loc].plot()
    plt.show()
