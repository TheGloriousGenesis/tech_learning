# install pdfminer.six
# install brew install pandoc
from pdfminer.high_level import extract_text
import pypandoc

# Extract raw text from PDF
text = extract_text("BigDataLdn2025.pdf")

if __name__ == "__main__":
    # Convert text to Markdown
    pypandoc.convert_text(text, "md", format="md", outputfile="output.md", extra_args=["--standalone"])
