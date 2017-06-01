import os
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal, stats


path = 'keys/'

# t1 = np.load(path + 'C4.npy')

residual = {}
# residual1 = {}
# residual2 = {}
# residual3 = {}
# residual4 = {}

def find_note(Data):
    t1 = Data
    for filename in os.listdir(path):
        t2 = filename.replace(".npy", "")
        t2data = np.load(path + filename)
        res = np.linalg.norm(t2data - t1) ** 2
        residual[t2] = res
        # res1 = np.amax(np.absolute(t2data-t1))
        # res2 = np.mean(np.absolute(t2data - t1))
        # res3 = np.linalg.norm(t2data - t1) ** 2
        # res4 = stats.kurtosis(t2data - t1)**2
        # residual1[t2] = res1
        # residual2[t2] = res2
        # residual3[t2] = res3 #?
        # residual4[t2] = res4


    note = min(residual, key=residual.get)
    #plot?
    # fig1 = plt.figure()
    # ax1 = fig1.add_subplot(411)
    # ax2 = fig1.add_subplot(412)
    # ax3 = fig1.add_subplot(413)
    # ax4 = fig1.add_subplot(414)
    # # ax1.cla()
    # # ax1.ion()  # enables interactive mode
    # ax1.bar(range(len(residual1)), residual1.values(), align='center')
    # ax2.bar(range(len(residual2)), residual2.values(), align='center')
    # ax3.bar(range(len(residual3)), residual3.values(), align='center')
    # ax4.bar(range(len(residual4)), residual4.values(), align='center')
    # plt.xticks(range(len(residual1)), residual1.keys())
    # # ax1.pause(0.001)
    #
    # plt.show()
    return note


# print(find_note(t1))
end = 1