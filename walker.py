# %%
import os
import numpy as np
from scipy.io import wavfile
import pandas as pd
import csv

path = '/home/chris/PycharmProjects/project/'
directs = []

for root, dirs, files in os.walk(path, topdown=True):
    for name in dirs:
        print(os.path.join(root, name))
        directs.append(dirs)

print(directs)
dircount = 0

for i in directs[1]:
    workpath = path + str(directs[1][dircount])
    print(workpath)  # path to move to
    dircount += 1  # counts to next directory
    os.chdir(workpath)  # moves into working directory
    onlyfiles = [f for f in os.listdir(workpath) if
                 os.path.isfile(os.path.join(workpath, f))]  # list of files to iterate over
    filecount = 0
    # with open(directs[1][dircount]+'.csv', 'w', newline='') as csvfile:"#create csv for folder
    for file in onlyfiles:  # loop through current files
        print(workpath + '/' + file)
        fs, data = wavfile.read(workpath + '/' + file)
        fftout = abs(np.fft.fft(data))
        freqs = abs(np.fft.fftfreq(fftout.size))
        df = pd.DataFrame(list(zip(np.log(fftout), freqs)),
                          columns=['ln(Amplitude)', 'Frequency'])  # create DataFrame for file
        df.to_csv(directs[1][dircount] + '.csv', encoding='utf-8')
