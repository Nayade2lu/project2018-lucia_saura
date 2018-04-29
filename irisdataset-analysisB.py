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


