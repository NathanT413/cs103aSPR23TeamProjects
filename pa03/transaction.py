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
    TEAM: ALL FUNCTIONS NEED A PARAMETER TUP TO FUNCTION WITH THE CLI FOR THE APP. YOU DO NOT NEED TO USE IT IN THE FUNCTION UNLESS A VALUE MUST BE PASSED IN TO IT.
 
    Author: Brandon J. Lacy (AG3NTZ3R0)
    '''
    
    def __init__(self, filepath):
        '''
        Establish a connection to the SQL database based upon the filepath provided as a parameter.

        Author: Brandon J. Lacy (AG3NTZ3R0)
        '''
        self.filepath = filepath
        self.runQuery("CREATE TABLE IF NOT EXISTS transactions (id INT, amount FLOAT, category TEXT, date DATE, description TEXT)", ())  

    def selectAll(self, tup):
        '''
        Select all of the items in the database.

        i.e. "python tracker.py --show-trans" 

        Author: Brandon J. Lacy (AG3NTZ3R0)
        '''
        return self.runQuery("SELECT * FROM transactions", ())

    def add(self, tup):
        '''
        Add an item to the database.
        
        i.e. "python tracker.py --add-trans 1 9.99 food 2023-03-23 fast-food"

        Author: Brandon J. Lacy (AG3NTZ3R0)
        '''
        return self.runQuery("INSERT INTO transactions VALUES(?, ?, ?, ?, ?)", (tup[0], tup[1], tup[2], tup[3], tup[4]))

    def runQuery(self, query, tup):
        '''
        Execute the requested query and return items as a list of dictionaries.

        Author: Brandon J. Lacy (AG3NTZ3R0)
        '''
        con = sqlite3.connect(self.filepath)
        cur = con.cursor()
        cur.execute(query, tup)
        tups = cur.fetchall()
        con.commit()
        con.close()
        return [toDict(t) for t in tups]
