# Dropout Regularization

Dropout is another regularization technique used in deep learning to reduce overfitting and improve the generalization of neural networks. Dropout introduces randomness during training so how does it work? It works by randomly dropping out a fraction of neurons during training such as setting their outputs to zero, which will prevent the network from replying too heavily on specific neurons. 

### Why is Dropout Important? 

This randomness technique acts as a form of noise that helps the model avoid learning spurious correlations. This is one of the techniques that has been shown to improve model performance significantly, especially in large networks. 

### How does it work?

This technique is applied during training by multiplying the output of each neuron by a random binary mask, where each element of the mask is sampled from a Bernoulli distribution. It means that... the "keep probability" (which you see in the picture I wrote below) parameter determines teh fraction of neurons that remain active. Let's say that if we have keep_prob = 0.5, half of the neurons are kept on average. 

<img width="700" alt="{7AA06300-F0E8-412F-A3DE-169C4E715F74}" src="https://github.com/user-attachments/assets/02f17906-d701-4d6f-a507-434c1928891c" />
