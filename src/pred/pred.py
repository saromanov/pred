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
    
    def _get_file_extension(self, path):
        ''' returns file extension like .csv, .txt
        '''
        filename, file_extension = os.path.splitext(path)
        return file_extension
    
    def _read_file(self, path, extension):
        if extension == '.csv':
            return pd.read_csv(path, index_col=0, header=0, parse_dates=True)



