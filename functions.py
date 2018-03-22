def pulldata(sql = 'select * from citizens',index_col=None):
    '''
    Pull data from database with sql query
    '''
    import pandas as pd
    import sqlite3
    con = sqlite3.connect('Data/data.db')
    with con:
        df = pd.read_sql(sql,con,index_col)
    return(df)