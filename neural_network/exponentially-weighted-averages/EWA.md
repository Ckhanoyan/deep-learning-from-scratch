# Exponential Weighted Averages 

It is often referred as  Exponential Moving Average (EMA). It is commonly used in machine learning and is one of ways to smooth out a sequence of values to emphasize recent data points over time. The equation for exponentially weighted averages is the basic idea that computes an average where each new value is weighted exponentially more than the older ones. The equation in general is below. 

    vt =β ⋅ vt−1 +(1−β)⋅ xt
​
Where: 
* vt is the exponentially weighted average at time step t
* vt-1 is the exponentially weighted average from the previous time step
* xt is the new value you are incorporating into the average
* β is the smoothing factor, usually close to 1, e.g., 0.9 or 0.99
* 1 - β is the weight given to the most recent observation

So if β is 0.99, the average will remember previous values for a long time and will respond slowly to new values. If β is 0.5, it will react much faster to the new values. 

### Real Life Use Case

In finanical markets such as stock prices, traders use the EMA to smooth out price data, helping them identify trends and make decisions about when to buy or sell.

### How to implement this code?

    def exponentially_weighted_average(values, beta=0.9):
    v = 0  # Initial value of the exponentially weighted average
    for t, x_t in enumerate(values):
        v = beta * v + (1 - beta) * x_t  # Update the weighted average
        print(f"Time Step {t+1}: Value = {x_t}, Weighted Average = {v}")
    return v

    # Example data: values at each time step
    data = [10, 12, 15, 14, 18, 16, 20]

    # Call the function with beta=0.9
    exponentially_weighted_average(data, beta=0.9)

Where: 
* The function exponentially_weighted_average accepts a list of values (data) and a smoothing factor (beta).
* It starts with an inital weighted average v = 0
* For each value in the list (x_t), it updates the exponentially weighted average using the equation vt = β * vt - 1 + (1 - β) * xt
* It prints the current value and the updated weighted average at each time stamp

Example:


<img width="800" alt="{6A7C4E9D-A3BF-4B85-A8A7-09C1D2F4E8C7}" src="https://github.com/user-attachments/assets/60099b76-196a-4f52-9d43-871a993cb215" />
