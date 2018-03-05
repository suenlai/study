#!/usr/bin/env python
#_*_coding:utf-8_*_
import numpy as np

a = np.zeros((4, 4), int)
np.fill_diagonal(a,2)
#print a
diagonal_matrix = np.asmatrix(a)
print diagonal_matrix.T
print diagonal_matrix.I
print diagonal_matrix.mean()
print diagonal_matrix.nonzero()
print "======="
diagonal_matrix = np.matrix([[3,2,1,5],[2,3,7,5],[5,2,6,10]])
#b = np.zeros((4,5),int)
np.fill_diagonal(diagonal_matrix,3)

print diagonal_matrix
print diagonal_matrix.I
print  np.round(diagonal_matrix.getI() * diagonal_matrix,2)
print  np.round(diagonal_matrix * diagonal_matrix.I,2)

print "-----"
print diagonal_matrix.T
print diagonal_matrix.T.I
print np.round(diagonal_matrix.T.I * diagonal_matrix.T ,2)

print '++++++++'
c = np.random.random_integers(100, size=(77,75))

diagonal_matrix = np.asmatrix(c)
U, s, V = np.linalg.svd(diagonal_matrix, full_matrices=True)
S = np.diag(s)
print U
print s
print S
print V



