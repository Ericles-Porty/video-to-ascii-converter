from PIL import Image
from messages_gui import no_directory_frames_found, sucess_message
import os


def image_to_ascii(image_path, width=100):
    chars = "@%#*+=-:. "  # Gradiente de intensidade
    num_chars = len(chars)  # Número de caracteres disponíveis
    scale_factor = 256 // num_chars  # Tamanho do intervalo para cada caractere

    img = Image.open(image_path).resize((width, width // 2)).convert("L")  # Redimensiona e converte para grayscale
    pixels = img.getdata()

    # Mapeia cada pixel para um caractere, garantindo que o índice esteja dentro do limite
    ascii_str = "".join([chars[min(pixel // scale_factor, num_chars - 1)] for pixel in pixels])

    # Quebra a string para formar linhas de comprimento igual ao `width`
    ascii_img = "\n".join([ascii_str[i:i + width] for i in range(0, len(ascii_str), width)])
    return ascii_img

def convert_frames_to_ascii(frames_dir="frames", ascii_dir="ascii", width=100):
    # Verifica se o diretório "frames" existe
    if not os.path.exists(frames_dir):
        no_directory_frames_found()
        return

    # Converter todos os frames
    os.makedirs(ascii_dir, exist_ok=True)

    for file in sorted(os.listdir(frames_dir)):
        ascii_art = image_to_ascii(f"{frames_dir}/{file}", width)
        with open(f"{ascii_dir}/{file}.txt", "w") as f:
            f.write(ascii_art)

    sucess_message()