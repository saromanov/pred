import os
import datetime
import fbprophet
import numpy as np
import pandas as pd

import plotly.plotly as py
import plotly.graph_objs as graph

class Dataset:
    ''' Dataset defens class
    for dataset handling
    '''
    def __init__(self, path):
        try:
            f = open(path)
            f.close()
        except IOError as e:
            print("Coundn't read the file {0}", e.errno)
            os._exit()
        except:
            print('Unexpected error')
            os._exit()
        self.ds = self._read_file(path, self._get_file_extension(path))
        if self.ds is None:
            raise Exception('Unable to create dataset. Format is not supported')
    
    def _prepare_dataset(self, ds):
        ds.reset_index(inplace=True)
        ds.drop_duplicates(subset='value', inplace=True)
        ds.sort_index(ascending=True, inplace=True)
    
    def plot(self):
        ''' plot of the data from dataset
        '''
        self.ds.plot()
    
    def size(self):
        return self.ds.size
    
    def _get_file_extension(self, path):
        ''' returns file extension like .csv, .txt
        '''
        filename, file_extension = os.path.splitext(path)
        return file_extension
    
    def _read_file(self, path, extension):
        if extension == '.csv':
            return pd.read_csv(path, index_col=0, header=0, parse_dates=True)


class Predict:
    '''
    Defines class for prediction of the data
    '''
    def __init__(self, ds):
        if not ds:
            raise Exception('Dataset is not defined')
        self._prophet = Prophet(interval_width=0.95)
    
    def run(self, preiods=365):
        future = self._prophet.make_future_dataframe(periods=365)
        forecast = self._prophet.predict(future)
        self._prophet.plot(forecast)
    
    def model(self, mod, names, title='title', yTitle='yTitle', color='#CCFFCC'):
        if len(names) > 0:
            mod = mod[names]
        plot = mod.iplot(kind='data', title=title, yTitle=yTitle)
        plot.data[0].showlegend = False
        plot.data[1].showlegend = False
        plot.data[1].fillcolor = color

