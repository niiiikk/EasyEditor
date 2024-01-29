from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QListWidget, QHBoxLayout, QVBoxLayout, QFileDialog)
import os 
from PIL import Image, ImageFilter
from PyQt5.QtCore import Qt 
from PyQt5.QtGui import QPixmap

class ImageProcessor:
    def __init__(self) -> None:
        self.image = None
        self.dir = None
        self.file = None
        self.save_dir = "Modified/"
    def loadImage(self, dir, filename):
        file_path = os.path.join(dir, filename)
        self.dir = dir
        self.file = filename
        self.image = Image.open(file_path)
    def do_bw(self):
        self.image = self.image.convert('L')
        self.changeImage()
    def saveImage(self):
        path = os.path.join(work_dir, self.save_dir)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path, self.file)
        self.image.save(image_path)
    def sharp(self):
        self.image = self.image.filter(ImageFilter.SHARPEN)
        self.changeImage()
    # def left(self):
    #     self.image = self.image.transpose(Image.ROTATE_90)
    #     self.changeImage()
    # def mirror(self):
    #     self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
    #     self.changeImage()
    def changeImage(self):
        self.saveImage()
        imagepath = os.path.join(self.dir, self.save_dir, self.file)
        self.showImage(imagepath)
    def transpose(self, cons):
        self.image = self.image.transpose(cons)
        self.changeImage()
        








    def showImage(self, path):
        label_main.hide()
        pixmapimage = QPixmap(path)
        w, h = label_main.width(), label_main.height()
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        label_main.setPixmap(pixmapimage)
        label_main.show()

def showChosenImage():
    if files.currentRow() >= 0:
        filename = files.currentItem().text()
        image.loadImage(work_dir, filename)
        file_path = os.path.join(work_dir, filename)
        image.showImage(file_path)
        

        
image = ImageProcessor()

app = QApplication([])
window = QWidget()

window.setWindowTitle('Easy Editor')
window.resize(700, 500)

layout_main = QHBoxLayout()

layout_left = QVBoxLayout()
layout_right = QVBoxLayout()

button_folder = QPushButton(text='папка')
files = QListWidget()
layout_left.addWidget(button_folder)
layout_left.addWidget(files)
label_main = QLabel(text='картинка')
layout_button = QHBoxLayout()
LeftButton = QPushButton(text='влево')
RightButton = QPushButton(text='вправо')
MirrorButton = QPushButton(text='зеркало')
SharpnessButton = QPushButton(text='резкость')
HBButton = QPushButton(text='Ч/Б')

layout_button.addWidget(LeftButton)
layout_button.addWidget(RightButton)
layout_button.addWidget(MirrorButton)
layout_button.addWidget(SharpnessButton)
layout_button.addWidget(HBButton)

layout_right.addWidget(label_main)
layout_right.addLayout(layout_button)

layout_main.addLayout(layout_left, stretch=20)
layout_main.addLayout(layout_right, stretch=80)
window.setLayout(layout_main)


window.show()

work_dir = ''

def filter(files, extensions):
    result = list()
    for file in files:
        for extension in extensions:
            if file.endswith(extension):
                result.append(file)
    return result

def show_files():
    extensions = ['.jpg','.jpeg', '.png', '.gif', '.bmp']
    chooseWorkdir()
    filess = filter(os.listdir(path=work_dir), extensions)
    files.clear()
    files.addItems(filess)






def chooseWorkdir():
    global work_dir
    work_dir = QFileDialog.getExistingDirectory()

button_folder.clicked.connect(show_files)
files.currentRowChanged.connect(showChosenImage)
HBButton.clicked.connect(image.do_bw)
SharpnessButton.clicked.connect(image.sharp)
LeftButton.clicked.connect(lambda:image.transpose(Image.ROTATE_90))
RightButton.clicked.connect(lambda:image.transpose(Image.ROTATE_270))
MirrorButton.clicked.connect(lambda:image.transpose(Image.FLIP_LEFT_RIGHT))

app.exec_()