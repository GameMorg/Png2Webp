import os
from tkinter import *
from tkinter import filedialog
from PIL import Image

root = Tk()
root.title("Конвертер изображений")
root.geometry("400x300")


def convert_images():
    source_folder = filedialog.askdirectory(title="Выберите исходную папку")
    destination_folder = filedialog.askdirectory(title="Выберите папку назначения")
    quality = quality_scale.get()

    for filename in os.listdir(source_folder):
        if filename.endswith(".png"):
            image = Image.open(os.path.join(source_folder, filename))
            new_filename = filename[:-4] + ".webp"
            image.save(os.path.join(destination_folder, new_filename), "webp", quality=quality)
            print(f"Изображение {filename} сконвертированно")


quality_label = Label(root, text="Уровень сжатия (0-100):")
quality_label.pack()
quality_scale = Scale(root, from_=0, to=100, orient=HORIZONTAL)
quality_scale.pack()
convert_button = Button(root, text="Конвертируйте изображения", command=convert_images)
convert_button.pack()

root.mainloop()
