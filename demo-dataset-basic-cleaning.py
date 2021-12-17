import pandas as pd
import numpy as np

def clean_tbl_name(filename):
  
    #rename csv, force lower case, no spaces, no dashes
    clean_tbl_name = filename.lower().replace(" ", "").replace("-","_").replace(r"/","_").replace("\\","_").replace("$","").replace("%","")
    
    tbl_name = '{0}'.format(clean_tbl_name.split('.')[0])

    return tbl_name



def clean_colname(dataframe):
  
    #force column names to be lower case, no spaces, no dashes
    dataframe.columns = [x.lower().replace(" ", "_").replace("-","_").replace(r"/","_").replace("\\","_").replace(".","_").replace("$","").replace("%","") for x in dataframe.columns]
    
    #processing data
    replacements = {
        'timedelta64[ns]': 'varchar',
        'object': 'varchar',
        'float64': 'float',
        'int64': 'int',
        'datetime64': 'timestamp'
    }

    col_str = ", ".join("{} {}".format(n, d) for (n, d) in zip(dataframe.columns, dataframe.dtypes.replace(replacements)))
    
    return col_str, dataframe.columns