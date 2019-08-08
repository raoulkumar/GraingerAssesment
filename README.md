# GraingerAssesment

So far I have spent about 5 hours on this assessment. A little over 2 hours to complete the notebook to build the model and complete the tasks for assessment #2. And a bit over 2 hours to understand how to build a web server with GET and POST requests, implement the model within the server, test with random data I supplied, and provide necessary documentation.

Jupyter notebook has work for both parts of the assessment. 

<h3> Assessment #1 </h3>
Using the Jupyter notebook called data_exploration.ipynb I created a logistic regression model with a set of features to predict the probability of a vehicle with unknown make is produced by one of the top 25 manufacturers from the data set.

This model has been saved to a local file 'LR_top25_model.sav' so it can be quickly loaded when running the server.

The server is built to take in JSON data of a corrupted row and output the probabilty the vehicle is made by one of the top 25 manufactuers from the data.
<h5> Port#: 8009 </h5>
***The guides below were used to create python server:

This will be my first time implementing a python server and I will use this guide as the structure:
https://blog.anvileight.com/posts/simple-python-http-server/

https://gist.github.com/nitaku/10d0662536f37a087e1b

**To Execute only need to run grainger_server.py wtih LR_top25_model.sav in the same directory as the script

$ bash run.sh

OR

$ python grainger_server.py


port number = 8009

<h5> Model Quality </h5>
This model is based upon the features of issue time, plate expiration date, agency, fine amount, and location (latitude & longitude)

Generally speaking these are features that are unlikely to provide any critical information as to which car manufacturer produced the vehicle because none of the features provided in the data are critical to the make of the car. The strengths of this model are that it can be retrained easily with different features that are more relevant to the make of the vehicle if available.

Another way to encode labeled data (non-numeric) is to create one-hot encoding for the vehicles (color, body style, violation, and any other relevant features) and use the one hot encoding to train the model using the information provided from these features.

Overall the model will provide a prediciton on the features utilized to trian, however, it could be improved with better feature selection.

Also the data that was used to train the model was heavily biased towards vehicles from the top25 manufacturers, with about 4 million vehicles within the top 25 manufacturers and approximately 400 thousand vehicles not made by the top 25 manufacturers.


Additionally there are more complex algorithms that are available to predict the probability the vehicle is made by one of the top 25 manufacturers such as a support vector machine.

<h3> Assessment #2 </h3>
See bottom of data_exploration.ipynb for calculations.
Code is all written using pandas library in python.

I see there is data for the state of the vehicles license plate. Need to figure out how to compare that value to the state the citation was made in. I know of a way to put the address and receive the state but this seems inefficient. Need to look into the agency and see if that provides any data as to where the citation was made. Once this is done, using logical indexing I can see how many rows have the same state between the two features and use that as a percentage to calculate the final task for #2.

Still need to implement sqlite implementation to compare the which method is actually faster
