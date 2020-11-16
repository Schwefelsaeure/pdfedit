from PyQt5.QtWidgets import QApplication
from PyQt5.QtQuick import QQuickView
from PyQt5.QtCore import QUrl

if __name__ == '__main__':
    app = QApplication([])

    view = QQuickView()
    url = QUrl("view.qml")

    view.setSource(url)
    view.show()
    
    app.exec_()
