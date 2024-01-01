import os
from PyQt5.QtWidgets import QFileDialog, QApplication, QMainWindow, QPushButton
from docx2pdf import convert

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Конвертер docx в pdf")
        self.setGeometry(300, 300, 400, 200)

        self.btn_open_folder = QPushButton('Выбрать папку', self)
        self.btn_open_folder.move(100, 50)
        self.btn_open_folder.clicked.connect(self.open_folder_dialog)

        self.show()

    def open_folder_dialog(self):
        folder_path = QFileDialog.getExistingDirectory(self, 'Выбрать папку')
        if folder_path:
            self.convert_to_pdf(folder_path)

    @staticmethod
    def convert_to_pdf(folder_path):
        for file_name in os.listdir(folder_path):
            if file_name.endswith('.doc') or file_name.endswith('.docx'):
                file_path = os.path.join(folder_path, file_name)
                out_path = os.path.join(folder_path, f"{os.path.splitext(file_name)[0]}.pdf")
                convert(file_path, out_path)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
