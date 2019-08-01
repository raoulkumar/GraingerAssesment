# GraingerAssesment

So far I have spent a little over 2 hours on this assessment and will be returning to complete the final tasks when I have more time.

Jupyter notebook has work for both parts of the assessment. 

For assessment 1 I have built the model using the uncorrupted data and tested with corrupted rows from the original data in the jupyter notebook and will use this code to build a script for the server.

I am working on creating a server where the model is created and when a post request with JSON data representing a row is sent, the system will use the logistic regression model to predict the probability that the vehicle make is one of the top 25 makes from the uncorrupted data

I will need to save the model coefficients and scaling transformation so that the server can run without having to calculate the model.

only calculation from the notebook that will be put into the POST function will be parse JSON data and remove relevant fields used for calculation. Scale data and then input scaled data into model to receive the probability of vehicle being one of the top 25 makes

This will be my first time implementing a python server and I will use this guide as the structure:
https://gist.github.com/nitaku/10d0662536f37a087e1b

For assessment 2
Code is all written using pandas library in python. Did not implement in sqlite yet, however it is my assumption that sqlite would perform these tasks faster than the pandas implementation

Still need to implement sqlite implementation to compare the which method is actually faster
