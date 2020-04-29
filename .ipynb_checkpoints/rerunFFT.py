# %%
import csv
import os

import numpy as np
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
    csv_path = "/home/chris/Documents/"  ## sets path to record csv output files

    # create csv for folder
    for file in onlyfiles:  # loop through current files
            print(workpath + '/' + file)
       # try:
#            with open(csv_path + directs[0][i] + '/' + file + '.csv', 'a', newline='') as csvfile:
            fs, data = wavfile.read(workpath + '/' + file)
            fftout = abs(np.fft.fft(data))
            N = len(fftout)
            print(N)
            print(csv_path + directs[0][i])
            for m in range(0, N - 1):
                fftout[2 * m] = data[m]
                fftout[2 * m + 1] = 0

                    # calculate power spectrum(magnitude) values from fft[]
                magnitude = []
                for n in range(0, int(N / 2 - 1)):
                    re = fftout[2 * n]
                    im = fftout[2 * n + 1]
                    magnitude.append(np.sqrt(re*re+im*im))
                        # find largest peak in power spectrum
                max_magnitude = float("-inf")
                max_index: int = -1
#                        print(magnitude[n])
                for j in range(0, len(magnitude)):
                    if magnitude[j] > max_magnitude:
                        max_magnitude = magnitude[j]
                        max_index = j
                                # convert largest peak to frequency
                        freq = max_index * fs / N
                        freqs = [file, 2/N, freq]
                                # freqs = abs(np.fft.fftfreq(fftout.size))/len(fftout)
                                #df = pd.DataFrame(
                                #    columns=['Frequency in Hertz'])  # create DataFrame for file
                                #row = pd.Series([freq])
                                #   dff = pd.concat([row, df], ingore_index=True)
                    with open(csv_path + directs[0][i] + str(filecount)+'.csv', 'a', newline='') as csvfile:
                        writing = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                                #                    if filecount < 1:
                        writing.writerow(freqs)


                    # dff.to_csv(csvfile, header=True)
            #                else:
            #                    dff.to_csv(csvfile, header=False)
            #   with open(csv_path + directs[0][i] + '.csv', 'a') as csvfile:
            #       if filecount < 1:
            #           dff.to_csv(csvfile, header=True)
            #       else:
            # dff.to_csv(csvfile, header=False)
         #   filecount += 1
            #continue
       # except:
        #    filecount += 1
        #    continue
            #    continue
            # except:
            #    filecount +=1
    dircount += 1  # counts to next directory
