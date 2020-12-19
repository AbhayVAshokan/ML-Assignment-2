# MACHINE LEARNING ASSIGNMENT 2 
## BITCOIN PRICE PREDICTOR


**Aim** : To create a machine learning model that can predict the bitcoin price in future.<br/>


**Requirements** : <br/> 
*1.Dataset* - BTC-USD.csv - Historical prices for BTC-USD stock on Yahoo Finance. It consists of daily, weekly or monthly format back to when Bitcoin USD stock was issued.For this particular application we  have used the dataset contents dated from 1st Jan 2015 to 19th Dec 2020.<br/>
Attributes in the dataset are Date, Open, High,	Low, Close,	AdjClose,	Volume. Here in the preproccessing, we selects the attributes  Date, Open, High,	Low, Close.
*2.Set up* - Import tensorflow, plotly, keras, numpy, pandas,

**Theory** : <br/> 
RNN - RNN or Recurrent Neural Networks, as the name suggests, is a repeating neural network. They are the kind whose output from the previous step is fed as input to the current step.
CNN was unable to deal with sequential data.Sequential data are an interdependent type of data. It always depends on the previous stage for itself to get propagated. For example Stock Prediction, 
this prediction is only possible by a thorough study in the stock market for a considerable amount of data. Likewise, a bitcoin price prediction can only be made by relating all historical prices. 

Since CNN can't depend on its previous data or each step is self-dependent,for our mentioned task, we are going to choose RNNs.  The overall challenge is to determine the difference between one Close price and the next. Not the actual Bitcoin price. This is because we are trying to predict something that could fluctuate marginally.
The Keras deep learning library provides the TimeseriesGenerator to automatically transform both univariate and multivariate time series data that we have at hand into samples, ready to train deep learning models.


**Approach** :<br/> 
*1.Splitting dataset* - The dataset is split into 80% training set and 20% test set. In this example the keras library automatically fetches it for us and splits into training and testing sets.<br/>
*2.Preprocessing*- The preprocessing steps involve selecting the column of interest particular for the task at hand in the following steps. <br/>
*3.Defining the model* - In constructing the model primarily we define a sequential model using high-level Keras API which uses TensorFlow on the backend. This is followed by addition of LSTM and Dense layers.<br/>
*4.Fitting the model* - Compiling is done where optimize function is 'adam' and loss funtion is 'mse' and now we fit the model that we defined in earlier step.<br/>
*5.Predicting outputs* - The model is used to predict the outputs on the test dataset.<br/>
*6.Displaying the results* - The results are displayed.Here in this case we plot a graph to visualize the predicted values and ground truth.<br/>

  
