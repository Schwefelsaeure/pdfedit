import fitz

test_pdf_input = "../../resources/inkscape.pdf"
test_svg_output = "test.svg"

def convert_pdf_to_svg(pdffile, filename):
    doc = fitz.open(pdffile)
    
    if doc.pageCount > 0:
        page = doc.loadPage(0);
        
        svg_string = page.getSVGimage()
        
        with open(test_svg_output, "w") as f:
            f.write(svg_string)

if __name__ == "__main__":
    print("Converting \"{}\" to \"{}\"...".format(test_pdf_input, test_svg_output))
    convert_pdf_to_svg(test_pdf_input, test_svg_output)
    print("Conversion finished.")
