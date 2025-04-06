import os


def load_frames_from_file(ascii_dir):
    """Carrega os frames diretamente do diretório."""
    frames = sorted(os.listdir(ascii_dir))
    for frame in frames:
        with open(f"{ascii_dir}/{frame}", "r") as f:
            yield f.read()


def load_frames_in_memory(ascii_dir):
    """Carrega todos os frames na memória."""
    frames = sorted(os.listdir(ascii_dir))
    frames_in_memory = []
    for frame in frames:
        with open(f"{ascii_dir}/{frame}", "r") as f:
            frames_in_memory.append(f.read())
    return frames_in_memory
