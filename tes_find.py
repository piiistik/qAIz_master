import pytesseract
from pytesseract import Output
import cv2

# Set path to tesseract executable (if necessary)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update path if different

# Load the image
image_path = '/path/to/your/image.png'
image = cv2.imread(image_path)

# Perform OCR on the image
data = pytesseract.image_to_data(image, output_type=Output.DICT)

# Search for specific text and get its coordinates
target_text = "B. yolk"  # The exact text you're looking for
found_coordinates = []

# Loop through all detected text
for i in range(len(data['text'])):
    if data['text'][i].strip().lower() == target_text.lower():  # Case-insensitive match
        x = data['left'][i]
        y = data['top'][i]
        width = data['width'][i]
        height = data['height'][i]
        found_coordinates.append((x, y, width, height))

        # Draw a rectangle around the found text (optional for visualization)
        cv2.rectangle(image, (x, y), (x + width, y + height), (0, 255, 0), 2)

# Save or display the output image with rectangles (optional)
output_path = '/path/to/output_image_with_boxes.png'
cv2.imwrite(output_path, image)
cv2.imshow("Detected Text", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Print found coordinates
if found_coordinates:
    print(f"Coordinates of '{target_text}': {found_coordinates}")
else:
    print(f"'{target_text}' not found in the image.")
