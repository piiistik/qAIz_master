import pytesseract
from PIL import Image

# Path to the Tesseract executable (required if not in your PATH)
# Uncomment and update the path if Tesseract isn't in your PATH.
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load the image file
image_path = "path_to_your_image_file.png"
image = Image.open(image_path)

# Perform OCR on the image
text = pytesseract.image_to_string(image)

print("Extracted Text:")
print(text)