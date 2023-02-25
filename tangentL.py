# Define the function f(x)
def f(x):
    return (x+1)*(x+2)*(x+3)*(x+4)*(x+5)*(x+6)*(x+7)*(x+8)*(x+9)/((x-1)*(x-2)*(x-3)*(x-4)*(x-5)*(x-6)*(x-7)*(x-8)*(x-9))

# Define the point where we want to find the tangent line
x0 = 0

# Calculate the derivative of f(x) using calculus
def derivative(f, x, h=0.0001):
    return (f(x+h) - f(x-h)) / (2*h)

slope = derivative(f, x0)

# Use the point-slope form of a line to write the equation of the tangent line
# The point (x0, f(x0)) is on the line, and the slope is the derivative at that point
# y - f(x0) = slope * (x - x0)
# Simplifying this equation gives us the equation of the tangent line
def tangent_line(x):
    return slope * (x - x0) + f(x0)

# Test the tangent line function by plotting it along with the original function
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 20, 1000)
y = f(x)
plt.plot(x, y, label='f(x)')
plt.plot(x, tangent_line(x), label='tangent line')
plt.legend()
plt.show()
