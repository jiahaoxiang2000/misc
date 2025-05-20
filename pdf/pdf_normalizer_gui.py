#!/usr/bin/env python3

import tkinter as tk
from tkinter import filedialog, messagebox
import os
import sys

sys.path.append(os.path.dirname(__file__))
from concatenate_pdfs import normalize_pdf_pages


class PDFNormalizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Normalizer")
        self.selected_file = None
        self.create_widgets()

    def create_widgets(self):
        self.select_btn = tk.Button(
            self.root, text="Select PDF", command=self.select_pdf
        )
        self.select_btn.pack(pady=10)
        self.file_label = tk.Label(self.root, text="No file selected")
        self.file_label.pack(pady=5)
        self.normalize_btn = tk.Button(
            self.root,
            text="Normalize PDF",
            command=self.normalize_pdf,
            state=tk.DISABLED,
        )
        self.normalize_btn.pack(pady=10)

    def select_pdf(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if file_path:
            self.selected_file = file_path
            self.file_label.config(text=os.path.basename(file_path))
            self.normalize_btn.config(state=tk.NORMAL)
        else:
            self.selected_file = None
            self.file_label.config(text="No file selected")
            self.normalize_btn.config(state=tk.DISABLED)

    def normalize_pdf(self):
        if not self.selected_file:
            messagebox.showwarning("No file", "Please select a PDF file first.")
            return
        output_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF Files", "*.pdf")],
            initialfile="normalized.pdf",
        )
        if not output_path:
            return
        try:
            result_path = normalize_pdf_pages(
                self.selected_file, output_path=output_path
            )
            messagebox.showinfo(
                "Success", f"PDF normalized and saved to:\n{result_path}"
            )
        except Exception as e:
            messagebox.showerror("Error", f"Failed to normalize PDF:\n{e}")


def main():
    root = tk.Tk()
    app = PDFNormalizerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
