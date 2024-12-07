import pytesseract
from PIL import Image
from screenshooter import screenshot
import keyboard
import pyautogui
from prompts import get_ai_response
from json import dumps
import webbrowser
from time import sleep


webbrowser.open('https://www.endquiz.com/quiz.php')


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

    prompt = "I will give you text from a quiz website. I want you to find the first question in it and identify it's answers. Select the correct one and return only it's text, no extra words.\n\nUse only words that are in the provided text. Give only raw answer, no extra words.\n###\n"
    answer = get_ai_response(prompt + text)
    print(answer)
    find_text_coords(image_path, answer)

def all_indexes(data, word):
    indexes = []
    for i, item in enumerate(data):
        if item == word:
            indexes.append(i)
    return indexes

def find_match(sentence, data):
    prompt = f"I will give you a list of pairs (int, string) and I want you to find the index of the first word of the sentence \"{sentence}\" when looking only on second elements in pairs. The strings can be faulty and might not match the sentence exactly, find the best possible match.\n\nReturn only raw index, no extra text."
    
    prompt += dumps(list(enumerate(data)))
    answer = get_ai_response(prompt)

    return int(answer.strip())


def find_text_coords(image_path, search_text):
    # Load the image using PIL
    image = Image.open(image_path)

    # Perform OCR on the image to get detailed data
    data = pytesseract.image_to_data(image, lang="eng", output_type=pytesseract.Output.DICT)
    print(data)
    data_string = dumps(data["text"])
    index = find_match(search_text, data["text"])
    (x, y, w, h) = (data['left'][index], data['top'][index], data['width'][index], data['height'][index])
    click(x + w//2, y+h//2)


def click(x, y):
    pyautogui.click(x, y)


while True:
    if keyboard.is_pressed("a+i"):
        read_screenshot()
    #sleep(4)
    #read_screenshot()

    if keyboard.is_pressed("c"):
        break
