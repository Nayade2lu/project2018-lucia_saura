#Lucia Saura 26/04/2018
#Iris Data set analysis https://archive.ics.uci.edu/ml/datasets/iris
#Project Programming and Scripting module

#Calculate the mean of each Setosa parameter

#Calculate Setosa sepal length mean
#Improting the numpy library
import numpy
#Read setosa data file into array
data = numpy.genfromtxt('iris-data-set-setosa.csv', delimiter=',')
#selecting the first column of the data
sepallenghtsetosa = data[:,0]
#calculating the mean of the first column
meansepallengthsetosa = numpy.mean(data[:,0])
#Code tested working in iPhyton
print("Setosa sepal length mean:", meansepallengthsetosa)

#Calculate Setosa sepal width mean
#selecting the second column of the data
sepalwidthtsetosa = data[:,1]
#calculating the mean of the second column
meansepalwidthsetosa = numpy.mean(data[:,1])
print("Setosa sepal width:", meansepalwidthsetosa)

#Calculate Setosa petal length mean
#selecting the third column of the data
petallengthtsetosa = data[:,2]
#calculating the mean of the third column
meanpetallengthsetosa = numpy.mean(data[:,2])
print("Setosa petal length:", meanpetallengthsetosa)

#Calculate Setosa petal width mean
#selecting the fourth column of the data
petalwidthtsetosa = data[:,3]
#calculating the mean of the fourth column
meanpetalwidthtsetosa = numpy.mean(data[:,3])
print("Setosa petal width:", meanpetalwidthtsetosa)


#--------------------Calculate the mean of each Versicolor parameter-----------------

#Calculate Versicolor sepal length mean

data = numpy.genfromtxt('iris-data-set-versicolor.csv', delimiter=',')
#selecting the first column of the data
sepallenghtversicolor = data[:,0]
#calculating the mean of the first column
meansepallengthversicolor = numpy.mean(data[:,0])
print("Versicolor sepal length mean:", meansepallengthversicolor)

#Calculate Versicolor sepal width mean
#selecting the second column of the data
sepalwidthtversicolor = data[:,1]
#calculating the mean of the second column
meansepalwidthversicolor = numpy.mean(data[:,1])
print("Versicolor sepal width:", meansepalwidthversicolor)

#Calculate Versicolor petal length mean
#selecting the third column of the data
petallengthtversicolor = data[:,2]
#calculating the mean of the third column
meanpetallengthversicolor = numpy.mean(data[:,2])
print("Versicolor petal length:", meanpetallengthversicolor)

#Calculate Versicolor petal width mean
#selecting the fourth column of the data
petalwidthtversicolor = data[:,3]
#calculating the mean of the fourth column
meanpetalwidthtversicolor = numpy.mean(data[:,3])
print("Versicolor petal width:", meanpetalwidthtversicolor)



#--------------------Calculate the mean of each Virginica parameter-----------------

#Calculate Virginica sepal length mean

data = numpy.genfromtxt('iris-data-set-virginica.csv', delimiter=',')
#selecting the first column of the data
sepallenvirginica = data[:,0]
#calculating the mean of the first column
meansepallenvirginica = numpy.mean(data[:,0])
print("Virginica sepal length mean:", meansepallenvirginica)

#Calculate Virginica sepal width mean
#selecting the second column of the data
sepalwidthtvirginica = data[:,1]
#calculating the mean of the second column
meansepalwidthvirginica = numpy.mean(data[:,1])
print("Virginica sepal width:", meansepalwidthvirginica)

#Calculate Virginica petal length mean
#selecting the third column of the data
petallengthtvirginica = data[:,2]
#calculating the mean of the third column
meanpetallengthvirginica = numpy.mean(data[:,2])
print("Virginica petal length:", meanpetallengthvirginica)

#Calculate Virginica petal width mean
#selecting the fourth column of the data
petalwidthtvirginica = data[:,3]
#calculating the mean of the fourth column
meanpetalwidthtvirginica = numpy.mean(data[:,3])
print("Virginica petal width:", meanpetalwidthtvirginica)






