# Gradients

Think of gradients as the "gas pedal". Big gradients are strong changes such as stepping hard on the gas, and small gradients are tiny adjustments such as a light tap on the gas. 

# Vanishing Gradients

Imagine you are driving in a long tunnel (representing a deep neural network), and it keeps getting darker and darker as you go deeper. This is what happens when gradients shrink as they are calculated layer by layer from the output to the input. The gradients may become too small that they are almost zero so that the model becomes very slow at learning. 

# Exploding Gradients

In the other world, imagine that you backpropagate through the network, and the gradients become bigger and bigger. It is like a snowball rolling downhill that will become bigger and bigger. When you get closer to the finish line (input layer), the gradients are so big that take huge or unstable steps during updates. The model will not be able to train or learn effectively. 
