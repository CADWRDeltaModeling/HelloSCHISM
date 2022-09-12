import os
from vtools.datastore.read_ts import *
import schimpy.plot_default_formats as pdf
import matplotlib.pyplot as plt

if __name__ == '__main__':
    os.chdir(os.path.dirname(__file__))
    pdf.set_color_cycle_dark2()
