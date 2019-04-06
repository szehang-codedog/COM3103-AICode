# -*- coding: utf-8 -*-
""" 
Example of use multi-layer perceptron
=====================================

Task: Approximation function: 0.5 * sin(x) + 0.5 cos(2x)

"""

import neurolab as nl
import numpy as np

# Create train samples
x_train = np.linspace(-7, 7, 100)             
t_train = np.sin(x_train) *0.5 + np.cos(2*x_train)*0.5   

size = len(x_train)

input = x_train.reshape(size,1)
target = t_train.reshape(size,1)


net = ### ADD CODE TO CREATE YOUR NEURAL NETWORK ###

# Train network
error = net.train(input, target, epochs=500, show=100, goal=0.02)

# Simulate network
x_test = np.linspace(-6.0,6.0, 205)
input_test = x_test.reshape(x_test.size,1)

y_test = net.sim(input_test).reshape(x_test.size)


# Plot result
import pylab as pl

pl.subplot(211)
pl.plot(error)
pl.xlabel('Epoch number')
pl.ylabel('error (default SSE)')

pl.subplot(212)
pl.plot(x_test, y_test, '-',x_train , t_train, '.')
pl.legend(['testing output', 'Target output'])
pl.show()
