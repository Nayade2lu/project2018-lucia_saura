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

    1. Need 1 code or function x 

    2. Need 2 code or function y 

    3. Need 3 code or function z 

    4. Need 4 /code or function w 

  * Iris data set results 

    1. Need of result 1 and code or function related 

    2. Need of result 2 and code or function related 

    3. Need of result 3 and code or function related 

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
       
 #### More projects reviewed
 Graphical plot project:
 http://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html
 



