import argparse
import os
from messages_gui import no_directory_ascii_found
from frame_loader import load_frames_from_file, load_frames_in_memory
from terminal_utils import display_frames

def run_ascii_player(fps, memory, ascii_dir="ascii"):
    if not os.path.isdir(ascii_dir):
        no_directory_ascii_found()
        return
    
    print(f"Running at {fps} fps")
    print(f"Memory mode: {'On' if memory else 'Off'}")

    if memory:
        frames = load_frames_in_memory(ascii_dir)
    else:
        frames = load_frames_from_file(ascii_dir)

    display_frames(frames, fps)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ASCII Player")
    parser.add_argument('--fps', type=int, default=30, help='Frames per second')
    parser.add_argument('--memory', action='store_true', help='Load all frames in memory')
    parser.add_argument('--ascii-dir', type=str, default="ascii", help='Directory with ASCII frames')
    args = parser.parse_args()

    run_ascii_player(fps=args.fps, memory=args.memory, ascii_dir=args.ascii_dir)
