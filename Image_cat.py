# 1) Открой файл фотографии и выведи его свойства (размер, формат, цветовой тип) в консоль.

# 2) Сделай оригинал чёрно-белым. Снова выведи свойства и сравни со свойствами оригинала. Что изменилось? Сохрани картинку как gray.jpg.

# 3) Сделай оригинал размытым. Сохрани картинку как blured.jpg.

# 4) Переверни оригинал на 180 градусов. Сохрани картинку как up.jpg.

from PIL import Image, ImageFilter

with Image.open('cat.jpg') as original:
    print(original.size)
    print(original.format)
    print(original.mode)
    original.show()


    cat_gray = original.convert('L')
    print(cat_gray.size)
    print(cat_gray.format)
    print(cat_gray.mode)
    cat_gray.save('gray.jpg')
    cat_gray.show()

    cat_gray = original.filter(ImageFilter.BLUR)
    cat_gray.save('blured.jpg')
    cat_gray.show()

    cat_gray = original.transpose(Image.ROTATE_180)
    cat_gray.save('up.jpg')
    cat_gray.show()

    





