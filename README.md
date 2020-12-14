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

Describe the steps taken to implement the classification.
<ol>
    <li>
        <b>Some main heading</b><br>
        Description
    </li>
    <li>...</li>
    <li>...</li>
    <li>...</li>
</ol>

---

### Results
Todo after the implementation part is compelete.
Confusion matrix, Accuracy, loss, etc.

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
