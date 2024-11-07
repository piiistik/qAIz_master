import pytesseract
from PIL import Image
from screenshooter import screenshot
import keyboard


def read_screenshot():
    screenshot()

    # Path to the Tesseract executable (required if not in your PATH)
    # Uncomment and update the path if Tesseract isn't in your PATH.

    pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

    # Load the image file
    image_path = "screenshots\\screenshot.png"
    image = Image.open(image_path)

    # Perform OCR on the image
    text = pytesseract.image_to_string(image, lang="eng", config="--psm 6")

    print("Extracted Text:")
    print(text)


while True:
    if keyboard.is_pressed("a") and keyboard.is_pressed("s"):
        read_screenshot()
