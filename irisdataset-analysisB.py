#Lucia Saura 28/04/2018
# approach matplotlib histogram

import numpy
#Read setosa data file into array
data = numpy.genfromtxt('iris-data-set-setosa.csv', delimiter=',')
# show data from sepal length setosa
firstcol = data[:,3]
#import the library matplot
import matplotlib.pyplot as pl
#create a histogram of sepal lenght setosa
pl.hist(firstcol)
#showing the histogram
pl.show()


#Read virginica data file into array
data = numpy.genfromtxt('iris-data-set-virginica.csv', delimiter=',')
# show data from sepal length virginica
firstcol = data[:,3]

import matplotlib.pyplot as pl
pl.hist(firstcol)
pl.show()


#Read versicolor data file into array
data = numpy.genfromtxt('iris-data-set-versicolor.csv', delimiter=',')
# show data from sepal length versicolor
firstcol = data[:,2]

import matplotlib.pyplot as pl
pl.hist(firstcol)
pl.show()



