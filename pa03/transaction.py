'''
A module for the transaction class.

Author: Brandon J. Lacy (AG3NTZ3R0)
'''


import os
import sqlite3  # It is a part of the standard Python package and doesn't need to be installed


def toDict(row):
    '''
    Return a dictionary entry for each row.
    
    Author: Brandon J. Lacy (AG3NTZ3R0)
    '''
    item = {'id': row[0], 'amount': row[1], 'category': row[2], 'date': row[3], 'description': row[4]}
    return item 


class Transaction:
    '''
    A class that is responsible for the persistant storage of financial transactions.
    
    Author: Brandon J. Lacy (AG3NTZ3R0)
    '''
    
    def __init__(self, filepath):
        '''
        Establish a connection to the SQL database based upon the filepath provided as a parameter.

        Author: Brandon J. Lacy (AG3NTZ3R0)
        '''
        self.filepath = filepath
        self.runQuery("CREATE TABLE IF NOT EXISTS transactions (id INT, amount FLOAT, category TEXT, date DATE, description TEXT)", ())  

    def selectAll(self):
        '''
        Select all of the items in the database.

        Author: Brandon J. Lacy (AG3NTZ3R0)
        '''
        return self.runQuery("SELECT * FROM transactions", ())

    def runQuery(self, query, tuple):
        '''
        Execute the requested query and return items as a list of dictionaries.

        Author: Brandon J. Lacy (AG3NTZ3R0)
        '''
        con = sqlite3.connect(self.filepath)
        cur = con.cursor()
        cur.execute(query, tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [toDict(t) for t in tuples]
