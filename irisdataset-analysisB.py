#Lucia Saura 28/04/2018
# approach matplotlib histogram

#Sepal length-------
import numpy
#Read setosa data file into array
data = numpy.genfromtxt('iris-data-set-setosa.csv', delimiter=',')
# show data from sepal length setosa
firstcol = data[:,0]
#import the library matplot
import matplotlib.pyplot as pl
#create a histogram of sepal lenght setosa
pl.hist(firstcol)
#showing the histogram
pl.show()


#Read virginica data file into array
data = numpy.genfromtxt('iris-data-set-virginica.csv', delimiter=',')
# show data from sepal length virginica
firstcol = data[:,0]

import matplotlib.pyplot as pl
pl.hist(firstcol)
pl.show()


#Read versicolor data file into array
data = numpy.genfromtxt('iris-data-set-versicolor.csv', delimiter=',')
# show data from sepal length versicolor
firstcol = data[:,0]

import matplotlib.pyplot as pl
pl.hist(firstcol)
pl.show()



#Sepal width------------------

#Read setosa data file into array
data = numpy.genfromtxt('iris-data-set-setosa.csv', delimiter=',')
# show data from sepal width setosa
seccol = data[:,1]
#import the library matplot
import matplotlib.pyplot as pl
#create a histogram of sepal width setosa
pl.hist(seccol)
#showing the histogram
pl.show()


#Read virginica data file into array
data = numpy.genfromtxt('iris-data-set-virginica.csv', delimiter=',')
# show data from sepal width virginica
seccol = data[:,1]

import matplotlib.pyplot as pl
pl.hist(seccol)
pl.show()


#Read versicolor data file into array
data = numpy.genfromtxt('iris-data-set-versicolor.csv', delimiter=',')
# show data from sepal width versicolor
seccol = data[:,1]

import matplotlib.pyplot as pl
pl.hist(seccol)
pl.show()

#Petal length------------------

#Read setosa data file into array
data = numpy.genfromtxt('iris-data-set-setosa.csv', delimiter=',')
# show data from petal length setosa
thirdcol = data[:,2]
#import the library matplot
import matplotlib.pyplot as pl
#create a histogram of petal lenght setosa
pl.hist(thirdcol)
#showing the histogram
pl.show()


#Read virginica data file into array
data = numpy.genfromtxt('iris-data-set-virginica.csv', delimiter=',')
# show data from petal length virginica
thirdcol = data[:,2]

import matplotlib.pyplot as pl
pl.hist(thirdcol)
pl.show()


#Read versicolor data file into array
data = numpy.genfromtxt('iris-data-set-versicolor.csv', delimiter=',')
# show data from sepal length versicolor
thirdcol = data[:,2]

import matplotlib.pyplot as pl
pl.hist(thirdcol)
pl.show()


#Petal width------------------

#Read setosa data file into array
data = numpy.genfromtxt('iris-data-set-setosa.csv', delimiter=',')
# show data from petal width setosa
foucolm = data[:,3]
#import the library matplot
import matplotlib.pyplot as pl
#create a histogram of petal width setosa
pl.hist(foucolm)
#showing the histogram
pl.show()


#Read virginica data file into array
data = numpy.genfromtxt('iris-data-set-virginica.csv', delimiter=',')
# show data from petal width virginica
foucolm = data[:,3]

import matplotlib.pyplot as pl
pl.hist(foucolm)
pl.show()


#Read versicolor data file into array
data = numpy.genfromtxt('iris-data-set-versicolor.csv', delimiter=',')
# show data from petal width versicolor
foucolm = data[:,3]

import matplotlib.pyplot as pl
pl.hist(foucolm)
pl.show()


