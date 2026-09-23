## Introduction
The aim of this project is to create a simple logistic regression classifier that will draw a straight line separating two point clouds.
The two point clouds are classified by one of 2 labels: 0 or 1.

## How this code works
# Initial information
Since this code can only draw straight lines there are only three parameters that can be adjusted.
The linear equation is expressed as follows: ax + by + c = 0, where:
- a - the rate x is changing
- b - the rate y is changing
- c - constant term

To simplify the code and use 2 weights instead of 3, this formula was simplified by assuming b == c:
ax + by + b = ax + b(y + 1) = 0

For code to start three values are needed:
- in_a - arbitrary initial a value
- in_b - arbitrary initial b value
- lr   - arbitrary learning rate

# Parameters adjustment
Each iteration starts by checking how the model classified every point.
For each point the value of the function is calculated given the current value of the weights a and b.
This value is given as an argument to the sigmoid function: p = sigmoid(s) = 1 / (1 + np.exp(-s)),
which allows us to calculate the probability that a point has either label 0 or 1.
Using this probability we are able to learn how wrong the prediction was, and how much the weights should be adjusted.

To calculate the step by which each weight should be changed we need to know:
- How weights a and b influence the rate/direction of the function
- How big the error was

We can calculate how a and b influence the rate/direction of the function by calculating partial derivatives of s with respect to a and b:
- ds/da = x
- ds/db = y + 1

Error can be calculated using cross-entropy:
L = -[label * log(p) + (1-label) * log(1-p)]

To find out how a and b should change to reduce this error, we need the derivative of L with respect to each of them.
Since L depends on p, and p depends on s (which depends on a and b), this requires the chain rule, in two steps:

1. How L changes with p:
   dL/dp = (1-label)/(1-p) - label/p

2. How p changes with s (the derivative of the sigmoid function itself):
   dp/ds = p * (1 - p)

Multiplying these together, we get the result:
dL/ds = dL/dp * dp/ds = p - label

Combining dL/ds with ds/da and ds/db gives the actual gradients:
- dL/da = dL/ds * ds/da = (p - label) * x
- dL/db = dL/ds * ds/db = (p - label) * (1 + y)

The learning rate lr then scales these gradients into the actual step taken each update:
- step_a = lr * dL/da = lr * (p - label) * x
- step_b = lr * dL/db = lr * (p - label) * (1 + y)

Due to implementation in the code, value label is replaced by target, which is the opposite label (target = 1 - label),
to match this project's convention that a positive s corresponds to label 0 rather than label 1.

# Accuracy check
The weights adjustment is continued in the while loop until the accuracy threshold is achieved.
Accuracy here is defined by how many points were classified correctly vs the total number of points.
Once the threshold is reached the while loop is broken and the final values of a and b are returned.
