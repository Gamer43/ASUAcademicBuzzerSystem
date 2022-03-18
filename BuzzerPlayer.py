import gpiozero
import guizero
import time

MAROON_RGB = "#B03060"
GOLD_RGB = "#FFD700"


class BuzzerPlayer():
        def __init__(self):
            self.count = 0
            self.btn = gpiozero.Button(4, hold_time=0.01)
            self.btn.when_held = self.pressed
            self.app = guizero.App(title="Player", width = 600, height = 300, bg=MAROON_RGB)
            self.app.when_closed = self.cleanup
            self.app.set_full_screen()
            self.name = guizero.Text(self.app, text="Player 1", size=200, font="Times New Roman", color="white", width = "fill", height = "fill")
            self.app.display()
        def pressed(self):
            if self.count % 2:
                self.app.cancel(self.flash_color)
                self.app.bg = MAROON_RGB
            else:
                self.app.repeat(500, self.flash_color)
            self.count = self.count + 1
        def flash_color(self):
            if self.app.bg == MAROON_RGB:
                self.app.bg = GOLD_RGB
            else:
                self.app.bg = MAROON_RGB
        def cleanup(self):
            if self.count % 2:
                self.app.cancel(self.flash_color)
            time.sleep(1)
            self.app.destroy()
        
Player = BuzzerPlayer()

