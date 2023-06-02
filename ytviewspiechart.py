#Jessie
#Pie chart of my resent youtube channel views

import sys
import matplotlib.pyplot as plt
import numpy as np

y = np.array([61,22,23,268,307,885])
yttitles = ['Fast X Secret Ending','Thug shaker at 3am','Hector is gay','Civvie11 Loves TNT','EDP445 is sent to Prison','Walter White Becomes Gay']


def absolute_value(val):
    a = np.round(val/100.*y.sum(), 0)
    return a

plt.pie(y, labels = yttitles,autopct=absolute_value)
plt.legend(loc='lower right')
plt.title('My most recent Youtube video views (graph)')
plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()