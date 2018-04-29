#Lucia Saura 28/04/2018
# approach matplotlib histogram
# Reference GMIT module programming and scripting: Topic 8 matplotlib

#Setosa--------------------------
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

seccol = data[:,1]
#create a histogram of sepal width setosa
pl.hist(seccol)
#showing the histogram
pl.show()

thirdcol = data[:,2]
#create a histogram of petal lenght setosa
pl.hist(thirdcol)
#showing the histogram
pl.show()

foucolm = data[:,3]
#create a histogram of petal width setosa
pl.hist(foucolm)
#showing the histogram
pl.show()



#Virginica---------------------
#Virginica data file into array
data = numpy.genfromtxt('iris-data-set-virginica.csv', delimiter=',')
# show data from sepal length virginica
firstcol = data[:,0]
import matplotlib.pyplot as pl
pl.hist(firstcol)
pl.show()

seccol = data[:,1]
#create a histogram of sepal width virginica
pl.hist(seccol)
#showing the histogram
pl.show()

thirdcol = data[:,2]
#create a histogram of petal lenght virginica
pl.hist(thirdcol)
#showing the histogram
pl.show()

foucolm = data[:,3]
#create a histogram of petal width virginica
pl.hist(foucolm)
#showing the histogram
pl.show()



#Versicolor--------------------------
#Read versicolor data file into array
data = numpy.genfromtxt('iris-data-set-versicolor.csv', delimiter=',')
# show data from sepal length versicolor
firstcol = data[:,0]

import matplotlib.pyplot as pl
pl.hist(firstcol)
pl.show()

seccol = data[:,1]
#create a histogram of sepal width versicolor
pl.hist(seccol)
#showing the histogram
pl.show()

thirdcol = data[:,2]
#create a histogram of petal lenght versicolor
pl.hist(thirdcol)
#showing the histogram
pl.show()

foucolm = data[:,3]
#create a histogram of petal width versicolor
pl.hist(foucolm)
#showing the histogram
pl.show()



