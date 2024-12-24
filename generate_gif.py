from gif_creator import create_gif
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ASCII to GIF")
    parser.add_argument('--ascii-dir', type=str, default="ascii", help='Directory with ASCII frames')
    parser.add_argument('--fps', type=int, default=30, help='Frames per second')
    parser.add_argument('--max-seconds', type=int, help='Max seconds')
    parser.add_argument('--output', type=str, default="output.gif", help='Output GIF')
    args = parser.parse_args()

    create_gif(args.ascii_dir, args.output, fps=args.fps, max_seconds=args.max_seconds)
