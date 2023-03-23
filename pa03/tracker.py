'''
An application that tracks finances with persistence with through the utilization of a SQL database.

Author: Brandon J. Lacy (AG3NTZ3R0)
'''


import sys

from transaction import Transaction


# Store the arguments from the command line execution of the script
# No arguments so prompt the user for them
if len(sys.argv) == 1:
    arg = input('cmd > ').split(' ')
# Numerous arguments so prompt the user to select one
elif len(sys.argv) > 2:
    print("Only one argument at a time.")

    args = [{i: sys.argv[1:][i]} for i in range(len(sys.argv[1:]))]
    for arg in args: print(arg)

    choice = int(input("Which argument should be executed? "))
    arg = sys.argv[1:][choice]
else:
    arg = sys.argv[1]

    
