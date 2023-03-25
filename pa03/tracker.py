'''
An application that tracks finances with persistence with through the utilization of a SQL database.

Author: Brandon J. Lacy (AG3NTZ3R0)
'''
import sys

from functools import partial
from transaction import Transaction


# Author: Brandon J. Lacy (AG3NTZ3R0)
# Store the arguments from the command line execution of the script
# No arguments so prompt the user for them
if len(sys.argv) == 1:
    arg = input('cmd > ').split(' ')
else:
    arg = sys.argv[1]
    # Store the values for the option
    vals = tuple(val for val in sys.argv[2:])

# Author: Brandon J. Lacy (AG3NTZ3R0)
trans_orm = Transaction('tracker.db')
# Act upon the option specified by the user (TEAM: REPLACE "" WITH METHOD AS SEEN BELOW) 
options = {
    '--help': "",
    '--show-trans': partial(trans_orm.selectAll),
    '--add-trans': partial(trans_orm.add),
    '--del-trans': "",
    '--sum-trans-d': "",
    '--sum-trans-m': "",
    '--sum-trans-y': "",
    '--sum-trans-c': ""
}

try:
    print(options[arg](vals))
except Exception as e:
    print("Unavailable option specified.")
    print(e)
