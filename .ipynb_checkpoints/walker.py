# %%
import os

import numpy as np
import pandas as pd
from scipy.io import wavfile

path = '/home/chris/PycharmProjects/project/data/'
directs = []

for root, dirs, files in os.walk(path, topdown=True):
    for name in dirs:
#        print(os.path.join(root, name))
        directs.append(dirs)

print(directs)
dircount = 0

for i in range(len(directs[0])):
    workpath = path + str(directs[0][i])
    print(workpath)  # path to move to

    os.chdir(workpath)  # moves into working directory
    onlyfiles = [f for f in os.listdir(workpath) if
                 os.path.isfile(os.path.join(workpath, f))]  # list of files to iterate over
    filecount = 0
    dircount += 1
    csv_path = '/media/chris/Backup Plus/csvs/'+ str(directs[0][i]) +'/'   #sets path to record csv output files
    os.mkdir('/media/chris/Backup Plus/csvs/'+ str(directs[0][i]))
    with open(csv_path + directs[0][i] + '.csv', 'w', newline='') as csvfile:
        # with open(directs[1][dircount]+'.csv', 'w', newline='') as csvfile:"#create csv for folder
        for file in onlyfiles:  # loop through current files
            print(workpath + '/' + file)

            try:
                fs, data = wavfile.read(workpath + '/' + file)
                fftout = abs(np.fft.fft(data))
                N = len(fftout)
                for m in range(0, N - 2):
                    fftout[2 * m] = data[m]
                    fftout[2 * m + 1] = 0
                    magnitude = []
                    for n in range(0, int(N / 2 - 1)):
                        re = fftout[2 * n]
                        im = fftout[2 * n + 1]
                        magnitude.append(np.sqrt(re * re + im * im))
                        max_magnitude = float(-9999999)
                        max_index: int = -1
                        for j in range(0, len(magnitude)):  # 1 less indent?
                            if magnitude[j] > max_magnitude:
                                max_magnitude = magnitude[j]
                                max_index = j
                                # convert largest peak to frequency
                                freq = max_index * fs / N
                                freqlist = []
                                freqlist.append(freq)

                df = pd.DataFrame(list(zip(file, np.mean(freqlist))),
                          columns=['clip file', 'Frequency'])  # create DataFrame for file
                with open(csv_path + file + '.csv', 'a') as f:
                    if filecount < 1:
                        df.to_csv(f, header=True)
                    else:
                        df.to_csv(f, header=False)
                    filecount+=1
                continue
            except:
                filecount +=1
        dircount += 1  # counts to next directory
