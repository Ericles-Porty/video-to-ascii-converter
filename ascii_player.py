import argparse
from frame_loader import load_frames_from_file, load_frames_in_memory
from terminal_utils import display_frames

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ASCII Player")
    parser.add_argument('--fps', type=int, default=30, help='Frames per second')
    parser.add_argument('--memory', action='store_true', help='Load all frames in memory')
    parser.add_argument('--ascii-dir', type=str, default="ascii", help='Directory with ASCII frames')
    args = parser.parse_args()

    fps = args.fps
    ascii_dir = args.ascii_dir
    print(f"Running at {fps} fps")
    print(f"Memory mode: {'On' if args.memory else 'Off'}")

    if args.memory:
        frames = load_frames_in_memory(ascii_dir)
    else:
        frames = load_frames_from_file(ascii_dir)

    # from gif_creator import create_gif
    # create_gif("ascii", "bad_apple_ascii.gif", fps=30, max_seconds=5)

    display_frames(frames, fps)
