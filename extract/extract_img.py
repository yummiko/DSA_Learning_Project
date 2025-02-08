from PIL import Image
import pytesseract

# Load the uploaded image
image_path = "extract/picturefolder/chapter3_reinforcement1.png"
image = Image.open(image_path)

# Extract text from the image using pytesseract
extracted_text = pytesseract.image_to_string(image)

# Render the text with Markdown formatting
def format_as_markdown(text):
    # Replace key patterns with Markdown math syntax
    text = text.replace("^", "**")  # Replace caret with Markdown power operator
    text = text.replace("log", "\\log")  # Math log formatting
    text = text.replace("O(", "\\mathcal{O}(")  # Big-O notation
    text = text.replace("n0", "n_0")  # Subscript
    return text

# Process and render the text
markdown_text = format_as_markdown(extracted_text)
print(markdown_text)