import pyautogui
import pytesseract
import time
import sys
from PIL import Image


LEFT_REGION  = (185, 125, 760, 835)   # x, y, platums, augstums
RIGHT_REGION = (964, 141, 786, 806)   # x, y, platums, augstums

# Cik lapas ieskaitot šobrīdējo
TOTAL_PAGES = 72

OUTPUT_FILE = "gramata.txt"

# ja nestrādā var šo vērtību uzlikt lielāku -> 1.5
PAGE_DELAY = 1.0

TESSERACT_LANG = "lav+eng"

pytesseract.pytesseract.tesseract_cmd = r".\Tesseract\tesseract.exe"

def screenshot_to_text(region, lang=TESSERACT_LANG, save_path=None):
    img = pyautogui.screenshot(region=region)
    if save_path:
        img.save(save_path)
    text = pytesseract.image_to_string(img, lang=lang)
    return text.strip()

def main():
    print(f"Sāksies pēc 3 sekundēm - noklikšķini uz pārlūka loga!")
    time.sleep(3)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:

        for page_num in range(1, TOTAL_PAGES + 1):
            print(f"Lapa {page_num}/{TOTAL_PAGES} ...")

            if page_num == 1:
                left_text  = screenshot_to_text(LEFT_REGION,  save_path="lapa_1_kreisa.png")
                right_text = screenshot_to_text(RIGHT_REGION, save_path="lapa_1_laba.png")
                print("Saglabāti: lapa_1_kreisa.png, lapa_1_laba.png")
            else:
                left_text  = screenshot_to_text(LEFT_REGION)
                right_text = screenshot_to_text(RIGHT_REGION)

            f.write(f"{'='*60}\n")
            f.write(f"LAPA {page_num}\n")
            f.write(f"{'='*60}\n\n")
            f.write("--- KREISĀ KOLONNA ---\n\n")
            f.write(left_text)
            f.write("\n\n--- LABĀ KOLONNA ---\n\n")
            f.write(right_text)
            f.write("\n\n")
            f.flush()

            pyautogui.press("right")
            time.sleep(PAGE_DELAY)

    print(f"\nGatavs! Teksts saglabāts: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
