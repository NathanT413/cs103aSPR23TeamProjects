'''
A file to test the functionality of transaction.py
'''
import sqlite3
import pytest

from transaction import Transaction

@pytest.fixture
def example_data():
    '''
    A few data entries to assist in the test of application functionality.

    Author: Brandon J. Lacy (AG3NTZ3R0)
    '''
    return [
        (1, 9.99, 'food', '2023-03-23', 'fast-food'),
        (2, 99.99, 'food', '2023-03-28', 'groceries')
    ]


@pytest.fixture
def example_data_dict(example_data):
    '''
    The dictionary representation of the example_data.
    
    Author: Brandon J. Lacy (AG3NTZ3R0)
    '''
    result = []
    for tup in example_data:
        cols = ['id', 'amount', 'category', 'date', 'description']
        example_dict = {}
        # for i in range(len(tup)):
        for i, j in enumerate(tup):
            # example_dict[cols[i]] = tup[i]
            example_dict[cols[i]] = tup[i]
        result.append(example_dict)
    return result


@pytest.fixture
def transaction_db(example_data, test_db='test_tracker.db'):
    '''
    Create the table for the tests and add the data.

    Author: Brandon J. Lacy (AG3NTZ3R0)
    '''
    con = sqlite3.connect(test_db)
    cur = con.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS transactions 
        (id INT, amount FLOAT, category TEXT, date DATE, description TEXT)'''
    )

    for tup in example_data:
        cur.execute("INSERT INTO transactions VALUES(?, ?, ?, ?, ?)", tup)

    con.commit()

    test_trans_orm = Transaction(test_db)

    yield test_trans_orm

    cur.execute("DROP TABLE transactions")
    con.commit()
    # con.close()


def test_select_all(transaction_db, example_data_dict):
    '''
    Test the ability to select all of the transactions in the database.
    
    Author: Brandon J. Lacy (AG3NTZ3R0)
    '''
    trans_orm = transaction_db

    results = trans_orm.select_all(())

    assert results == example_data_dict


def test_add(transaction_db, example_data_dict):
    '''
    Test the ability to add a transaction to the database.
    
    Author: Brandon J. Lacy (AG3NTZ3R0)
    '''
    trans_orm = transaction_db

    tup = (3, 0.99, 'food', '2023-03-29', 'gum')
    updated_example_data_dict = example_data_dict
    updated_example_data_dict.append({
        'id': tup[0],
        'amount': tup[1],
        'category': tup[2],
        'date': tup[3],
        'description': tup[4]
    })

    trans_orm.add(tup)

    results = trans_orm.select_all(())

    assert results == updated_example_data_dict
