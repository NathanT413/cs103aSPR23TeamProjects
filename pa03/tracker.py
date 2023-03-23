'''
An application that tracks finances with persistence with through the utilization of a SQL database.

Author: Brandon J. Lacy (AG3NTZ3R0)
'''


from transaction import Transaction


def main():
    '''
    The main location in which the code will execute.
    
    Author: Brandon J. Lacy (AG3NTZ3R0)
    '''
    filepath = "tracker.db"
    trans_db = Transaction(filepath)
    
    print(trans_db.selectAll())


if __name__ == '__main__':
    main()
