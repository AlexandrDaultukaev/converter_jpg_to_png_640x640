# This is a sample Python script.
from PIL import Image
from typing import Tuple, List
import os


def resize_image(input_image_path: str,
                 output_image_path: str,
                 size: Tuple[int, int]) -> None:
    original_image = Image.open(input_image_path)
    width, height = original_image.size

    resized_image = original_image.resize(size)
    width, height = resized_image.size
    resized_image.save(output_image_path)


def list_files(folder: str) -> List[str]:
    num = [f for f in os.listdir(folder)
           if os.path.isfile(os.path.join(folder, f))]
    return num


def formatting() -> None:
    folder_from = input("Введите папку, откуда брать изображения?\n")
    folder_to = input("Введите название папки, куда складывать изображения?\n")

    if not os.path.exists(folder_from):
        print("Такой папки не существует\n")

    try:
        os.mkdir(folder_to)
    except FileExistsError:
        pass

    try:
        os.mkdir("tmp")
    except FileExistsError:
        pass

    files = list_files(folder_from)

    for i in range(len(files)):
        os.rename(f"{folder_from}/{files[i]}", f"{folder_from}/{i}.{files[i].split('.')[1]}")

    for i in range(len(files)):
        im = Image.open(f"{folder_from}/{i}.{files[i].split('.')[1]}")
        im.save(f'tmp/{i}.png')

    for i in range(len(files)):
        resize_image(input_image_path=f'tmp/{i}.png',
                     output_image_path=f'{folder_to}/{i}.png',
                     size=(640, 640))

    for i in range(len(files)):
        os.remove(f'tmp/{i}.png')
    os.rmdir("tmp")


formatting()
