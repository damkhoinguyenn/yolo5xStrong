import matplotlib.pyplot as plt
import pandas as pd

# Load data from the first text file
df1 = pd.read_csv('C:/Users/dammi/Documents/StrongxYolo5/runs/track/HandStrong(0.25,0.25)/tracks/handAndStand.txt', delimiter=' ', header=None, names=['Frame', 'ID'])

# Load data from the second text file
df2 = pd.read_csv('C:/Users/dammi/Documents/StrongxYolo5/runs/track/HandStrong(0.5,0.5)/tracks/handAndStand.txt', delimiter=' ', header=None, names=['Frame', 'ID'])

# Load data from the third text file (update the path to your third file)
df3 = pd.read_csv('C:/Users/dammi/Documents/StrongxYolo5/runs/track/HandStrong(0.75,0.75)/tracks/handAndStand.txt', delimiter=' ', header=None, names=['Frame', 'ID'])

# Create the plot with the desired figure size
fig, axs = plt.subplots(figsize=(10, 6))  # Adjust the size as needed

# Plot data from the first file
axs.plot(df1['Frame'], df1['ID'], alpha=0.5, linewidth=2, color='blue', label='Hand: conf_thres=0.25, iou_thres=0.25')

# Plot data from the second file
axs.plot(df2['Frame'], df2['ID'], alpha=0.5, linewidth=2, color='red', label='Hand: conf_thres=0.5, iou_thres=0.5')

# Plot data from the third file
axs.plot(df3['Frame'], df3['ID'], alpha=0.5, linewidth=2, color='green', label='Hand: conf_thres=0.75, iou_thres=0.75')

# Draw lines at x=0 and y=0
axs.axhline(y=0, color='k', linewidth=1)  # Horizontal line at y=0
axs.axvline(x=0, color='k', linewidth=1)  # Vertical line at x=0

# Set the limits for x and y axes
axs.set_xlim([min(df1['Frame'].min(), df2['Frame'].min(), df3['Frame'].min()) - 1, max(df1['Frame'].max(), df2['Frame'].max(), df3['Frame'].max()) + 1])
axs.set_ylim([min(df1['ID'].min(), df2['ID'].min(), df3['ID'].min()) - 1, max(df1['ID'].max(), df2['ID'].max(), df3['ID'].max()) + 1])

# Add legends, labels, etc.
axs.legend()
axs.set_xlabel('Frames')
axs.set_ylabel('IDs')

plt.tight_layout()

# Save or display the plot
save_img = input("Do you want to save the plot? (y/n): ").strip().lower()
if save_img == 'y':
    file_name = input("Enter the filename for image: ").strip()
    file_path = f'{file_name}.jpg'  # Save as JPG
    fig.savefig(file_path, format='jpg', dpi=100)
    print(f"Plot saved as '{file_path}'.")
    plt.show()
elif save_img == 'n':
    plt.show()
else:
    print("Invalid input. Image not saved.")
