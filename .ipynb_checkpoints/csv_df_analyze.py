import os

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set()

path = '/home/chris/Documents/'

onlyfiles = [f for f in os.listdir(path) if
             os.path.isfile(os.path.join(path, f))]
aggregate = []

for file in sorted(onlyfiles):
    df = pd.read_csv(path + file)
    # print(df)
#    series_mean = np.mean(df['Clean Hz'])  # remove to use full data
#    print(series_mean)  # remove to use full data
#    aggregate.append(series_mean)  # remove to use full data
    hz = df['Clean Hz']

#   HAVE FUN!!!
    # plotting games

    # N, bins, patches = plt.hist(hz, bins=20)

    # color code by height
    #    fracs = N / N.max()

    #    norm = colors.Normalize(fracs.min(), fracs.max())

    #    for thisfrac, thispatch in zip(fracs, patches):
    #        color = plt.cm.viridis(norm(thisfrac))
    #        thispatch.set_facecolor(color)

    # plt.hist(hz, bins=20, density=True)
    #sns.swarmplot(x=hz)
    # good
    # plt.hist(hz, bins=10)
    #plt.xlim(0, 1000)
    #plt.ylim(0, 5000)
    plt.title(file + ' frequency distribution histogram')

    plt.plot(hz, linestyle=None)
    # plt.gca().yaxis.set_major_formatter(PercentFormatter(xmax=1))

    # plt.savefig('/home/chris/Desktop/' + file + '.pdf', format='pdf', dpi=1200)
    plt.show()
    files = [hz]




