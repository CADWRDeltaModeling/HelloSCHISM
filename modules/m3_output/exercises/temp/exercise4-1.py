from vtools.datastore.read_ts import *
import schimpy.plot_default_formats as pdf
import matplotlib.pyplot as plt

if __name__ == '__main__':
    pdf.set_color_cycle_dark2()
    fpath_in = '9414290_gageheight.txt'
    ts = read_ts(fpath_in)
    ts.plot()
    plt.show()