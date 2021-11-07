# This is a sample Python script.
from PIL import Image
import os

def resize_image(input_image_path,
                 output_image_path,
                 size):
    original_image = Image.open(input_image_path)
    width, height = original_image.size

    resized_image = original_image.resize(size)
    width, height = resized_image.size
    resized_image.save(output_image_path)


for i in range(1, 101):
    im = Image.open(f'../Fake/{i}.jpg')
    im.save(f'../Fake_png/{i}.png')

for i in range(1, 101):
    resize_image(input_image_path=f'../Fake_png/{i}.png',
                 output_image_path=f'../Fake_png_640/{i}.png',
                 size=(640, 640))
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
