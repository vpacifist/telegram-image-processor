from rembg import remove
from PIL import Image, ImageFilter

def crop_image(input_image_path, output_image_path, crop_box):
    """
    Обрезка изображения.

    :param input_image_path: Путь к исходному изображению.
    :param output_image_path: Путь для сохранения обрезанного изображения.
    :param crop_box: Координаты обрезки в формате (left, upper, right, lower).
    """
    with Image.open(input_image_path) as img:
        cropped_image = img.crop(crop_box)
        cropped_image.save(output_image_path)

def remove_background(input_image_path, output_image_path):
    """
    Удаление фона с изображения.

    :param input_image_path: Путь к исходному изображению.
    :param output_image_path: Путь для сохранения изображения с удалённым фоном.
    """
    # Открываем изображение с помощью PIL
    with Image.open(input_image_path) as img:
        # Применяем функцию удаления фона
        output = remove(img)
        # Сохраняем изображение с удалённым фоном
        output.save(output_image_path)

def blur_avatar(input_image_path, output_image_path, blur_radius=10):
    """
    Применение размытия к аватарке.

    :param input_image_path: Путь к исходной аватарке.
    :param output_image_path: Путь для сохранения размытой аватарки.
    :param blur_radius: Радиус размытия (по умолчанию 10).
    """
    # Открываем изображение с помощью PIL
    with Image.open(input_image_path) as img:
        # Применяем фильтр GaussianBlur
        blurred_image = img.filter(ImageFilter.GaussianBlur(blur_radius))
        # Сохраняем изображение с эффектом размытия
        blurred_image.save(output_image_path)