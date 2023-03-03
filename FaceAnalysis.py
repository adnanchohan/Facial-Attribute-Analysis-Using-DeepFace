from deepface import DeepFace as df
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
from PyQt5 import uic

class runFaceAnalysis(QMainWindow):
    def __init__(self):
        super(runFaceAnalysis, self).__init__()

        uic.loadUi("RunFaceAnalysis.ui", self)

        self.openImage.clicked.connect(self.clicker)
        self.exit.clicked.connect(self.appQuit)
        self.runAnalysis.clicked.connect(self.anaysis)

        # self.show()

    def clicker(self):

        self.fname = QFileDialog.getOpenFileName(self, "Open File", "d:\\MyProjects\\FYP\\Main Project\\UnknownFaces", "All Files (*);; PNG Files (*.png);;Jpg FIles (*.jpg)")

        self.pixmap = QPixmap(self.fname[0])
        self.imageView.setPixmap(self.pixmap)

    def appQuit(self):
        app.quit()

    def anaysis(self):
        # img_path = self.fname[0]
        a = df.analyze(self.fname[0])

        e, b, c, d = a['age'], a['gender'], a['dominant_race'], a['dominant_emotion']
        # print(e, b, c, d)
        self.age.setText(f'{e}')
        self.gender.setText(f'{b}')
        self.race.setText(f'{c}')
        self.emotion.setText(f'{d}')

app = QApplication(sys.argv)
UIWindow = runFaceAnalysis()
app.exec_()