# What is Softmax? 

Apparently, it is a function that takes a vector of raw scores (logits) from a model like [3.0, 1.0, 0.2] and converts them into probabilities for each class ensuring that probabilities sum to 1. Also, each probability lies between 0 and 1. So, what does the softmax formula look like in general? 

    P(y_i) = e^(z_i) / SUM(e^(z_j)), for j = 1 to n

Z(i) is the raw score (logit) for class i. SUM(e^(z_j)) is the sum of exponentials of all logits. 

## Why is it important? Health Insurance Approval Example

Softmax outputs probabilities for each class, making it ideal for multi-classification. Let's focus on an example using health insurance approval statuses that include three categories, "Approved", "Pending", and "Rejected". You can have any real numbers such as [2.5, 1.2, 0.3] so we need to interpret these scores meaningfully. 

We will use [2.5, 1.2, 0.3] for this work below. 

Exponentiate each logit

    = e^(2.5), e^(1.2), e^(0.3) 
    = 12.18, 3.32, 1.35 
    = 16.85 

Then you normalize to probabilites by this below

    = 12.18 / 16.85 then 0.723 
    = 3.32 / 16.85 then 0.197 
    = 1.35 / 16.85 then 0.08

With this output above, we can say that we have approval with 72.3% confidence, pending with 19.7% confidence, and rejected with 8.0% confidence. Below is the code example.

    import numpy as np

    # Logits from the model
    logits = np.array([2.5, 1.2, 0.3])  # Approved, Pending, Rejected

    # Apply softmax
    exp_logits = np.exp(logits)  # Exponentials of logits
    probabilities = exp_logits / np.sum(exp_logits)  # Normalize to probabilities

    # Print results
    statuses = ["Approved", "Pending", "Rejected"]
    for status, prob in zip(statuses, probabilities):
      print(f"Probability of {status}: {prob:.2f}")

Then we get this output below. 

    Exponentiated logits (e^z): [12.18249396  3.32011692  1.34985881]
    Probabilities: [0.72397226 0.1979918  0.07803594]
    Probability of Approved: 0.72
    Probability of Pending: 0.20
    Probability of Rejected: 0.08

    
