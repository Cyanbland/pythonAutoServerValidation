import pytesseract
import pyautogui
import time
from random import randint, randrange
try:
    from PIL import Image
except ImportError:
    import Image

#windows 220 zoom
#X check box 598 - 647
#Y check box 630 - 677

pytesseract.pytesseract.tesseract_cmd = r'F:\Program Files\Tesseract-OCR\tesseract.exe'


def main():
    option = str(input("Do you want to start the program now?"))
    if option in ['sim', 's', 'si', 'yes', 'y']:
        get_screenshot(0)
        time.sleep(2)
        current_value = ocr_core(r'C:\Users\Usuario\PycharmProjects\exercises\minecraft-server\imgs\0.png')
        print("First value is %s" % (current_value))

        while True:
            index = 1

            get_screenshot(index)
            time.sleep(2)
            current_value = ocr_core(r'C:\Users\Usuario\PycharmProjects\exercises\minecraft-server\imgs\%s.png' % (str(index)))
            random_threshold = randint(5, 15)
            print(random_threshold)
            if current_value == str(random_threshold):
                #click renew
                print("clicking renew")
                pyautogui.click(x = 362, y = 860)
                time.sleep(randrange(1, 5))

                randomx = randrange(598, 647)
                randomy = randrange(630, 677)
                #click captcha
                pyautogui.click(x = randomx, y = randomy)

            print("Value is %s " % (current_value))
            time.sleep(60)


def ocr_core(filename):
    text = pytesseract.image_to_string(Image.open(filename))
    return text


def get_screenshot(index):
    screenshot = pyautogui.screenshot(region=(189, 840, 31, 31))
    screenshot.save(r'C:\Users\Usuario\PycharmProjects\exercises\minecraft-server\imgs\%s.png' % (str(index)))


main()

