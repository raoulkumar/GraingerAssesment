from http.server import HTTPServer, BaseHTTPRequestHandler

from io import BytesIO
import json

import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import pickle


filename = 'LR_top25_model.sav'
print('Loading model...')
LR_pipe = pickle.load(open(filename,'rb'))
print('Model has been downloaded.')

port=8009
#shutdown(port)
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Grainger Assesment Model')

    def do_POST(self):
        #parse JSON Data into np array with 6 arguments below
        # Issue time, Plate Expiry Date, Agency, Fine amount, Latitude, Longitude
        #input np array as input to LR_pipe
        #ypredict = LR_pipe.predict_proba(xtest)
        #return second index of ypredict - probability vehicle is top25
        content_length = int(self.headers['Content-Length'])
        body = json.loads(self.rfile.read(content_length))
        xtest = np.array([float(body['Issue time']), float(body['Plate Expiry Date']), float(body['Agency']), float(body['Fine amount']), float(body['Latitude']), float(body['Longitude'])])
        xtest = xtest.reshape(1,-1)
        ypredict = LR_pipe.predict_proba(xtest)
        yprob = str(ypredict[:,1])
        print('Probabilty of top 25 make:', ypredict[:,1])
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        response.write(b'\n\nData Received ')
        response.write(b'Probability of Top 25 make:')
        response.write(str.encode(yprob))
        response.write(b'\n\n')
        self.wfile.write(response.getvalue())


httpd = HTTPServer(('localhost', port), SimpleHTTPRequestHandler)
httpd.serve_forever()



'''
Test json dict
{'Issue time':'1251.0', 'Plate Expiry Date':'200304.0', 'Agency':'1.0', 'Fine amount':'50.0', 'Latitude':'99999.0', 'Longitude':'99999.0'}

'''