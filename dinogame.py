from PIL import ImageGrab, ImageOps
import time
import pyautogui as pag
import numpy as np

# Let's automate the dino game of chrome...!!


class DinoBot:
    def __init__(self):
        self.restart_coords = (487, 414)
        self.dino_coords = (70, 460)
        self.area = (self.dino_coords[0] + 105, self.dino_coords[1], self.dino_coords[0] + 235, self.dino_coords[1] + 3)
        self.jump_count = 0

    def set_dino_coords(self, x, y):
        if self.jump_count % 5 == 0:
            self.dino_coords = (self.dino_coords[0] + 15, self.dino_coords[1])

    def restart(self):
        pag.click(self.restart_coords)
        pag.keyDown('down')

    def jump(self):
        pag.keyUp('down')
        pag.keyDown('space')
        time.sleep(0.095)
        pag.keyUp('space')
        pag.keyDown('down')
        self.jump_count += 1

    def detection_area(self):
        image = ImageGrab.grab(self.area)
        gray_img = ImageOps.grayscale(image)
        arr = np.array(gray_img.getcolors())
        return arr.mean()

    def main(self):
        self.restart()
        while True:
            if self.detection_area() < 273:
                self.jump()


bot = DinoBot()
bot.main()
