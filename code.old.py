import usb_hid
from time import sleep
import board
import digitalio
    
btnDE = digitalio.DigitalInOut(board.GP18)
btnDE.direction = digitalio.Direction.INPUT
btnDE.pull = digitalio.Pull.DOWN
btnUS = digitalio.DigitalInOut(board.GP19)
btnUS.direction = digitalio.Direction.INPUT
btnUS.pull = digitalio.Pull.DOWN

while True:
    if btnDE.value:
        import usb_hid
        from adafruit_hid.keyboard import Keyboard
        import de
        from de_keycode import Keycode as co
        keyboard = Keyboard(usb_hid.devices)
        keyboard_layout = de.KeyboardLayout(keyboard)
        keyboard.press(co.GUI)
        sleep(0.5)
        keyboard.release(co.GUI)
        sleep(1)
        keyboard_layout.write("python")
        sleep(0.05)
        keyboard.press(co.ENTER)
        sleep(0.05)
        keyboard.release(co.ENTER)
        
    if btnUS.value:
        from adafruit_hid.keyboard import Keyboard
        from adafruit_hid.Keyboard_layout_us import KeyboardLayoutUS
        from adafruit_hid.keycode import Keycode as co 
        keyboard = Keyboard(usb_hid.devices)
        keyboard_layout = KeyboardLayoutUS(keyboard)
        keyboard.press(co.GUI)
        sleep(0.5)
        keyboard.release(co.GUI)
        sleep(1)
        keyboard_layout.write("python")
        sleep(0.05)
        keyboard.press(co.ENTER)
        sleep(0.05)
        keyboard.release(co.ENTER)
        