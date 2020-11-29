import argparse
import fitz
import os

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

    # Configure GUI elements
    # window.setCentralWidget(svg_widget)
    configure_qt_signals_and_slots(form, window)

    # Show the GUI
    window.show()
    app.exec_()

def configure_qt_signals_and_slots(form, window):
    form.action_open.triggered.connect(lambda: open_file_dialog(window, form))
    tabs = form.tab_open_documents
    tabs.tabCloseRequested.connect(lambda index: tabs.removeTab(index))

def open_file_dialog(parent, form):
    # TODO: Use "tr()" to translate strings
    (filename, selected_filter) = QFileDialog.getOpenFileName(parent, "Open PDF File", "~", "PDF Files (*.pdf)")

    if filename:
        svg_string = convert_pdf_to_svg(filename)

        if svg_string != None:
            delete_welcome_tab_if_present(form)

            svg_widget = QSvgWidget()
            svg_widget.renderer().load(bytearray(svg_string, encoding="utf-8"))

            # TODO: Show only basename(filename) and not complete path.
            file_basename = os.path.basename(filename)
            form.tab_open_documents.addTab(svg_widget, file_basename)

def delete_welcome_tab_if_present(form):
    tab_widget = form.tab_open_documents
    tab_index = tab_widget.indexOf(form.welcome_tab)

    if tab_index >= 0:
        tab_widget.removeTab(tab_index)

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
