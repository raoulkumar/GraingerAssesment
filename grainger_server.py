from http.server import HTTPServer, BaseHTTPRequestHandler

from io import BytesIO
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
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        response.write(b'This is POST request. ')
        response.write(b'Received: ')
        response.write(body)
        self.wfile.write(response.getvalue())


httpd = HTTPServer(('localhost', port), SimpleHTTPRequestHandler)
httpd.serve_forever()