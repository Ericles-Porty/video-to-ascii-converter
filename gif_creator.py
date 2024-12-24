from PIL import Image, ImageDraw, ImageFont
import os


def ascii_to_image(ascii_text, image_size=(500, 500), font_size=10):
    """Converte texto ASCII em uma imagem."""
    font = ImageFont.truetype("consola.ttf", font_size)
    img = Image.new("RGB", image_size, "black")
    draw = ImageDraw.Draw(img)

    for i, line in enumerate(ascii_text.splitlines()):
        draw.text((5, i * font_size), line, font=font, fill="white")

    return img


def create_gif(ascii_dir, output_gif, fps=30, max_seconds=None):
    """Cria um GIF a partir dos frames ASCII."""
    frames = sorted(os.listdir(ascii_dir))
    if max_seconds:
        frames = frames[:fps * max_seconds]

    images = []
    for frame in frames:
        with open(f"{ascii_dir}/{frame}", "r") as f:
            ascii_text = f.read()
        images.append(ascii_to_image(ascii_text))

    images[0].save(output_gif, save_all=True, append_images=images[1:], duration=1000 / fps, loop=0)
    print(f"GIF criado: {output_gif}")
