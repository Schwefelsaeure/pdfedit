import argparse
import fitz

test_file = "../resources/test.pdf"

def parse_command_line_arguments():
    parser = argparse.ArgumentParser(description="pdfedit - a free an open source PDF editor")

    parser.add_argument("files", type=str, nargs="*",
                        help="Open the given file(s)")

    return parser.parse_args()

if __name__ == "__main__":
    args = parse_command_line_arguments()
    
    doc = fitz.open(test_file)
    
    if doc.pageCount > 0:
        page = doc.loadPage(0);
        
        txt = page.getSVGimage()
        with open("test.svg", "w") as file:
            file.write(txt)
