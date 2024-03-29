# README

The goal is to implement a free and open-source PDF editor using Python and Qt.

Design principles:
- Keep It Simple, Stupid (KISS)!
- Write unit tests (for non-GUI parts).
- Use Qt as GUI framework and PyMuPDF to access PDF functionalities.

## For developers

### Install dependencies

For Arch Linux:

```
sudo pacman -S install qt6-base qt6-tools qtcreator python-pyqt6
pip install -r requirements.txt
```

**Note:** This also installs two useful Qt programs: [Qt Designer](https://doc.qt.io/qt-5/qtdesigner-manual.html) and [Qt Creator](https://doc.qt.io/qtcreator/index.html). Both applications offer a WYSIWYG editor to easily create GUIs.

Run test files:

```
cd <repo>/resources/test_dependencies/
python3 test_pymupdf.py 
python3 test_pyqt_qml.py
python3 test_pyqt_qtwidgets.py
```
