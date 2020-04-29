import os

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set()
directs = []

path = '/home/chris/Documents/'
for root, dirs, files in os.walk(path, topdown=True):
    for name in dirs:
#        print(os.path.join(root, name))
        directs.append(dirs)

print(directs)
dircount = 0

for i in range(len(directs[0])):
    lang = directs[0][i]

    os.chdir(path+lang)

    data = pd.read_csv('00'+lang+'.csv', sep=",", header=None, index_col =1)

    data.plot(kind='hist')
    plt.ylim([0,8000])
    plt.ylabel('Frequency')
    plt.xlabel('Samples (avg of utterance)')
    plt.title(lang)

    plt.show()
    plt.savefig(path+lang+'.svg')