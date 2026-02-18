import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.animation import FuncAnimation
import pandas as pd

# Apply Seaborn styling
sns.set_theme(style="darkgrid")

fig, ax = plt.subplots(figsize=(8, 5))

def update(frame):
    try:
        # 1. Read the data
        with open('data.txt', 'r') as f:
            data = [float(line.strip()) for line in f if line.strip()]
        
        # 2. Convert to a DataFrame (Seaborn works best with Pandas)
        df = pd.DataFrame({'Time': range(len(data)), 'Value': data})
        
        # 3. Clear the axis and redraw the Seaborn plot
        ax.clear()
        sns.lineplot(data=df, x='Time', y='Value', ax=ax, color='teal')
        
        # 4. Maintain labels (clearing the axis removes them)
        ax.set_title("Live Seaborn Feed")
        ax.set_xlabel("Seconds Elapsed")
        ax.set_ylabel("Sensor Value")
        
    except (FileNotFoundError, ValueError, IndexError):
        pass

# Update every 1000ms (1 second)
ani = FuncAnimation(fig, update, interval=1000, cache_frame_data=False)

plt.show()