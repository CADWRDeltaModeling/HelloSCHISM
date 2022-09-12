import os
from vtools.datastore.read_ts import *
import schimpy.plot_default_formats as pdf
from schimpy.station import *
import matplotlib.pyplot as plt
import datetime
import pdb

if __name__ == '__main__':
    os.chdir(os.path.dirname(__file__))
    time_basis = datetime.datetime(2009, 2, 10)
    pdf.set_color_cycle_dark2()
    fig, ax = plt.subplots()
