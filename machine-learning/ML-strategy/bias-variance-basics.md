# Bias and Variance 

<img width="800" alt="{E4824B5F-5DE5-4C4E-BBE3-8E4AFF6D6BF7}" src="https://github.com/user-attachments/assets/ed7e78b0-1cb3-48c4-9c2e-c04f5387b4d8" />

The goal is to get both low bias and low variance in coding and deep learning. Sometimes, you may receive some kinds of errors from training set and development set. 

| **Scenario**     | **Train Set Error** | **Dev Set Error** | **Observation**                 |
|-------------------|---------------------|-------------------|----------------------------------|
| **A** (High Variance) | 1%                 | 11%               | High variance: model overfits training data. |
| **B** (High Bias)     | 15%                | 16%               | High bias: model underfits the data. |
| **C** (High Bias and High Variance) | 15%                | 30%               | High bias and high variance: worst of both worlds. |
| **D** (Low Bias and Low Variance) | 0.5%              | 1%                | Low bias and low variance: ideal scenario. |

Key takeaways: 
* High variance: the model performs well on the training set but poorly generalizes to the dev set
* High bias: the model performs poorly on both the training and dev sets, including underfitting
* Both high bias and high variance: the model is neither fitting well to the training set nor generalizing to the dev set
* Low bias and low variance: the model performs well on both the training and dev sets, achieving close-to-optimal results 
