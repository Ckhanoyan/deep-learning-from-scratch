# What is vectorization and why it is important for multiple examples in a neural network? 

Based on my understanding, it helps optimize computations while handling multiple training examples. I guess that before vectorization (recall I provided some real life analogies on how much vectorization matters for machine learning - under the basics folder). At first, the neural network processes one example x(i) at a time using loops such as from i = 1 to m, where m is the number of training examples. 

Once vectorization is implemented, all calculations are done simultaneously using matrix operations, resulting in increasing speed after all. 

This approach is a fundamental concept in neural networks and machine learning, and this is something I will need to practice learning a bit more based on a daily basis to understand the whole picture. Also, I learned one thing from my learning process, and vectorization typically works much better and faster on modern hardware such as GPU so I guess GPU is important to consider as well. 
