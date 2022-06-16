# cali-fire-analysis
### California Fires Analysis
Analysis of the factors that lead to California Fires with different models. 

In this project,I was trying to create a classification model that can predict the size of a fire or a classifcation model that can predict the size of the fire of big(2), medium(1),and small(0). To create this model, I decided to create a dataset with the features being the variables that I think are correlated to fires. Features I initially thought of were weather, temperature, and elevation. I also added average income in those areas to see if they have an effect on the models.

I was able to collect this data from various sources. The initial data on all the fires came from California Fires. Then, I was able to web scrape average temperature from the area of the fire with Weather Underground. I was also able to get the minimum temperature, and maxximum temperature, with other factor like rainfall.Next, I collected the local elevation of where the fire occured to see if elevation would have an effect on the model. Other data that I included was the average income of the population in the region where the fire was. These were all stored in a csv file and vectorized when needed.

<<<<<<< HEAD
<<<<<<< HEAD
First, I preporcessed the data. I removed huge fires and really small fires from the dataset. I used the StandardScalar function in sklearn to normalize all the vectors. I then used a linear regression to determine how accurate my predictions were. The predictions had an RSME of 4000. I tested some other models to figure out that I had that linear regression was the best so far.


	
=======
The model was

Pivoted to a web app that can display the fires from 2013 to 2020 layered with other stats and such


Also playing around with this [repo](https://archive.ics.uci.edu/ml/datasets/forest+fires) to look for better techniques for analyzing my data.
>>>>>>> e40695bb025e45dcfad2b3522b71ac4e588a99a6

### UCI Fire Data Repository
After running into some trouble analyzing my own collected fire data, I decided to try creating a good model for a different data a set. In this data set, I tried a variety of techniques to increase the classfication results. I haven't been able to have a classification score higher than 55% which is not so good.

Preprocessing:   
The first step to the problem is to clean up the data and make it readable for the algorithm. I first tokenized the weekdays and the months of the year. Intrestingly, I knew about tokenization befor I learned it in any class. Then, I created the classes of 1 and 0 by looking at the fire size. Next, I normalized all the vectors with the sklearn Standard Scalar class.   

Feature Selection:   
I tried many different feature selection methods found in sklearn like the lasso model rfe estimator. Both these feature elimination methods in sklearn produced similar results. The best features seemed to be the location on the plot of land and the month. Even though the rain was always zero. This feature led to better results anyway.

Model:
I split the models and proceeded to try out many models to see which one was the best.I tried logistic regression, svm, but the best model I tried was the Random Forest Classifier which led to the best accuracy of .615. I next used Randomized search to hyper tune the parameters of the model. This tuning led to worse results. I definetly don't know alot about machine learning still. In the uciFireData jupyter notebook, there are many plots comparing the predictions vesus the actual classes.


