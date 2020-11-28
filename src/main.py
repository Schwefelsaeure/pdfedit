import argparse
import fitz

from PyQt5 import uic
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QApplication, QFileDialog

def parse_command_line_arguments():
    parser = argparse.ArgumentParser(description="pdfedit - a free an open source PDF editor")

    parser.add_argument("files", type=str, nargs="*",
                        help="Open the given file(s)")

    return parser.parse_args()

def run_qt_application():
    # Create GUI elements
    Form, Window = uic.loadUiType("./gui/main_window.ui")

    app = QApplication([])
    window = Window()
    form = Form()
    form.setupUi(window)
    svg_widget = QSvgWidget()

    # Configure GUI elements
    window.setCentralWidget(svg_widget)
    configure_qt_signals_and_slots(form, window, svg_widget)

    # Show the GUI
    window.show()
    app.exec_()

def configure_qt_signals_and_slots(form, window, svg_widget):
    form.action_open.triggered.connect(lambda: open_file_dialog(window, svg_widget))

def open_file_dialog(parent, svg_widget):
    # TODO: Use "tr()" to translate strings
    (filename, selected_filter) = QFileDialog.getOpenFileName(parent, "Open PDF File", "~", "PDF Files (*.pdf)")

    if filename:
        svg_string = convert_pdf_to_svg(filename)

        if svg_string != None:
            svg_widget.renderer().load(bytearray(svg_string, encoding="utf-8"))

def convert_pdf_to_svg(filename):
    doc = fitz.open(filename)

    if doc.pageCount > 0:
        page = doc.loadPage(0);

        svg_string = page.getSVGimage()
        return svg_string
    else:
        return None

if __name__ == "__main__":
    args = parse_command_line_arguments()

    run_qt_application()
