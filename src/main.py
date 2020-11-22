import argparse
import fitz

from PyQt5 import uic
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QApplication

test_pdf_input = "../resources/inkscape.pdf"
test_svg_output = "test.svg"

def parse_command_line_arguments():
    parser = argparse.ArgumentParser(description="pdfedit - a free an open source PDF editor")

    parser.add_argument("files", type=str, nargs="*",
                        help="Open the given file(s)")

    return parser.parse_args()

def convert_pdf_to_svg(pdffile, filename):
    doc = fitz.open(pdffile)
    
    if doc.pageCount > 0:
        page = doc.loadPage(0);
        
        svg_string = page.getSVGimage()
        return svg_string
    else:
        return None

def run_qt_application(svg_string):
    Form, Window = uic.loadUiType("./gui/main_window.ui")

    app = QApplication([])

    window = Window()
    form = Form()
    form.setupUi(window)
    window.show()

    svg_widget = QSvgWidget()
    svg_widget.renderer().load(bytearray(svg_string, encoding="utf-8"))

    window.setCentralWidget(svg_widget)

    app.exec_()

if __name__ == "__main__":
    args = parse_command_line_arguments()
    
    svg_string = convert_pdf_to_svg(test_pdf_input, test_svg_output)
    
    if svg_string != None:
        run_qt_application(svg_string)
