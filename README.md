# Project 2018 Lucia Saura
# Programming and Scripting 

![](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Machine+Learning+R/iris-machinelearning.png)

# IRIS DATASET

## Plan: 

1.  _General Research_

2.  _Iris Dataset Projects research_ 

3.  _Ideas of what problem we want to solve_

4.  _Viability of solving in code_

5.  _Code plan_ 

  * Iris data set investigation (Python) 

    1. Need section of code 1: Numpy library

    2. Need section of code 2: Import the data from the dataset

    3. Need section of code 3: Select the data from 1 column

    

  * Iris data set obtention of results (Python code) 
  
    1. Get the mean using numpy

    2. Print function 
    
  * Optimization of the code

6. _Analysis of results_

7. _Conclusion_


#### General Research 

- First approach: Looking for other projects and general info 

References:
https://archive.ics.uci.edu/ml/datasets/iris  

- Difference between petal and sepal 

   Sepal: Sepals are leaf-like parts that enclose the flower bud 

   Petal: Petals are modified leaves that surround the reproductive parts of flowers 

   References:
   https://www.hunker.com/13426267/what-is-the-difference-between-sepals-petals 

   https://en.wikipedia.org/wiki/Petal 

###### General Research about the data set
   Initial investigation by Fisher

   Fisher,R.A. "The use of multiple measurements in taxonomic problems" Annual Eugenics, 7, Part II, 179-188 (1936); also in      "Contributions to Mathematical Statistics" (John Wiley, NY, 1950).  

   http://rcs.chemometrics.ru/Tutorials/classification/Fisher.pdf 

   (complex to understand the formulas and calculations)
   First approach in the paper presents the idea of a function that will maximize the difference between the means of the        standard deviations between the two species compared Iris setosa and Iris versicolor (Iris virginica is not taken into        account in this first approach due to be colleted in a different colony)
   The investigation continues with the calculation of the sums of the squares and products of deviations from the means.        Fisher contemplates as well the degrees of freedom.
   
   Complex math and tables in getting the distribution of the data in the frequency histogram 
   
   The conclusion that reaches Fisher in his paper is that there is overlap in the I. virginica and I. versicolor so the          diagnosis of this two species cannot be based solely on these four mesurements (eventough these mesurements can lead to a      more complete discrimination)  while I. setosa presents a very diferentiated representation in the frequency histogram. 
   
   
   
     CONTEXT
     - What is a taxonomic problem?
     Taxonomy is the science of naming, describing and classifying organisms and includes all plants, animals and                  microorganisms of the world.

     Reference: https://www.cbd.int/gti/taxonomy.shtml  
     
     - Degrees of Freedom
     Statistics: The number of independent values or quantities which can be assigned to a statistical distribution
     Reference: Google Dictionary
     
     - Frequency histogram
     A frequency distribution table is a table that shows how often a data point or a group of data points appears in a given      data set. To make a frequency distribution table, first divide the numbers over which the data ranges into intervals of        equal length. Then count how many data points fall into each interval.
     
     References: https://statistics.laerd.com/statistical-guides/understanding-histograms.php
     http://www.sparknotes.com/math/algebra1/graphingdata/section2/
     
    
#### Iris data set projects research

Patrick S. Hoey "Statistical Analysis of the Iris Flower Dataset" University of Massachusetts At Lowell

http://patrickhoey.com/downloads/Computer_Science/03_Patrick_Hoey_Data_Visualization_Dataset_paper.pdf

In the papper Patrick S. Hoey analyses briefly Fisher's work and describes how to discriminate data to identify the different type of Iris flowers.
The goal of his disciminant analysis is to produce a simple function that, given the four measurements, will
classify a flower correctly.
Hoey makes use of Graphical plots in the form of scatterplot graphs and works with the data to obtain 
- A scatterplot graph that compares the sepal length with the classification of flower.
- Another scatterplot graph that compares the sepal width with the classification of flower.
- A scatterplot graph that compares the petal length with the classification of flower. 
- And a scatterplot graph that compares the petal width with the classification of flower.
From these four scatterplots Hoey determines a pattern and creates a possible predictor.

Second part of Holey papper: Java application to analyze the data
The functions find the mean, mode, median, range, variance, standard deviation, minimum value and maximum values.

       CONTEXT
       - Scatter plots: Scatter plots are similar to line graphs. Scatter plots show how much one variable is affected by            another. The relationship between two variables is called their correlation . The closer the data points come when            plotted to making a straight line, the higher the correlation between the two variables, or the stronger the                  relationship.
       References: http://mste.illinois.edu/courses/ci330ms/youtsey/scatterinfo.html
 
 #### Machine learning project
 Jason Brownlee on June 10, 2016
 https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
 
 This project guides trough a series of steps on building a simple Machine Learning project using Python.
 The post covers the basic steps to accomplish the task and introduces stepby step the code that will accomplish the machine    learning project.
 Recommendation of installing SciPy platform and libraries
   
   _Main steps in the project:_
    
   - Loading The Data
      - Importing libraries
      - Loading Dataset
    
   - Summarizing the Dataset
      - Dimensions of Dataset
      - Peek at the Data
      - Statistical Summary
      - Class Distribution
   
   - Data Visualization
      - Univariate Plots
      - Multivariate Plots
    
   - Evaluation of some Algorithms
      - Creating a Validation Dataset
      - Test Harness
      - Build Models
      - Select Best Model
    
   - Making Predictions
   
 ### Linear discriminant model to classify the species:
 Rafael Santos
 http://www.lac.inpe.br/~rafael.santos/Docs/R/CAP394/WholeStory-Iris.html
 
 Library: datasets
 Models
 Summary function
 Boxplot
 Histogram
 Violin plots
 Correlations between Variables
 Scatterplot matrices
 
 Library: MASS
 Parallel coordinate plot
 
 Library: C50
 Decission Trees
 
       
 #### More projects reviewed
 Graphical plot project:
 http://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html
 
 Visualizations:
 https://www.kaggle.com/benhamner/python-data-visualizations
 
 
 ## Ideas of what problem we want to solve
 Idea 1: Obtain the minimum and maximum of each flower of each column
 Idea 2: Obtain the mean of each parameter of each flower independently to categorise the flowers attending to that
 Idea 3: Graphics to see tendences
 Idea 4: Machine learning project
 
 #### Selected idea for the project: Obtain the mean of each parameter of each flower 
Attending to the Iris data set, the outcome of this Python program is to find the mean of each column of each flower. The goal is to identify if the difference is relevant to help in clasifying the flowers based on the mean of each column.

Altough might not be related with the main goal of the project. I would try to integrate also some graphics to experiment with with matplotlib and pyplot.
 
## Viavility
The probability of achieving the project with Python is high due to the resources in the course, specially Topic 8: Calculating with numpy.

## Code plan

 ### Iris data set investigation (Python) 

   1. Need section of code 1: Numpy library

   2. Need section of code 2: Import the data from the dataset

   3. Need section of code 3: Select the data from 1 column


##### Numpy Library


Steps to solve Iris data set project:
1. Reasearch and copy the Iris data set
2. Create a csv with the data
3. Divide the data attending to the different type of flowers (removing the data from the other flowers)
4. Import numpy
5. read the first flower data set into array (Setosa)
6. Obtain the data from the first column: Setosa sepal length
7. Calculte the mean 
8. Print the rsults

8. Repeat the previous steps with second column of the data: Setosa sepal width
9. Repeat the previous steps with third column of the data: Setosa petal length
10. Repeat the previous steps with fourth column: Setosa spetal width

11. Repeat all the previous steps for Versicolor
12. Repeat all the previus steps for Virginica

 *initiate ipython and try the commands in the terminal first, then copy the code into the python file


#### Results from the data analysis of the mean of each column

##### Code to obtain the results
  1. Get the mean using numpy

  2. Print function 
  
##### Optimization of the code
- Removed duplications importing the numpy library
- Removed duplications reading files into array
Approximately 20 lines of code removed

##### Results

Setosa sepal length mean: 5.006
Setosa sepal width: 3.418
Setosa petal length: 1.464
Setosa petal width: 0.244

Versicolor sepal length mean: 5.936
Versicolor sepal width: 2.77
Versicolor petal length: 4.26
Versicolor petal width: 1.326

Virginica sepal length mean: 6.588
Virginica sepal width: 2.974
Virginica petal length: 5.552
Virginica petal width: 2.026

##### Graphics to see tendences
Histograms from the 3 parametersof the three flowers
Setosa sepal length
![](https://github.com/Nayade2lu/project2018-lucia_saura/blob/master/Setosa-sep-length-hist.png)
Versicolor sepal length
![](https://github.com/Nayade2lu/project2018-lucia_saura/blob/master/Versicolor-sep-length-hist.png)
Virginica sepal length
![](https://github.com/Nayade2lu/project2018-lucia_saura/blob/master/Virginica-sep-lenght-hist.png)


## Analysis of results

From this results we can extract that setosa could be the variety with more diferentiate parameters specially on the petal length and width. The petal width and length results could be used as an orientative number to categorize the Iris setosa.

Versicolor and Virginica have similar mean for the sepal width. Except from the width, the Iris Virginica is higher in sepal length, petl length and petal width. These three measurements could help to diferentiate Virginica from Versicolor.

## Conclusion
Despite the previous analysis, the mean should be taken as an orientative parameter not as an absolute one in order to categorise the three varieties.

The Iris data set can receive multiple treatments to show models, tendences or predictabilities. The mean approach is a basic study of the data set using Python code.




More references:
Histograms:
https://www.mathworks.com/help/matlab/ref/matlab.graphics.chart.primitive.histogram.html;jsessionid=ff05bc250d1a965089cfe3ac40b2


Notes: 
1. Attempt to use library Datasets failed
   Error:
   ModuleNotFoundError: No module named 'datasets'


 
 
      
      
 



