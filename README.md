# GraingerAssesment

So far I have spent almost 4 hours on this assessment and will be returning to complete the final tasks when I have more time.

Jupyter notebook has work for both parts of the assessment. 

For assessment 1 I have built the model using the uncorrupted data and tested with corrupted rows from the original data in the jupyter notebook and will use this code to build a script for the server.

I am working on creating a server where the model is created and when a post request with JSON data representing a row is sent, the system will use the logistic regression model to predict the probability that the vehicle make is one of the top 25 makes from the uncorrupted data

In the notebook I saved the model to a .sav file using pickle. In the server I will have to load all necessary libraries and load the model using pickle from the created file. Then in the post function I will have to parse the row data into a numpy array where I use the 6 selected features to calculate if the vehicle is in the top25. The np array will then be input into the loaded model and it will output the probability that the vehicle was made by one of the top25 manufacturers.

***Server still needs to parse JSON data into numpy array and input into loaded pipeline and output probabilities then will be complete

This will be my first time implementing a python server and I will use this guide as the structure:
https://blog.anvileight.com/posts/simple-python-http-server/

https://gist.github.com/nitaku/10d0662536f37a087e1b

**To Execute only need to run grainger_server.py
$python grainger_server.py

For assessment 2
Code is all written using pandas library in python. Did not implement in sqlite yet, however it is my assumption that sqlite would perform these tasks faster than the pandas implementation

Still need to implement sqlite implementation to compare the which method is actually faster
