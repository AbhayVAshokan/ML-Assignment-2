# ML Assignment 2

---
## Mushroom Classification using Random Forest Classifier
> Safe to eat or deadly poison?

This dataset includes descriptions of hypothetical samples corresponding to 23 species of gilled mushrooms in the Agaricus and Lepiota Family Mushroom drawn from The Audubon Society Field Guide to North American Mushrooms (1981). Each species is identified as definitely edible, definitely poisonous, or of unknown edibility and not recommended. This latter class was combined with the poisonous one. The Guide clearly states that there is no simple rule for determining the edibility of a mushroom; no rule like "leaflets three, let it be'' for Poisonous Oak and Ivy.

    Time period: Donated to UCI ML 27 April 1987.

> Source: <a href="https://www.kaggle.com/uciml/mushroom-classification">Mushroom Classification: Kaggle</a>

---

### Random Forest

Random forests or random decision forests are an ensemble learning method for classification, regression and other tasks that operate by constructing a multitude of decision trees at training time and outputting the class that is the mode of the classes (classification) or mean/average prediction (regression) of the individual trees.
We can understand the working of Random Forest algorithm with the help of following steps −

Step 1 − First, start with the selection of random samples from a given dataset.

Step 2 − Next, this algorithm will construct a decision tree for every sample. Then it will get the prediction result from every decision tree.

Step 3 − In this step, voting will be performed for every predicted result.

Step 4 − At last, select the most voted prediction result as the final prediction result.

---

### About the dataset

This dataset includes descriptions of hypothetical samples corresponding to 23 species of gilled mushrooms in the Agaricus and Lepiota Family Mushroom drawn from The Audubon Society Field Guide to North American Mushrooms (1981). Each species is identified as definitely edible, definitely poisonous, or of unknown edibility and not recommended. This latter class was combined with the poisonous one. The Guide clearly states that there is no simple rule for determining the edibility of a mushroom; no rule like "leaflets three, let it be'' for Poisonous Oak and Ivy.
The objective of this classifier is to categorise the mushroom species into poisonous and non poisonous.

---

### Approach

<ol>
    <li><b>Splitting dataset</b><br>
        The dataset is split into 80% training set and 20% test set. The datasets are saved in csv format.
    </li>
    <li><b>Preprocessing</b><br>
        Label Encoder is used first. It converts the labels into numeric form. <br />  
        Standard Scaler is then used to normalize the values centred at 0.
    </li>
    <li><b>Fitting the model</b><br>
        The Random Forest Classifier model is fit using the training dataset.
    </li>
    <li><b>Predicting outputs</b><br>
        The model is used to predict the outputs on the test dataset.
    </li>
    <li><b>Displaying the results</b><br>
        The 50-fold cross validation results, confusion matrix and precision score are displayed.
    </li>
</ol>

---

### Results
<ol>
    <li><b>Cross validation</b><br>
        50-fold cross validation is performed, wherein the input data is split into 50 random mutually exclusive subsets. The model is first trained using all but one subset of the dataset and tested using the remaining subset. The next time, a new model is similarly trained using 49 subsets but the subset used for training would now be a new one. The process is performed 50 times till all the subsets are used once for testing and an average of the precision obtained each time is obtained as the result. The model achieves a average precision of 1 when 50-fold cross validation is performed.
    </li>
    <li><b>Confusion matrix</b><br>
        The confusion matrix gives us the number of true positives, false positives, true negatives and false negatives. The model correctly predicts all the data in the test set. 822 true positives and 803 true negatives are obtained and we get no false positives or false negatives.
    </li>
    <li><b>Precision</b><br>
        Precision of the model expresses the proportion of data points our model says is relevant which are actually relevant. The model has a precision of 1.
    </li>
</ol>

---

### Setup

1. Creating a virtual environment
```
python3 -m venv venv
source venv/bin/activate
```

2. Installing the dependencies
```
pip install -r requirements.txt
```
