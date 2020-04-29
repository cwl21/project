# %%
import csv
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
    csv_path = "/home/chris/Documents/"  #sets path to record csv output files

      #create csv for folder
    for file in onlyfiles:  # loop through current files
            #print(workpath + '/' + file)

        try:

            with open(csv_path + directs[0][i] + '/' + file + '.csv', 'r', newline='') as csvfile:
                print(csv_path + directs[0][i] + '/' + file)
                fs, data = wavfile.read(workpath + '/' + file)
                w = np.fft.fft(data)
                #freqs = abs(np.fft.fftfreq(fftout.size))/len(fftout)
                freqs = np.fft.fftfreq(len(w))
                print(freqs.min(), freqs.max())
                idx = np.argmax(np.abs(w))
                freq = freqs[idx]
                freq_in_hertz = abs(freq * fs)
                print(freq_in_hertz)
                df = pd.DataFrame(
                      columns=['Frequency in Hertz'])  # create DataFrame for file
                row = pd.Series([freq_in_hertz])
                #dff = pd.concat([row, df], ingore_index=True)
                #with open(csv_path + directs[0][i] + file+'.csv', 'a', newline='') as csvfile:
                writing = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
#                if filecount < 1:
                writing.writerow(row)

                    #dff.to_csv(csvfile, header=True)
#                else:
#                    dff.to_csv(csvfile, header=False)
             #   with open(csv_path + directs[0][i] + '.csv', 'a') as csvfile:
             #       if filecount < 1:
             #           dff.to_csv(csvfile, header=True)
             #       else:
                       # dff.to_csv(csvfile, header=False)
                filecount+=1
            continue
        except:
            filecount+=1
            continue
            #    continue
            #except:
            #    filecount +=1
    dircount += 1  # counts to next directory
