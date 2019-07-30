# GraingerAssesment
Jupyter notebook has work for both parts of the assesment. 

For assesment 1 I am working on creating a server where the model is created and when a post request with JSON data representing a row is sent, the system will use the logistic regression model to predict the probability that the vehicle make is one of the top 25 makes from the uncorrupted data

only calculation from the notebook that will be put into the POST function will be parse JSON data and remove relevant fields used for calculation. Scale data and then input scaled data into model to receive the probability of vehicle being one of the top 25 makes

For assessment 2
Code is all written using pandas library in python. Did not implement in sqlite yet, however it is my assumption that sqlite would perform these tasks faster than the pandas implementation
