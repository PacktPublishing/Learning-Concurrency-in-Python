from theano import *
import numpy
import theano.tensor as T

x = T.dmatrix('x')
y = T.dmatrix('y')
z = x + y
f = function([x,y],z)

print(f(\
  [[2,3],[4,5]],\
  [[2,3],[4,5]]\
))
