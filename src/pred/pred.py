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
    
    def _get_file_extension(self, path):
        ''' returns file extension like .csv, .txt
        '''
        filename, file_extension = os.path.splitext(path)
        return file_extension



