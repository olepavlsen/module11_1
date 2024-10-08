from PIL import Image, ImageFilter

# Открытие изображения и его отображение на экране:
image = Image.open('flower.jpg')
image.show()

# Конвертирование из JPG в PNG:
flower = Image.open("flower.jpg")
flower.save('flower.png', 'png')

# Создание миниатюры:
image = Image.open('flower.jpg')
image.thumbnail((200, 200))
image.save('flower_thumbnail.jpg')

# Размытие изображения:
# размываем изображение
original = Image.open("flower.png")
blurred = original.filter(ImageFilter.BLUR)

# открываем оригинал и размытое изображение
original.show()
blurred.show()

# сохраняем изображение
blurred.save("blurred.png")

# Обрезка изображений через crop
image = Image.open('flower.jpg')
cropped = image.crop((200, 200, 800, 1000))
cropped.save('cropped_flower.jpg')
cropped.show()

# Поворачивание изображения — метод rotate
flower_1 = Image.open("flower.jpg")
rotated = flower_1.rotate(180)
rotated.save('flower_rotated.jpg')
rotated.show()