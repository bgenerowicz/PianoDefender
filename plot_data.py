import matplotlib.pyplot as plt
def plot_data(Data):
    plt.cla()
    plt.ion()  # enables interactive mode
    plt.plot(Data)  # result shows immediatelly (implicit draw())
    # plt.ylim([1e6,1e10])
    plt.pause(0.001)
    plt.show()