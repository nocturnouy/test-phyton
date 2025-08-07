import os
import curses
import subprocess

def main(stdscr):
    # Clear screen
    stdscr.clear()
    curses.curs_set(0)  # Hide cursor

    directory = './videos'
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    selected = 0

    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "Select a file and press Enter:")

        for idx, file in enumerate(files):
            if idx == selected:
                stdscr.addstr(idx + 1, 0, f"> {file}", curses.A_REVERSE)
            else:
                stdscr.addstr(idx + 1, 0, f"  {file}")

        key = stdscr.getch()
        if key == curses.KEY_UP and selected > 0:
            selected -= 1
        elif key == curses.KEY_DOWN and selected < len(files) - 1:
            selected += 1
        elif key == ord('\n'):
            # stdscr.clear()
            # stdscr.addstr(0, 0, f"You selected: {files[selected]}")
            # stdscr.refresh()
            # stdscr.getch()
            subprocess.run(['python3', 'play.py', str(selected)])
            break

        stdscr.refresh()

if __name__ == "__main__":
    curses.wrapper(main)
