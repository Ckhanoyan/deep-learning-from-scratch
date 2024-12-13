# Loss Function 

A loss function is important to be used in evaluating the performance of your model. It is a mathematical function to measure the difference between the predicted output and the actual target (ground truth). It also helps the model improve by guiding the optimization process such as gradient process that we just discussed previously. 

### Loss Function Example for Health Insurance Approval 

How do we use a loss function to evaluate this health insurance approval prediction model? We need to consider all inputs (income, age, etc.), output (probability of approval), and targets (1 for approval and 0 for denied). So, if the model predicts probabilities, we might need to use cross-entropy loss for classification. 
