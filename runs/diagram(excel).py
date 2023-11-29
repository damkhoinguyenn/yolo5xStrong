import matplotlib.pyplot as plt
import pandas as pd

# Load your data into a pandas DataFrame
df = pd.read_excel('C:/Users/dammi/Documents/StrongxYolo5/runs/track/StandStrong(0.05,0.95)/tracks/0.05.0.95.xlsx')

# Use the integer column names directly
frames = df[64]
ids = df[1]

# Create the plot with the desired figure size
fig, axs = plt.subplots(figsize=(10, 2))  # Adjust the size as needed

# Scatter plot
axs.scatter(frames, ids, alpha=0.5, label='conf_thres=0.05,iou_thres=0.95')

# Draw lines at x=0 and y=0
axs.axhline(y=0, color='k', linewidth=1)  # Horizontal line at y=0
axs.axvline(x=0, color='k', linewidth=1)  # Vertical line at x=0

# Set the limits for x and y axes
axs.set_xlim([frames.min() - 1, frames.max() + 1])  # Adjust as needed
axs.set_ylim([ids.min() - 1, ids.max() + 1])  # Adjust as needed

# Add legends, labels, etc.
axs.legend()
axs.set_xlabel('Frames')
axs.set_ylabel('IDs')

plt.tight_layout()

# Save image
save_img = input("Do you want to save the plot? (y/n): ").strip().lower()
if save_img == 'y':
    file_name = input("Enter the filename for image: ").strip()
    file_path = f'{file_name}.jpg'  # Save as JPG
    fig.savefig(file_path, format='jpg', dpi=100)
    print(f"Plot saved as '{file_path}'.")
elif save_img == 'n':
    print("Image not saved.")
else:
    print("Invalid input. Image not saved.")

plt.show()
