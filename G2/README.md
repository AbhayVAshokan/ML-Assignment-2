# ML Assignment 2

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AbhayVAshokan/ML-Assignment-2/blob/master/G2/mnist_cnn.ipynb) <br/>
This project can be easily setup and run by using Google Colaboratory. Colaboratory is a research tool for machine learning education and research. It’s a Jupyter notebook environment that requires no setup to use. Simply click on the badge to get started.


## MNIST digit classifier using Convolutional Neural Network


The MNIST dataset was constructed from two datasets of the US National Institute of Standards and Technology (NIST). The training set consists of handwritten digits from 250 different people, 50 percent high school students, and 50 percent employees from the Census Bureau. Note that the test set contains handwritten digits from different people following the same split.
It is a good database for people who want to try learning techniques and pattern recognition methods on real-world data while spending minimal efforts on pre processing and formatting.

> Source: <a href="http://yann.lecun.com/exdb/mnist/"> THE MNIST DATABASE</a>
---
The MNIST dataset is one of the most common datasets used for image classification and accessible from many different sources. In fact, even Tensorflow and Keras allow us to import and download the MNIST dataset directly from their API. Therefore, using the following two lines we can import TensorFlow and MNIST dataset under the Keras API.

### Convolutional Neural Network (ConvNet/CNN)

A **Convolutional Neural Network (ConvNet/CNN)** is a Deep Learning algorithm which can take in an input image, assign importance (learnable weights and biases) to various aspects/objects in the image and be able to differentiate one from the other. The pre-processing required in a ConvNet is much lower as compared to other classification algorithms. While in primitive methods filters are hand-engineered, with enough training, ConvNets have the ability to learn these filters/characteristics.


---

### Approach

<ol>
    <li><b>Splitting dataset</b><br>
        The dataset is split into 80% training set and 20% test set. In this example the keras library automatically fetches it for us and splits into training and testing sets.
    </li>
    <li><b>Preprocessing</b><br>
        The preprocessing steps involve expanding dimensions of the image array from 3 to 4 and normalizing the values. Detailed explainations are provide in the python notebook.
    </li>
    <li><b>Defining the model</b><br>
        Defining the structure of the model. The model is constructed by using high-level Keras API which uses either TensorFlow or Theano on the backend. We are importing the Sequential Model from Keras and add Conv2D, MaxPooling, Flatten, Dropout, and Dense layers.
    </li>
    <li><b>Fitting the model</b><br>
        Compile and fit the model that we defined in earlier step.
    </li>
    <li><b>Predicting outputs</b><br>
        The model is used to predict the outputs on the test dataset.
    </li>
    <li><b>Displaying the results</b><br>
        The validation results are displayed : The loss and accuracy of the model.
    </li>
</ol>

---

### Results
<ol>
    <li><b>Loss of Model</b><br>
        The Loss Function is one of the important components of Neural Networks. Loss is nothing but a prediction error of Neural Net. And the method to calculate the loss is called Loss Function. In simple words, the Loss is used to calculate the gradients.
    </li>
    <li><b>Accuracy of Model</b><br>
        It is the ratio of number of correct predictions to the total number of input samples.
    </li>
    
</ol>

---

### Setup

#### Open `mnist_cnn.ipynb` in Google colab
Colaboratory is a research tool for machine learning education and research. It’s a Jupyter notebook environment that requires no setup to use. Click on the following badge to open.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AbhayVAshokan/ML-Assignment-2/blob/master/G2/mnist_cnn.ipynb) <br/>