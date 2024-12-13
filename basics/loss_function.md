# Loss Function 

A loss function is important to be used in evaluating the performance of your model. It is a mathematical function to measure the difference between the predicted output and the actual target (ground truth). It also helps the model improve by guiding the optimization process such as gradient process that we just discussed previously. 

### Loss Function Example for Health Insurance Approval 

How do we use a loss function to evaluate this health insurance approval prediction model? We need to consider all inputs (income, age, etc.), output (probability of approval), and targets (1 for approval and 0 for denied). So, if the model predicts probabilities, we might need to use cross-entropy loss for classification. 

What does the loss function look like in both formula and code?

The formula looks like this in code below: 

    L = - (1/N) ∑ [y_i * log(p_i) + (1 - y_i) * log(1 - p_i)]

Where:
- y_i: Actual label (0 or 1)
- p_i: Predicted probability
- N: Number of examples

### Implementing Cross-Entropy Loss with NumPy 

    import numpy as np

    # Simulated predictions and actual labels
    predictions = np.array([0.9, 0.7, 0.2, 0.4])  # Model's predicted probabilities
    labels = np.array([1, 1, 0, 0])  # Ground truth (approved = 1, denied = 0)

    # Function to calculate cross-entropy loss
    def cross_entropy_loss(predictions, labels):
      # Clip predictions to avoid log(0)
      predictions = np.clip(predictions, 1e-10, 1 - 1e-10)
      # Compute loss for each instance
      loss = - (labels * np.log(predictions) + (1 - labels) * np.log(1 - predictions))
      # Average loss across all instances
      return np.mean(loss)

    # Calculate and print the loss
    loss = cross_entropy_loss(predictions, labels)
    print(f"Cross-Entropy Loss: {loss:.4f}")

The result we will get from the code above is:

    Cross-Entropy Loss: 0.2162

The cross-entropy loss for the provided predictions and labels is approximately 0.2990. To interpret this result, this indicates how well the model's predicted probabilities match the actual labels. Lower values signify better performance. 
