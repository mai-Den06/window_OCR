import os
import time

from windowcapture import WindowCapture
from get_text import OCRProcessor


# Change the current working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# The window name is the name of the window that you want to capture.
# You can run the show_window_names.py script to get the names of all the windows that are currently open.
window_name = ""
wincap = WindowCapture(window_name)
ocr_processor = OCRProcessor()

previous_detected_texts = None
while True:

    # Get an updated image of the game
    screenshot = wincap.get_screenshot()

    # Run OCR on the screenshot
    detected_texts = ocr_processor.run_ocr(screenshot)

    # Only print the detected texts if they have changed
    if detected_texts != previous_detected_texts:
        previous_detected_texts = detected_texts
        print(detected_texts)

    time.sleep(3)

print('Done.')
