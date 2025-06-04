Certainly! Here's a revised `README.md` tailored to your script, which serves as a "Doge Filter" by highlighting potentially problematic words in grant applications:

---

# DOGE Filter: Grant Proposal Word Highlighter

**DOGE Filter** is a Python script designed to assist grant writers by highlighting words and phrases in PDF documents that may trigger scrutiny or rejection in grant applications. T

## 🚀 Features

* **PDF Highlighting**: Automatically highlights specified words and phrases in a PDF document.
* **Customizable Word List**: Modify the list of target words to suit specific grant guidelines.
* **Adjustable Highlight Colors**: Change the color of highlights to differentiate categories or levels of concern.

## 🛠 Installation

Ensure you have Python 3.7 or higher installed. Then, install the required library:

```bash
pip install pymupdf
```

## 📄 Usage

1. **Set the PDF File Path**: Update the `FILE_NAME` variable in the script to point to your PDF file.

   ```python
   FILE_NAME = '/path/to/your/document.pdf'
   ```

2. **Customize Target Words**: Modify the `TARGET_WORDS` list to include words or phrases you want to highlight.

   ```python
   TARGET_WORDS = [
       "activism", "equity", "diverse", "inclusive", "systemic", "LGBTQ", "female", "race", "justice", "bias"
   ]
   ```

3. **Run the Script**: Execute the script to generate a new PDF with highlighted terms.

   ```bash
   python doge_filter.py
   ```

   The output will be saved as `highlighted.pdf` in the same directory.

## 🎨 Customizing Highlight Colors

To change the highlight color, locate the following lines in the script:

```python
annot = page.add_highlight_annot(rects)
annot.set_colors(stroke=(1, 0, 0))  # Red color
annot.update()
```

Modify the `stroke` parameter to your desired RGB color:

* **Red**: `(1, 0, 0)`
* **Yellow**: `(1, 1, 0)`
* **Green**: `(0, 1, 0)`
* **Blue**: `(0, 0, 1)`

For example, to change the highlight color to yellow:

```python
annot.set_colors(stroke=(1, 1, 0))  # Yellow color
```
---
For inquiries email me at brunohg@umich.edu


