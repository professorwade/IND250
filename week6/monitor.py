import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Initialize the figure and axis
fig, ax = plt.subplots()
x_data, y_data = [], []
line, = ax.plot([], [], lw=2)

def init():
    """Set up the base background of the plot."""
    ax.set_xlim(0, 50)  # Adjust based on expected data volume
    ax.set_ylim(0, 100) # Adjust based on expected data range
    return line,

def update(frame):
    """Function called repeatedly to update the plot."""
    try:
        with open('data.txt', 'r') as f:
            # Read all lines and convert to floats
            data = [float(line.strip()) for line in f if line.strip()]
            
        # Update the data for the line
        y_data = data
        x_data = list(range(len(y_data)))
        
        line.set_data(x_data, y_data)
        
        # Optional: Auto-scale axes as data grows
        ax.set_xlim(0, max(50, len(x_data)))
        ax.set_ylim(min(y_data)-5, max(y_data)+5)
        
    except (FileNotFoundError, ValueError):
        # Handle cases where the file is empty or being written to
        pass
        
    return line,

# Create the animation object
# interval=1000 means it checks the file every 1000ms (1 second)
ani = FuncAnimation(fig, update, init_func=init, interval=1000, cache_frame_data=False)

plt.title("Live Data Feed from data.txt")
plt.xlabel("Sample Index")
plt.ylabel("Value")
plt.show()
