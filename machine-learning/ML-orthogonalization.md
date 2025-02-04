# Orthogonalization 

Well, now, what is orthogonalization in machine learning? It is a way to break down a problem into separate, independent parts where you can tackle one effectively. For example, it can help keep different concerns - learning rate, reducing bias, overfitting, and improving generalization - separate, making it easier to debug and improve my model. 

Without orthogonzalization, it would be hard to pinpoint whether the issue is with the data, the model complexity, or the process. 

### Use Case: Speech Recognition

Let's use this case as we are all building a voice assistant. The reason why I chose this topic is because I was on American Inventor ABC show trying to win the competition with my voice recognition prototype (I did not anyways). We would address different challenges separately such as 1) reducing bias by correctly recognizing words in a clean, noise-free setting, 2) handling background noise, and 3) personalization by fine-tuning it to better understand different accents and speech patterns. 

### Andrew Ng's Framework: 

His framework breaks things into training data, dev data, test, data, and real-world performance, helping pinpoint exactly where a model is struggling. 

* Training Set: improve architecture (bigger network), increase capacity, or reduce bias 
* Dev Set: employ regularization, better hyperparameters, bigger training set
* Test Set: bigger dev set
* Real-World Use: change dev set or cost function
