import os
import subprocess
import sys

# Get the number of videos to play from the command-line argument
num_videos = int(sys.argv[1]) if len(sys.argv) > 1 else 0

# Specify the directory path
directory = './videos'

# Get a list of all files in the directory
files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and f.endswith('.mp4')]

# Check if any MP4 files were found
if files:
    try:
        file_path = os.path.join(directory, files[num_videos])
    except IndexError:
        file_path = os.path.join(os.getcwd(), 'default.png')
else:
    file_path = os.path.join(os.getcwd(), 'default.png')

print(f"Playing video: {file_path}")

parameters = [ '--start-time=1', '--stop-time=2', '--repeat', '--no-audio']  # Optional parameters for VLC
subprocess.run(['vlc', *parameters, file_path])
