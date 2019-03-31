from __future__ import division
import numpy as np
#from random import choice, uniform, randint
import pandas as pd
import sys
import os
import matplotlib.pyplot as plt
from statsmodels.nonparametric.smoothers_lowess import lowess

mydir = os.path.expanduser('~/GitHub/Dine-College-ASCEND/python/Jamie_Data/')
df = pd.read_csv(mydir+'/Flight_Data.TXT')


# 'Co2_ppm'
fs = 13

fig = plt.figure()

y1 = df['Co2_ppm']
x = range(len(y1)) # a list representing time

smoothed = lowess(y1, x, is_sorted=True, frac=0.025, it=0)

# CH4 vs. time
fig.add_subplot(1, 1, 1)
clr = ['0.2']

plt.plot(df['Co2_ppm'], color = '0.3', linewidth=2.5, alpha=1.0)
plt.plot(smoothed[:,0], smoothed[:,1], color = 'red', linewidth=1.0, alpha=1.0)
#plt.axvspan(2600, 3800,alpha=0.5,color='red')

plt.xlabel("Time", fontsize=fs)
plt.ylabel("Concentration", fontsize=fs)
plt.tick_params(axis='both', which='major', labelsize=fs-1)

plt.subplots_adjust(wspace=0.5, hspace=0.5)
plt.savefig(mydir + 'figures/Fig1.png', dpi=400, bbox_inches = "tight")
plt.close()
