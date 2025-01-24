def exponentially_weighted_average_with_bias_correction(values, beta=0.9):
    v = 0  # Initial value of the exponentially weighted average
    corrected_v = 0  # Bias-corrected version of the exponentially weighted average
    for t, x_t in enumerate(values):
        v = beta * v + (1 - beta) * x_t  # Update the weighted average
        # Apply bias correction
        corrected_v = v / (1 - beta ** (t + 1))  # Bias correction formula
        print(f"Time Step {t+1}: Value = {x_t}, Weighted Average = {v}, Corrected Average = {corrected_v}")
    return corrected_v

# Example data: values at each time step
data = [10, 12, 15, 14, 18, 16, 20]

# Call the function with beta=0.9
exponentially_weighted_average_with_bias_correction(data, beta=0.9)
