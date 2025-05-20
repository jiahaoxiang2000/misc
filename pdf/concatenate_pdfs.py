#!/usr/bin/env python3

import os
import sys
import argparse
from PyPDF2 import PdfMerger, PdfReader, PdfWriter
import tempfile


def normalize_pdf_pages(input_path, a4_width=595, a4_height=842, output_path=None):
    """Normalize pages to standard size. If output_path is given, write to it."""
    reader = PdfReader(input_path)
    writer = PdfWriter()
    modified = False
    for page in reader.pages:
        width = float(page.mediabox.width)
        height = float(page.mediabox.height)
        # Scale up if too small, scale down if too large
        if (
            width > a4_width * 1.1
            or height > a4_height * 1.1
            or width < a4_width * 0.9
            or height < a4_height * 0.9
        ):
            scale_x = a4_width / width
            scale_y = a4_height / height
            scale = min(scale_x, scale_y)
            page.scale(scale, scale)
            modified = True
        writer.add_page(page)
    if modified or output_path:
        if not output_path:
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
            temp_path = temp_file.name
            temp_file.close()
        else:
            temp_path = output_path
        with open(temp_path, "wb") as output_file:
            writer.write(output_file)
        return temp_path
    return input_path


def concatenate_pdfs(output_path="combined.pdf", input_dir="."):
    # Create a PdfMerger object
    merger = PdfMerger()

    # Get all PDF files in the specified directory
    pdf_files = [f for f in os.listdir(input_dir) if f.endswith(".pdf")]

    # Sort the files by name
    pdf_files.sort(
        key=lambda x: (
            int(x.split(".")[0]) if x.split(".")[0].isdigit() else float("inf")
        )
    )

    print(f"Found {len(pdf_files)} PDF files in '{input_dir}': {', '.join(pdf_files)}")

    temp_files = []  # Track created temporary files for cleanup

    # Add each PDF file to the merger
    for pdf in pdf_files:
        try:
            pdf_path = os.path.join(input_dir, pdf)
            print(f"Processing {pdf_path}")
            # Normalize the PDF pages before appending
            normalized_path = normalize_pdf_pages(pdf_path)

            if normalized_path != pdf_path:
                temp_files.append(normalized_path)
                print(f"  - Normalized pages in {pdf}")

            print(f"  - Adding to merged document")
            merger.append(normalized_path, import_outline=False)
        except Exception as e:
            print(f"Error processing {pdf}: {e}")
            print("Skipping this file and continuing...")
            continue

    # Write the merged PDF to the output file
    if len(merger.pages) > 0:
        print(f"Writing combined PDF to {output_path}")
        merger.write(output_path)
        merger.close()
        print(f"Successfully created {output_path}")
    else:
        print("No valid PDF files were found or processed.")
        return False

    # Clean up temporary files
    for temp_file in temp_files:
        try:
            os.remove(temp_file)
        except:
            pass

    return True


if __name__ == "__main__":
    # Set up argument Parser
    parser = argparse.ArgumentParser(
        description="Concatenate PDF files in current directory. Files are combined in numerical order "
        "if filenames start with numbers (e.g., 1.pdf, 2.pdf, 10.pdf), "
        "otherwise alphabetically."
    )
    parser.add_argument(
        "-o",
        "--output",
        default="combined.pdf",
        help="Output file path (default: combined.pdf)",
    )
    parser.add_argument(
        "-d",
        "--directory",
        default=".",
        help="Directory containing PDF files (default: current directory)",
    )
    args = parser.parse_args()

    # Run with the specified output path and input directory
    success = concatenate_pdfs(output_path=args.output, input_dir=args.directory)
    if not success:
        sys.exit(1)
