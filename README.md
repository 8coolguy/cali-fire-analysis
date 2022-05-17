# cali-fire-analysis
Analysis of the factors that lead to California Fires with different models. 

Work in progress. The data was webscraped from Wundergroud, google map api, and Cal fires using selenium or their apis. Trying to create a prdictive model of California fires. Currently having a bad time. Also looking at the UCI fire predictive paper for tips and tricks. Also playing around with this [repo](https://archive.ics.uci.edu/ml/datasets/forest+fires) to look for better techniques for analyzing my data.

### UCI Fire Data Repository
After running into some trouble analyzing my own collected fire data, I decided to try creating a good model for a different data a set. In this data set, I tried a variety of techniques to increase the classfication results. I haven't been able to have a classification score higher than 55% which is not so good.

Preprocessing:   
The first step to the problem is to clean up the data and make it readable for the algorithm. I first tokenized the weekdays and the months of the year. Intrestingly, I knew about tokenization befor I learned it in any class. Then, I created the classes of 1 and 0 by looking at the fire size. Next, I normalized all the vectors with the sklearn Standard Scalar class.   

Feature Selection:   
I tried many different feature selection methods found in sklearn like the lasso model rfe estimator. Both these feature elimination. These


