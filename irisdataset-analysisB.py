#Lucia Saura
#Based on code from https://stackoverflow.com/questions/23061657/plot-histogram-with-colors-taken-from-colormap



import numpy
import matplotlib as pl
pl.hist(foucolm)
#Read versicolor data file into array
data = numpy.genfromtxt('iris-data-set-versicolor.csv', delimiter=',')
# show data from petal width versicolor
foucolm = data[:,3]

# This is  the colormap I'd like to use.
cm = pl.cm.get_cmap('RdYlBu_r')

# Plot histogram.
n, bins, patches = pl.hist(data, 25, normed=1, color='green')
bin_centers = 0.5 * (bins[:-1] + bins[1:])

# scale values to interval [0,1]
foucolm = bin_centers - min(bin_centers)
foucolm /= max(foucolm)

for c, p in zip(foucolm, patches):
    pl.setp(p, 'facecolor', cm(c))

pl.show()


