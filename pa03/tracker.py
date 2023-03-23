'''
An application that tracks finances with persistence with through the utilization of a SQL database.
'''


from transaction import Transaction


def main():
    '''The main location in which the code will execute.'''
    filepath = "tracker.db"
    trans_db = Transaction(filepath)
    
    print(trans_db.selectAll())


if __name__ == '__main__':
    main()
