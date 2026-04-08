import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/shots.csv")

# Create pitch
fig, ax = plt.subplots(figsize=(10, 7))

# Pitch outline
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)

# Draw pitch lines
ax.plot([0,100],[0,0])
ax.plot([0,0],[0,100])
ax.plot([100,100],[0,100])
ax.plot([0,100],[100,100])

# Halfway line
ax.plot([50,50],[0,100])

# Goal box (right side)
ax.plot([83,100],[21,21])
ax.plot([83,83],[21,79])
ax.plot([83,100],[79,79])

# Separate teams
barca = df[df['team'] == 'Barcelona']
newcastle = df[df['team'] == 'Newcastle']

# Plot shots
for i in range(len(df)):
    if df.iloc[i]['team'] == 'Barcelona':
        color = 'blue'
        marker = 'o'
    else:
        color = 'red'
        marker = 'x'
    if df.iloc[i]['result'] == 'Goal':
        size = 200
    else:
        size = 60

    ax.scatter(df.iloc[i]['x'], df.iloc[i]['y'], s=size, c=color, marker=marker, alpha=0.7)

ax.scatter([], [], marker='o', label='Barcelona')
ax.scatter([], [], marker='x', label='Newcastle')
ax.legend()

# Titles
ax.set_title("Shot Map: Barcelona vs Newcastle")
ax.legend()

# Remove axis numbers
ax.set_xticks([])
ax.set_yticks([])

plt.tight_layout()
plt.savefig("visuals/shot_map.png", dpi=300)
plt.show()