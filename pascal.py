# -*- coding: utf-8 -*- 

"""
This module contains my realization of pascal triangle.
But on this site http://rosettacode.org/wiki/Pascal's_triangle#Python 
I was found the most beautifull realization of this problem on python.

def pascal(n):
   '''Prints out n rows of Pascal's triangle.
   It returns False for failure and True for success.'''
   row = [1]
   k = [0]
   for x in range(max(n,0)):
      print row
      row=[l+r for l,r in zip(row+k,k+row)]
   return n>=1
On this vode we just shake the previuos row.
Very elegant.

"""


def pascal(col_n, row_n):
    if col_n in [0, row_n]: return 1
    if row_n in [0, 1]: return 1
    formated_row = lambda r: ' '.join(map(str, r)).center((row_n+1)*3)
    prev_row = [1,1]
    print formated_row([1])
    print formated_row(prev_row)
    curr_row = []
    curr_row_n = 2
    while curr_row_n <= row_n:
        curr_row.append(1)
        curr_col_n = 1
        while curr_col_n < curr_row_n:
            curr_row.append(prev_row[curr_col_n - 1] + prev_row[curr_col_n])
            curr_col_n += 1
        curr_row.append(1)
        prev_row = curr_row[:]
        print formated_row(prev_row)
        curr_row = []
        curr_row_n += 1
    return prev_row[col_n]

if __name__ == '__main__':
    print pascal(1, 6)
