from reportlab.lib.pagesizes import A4, letter, landscape
from reportlab.pdfgen import canvas
import os
from PyPDF2 import PdfMerger


def create_pdf(path, width, height, text):
    c = canvas.Canvas(path, pagesize=(width, height))
    c.drawString(100, height - 100, text)
    c.showPage()
    c.save()


def create_mixed_size_pdf(output_path):
    os.makedirs("../data", exist_ok=True)
    temp_files = []
    # Create individual PDFs with different sizes and orientations
    sizes = [
        (595, 842, "A4 Portrait"),
        (842, 595, "A4 Landscape"),
        (612, 792, "Letter Portrait"),
        (792, 612, "Letter Landscape"),
        (1200, 1600, "Large Portrait"),
        (1600, 1200, "Large Landscape"),
        (2000, 3000, "Extra Large Portrait"),
        (3000, 2000, "Extra Large Landscape"),
        (300, 400, "Small Portrait"),
        (400, 300, "Small Landscape"),
    ]
    for i, (w, h, label) in enumerate(sizes):
        temp_path = f"../data/_temp_{i}.pdf"
        create_pdf(temp_path, w, h, label)
        temp_files.append(temp_path)
    # Merge into one PDF
    merger = PdfMerger()
    for temp in temp_files:
        merger.append(temp)
    merger.write(output_path)
    merger.close()
    # Clean up temp files
    for temp in temp_files:
        os.remove(temp)


if __name__ == "__main__":
    os.makedirs("../data", exist_ok=True)
    print("Test PDFs created in ../data/")
    create_mixed_size_pdf("../data/mixed_sizes.pdf")
    print("Mixed size PDF created as ../data/mixed_sizes.pdf")
