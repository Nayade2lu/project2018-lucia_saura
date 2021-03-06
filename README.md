# Project 2018 Lucia Saura
# Programming and Scripting 

![](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Machine+Learning+R/iris-machinelearning.png)

# IRIS DATASET
Items in the repository:
 - README: Research, analysis and documentation (current file)
 - irisdataset-analysis.py: Python file to calculate the mean of each parameter of each specie
 - irisdataset-analysisB.py : Python file to obtain histograms
 - png files: histograms images to link in the current README

# Plan: 

1.  _General Research_

2.  _Iris Dataset Projects research_ 

3.  _Ideas on the problem to solve_

4.  _Viability of solving in code_

5.  _Code plan_ 

  * Iris data set analysis (Python) 

    1. Need section of code 1: Numpy library

    2. Need section of code 2: Import the data from the dataset

    3. Need section of code 3: Select the data from 1 column

    

  * Iris data set obtention of results (Python code) 
  
    1. Get the mean using numpy

    2. Print function 
    
  * Optimization of the code

6. _Analysis of results_

7. _Conclusion_


## General Research 

- First approach: Looking for other projects and general info 

References:
https://archive.ics.uci.edu/ml/datasets/iris  

- Difference between petal and sepal 

      Sepal: Sepals are leaf-like parts that enclose the flower bud 

      Petal: Petals are modified leaves that surround the reproductive parts of flowers 

      References:
      https://www.hunker.com/13426267/what-is-the-difference-between-sepals-petals 

      https://en.wikipedia.org/wiki/Petal 

### General Research about the data set
   Initial investigation by Fisher

   Fisher,R.A. "The use of multiple measurements in taxonomic problems" Annual Eugenics, 7, Part II, 179-188 (1936); also in      "Contributions to Mathematical Statistics" (John Wiley, NY, 1950).  

   http://rcs.chemometrics.ru/Tutorials/classification/Fisher.pdf 

   (complex to understand the formulas and calculations)
   
   First approach in the paper presents the idea of a function that will maximize the difference between the means of the        standard deviations between the two species compared Iris setosa and Iris versicolor (Iris virginica is not taken into        account in this first approach due to be collected in a different colony).
   
   The investigation continues with the calculation of the sums of the squares and products of deviations from the means.        Fisher contemplates as well the degrees of freedom.
   
   The paper shows as well, complex math and tables to get the distribution of the data in the frequency histograms. 
   
   The conclusion that reaches Fisher in his paper is that there is overlap in the I. virginica and I. versicolor so the          diagnosis of this two species cannot be based solely on these four measurements (even though these measurements can lead to    a more complete discrimination)  while I. setosa presents a very differentiated representation in the frequency histogram. 
   
   
   
     CONTEXT
     - What is a taxonomic problem?
     Taxonomy is the science of naming, describing and classifying organisms and includes all plants,animals and microorganisms of the world.

     Reference: https://www.cbd.int/gti/taxonomy.shtml  
     
     - Degrees of Freedom
     Statistics: The number of independent values or quantities which can be assigned to a statistical distribution
     Reference: Google Dictionary
     
     - Frequency histogram
     A frequency distribution table is a table that shows how often a data point or a group of data points appears in a given data set. To make a frequency distribution table, first divide the numbers over which the data ranges into intervals of        equal length. Then count how many data points fall into each interval.
     
     References: https://statistics.laerd.com/statistical-guides/understanding-histograms.php
     http://www.sparknotes.com/math/algebra1/graphingdata/section2/
     
    
## Iris data set projects research

Patrick S. Hoey "Statistical Analysis of the Iris Flower Dataset" University of Massachusetts At Lowell

http://patrickhoey.com/downloads/Computer_Science/03_Patrick_Hoey_Data_Visualization_Dataset_paper.pdf

In the paper Patrick S. Hoey analyses briefly Fisher's work and describes how to discriminate data to identify the different type of Iris flowers.
The goal of his discriminant analysis is to produce a simple function that, given the four measurements, will
classify a flower correctly.
Hoey makes use of Graphical plots in the form of scatterplot graphs and works with the data to obtain 
- A scatterplot graph that compares the sepal length with the classification of flower.
- Another scatterplot graph that compares the sepal width with the classification of flower.
- A scatterplot graph that compares the petal length with the classification of flower. 
- And a scatterplot graph that compares the petal width with the classification of flower.

From these four scatterplots Hoey determines a pattern and creates a possible predictor.

Second part of Holey paper: Java application to analyze the data

The functions find the mean, mode, median, range, variance, standard deviation, minimum value and maximum values.

       CONTEXT
       - Scatter plots: Scatter plots are similar to line graphs. Scatter plots show how much one variable is affected by  another. The relationship between two variables is called their correlation . The closer the data points come when            plotted to making a straight line, the higher the correlation between the two variables, or the stronger the                  relationship.
    References: http://mste.illinois.edu/courses/ci330ms/youtsey/scatterinfo.html
 
 #### Machine learning project
 Jason Brownlee on June 10, 2016
 https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
 
 This project guides through a series of steps on building a simple Machine Learning project using Python.
 The post covers the basic steps to accomplish the task and introduces step by step the code that will accomplish the machine   learning project.
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
   
 #### Linear discriminant model to classify the species:
 Rafael Santos
 http://www.lac.inpe.br/~rafael.santos/Docs/R/CAP394/WholeStory-Iris.html
 
 - Library: datasets
 - Models
 - Summary function
 - Boxplot
 - Histogram
 - Violin plots
 - Correlations between Variables
 - Scatterplot matrices
 
 - Library: MASS
 - Parallel coordinate plot
 
 - Library: C50
 - Decision Trees
 
       
 #### More projects reviewed
 Graphical plot project:
 http://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html
 
 Visualizations:
 https://www.kaggle.com/benhamner/python-data-visualizations
 
 Machine learning:
 https://www.kaggle.com/jchen2186/machine-learning-with-iris-dataset
 
 
 
 ## Ideas on the problem to solve
 Idea 1: Obtain the minimum and maximum of each flower of each column
 
 Idea 2: Obtain the mean of each parameter of each flower independently to categorise the flowers
 
 Idea 3: Graphics to see tendences
 
 Idea 4: Machine learning project
 
 #### Selected idea for the project: Obtain the mean of each parameter of each flower and graphics to see tendences
Attending to the Iris data set, the outcome of this Python program is to find the mean of each column of each flower. The goal is to identify if the difference is relevant to help in classifying the flowers based on the mean of each column.

Although might not be related with the main goal of the project. I would try to integrate also some graphics to experiment with with matplotlib and pyplot.
 
## Viability
The probability of achieving the project with Python is high due to the resources in the course, specially Topic 8: Calculating with numpy and matplotlib.

## Code plan

 ### Iris data set analysis (Python) 

   1. Need section of code 1: First, import Numpy library

   2. Need section of code 2: Secondly, import the data from the dataset (getfromtxt function)

   3. Need section of code 3: Third, select the data from 1 column


#### Steps to solve Iris data set project:
1. Research and copy the Iris data set
2. Create a csv with the data
3. Keep only the data of aspecie (removing the data from the other flowers in the csv)
4. Import numpy
5. read the first flower data set into array (Setosa)
6. Obtain the data from the first column: Setosa sepal length
7. Calculate the mean 
8. Print the rsults

8. Repeat the previous steps with second column of the data: Setosa sepal width
9. Repeat the previous steps with third column of the data: Setosa petal length
10. Repeat the previous steps with fourth column: Setosa petal width

11. Repeat all the previous steps for Versicolor
12. Repeat all the previous steps for Virginica

 *initiate ipython and try the commands in the terminal first, then copy the code into the python file


#### Code to obtain the results

  1. Get the mean using numpy with the function numpy.mean

  2. Print function 
  
#### Optimization of the code
- Removed duplications importing the numpy library
- Removed duplications reading files into array

Approximately 20 lines of code removed

#### Results

- Setosa sepal length mean: 5.006
- Setosa sepal width: 3.418
- Setosa petal length: 1.464
- Setosa petal width: 0.244


- Versicolor sepal length mean: 5.936
- Versicolor sepal width: 2.77
- Versicolor petal length: 4.26
- Versicolor petal width: 1.326


- Virginica sepal length mean: 6.588
- Virginica sepal width: 2.974
- Virginica petal length: 5.552
- Virginica petal width: 2.026


## Analysis of results
### Mean
From these results setosa is be the variety with more differentiate parameters specially on the petal length and width. The petal width and length mean results can be used, as orientative numbers, to categorize the Iris setosa.

Versicolor and Virginica have similar mean for the sepal width. The Iris virginica has higher values in sepal length, petal length and petal width. These three measurements could help to differentiate virginica from versicolor.

### Graphics to see tendences
Histograms: Sepal and petal length, sepal and petal width

Setosa sepal length        |  Versicolor sepal length  |  Virginica sepal length
:-------------------------:|:-------------------------:|:-------------------------:
![Setosa sepal length](https://github.com/Nayade2lu/project2018-lucia_saura/blob/master/Setosa-sep-length-hist.png)  |  ![Versicolor sepal length](https://github.com/Nayade2lu/project2018-lucia_saura/blob/master/Versicolor-sep-length-hist.png)|  ![Virginica sepal length](https://github.com/Nayade2lu/project2018-lucia_saura/blob/master/Virginica-sep-lenght-hist.png)

As we can observe from the graphics, in terms of the sepal length the vast majrity of setosa samples are in a range between 4,6 and 5,5 cm while Versicolor and Virginica are between 5,3 and 7,3. This differentiation can be a key factor to clasificate the Iris setosa.

Setosa sepal width       |  Versicolor sepal width  |  Virginica sepal width
:-------------------------:|:-------------------------:|:-------------------------:
![Setosa sepal width](https://github.com/Nayade2lu/project2018-lucia_saura/blob/master/Setosa-sep-width-hist.png)  |  ![Versicolor sepal width](https://github.com/Nayade2lu/project2018-lucia_saura/blob/master/Versicolor-sep-width-hist.png)|  ![Virginica sepal width](https://github.com/Nayade2lu/project2018-lucia_saura/blob/master/Virginica-sep-width-hist.png)

In terms of sepal width, the three varieties are in a very similar range. The division of the flowers attending to this parameter would be highly difficult.

Setosa petal length        |  Versicolor petal length  |  Virginica petal length
:-------------------------:|:-------------------------:|:-------------------------:
![Setosa petal length](https://github.com/Nayade2lu/project2018-lucia_saura/blob/master/Setosa-pet-length.png)  |  ![Versicolor petal length](https://github.com/Nayade2lu/project2018-lucia_saura/blob/master/Versicolor-pet-length-hist.png)|  ![Virginica petal length](https://github.com/Nayade2lu/project2018-lucia_saura/blob/master/Virginica-pet-length-hist.png)

Regarding the petal length, setosa has again the lowest numbers comprised between 1 and 1,9 cm. Most of versicolor samples are between 3,8 and 5. while most of virginica ones starts around 4,7 to 6,3. 
Thanks to the histograms a relevant difference can be appreciated between the three species. This difference in the petal length could help in the categorization of the Iris varieties.

Setosa petal width        |  Versicolor petal width  |  Virginica petal width
:-------------------------:|:-------------------------:|:-------------------------:
![Setosa petal length](https://github.com/Nayade2lu/project2018-lucia_saura/blob/master/Setosa-pet-width-hist.png)  |  ![Versicolor petal length](https://github.com/Nayade2lu/project2018-lucia_saura/blob/master/Versicolor-pet-width-hist.png)|  ![Virginica petal length](https://github.com/Nayade2lu/project2018-lucia_saura/blob/master/Virginica-pet-width-hist.png)

From this last measurement, the petal width another important conclusion can be extracted, setosa is the smallest one with all values between 0,1 and 0,6, versicolor is the medium one with values between 1 and 1,8 and virginica is the bigger one with most of the values between 1,7 and 2,5.

## Conclusion
To conclude the analysis, from the histograms and the mean a differentiation between at least two of the species can be made, specially because of the graphical representation on the histograms. 

From the mean analysis and the histograms, setosa would be the specie easier to categorise as it has very differentiative smaller petal length and width. Versiolor follows the scale attending to petal size, as it is the specie with medium values in both the petal length and width. And finally, virginica is the specie with bigger values for both petal length and width. 

The sepals are too similar in size, so it's much more relevant to take in consideration the petal measurements to identify the species.

To sum up, the petal width can be taken as a valuable reference to differentiate the species: a flower could be classified as setosa if the petal width is between 0,1 and 0,6 cm, versicolor between 1 and 1,8 and virginica between 1,7 and 2,5. 

If the number would be between 1,4 and 1,8 cm it could be questioned if the flower is virginica or versicolor as both have a lot of samples on that range. In that case, the petal width could help in the classification: 3,8 - 5 virginica; 4,7 - 6,3 versicolor. Still if petal width was between 4,5 and 5, the differentiation between this two species would be highly complex as the sepal results are very similar between both species and wouldn't help on the classification. 

The results from the current analysis show a correlation with Fisher study in concluding that even though these measurements can lead to a more complete discrimination, the diagnosis of versicolor and virginica would be higly difficult based solely on these four measurements, while setosa could be differentiated from the other two species with the four measuremnts taken.

## Code conclusion
Finally, as a code conclusion of the analysis, it has been extremely useful the numpy library and the matplotlib library. 

Numpy library because of the getfromtxt function that allows to extract a column of the data and matplotlib because of the histogram function that shows the data graphically organized in bins.

Highly valued also, the README style approach of inserting images into tables to align them in the same row.


### More references:
Histograms:https://www.mathworks.com/help/matlab/ref/matlab.graphics.chart.primitive.histogram.html;jsessionid=ff05bc250d1a965089cfe3ac40b2

Histograms color:
https://stackoverflow.com/questions/23061657/plot-histogram-with-colors-taken-from-colormap

Histograms color:
https://matplotlib.org/api/_as_gen/matplotlib.pyplot.hist.html#matplotlib.pyplot.hist

Attribute error:
https://github.com/matplotlib/matplotlib/issues/10147

Histogram color:
https://www.mathworks.com/help/matlab/ref/matlab.graphics.chart.primitive.histogram.html

Scatter plot: 
https://matplotlib.org/gallery/shapes_and_collections/scatter.html

Modules:
https://docs.python.org/3/tutorial/modules.html

Interactive mode:
https://stackoverflow.com/questions/39828744/visual-studio-code-interactive-python-console
https://en.wikibooks.org/wiki/Python_Programming/Interactive_mode

Clone a github repository in the computer:
http://lemoncode.net/lemoncode-blog/2017/12/12/git-y-visual-studio-code

SciPy:
https://www.scipy.org/


### Notes: 
1. Attempt to use library Datasets failed

   Error:
   
   ModuleNotFoundError: No module named 'datasets'
   
2. Attempt to customize color of the histograms failed

   Error: 
   
   AttributeError: 'NoneType' object has no attribute 'seq'


 
 
      
      
 



