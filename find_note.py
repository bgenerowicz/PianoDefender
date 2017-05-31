import os
import numpy as np
import matplotlib.pyplot as plt


path = 'keys/'

# t1 = np.load(path + 'C4.npy')


residual = {}
def find_note(Data):
    t1 = Data
    for filename in os.listdir(path):
        t2 = filename.replace(".npy", "")
        t2data = np.load(path + filename)
        res = np.amax(np.absolute(t2data-t1))
        residual[t2] = res


    note = min(residual, key=residual.get)
    return note


# print(find_note(t1))