'''
vscode can only show one interactive window at a time. if multiple plots are rendered, only one will appear and
it must be closed before another one can be shown!
''' 

'''
installing libraries that aren't part of the basic python package:

1. go to terminal
2. run "pip install ___" or "pip3 install ___" (where ___ is the library)
'''

'''
lists
- store heterogenous data like an array
- same as arrays (which only store the same data type) in python in terms of syntax & usage
'''

list = ["name", 7, 0.6, True]
arr = [0, 5, 6, 24, 6]


'''
matplotlib library

- visualizes 2D data
- can be used in python scripts, shell, web application servers, or other GUI toolkits
- plots data, provides object-oriented APIs to integrate plots into applications
'''

#YOU CANNOT NAME THE PROGRAM "matplotlib.py" IT THROWS AN ERROR :(
from matplotlib import pyplot as plt

#data we will plot
x1 = [1, 3, 4, 5, 6, 7, 8, 9, 10]
y1 = [7, 4, 1, 2, 6, 8, 6, 3, 4]
x2 = [1, 2, 3, 5, 7, 8, 9, 11, 12]
y2 = [5, 6, 7, 1, 1, 1, 2, 3, 4]


'''
LINE GRAPH (connect points with a straight line)

plot(x, y)
'''

#add the data separately, but it gets put on the same plot
plt.plot(x1, y1, label="data set 1", linewidth=4) #label param = name of series for legend
plt.plot(x2, y2, label="data set 2", linewidth=4)

#extra stuff
plt.grid(True) #shows the grid in the background
plt.legend() #show the legend (why we have labels)

#show plot
plt.show()


'''
BAR GRAPH (bars to compare quantities)

bar(x, y)
'''

#add the data separately, but it gets put on the same plot
plt.bar(x1, y1, label="data set 1", linewidth=4)
plt.bar(x2, y2, label="data set 2", linewidth=4)

#extra stuff
plt.grid(True) #shows the grid in the background
plt.legend() #show the legend

#show plot
plt.show()


'''
SCATTER PLOT (individual points)

scatter(x, y)
'''

#add the data separately, but it gets put on the same plot
plt.scatter(x1, y1, label="data set 1")
plt.scatter(x2, y2, label="data set 2")

#extra stuff
plt.grid(True) #shows the grid in the background
plt.legend() #show the legend

#show plot
plt.show()

'''
HISTOGRAM (frequency of values)

hist(x, y, bins)
'''

numbins = 7

#add the data separately, but it gets put on the same plot
plt.hist(y1, label="data set 1", bins=numbins)
plt.hist(y2, label="data set 2", bins=numbins)

#extra stuff
plt.grid(True) #shows the grid in the background
plt.legend() #show the legend

#show plot
plt.show()