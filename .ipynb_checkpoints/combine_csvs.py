import csv
import os

import pandas as pd

path = '/home/chris/Documents/'
directs = []

for root, dirs, files in os.walk(path, topdown=True):
    for name in dirs:
#        print(os.path.join(root, name))
        directs.append(dirs)

print(directs)
dircount = 0

for i in sorted(directs[0]):
    workpath = path + i
    print(workpath)  # path to move to

    os.chdir(workpath)  # moves into working directory
    onlyfiles = [f for f in os.listdir(workpath) if
                 os.path.isfile(os.path.join(workpath, f))]  # list of files to iterate over
    framecount = 0
    #csv_path = "/home/chris/Documents/"  #sets path to record csv output files
    df = pd.DataFrame(
        columns=['File', 'Frequency in Hertz'])  # create DataFrame for file
      #create csv for folder
    filecount = 0
    for file in sorted(onlyfiles):  # loop through current files

#        data = pd.read_csv(workpath + '/' + file)
        with open(workpath + '/' + file, newline='') as csvfile:
            filename = pd.Series(file)
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')

            for row in spamreader:
                #try:
                print(row)
                print(workpath + '/' + file)
                #    continue
                #except:
                #    continue

                df.loc[filecount]=[file, str(row)]
                filecount += 1
    print(df)
    df.to_csv(workpath + '/' + '0_' + i + '.csv')
framecount += 1

#send df to csv


        #with open(csv_path + str(directs[0][i]) + '/' + str(directs[0][i] + '.csv')):
#df.to_csv(csv_path + str(directs[0][i]) + '/' + str(directs[0][i]) + '.csv', index=False)
