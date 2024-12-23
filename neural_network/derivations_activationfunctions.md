# Derivations of activation functions 

This derivation involves computing the derivaties of the activation functions g(z), and it seems to be important to understand why sometimes your or my activation function is not performing well. We can either tweak or combine it with other functions to improve performance in a machine learning model. this also explains the gradient or slope of the sigmoid function, g(z). 

## Derivation of Sigmoid Function 

Remember the sigmoid function, and it provides any values between 0 and 1, making it useful for probabilities in classification problems. The goal is to compute the derivative g'(z), which represents how sensitive g(z) is to changes in z.

1. Set up the derivate:
   
   g'z = d / dz ( 1 / (1 + e(-z)))
  
3. Use the chain rule
   
5. Simplify:

   g'(z) = e(-z) / (1 + e(-z)(2)

4. The devriation formula is is g'(z) = g(z) * (1 - g(z)), which is easy to compute using the sigmoid value directly.

## Derivate of Tanh (g'(z))

How to set up the derivate, which is this, g'(z) = d / dz tanh(z). Use the mathematical property that is g'(z) = 1 - tanh(2)(z) 
* Since g(z) is tanh(z), the derivative formula can be written as g'(z) = 1 - g(z)(2)

## ReLU and Leaky ReLU 

### ReLU 

The ReLU function is g(z) = max(0,z) 

Behavior: 
* For z > 0: g(z) = z
* For z < 0: g(z) = 0

Derivative: 
* z > 0, g'(z) = 1
* z < 0, g'(z) = 0

Key notes:
this derivative formula is simple and efficient, but if it comes with z that is equal to or under 0, then it can lead to dead neurons. 

### Leaky ReLU 

The Leakly ReLU function only modifies ReLu due to dead neurons by allowing a small, non-zero gradient when z < 0. The formula is below: 

g(z) = max (0.01z, z) 

Behavior:
* z > 0, 0:g(z) = z
* z < 0, g(z) = 0.01z (or another small slope like 0.01)

Derivative: 
* for z > 0, then it is 0:g'(z) = 1
* for z < 0, then it is 0:g'(z) = 0.01

Key notes: 
It helps avoid dead neurons by maintaining a small gradient for z < 0, improving model performance in some cases. 


