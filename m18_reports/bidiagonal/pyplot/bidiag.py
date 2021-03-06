#!/home/mawussi/anaconda2/bin/python
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_context('paper', font_scale=1.7)
sns.set_style('whitegrid')
#mpl.rc('font', **{'family':'serif', 'serif':['Computer Modern Roman'], \
    #                                'monospace': ['Computer Modern Typewriter']})
params = {'backend': 'pdf',
                    #'axes.labelsize': 8,
                    'font.size': 10,
                    'legend.fontsize': 8,
                    #'xtick.labelsize': 8,
                    #'ytick.labelsize': 8,
          #          'text.usetex': True,
                    #'figure.figsize': fig_size,
                    'axes.unicode_minus': True}
plt.rc('font', family='serif', serif='Times')
plt.rc('text', usetex=True)
plt.rc('xtick', labelsize=8)
plt.rc('ytick', labelsize=8)
plt.rc('axes', labelsize=8)
mpl.rcParams.update(params)


plt.figure(figsize=(9, 7))
ax = plt.subplot(111)
ax.spines["top"].set_visible(False)
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()
plt.grid(True)

## KNL data with M= 20000
KNL = pd.DataFrame.from_csv('data/DGE2GB_KNL.csv', parse_dates=False)
KNL.Gflop_V2.plot(color=sns.xkcd_rgb["windows blue"],lw=4.2, label="Early update")
KNL.Gflop_V1.plot(color=sns.xkcd_rgb["amber"],lw=4.2, label="Late update")
KNL.Gflop_QUARK.plot(color=sns.xkcd_rgb["pale red"],lw=4.2, label="Plasma-2.8.0")

plt.xticks(range(0, 20001, 2000), [str(x) + 'k' for x in range(0,21,2)],fontsize=22)
plt.yticks(range(0, 451, 50),fontsize=22)
plt.ylim(0, 450)
plt.xlabel("Matrix size(M=N)",fontsize=22)
plt.legend(loc="upper left",fontsize=22)
plt.ylabel("GFLOP/S",fontsize=22)
# Finally, save the figure as a PNG.
# You can also save it as a PDF, JPEG, etc.
# Just change the file extension in this call.
# bbox_inches="tight" removes all the extra whitespace on the edges of your plot.
plt.savefig("../fig/dge2gb_KNL.eps", bbox_inches="tight");  

### HBW

plt.figure(figsize=(9, 7))
ax = plt.subplot(111)
ax.spines["top"].set_visible(False)
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()
plt.grid(True)

## KNL data with M= 20000
KNL_HBW = pd.DataFrame.from_csv('data/DGE2GB_KNL_HBW.csv', parse_dates=False)
KNL_HBW.Gflop_V2.plot(color=sns.xkcd_rgb["windows blue"],lw=4.2, label="Early update")
KNL_HBW.Gflop_V1.plot(color=sns.xkcd_rgb["amber"],lw=4.2, label="Late update")
KNL_HBW.Gflop_QUARK.plot(color=sns.xkcd_rgb["pale red"],lw=4.2, label="Plasma-2.8.0")

plt.xticks(range(0, 20001, 2000), [str(x) + 'k' for x in range(0,21,2)],fontsize=22)
plt.yticks(range(0, 451, 50),fontsize=22)
plt.ylim(0, 450)
plt.legend(loc="upper left",fontsize=22)
plt.ylabel("GFLOP/S",fontsize=22)
plt.xlabel("Matrix size (M=N)",fontsize=22)
plt.savefig("../fig/dge2gb_KNL_HBW.eps", bbox_inches="tight");

