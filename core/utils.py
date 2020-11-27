import pandas as pd
from matplotlib import pyplot as plt


def exercicio1():
    dataframe = pd.read_fwf(
        'static/data.txt', header=None,
        names=["Router1", "Router2", "Router3",
               "Router4", "Router5", "Router6", "Router7", "Room"]
    )
    Routers = ["Router1", "Router2", "Router3", "Router4", "Router5", "Router6", "Router7"]
    Room1 = dataframe[dataframe["Room"] == 1]  # Select a subclass of dataframe with all informations of Room1
    Room1 = Room1[Routers]  # Exclude the Room column

    mean1 = Room1.mean()
    #mean1.plot.bar(stacked=True, rot=0)
    #plt.title("Room 1 Intensity in Module")
    #plt.show()

    Room2 = dataframe[dataframe["Room"] == 2]  # Select a subclass of dataframe with all informations of Room2
    Room2 = Room2[Routers]  # Exclude the Room column

    mean2 = Room2.mean()
    #mean2.plot.bar(stacked=True, rot=0)
    #plt.title("Room 2 Intensity ")
    #plt.show()


    Room3 = dataframe[dataframe["Room"] == 3]  # Select a subclass of dataframe with all informations of Room3
    Room3 = Room3[Routers]  # Exclude the Room column

    mean3 = Room3.mean()
    #mean3.plot.bar(stacked=True, rot=0)
    #plt.title("Room 3 Intensity in Module")
    #plt.show()


    Room4 = dataframe[dataframe["Room"] == 4]  # Select a subclass of dataframe with all informations of Room4
    Room4 = Room4[Routers]  # Exclude the Room column

    mean4 = Room4.mean()
    #mean4.plot.bar(stacked=True, rot=0)
    #plt.title("Room 4 Intensity in Module")
    #plt.show()

    conclusion1 = " Para a sala 1: De acordo com os dados apresentados, " \
                 "o roteador dois é o mais intenso pois apresenta a média maior do que os demais."

    conclusion2 = "Seguindo esta lógica os roteadores mais intensos nas salas 2,3 e 4 respectivamente são:" \
                  "Roteador 1, Roteador 1 e Roteador 2"

    return mean1, mean2, mean3, mean4

def exercicio2():
    dataframe = pd.read_fwf(
        'static/data.txt', header=None,
        names=["Router1", "Router2", "Router3",
               "Router4", "Router5", "Router6", "Router7", "Room"]
    )
    Routers = ["Router1", "Router2", "Router3", "Router4", "Router5", "Router6", "Router7"]
    Room1 = dataframe[dataframe["Room"] == 1]  # Select a subclass of dataframe with all informations of Room1
    Room1 = Room1[Routers]  # Exclude the Room column




    Room2 = dataframe[dataframe["Room"] == 2]  # Select a subclass of dataframe with all informations of Room2
    Room2 = Room2[Routers]  # Exclude the Room column



    Room3 = dataframe[dataframe["Room"] == 3]  # Select a subclass of dataframe with all informations of Room3
    Room3 = Room3[Routers]  # Exclude the Room column




    Room4 = dataframe[dataframe["Room"] == 4]  # Select a subclass of dataframe with all informations of Room4
    Room4 = Room4[Routers]  # Exclude the Room column


    conclusion1 = " Para a sala 1: De acordo com os dados apresentados, " \
                 "o roteador dois é o mais intenso pois apresenta a média maior do que os demais."

    conclusion2 = "Seguindo esta lógica os roteadores mais intensos nas salas 2,3 e 4 respectivamente são:" \
                  "Roteador 1, Roteador 1 e Roteador 2"

    return dataframe.corr(), Room1, Room2, Room3, Room4

def exercicio3():
    dataframe = pd.read_fwf(
        'static/data.txt', header=None,
        names=["Router1", "Router2", "Router3",
               "Router4", "Router5", "Router6", "Router7", "Room"]
    )
    general_mean = dataframe.mean()

    Routers = ["Router1", "Router2", "Router3", "Router4", "Router5", "Router6", "Router7"]
    Room1 = dataframe[dataframe["Room"] == 1]  # Select a subclass of dataframe with all informations of Room1
    Room1 = Room1[Routers]  # Exclude the Room column
    mean1 = Room1.mean()




    Room2 = dataframe[dataframe["Room"] == 2]  # Select a subclass of dataframe with all informations of Room2
    Room2 = Room2[Routers]  # Exclude the Room column
    mean2 = Room2.mean()


    Room3 = dataframe[dataframe["Room"] == 3]  # Select a subclass of dataframe with all informations of Room3
    Room3 = Room3[Routers]  # Exclude the Room column
    mean3 = Room3.mean()



    Room4 = dataframe[dataframe["Room"] == 4]  # Select a subclass of dataframe with all informations of Room4
    Room4 = Room4[Routers]  # Exclude the Room column
    mean4 = Room4.mean()

    conclusion1 = " Para a sala 1: De acordo com os dados apresentados, " \
                 "o roteador dois é o mais intenso pois apresenta a média maior do que os demais."

    conclusion2 = "Seguindo esta lógica os roteadores mais intensos nas salas 2,3 e 4 respectivamente são:" \
                  "Roteador 1, Roteador 1 e Roteador 2"

    return general_mean, mean1, mean2, mean3, mean4

def exercicio4():
    """
dataframe = pd.read_fwf(
    'data.txt', header=None,
    names=["Router1", "Router2", "Router3",
               "Router4", "Router5", "Router6", "Router7", "Room"]
)
 dataframe.boxplot(column=['Router7'], by='Room')
 plt.show()

plt.show()
    :return:
    """
    return

def exercicio5():
    dataframe = pd.read_fwf(
        'static/data.txt', header=None,
        names=["Router1", "Router2", "Router3",
               "Router4", "Router5", "Router6", "Router7", "Room"]
    )
    general_mean = dataframe.mean()

    Rooms = ["Router1", "Router2", "Router3", "Router4", "Router5", "Router6", "Router7"]
'''
Router1 = dataframe["Router1"]
Router2 = dataframe["Router2"]
Router3 = dataframe["Router3"]
Router4 = dataframe["Router4"]
Router5 = dataframe["Router5"]
Router6 = dataframe["Router6"]
Router7 = dataframe["Router7"]

norm1 = (Router1 - Router1.mean()) / Router1.std()
norm2 = (Router2 - Router2.mean()) / Router2.std()
norm3 = (Router3 - Router3.mean()) / Router3.std()
norm4 = (Router4 - Router4.mean()) / Router4.std()
norm5 = (Router5 - Router5.mean()) / Router5.std()
norm6 = (Router6 - Router6.mean()) / Router6.std()
norm7 = (Router7 - Router7.mean()) / Router7.std()

fig, axes = plt.subplots(nrows=2, ncols=1)
norm1.hist(ax=axes[0], density="True", cumulative="True",bins=10)
norm1.hist(ax=axes[1], density="True", range=(-5,5), bins=15)
plt.show()

fig, axes = plt.subplots(nrows=2, ncols=1)
norm2.hist(ax=axes[0], density="True", cumulative="True",bins=10)
norm2.hist(ax=axes[1], density="True", range=(-5,5), bins=15)
plt.show()

fig, axes = plt.subplots(nrows=2, ncols=1)
norm3.hist(ax=axes[0], density="True", cumulative="True",bins=10)
norm3.hist(ax=axes[1], density="True", range=(-5,5), bins=15)
plt.show()

fig, axes = plt.subplots(nrows=2, ncols=1)
norm4.hist(ax=axes[0], density="True", cumulative="True",bins=10)
norm4.hist(ax=axes[1], density="True", range=(-5,5), bins=15)
plt.show()

fig, axes = plt.subplots(nrows=2, ncols=1)
norm5.hist(ax=axes[0], density="True", cumulative="True",bins=10)
norm5.hist(ax=axes[1], density="True", range=(-5,5), bins=15)
plt.show()

fig, axes = plt.subplots(nrows=2, ncols=1)
norm6.hist(ax=axes[0], density="True", cumulative="True",bins=10)
norm6.hist(ax=axes[1], density="True", range=(-5,5), bins=15)
plt.show()

fig, axes = plt.subplots(nrows=2, ncols=1)
norm7.hist(ax=axes[0], density="True", cumulative="True",bins=10)
norm7.hist(ax=axes[1], density="True", range=(-5,5), bins=15)
plt.show()

Kolmogorov Smirnov test

_, p1  = kstest(norm1, 'norm')
_,p2 = ks_statistic, p_value = kstest(norm2, 'norm')
_,p3 = ks_statistic, p_value = kstest(norm3, 'norm')
_,p4 = ks_statistic, p_value = kstest(norm4, 'norm')
_,p5 = ks_statistic, p_value = kstest(norm5, 'norm')
_,p6 = ks_statistic, p_value = kstest(norm6, 'norm')
_,p7 = ks_statistic, p_value = kstest(norm7, 'norm')

    conclusion1 = " Para a sala 1: De acordo com os dados apresentados, " \
                 "o roteador dois é o mais intenso pois apresenta a média maior do que os demais."

    conclusion2 = "Seguindo esta lógica os roteadores mais intensos nas salas 2,3 e 4 respectivamente são:" \
                  "Roteador 1, Roteador 1 e Roteador 2"

    return general_mean, mean1, mean2, mean3, mean4
'''