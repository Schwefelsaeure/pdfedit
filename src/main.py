import argparse
import fitz
import os

from PyQt6 import uic
from PyQt6.QtCore import QCoreApplication
from PyQt6.QtCore import QLocale
from PyQt6.QtCore import QTranslator
from PyQt6.QtSvgWidgets import QSvgWidget
from PyQt6.QtWidgets import QApplication, QFileDialog, QGridLayout

def parse_command_line_arguments():
    parser = argparse.ArgumentParser(description="pdfedit - a free an open source PDF editor")

    parser.add_argument("files", type=str, nargs="*",
                        help="Open the given file(s)")

    return parser.parse_args()

def run_qt_application():
    # Create GUI elements
    Form, Window = uic.loadUiType("./gui/main_window.ui")

    app = QApplication([])
    load_translator("en_US.qm", app)

    window = Window()
    form = Form()
    form.setupUi(window)

    # Configure GUI elements
    # window.setCentralWidget(svg_widget)
    configure_qt_signals_and_slots(form, window)

    # Show the GUI
    window.show()
    app.exec()

def load_translator(filename, app):
    translator = QTranslator()
    search_directory = "i18n"

    if translator.load(filename, search_directory):
        app.installTranslator(translator)

def configure_qt_signals_and_slots(form, window):
    form.action_open.triggered.connect(lambda: open_file_dialog(window, form))
    tabs = form.tab_open_documents
    tabs.tabCloseRequested.connect(lambda index: tabs.removeTab(index))

def open_file_dialog(parent, form):
    # TODO: Use "tr()" to translate strings
    (filename, selected_filter) = QFileDialog.getOpenFileName(parent,
                                                              QCoreApplication.translate("open_file_dialog", "Open PDF File"),
                                                              "",
                                                              "PDF (*.pdf)")

    if filename:
        svg_string = convert_pdf_to_svg(filename)

        if svg_string != None:
            delete_welcome_tab_if_present(form)

            svg_widget = QSvgWidget()
            svg_widget.renderer().load(bytearray(svg_string, encoding="utf-8"))

            file_basename = os.path.basename(filename)
            form.tab_open_documents.addTab(svg_widget, file_basename)

            # TODO: Define a reasonable thumbnail size of m x n pixels and set size here.
            grid = QGridLayout()
            form.page_pdf_pages.setLayout(grid)
            svg_thumbnails = create_page_thumbnails(filename)

            for svg_thumbnail in svg_thumbnails:
                svg_widget = QSvgWidget()
                svg_widget.renderer().load(bytearray(svg_thumbnail, encoding="utf-8"))
                svg_widget.resize(20, 30)
                grid.addWidget(svg_widget)

def delete_welcome_tab_if_present(form):
    tab_widget = form.tab_open_documents
    tab_index = tab_widget.indexOf(form.welcome_tab)

    if tab_index >= 0:
        tab_widget.removeTab(tab_index)

def create_page_thumbnails(filename):
    pages_as_svg = []

    doc = fitz.open(filename)

    for page_number in range(0, doc.pageCount):
        print("Creating thumbnail page {}".format(page_number + 1))
        page = doc.loadPage(page_number);
        svg_string = page.getSVGimage()
        pages_as_svg.append(svg_string)

    return pages_as_svg

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
