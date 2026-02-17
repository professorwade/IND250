import matplotlib.pyplot as plt

# 1. Prepare your data
x_values = [0, 1, 2, 3, 4, 5]
y_values = [0, 1, 4, 9, 16, 25]  # y = x^2

# 2. Create the plot
plt.figure(figsize=(8, 5))
plt.plot(x_values, y_values, label='$y = x^2$', color='blue', marker='o')

# 3. Add labels and title
plt.title('Simple Quadratic Plot')
plt.xlabel('Input (x)')
plt.ylabel('Output (y)')
plt.legend()
plt.grid(True)

# 4. Show the result
plt.show()
