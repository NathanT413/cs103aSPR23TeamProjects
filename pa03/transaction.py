'''
A module for the transaction class.

Author: Brandon J. Lacy (AG3NTZ3R0)
'''
import sqlite3  # It is a part of the standard Python package and doesn't need to be installed


def to_dict(row):
    '''
    Return a dictionary entry for each row.
    
    Author: Brandon J. Lacy (AG3NTZ3R0)
    '''
    item = {
        'id': row[0],
        'amount': row[1],
        'category': row[2],
        'date': row[3],
        'description': row[4]
    }
    return item


class Transaction:
    '''
    A class that is responsible for the persistant storage of financial transactions.
    TEAM: ALL FUNCTIONS NEED A PARAMETER TUP TO FUNCTION WITH THE CLI FOR THE APP. 
    YOU DO NOT NEED TO USE IT IN THE FUNCTION UNLESS A VALUE MUST BE PASSED IN TO IT.
 
    Author: Brandon J. Lacy (AG3NTZ3R0)
    '''

    def __init__(self, filepath):
        '''
        Establish a connection to the SQL database based upon the filepath provided as a parameter.

        Author: Brandon J. Lacy (AG3NTZ3R0)
        '''
        self.filepath = filepath
        self.run_query('''
            CREATE TABLE IF NOT EXISTS transactions 
            (id INT, amount FLOAT, category TEXT, date DATE, description TEXT)
            ''', ()
        )

    def select_all(self, tup):
        '''
        Select all of the items in the database.

        i.e. "python tracker.py --show-trans" 

        Author: Brandon J. Lacy (AG3NTZ3R0)
        '''
        return self.run_query("SELECT * FROM transactions", tup)

    def add(self, tup):
        '''
        Add an item to the database.
        
        i.e. "python tracker.py --add-trans 1 9.99 food 2023-03-23 fast-food"

        Author: Brandon J. Lacy (AG3NTZ3R0)
        '''
        return self.run_query('''
            INSERT INTO transactions VALUES(?, ?, ?, ?, ?)
            ''', (tup[0], tup[1], tup[2], tup[3], tup[4]))
    
    def delete(self, tup):
        '''
        Deletes an item from the database.
        
        i.e. "python tracker.py --del-trans 5"

        Author Eric Wang
        '''

        return self.run_query("DELETE FROM transactions WHERE id = (?)", tup[0])
    
    def sum_date(self, tup):
        '''
        Summarizes transactions by day given date, month and year
        
        i.e. "python tracker.py --sum-trans-d 2023-03-24"

        Author Eric Wang
        '''
        return self.run_query("SELECT * FROM transactions WHERE date=?", tup)
    
    def sum_month(self, tup):
        '''
        Summarizes transactions by month given month and year
        
        i.e. "python tracker.py --sum-trans-m 2023-03"

        Author Eric Wang
        '''
        return self.run_query("SELECT * FROM transactions WHERE date LIKE ? ORDER BY date DESC", ('%' + tup[0] + '%',))
    
    def sum_year(self, tup):
        '''
        Summarizes transactions by year given year
        
        i.e. "python tracker.py --sum-trans-y 2023"

        Author Eric Wang
        '''
        return self.run_query("SELECT * FROM transactions WHERE date LIKE ? ORDER BY date DESC", ('%' + ''.join(tup) + '%',))
        

    def run_query(self, query, tup):
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
        return [to_dict(t) for t in tups]
