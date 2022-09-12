from vtools.datastore.read_ts import *
import schimpy.plot_default_formats as pdf
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
    
    obs_fpath = '9414290_gageheight.txt'
    ts_obs = read_ts(obs_fpath)
    ts_obs=ts_obs.rename(columns={"Water Level":"Obs"})
    ts_obs.plot(legend=True)
    all_ts_sim=read_staout(outputs_fpath,station_fpath,time_basis)
    all_ts_sim[station_name+"_"+sub_loc].plot(label="Sim",legend=True)
    
    pdf.set_color_cycle_dark2()
    plt.show()
