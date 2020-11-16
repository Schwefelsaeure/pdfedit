from PyQt5.QtWidgets import QApplication, QWidget, QLabel

if __name__ == '__main__':
    app = QApplication([])
    window = QWidget()
    
    label = QLabel(window)
    label.setText("Hello World!")
    label.move(110, 85)
    
    window.setGeometry(0, 0, 320, 200)
    window.setWindowTitle("PyQt5: Hello World")
    window.show()
    
    app.exec_()
