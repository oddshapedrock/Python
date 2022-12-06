
from PIL import Image
from pytesseract import pytesseract
import pyautogui
import time

while True:
    
    
    im = pyautogui.screenshot()
    im2 = pyautogui.screenshot('my_screenshot.png',region=(94,182,1169,157))
    # im2 = pyautogui.screenshot('my_screenshot.png')

    path_to_image = 'my_screenshot.png'

    tess_path = r'C:\Users\SAH00113\AppData\Local\Tesseract-OCR\tesseract.exe'

    pytesseract.tesseract_cmd = tess_path

    img = Image.open(path_to_image)

    text = pytesseract.image_to_string(img)
    print(text)

    pyautogui.write(text)
    
    pyautogui.press('enter')
    pyautogui.press('enter')
    