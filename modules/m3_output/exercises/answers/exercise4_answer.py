import os
from vtools.datastore.read_ts import *
import schimpy.plot_default_formats as pdf
from schimpy.station import *
import matplotlib.pyplot as plt
import datetime
import pdb

if __name__ == '__main__':
    os.chdir(os.path.dirname(__file__))
    time_basis = datetime.datetime(2000, 1, 1)
    pdf.set_color_cycle_dark2()
    fig, ax = plt.subplots()

    # Set inputs for gathering model data
    station_fpath = "../station.in"
    outputs_fpath = "../outputs/staout_1"
    station_name = "oc_in" # Ocean Boundary Inland
    sub_loc = "default"
    sim_data=read_staout(outputs_fpath,station_fpath,time_basis)
    
    # Set inputs for gathering obs data
    obs_fpath = '9414290_gageheight.txt'  
    ts_obs = read_ts(obs_fpath)
    ts_obs=ts_obs.rename(columns={"Water Level":"Obs"})

    # Plot obs data
    ts_obs.plot(legend=True, ax=ax)

    # Plot model output
    sim_data[station_name+"_"+sub_loc].plot(label="Sim", legend=True, ax=ax, linestyle='dashed')

    plt.show()
