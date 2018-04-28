#Lucia Saura 28/04/2018
# approach matplotlib histogram

import numpy
#Read setosa data file into array
data = numpy.genfromtxt('iris-data-set-setosa.csv', delimiter=',')

firstcol = data[:,0]

import matplotlib.pyplot as pl
pl.hist(firstcol)
pl.show()


#Read virginica data file into array
data = numpy.genfromtxt('iris-data-set-virginica.csv', delimiter=',')

firstcol = data[:,0]

import matplotlib.pyplot as pl
pl.hist(firstcol)
pl.show()


#Read versicolor data file into array
data = numpy.genfromtxt('iris-data-set-versicolor.csv', delimiter=',')

firstcol = data[:,0]

import matplotlib.pyplot as pl
pl.hist(firstcol)
pl.show()

