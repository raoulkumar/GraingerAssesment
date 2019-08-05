# GraingerAssesment

So far I have spent about 5 hours on this assessment and will be returning to complete the final tasks when I have more time.

Jupyter notebook has work for both parts of the assessment. 

<h3> Assessment #1 </h3>
Using the Jupyter notebook called data_exploration.ipynb I created a linear regression model with a set of features to predict the probability of a vehicle with unknown make is produced by one of the top 25 manufacturers from the data set.

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


<h3> Assessment #2 </h3>
See bottom of data_exploration.ipynb for calculations.
Code is all written using pandas library in python.

Still need to implement sqlite implementation to compare the which method is actually faster
