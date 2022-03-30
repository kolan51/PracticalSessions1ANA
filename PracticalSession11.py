#!/usr/bin/env python
import sys


# Helper Functions

# cnf formula for exactly one of the variables in list A to be true
def exactly_one(A):
    temp = ""
    temp = temp + atleast_one(A)
    temp = temp + atmost_one(A)
    return temp


# cnf formula for atleast one of the variables in list A to be true
def atleast_one(A):
    temp = ""
    for x in A:
        temp = temp + " " + str(x)
    temp = temp + " 0\n"
    return temp


# cnf formula for atmost one of the variables in list A to be true
def atmost_one(A):
    temp = ""
    for x in A:
        for y in A[A.index(x) + 1:]:
            temp = temp + " -" + str(x) + " -" + str(y) + " 0\n"
    return temp


def reduce_nq_sat(n):
    # function to map position (r,c) 0 <= r,c < n, in an nxn grid to the integer
    # position when the grid is stored linearly by rows.
    def varmap(r, c, n):
        return r * n + c + 1

    # Start Solver
    spots = n * n
    # Exactly 1 queen per row
    temp = ""
    for row in range(0, n):
        A = []
        for column in range(0, n):
            position = varmap(row, column, n)
            A.append(position)
        temp = temp + exactly_one(A)

    # Exactly 1 queen per column
    for column in range(0, n):
        A = []
        for row in range(0, n):
            position = varmap(row, column, n)
            A.append(position)
        temp = temp + exactly_one(A)

    # Atmost 1 queen per negative diagonal from left
    for row in range(n - 1, -1, -1):
        A = []
        for x in range(0, n - row):
            A.append(varmap(row + x, x, n))
        temp = temp + atmost_one(A)

    # Atmost 1 queen per negative diagonal from top
    for column in range(1, n):
        A = []
        for x in range(0, n - column):
            A.append(varmap(x, column + x, n))
        temp = temp + atmost_one(A)

    # Atmost 1 queen per positive diagonal from right
    for row in range(n - 1, -1, -1):
        A = []
        for x in range(0, n - row):
            A.append(varmap(row + x, n - 1 - x, n))
            temp = temp + atmost_one(A)

    # Atmost 1 queen per positive diagonal from top
    for column in range(n - 2, -1, -1):
        A = []
        for x in range(0, column + 1):
            A.append(varmap(x, column - x, n))
            temp = temp + atmost_one(A)
    print('p cnf ' + str(n * n) + ' ' + str(temp.count('\n')))
    print(temp)


if __name__ == '__main__':

    if len(sys.argv) == 1:
        n = int(input("Enter chess board size: "))
    else:
        n = int(sys.argv[1])

    reduce_nq_sat(n)
