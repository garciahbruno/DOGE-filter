
````markdown
# 📄 PDF Word Highlighter

A Python script that highlights specific words or phrases in a PDF using the [`PyMuPDF`](https://pymupdf.readthedocs.io/) library.

---

## 🔧 Requirements

- Python 3.7 or higher  
- [`PyMuPDF`](https://pypi.org/project/PyMuPDF/)

Install it with:

```bash
pip install pymupdf
````

---

## 🗂 Setup

1. Set the path to your PDF in the `FILE_NAME` variable:

```python
FILE_NAME = '/Users/yourname/Downloads/yourfile.pdf'
```

2. Edit the `TARGET_WORDS` list to include the words or phrases you want to highlight:

```python
TARGET_WORDS = ["diverse", "equity", "justice", ...]
```

---

## 🎨 Change Highlight Color

To customize the highlight color, change this line:

```python
annot.set_colors(stroke=(R, G, B))
```

Common colors:

* Red: `(1, 0, 0)`
* Yellow: `(1, 1, 0)`
* Green: `(0, 1, 0)`
* Blue: `(0, 0, 1)`

Don’t forget to follow it with:

```python
annot.update()
```

---

## 🚀 Run the Script

```bash
python your_script.py
```

A new file called `highlighted.pdf` will be saved in the same directory, with all matching words highlighted.

```

Let me know if you want it themed (e.g. dark mode badge, emoji-free, ultra-minimalist, etc.).
```
## 🛠️ Need Help?
If you are having issues installing it I recommend asking ChatGPT or shoot me an email at brunohg@umich.edu
