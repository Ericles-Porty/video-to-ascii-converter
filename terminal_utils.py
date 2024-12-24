import os
import time


def clear_terminal():
    """Limpa o terminal."""
    os.system("cls" if os.name == "nt" else "clear")


def display_frames(frames, frame_rate):
    """Exibe os frames no terminal."""
    for frame in frames:
        print(frame)
        time.sleep(1 / frame_rate)
        clear_terminal()
