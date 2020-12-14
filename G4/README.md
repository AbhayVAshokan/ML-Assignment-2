# ML assignment 2
## Abalone age classification using K Nearest Neighbours
Predicting the age of abalone from physical measurements. The age of abalone is determined by cutting the shell through the cone, staining it, and counting the number of rings through a microscope - a boring and time-consuming task. Other measurements, which are easier to obtain, are used to predict the age.
### Attributes
Given is the attribute name, attribute type, the measurement unit and a brief description. The number of rings is the value to predict: either as a continuous value or as a classification problem.

Name / Data Type / Measurement Unit / Description

---
Sex - nominal - NIL - M, F, and I (infant)

Length - continuous - mm - Longest shell measurement

Diameter - continuous - mm - perpendicular to length

Height - continuous - mm - with meat in shell

Whole weight - continuous - grams - whole abalone

Shucked weight - continuous - grams - weight of meat

Viscera weight - continuous - grams - gut weight (after bleeding)

Shell weight - continuous - grams - after being dried

Rings - integer - NIL - +1.5 gives the age in years

---

## K Nearest Neighbours

K-nearest neighbors (KNN) algorithm uses ‘feature similarity’ to predict the values of new datapoints which further means that the new data point will be assigned a value based on how closely it matches the points in the training set.

Step 1 − For implementing any algorithm, we need dataset. So during the first step of KNN, we must load the training as well as test data.

Step 2 − Next, we need to choose the value of K i.e. the nearest data points. K can be any integer.

Step 3 − For each point in the test data do the following −

  * 3.1 − Calculate the distance between test data and each row of training data with the help of any of the method namely: Euclidean, Manhattan or Hamming distance. The most commonly used method to calculate distance is Euclidean.

  * 3.2 − Now, based on the distance value, sort them in ascending order.

  * 3.3 − Next, it will choose the top K rows from the sorted array.

  * 3.4 − Now, it will assign a class to the test point based on most frequent class of these rows.

Step 4 − End

---

## Approach

<ol>
    <li><b>Splitting dataset</b><br>
        The dataset is split into 75% training set and 25% test set.
    </li>
    <li><b>Preprocessing</b><br>
        Label Encoder is used first. It converts the labels into numeric form. <br />  
        Standard Scaler is then used to normalize the values centred at 0.
    </li>
    <li><b>Fitting the model</b><br>
        The K Nearest Neighbours model is fit using the training dataset.
    </li>
    <li><b>Predicting outputs</b><br>
        The model is used to predict the outputs on the test dataset.
    </li>
    <li><b>Displaying the results</b><br>
        The confusion matrix, precision, recall and f1-score are then displayed
    </li>
</ol>

## Setup

Install sklearn, pandas and numpy

Run knn.py
