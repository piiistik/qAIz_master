from PIL import ImageGrab

def screenshot():
    # Capture the entire screen
    screenshot = ImageGrab.grab()

    # Save the screenshot to a file
    screenshot.save("screenshots\\screenshot.png")

    # Close the screenshot
    screenshot.close()