import os
import sys
import time
import tty
import termios
import subprocess
import socket
import json

def getch():
    """Get a single character from standard input (works on Unix)."""
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

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

# Set up mpv IPC socket
socket_path = '/tmp/mpvsocket'
if os.path.exists(socket_path):
    os.remove(socket_path)

mpv_cmd = [
    'mpv',
    file_path,
    f'--input-ipc-server={socket_path}',
    '--force-window=yes',  # always show window
    '--pause=no',
    '--loop',  # loop the video
]
mpv_proc = subprocess.Popen(mpv_cmd)

# Wait for mpv to create the socket
for _ in range(60):
    if os.path.exists(socket_path):
        break
    time.sleep(0.1)
else:
    print("Failed to connect to mpv IPC socket.")
    mpv_proc.terminate()
    sys.exit(1)

def mpv_command(command, args=None):
    if not os.path.exists(socket_path):
        return  # Socket is gone, mpv has quit
    msg = {"command": [command] + ([] if args is None else args)}
    try:
        with socket.socket(socket.AF_UNIX) as client:
            client.connect(socket_path)
            client.sendall((json.dumps(msg) + '\n').encode('utf-8'))
    except (ConnectionRefusedError, FileNotFoundError, BrokenPipeError):
        pass  # mpv has already quit or socket is closed

print("Press '7' to rewind 1 second, 'q' to quit.")

try:
    while True:
        key = getch()
        if key == '7':
            mpv_command('seek', ['-1'])
        elif key == 'q':
            mpv_command('quit')
            break
finally:
    mpv_proc.wait()
    if os.path.exists(socket_path):
        os.remove(socket_path)
