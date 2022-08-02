"""
This Script is made by Lazymaz
-------------------------------
Do you know that UI of Arch? Ugh, that full screen Shell with lots of text,
and also the Installation, more painful. Let's make it easy.
And that why I made this Script.
This Script provides an easy Installation.
Just some text replacement and then enjoy the auto-installer.
I will group it like "1)". This requires circuit python 7
group:

line: 70
1) Change the SSID to your Home network.

line: 75
2) Change the password to your wifi passphrase (if theres no passphrase of your wifi network type nothing)

line:79
3) At 2), if theres no passphrase, set it to any number you like.
but if you have a passphrase, set it to "1".

line: 89
4) Set it to your network card.
"""
#Library import
import usb_hid
from time import sleep
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
import de
from de_keycode import Keycode as keycode_de
from adafruit_hid.Keyboard_layout_us import KeyboardLayoutUS as us
from adafruit_hid.keycode import Keycode as keycode_us
import us_dvo as dvorak
from adafruit_hid.keycode import Keycode as keycode_dvo
import br
from br_keycode import Keycode as keycode_br
import cz
from cz_keycode import Keycode as keycode_cz
import cz1
from cz1_keycode import Keycode as keycode_cz1
import es
from es_keycode import Keycode as keycode_es
import fr
from fr_keycode import Keycode as keycode_fr
import hu
from hu_keycode import Keycode as keycode_hu
import it
from it_keycode import Keycode as keycode_it
import po
from po_keycode import Keycode as keycode_po
import sw
from sw_keycode import Keycode as keycode_sw
import tr
from tr_keycode import Keycode as keycode_tr

"""
Pin Layout Configurator (PLC)
-----------------------------
This is a little A.I. that configures the Layout of the Keyboard.
How? It configures himself by checking the pins.

Like: GP0 to button, button to 3V3(OUT) is the US keyboard layout.
"""


"""
Now, this sets the A.I. up.
It configures Pins (like GP0 as a US keyboard layout),
says what to do if one of the pins gets pressed and so on.
"""
#creates Object "keyboard"
keyboard = Keyboard(usb_hid.devices)

#creates variable for wifi SSID
wifi_SSID = "Your WIFI"  #1)

#creates variable for wifi password
password = "Password1234"    #2)

#creates variable for wifi password setting
wifi_has_password = 1   #3)

#creates variable for internet device
device = "wlan0" #4)

#creates US keyboard option
btn_us_layout = digitalio.DigitalInOut(board.GP0)
btn_us_layout.direction = digitalio.Direction.INPUT
btn_us_layout.pull = digitalio.Pull.DOWN

btn_de_layout = digitalio.DigitalInOut(board.GP1)
btn_de_layout.direction = digitalio.Direction.INPUT
btn_de_layout.pull = digitalio.Pull.DOWN

btn_dvo_layout = digitalio.DigitalInOut(board.GP2)
btn_dvo_layout.direction = digitalio.Direction.INPUT
btn_dvo_layout.pull = digitalio.Pull.DOWN

btn_br_layout = digitalio.DigitalInOut(board.GP3)
btn_br_layout.direction = digitalio.Direction.INPUT
btn_br_layout.pull = digitalio.Pull.DOWN

btn_cz_layout = digitalio.DigitalInOut(board.GP4)
btn_cz_layout.direction = digitalio.Direction.INPUT
btn_cz_layout.pull = digitalio.Pull.DOWN

btn_cz1_layout = digitalio.DigitalInOut(board.GP5)
btn_cz1_layout.direction = digitalio.Direction.INPUT
btn_cz1_layout.pull = digitalio.Pull.DOWN

btn_es_layout = digitalio.DigitalInOut(board.GP6)
btn_es_layout.direction = digitalio.Direction.INPUT
btn_es_layout.pull = digitalio.Pull.DOWN

btn_fr_layout = digitalio.DigitalInOut(board.GP7)
btn_fr_layout.direction = digitalio.Direction.INPUT
btn_fr_layout.pull = digitalio.Pull.DOWN

btn_hu_layout = digitalio.DigitalInOut(board.GP8)
btn_hu_layout.direction = digitalio.Direction.INPUT
btn_hu_layout.pull = digitalio.Pull.DOWN

btn_it_layout = digitalio.DigitalInOut(board.GP9)
btn_it_layout.direction = digitalio.Direction.INPUT
btn_it_layout.pull = digitalio.Pull.DOWN

btn_po_layout = digitalio.DigitalInOut(board.GP10)
btn_po_layout.direction = digitalio.Direction.INPUT
btn_po_layout.pull = digitalio.Pull.DOWN

btn_sw_layout = digitalio.DigitalInOut(board.GP11)
btn_sw_layout.direction = digitalio.Direction.INPUT
btn_sw_layout.pull = digitalio.Pull.DOWN

btn_tr_layout = digitalio.DigitalInOut(board.GP12)
btn_tr_layout.direction = digitalio.Direction.INPUT
btn_tr_layout.pull = digitalio.Pull.DOWN
while True:
    if btn_us_layout.value:
        us_layout = us(keyboard)
        us_layout.write("iwctl station "+device+' scan')
        keyboard.press(keycode_us.ENTER)
        sleep(0.1)
        keyboard.release(keycode_us.ENTER)
        sleep(0.1)
        us_layout.write("iwctl station "+device+" get-networks")
        keyboard.press(keycode_us.ENTER)
        sleep(0.1)
        keyboard.release(keycode_us.ENTER)
        if wifi_has_password == 1:
            us_layout.write("iwctl --passphrase "+password+" station "+device+" connect "+wifi_SSID)
            sleep(0.1)
            keyboard.press(keycode_us.ENTER)
            sleep(0.1)
            keyboard.release(keycode_us.ENTER)
            sleep(0.1)
            us_layout.write("timedatectl set-ntp true")
            sleep(0.1)
            keyboard.press(keycode_us.ENTER)
            sleep(0.1)
            keyboard.release(keycode_us.ENTER)
        
        if wifi_has_password != 1:
            us_layout.write("iwctl station wlan0 connect", wifi_SSID)
            sleep(0.1)
            keyboard.press(keycode_us.ENTER)
            sleep(0.1)
            keyboard.release(keycode_us.ENTER)
            sleep(0.1)
            us_layout.write("timedatectl set-ntp true")
            sleep(0.1)
            keyboard.press(keycode_us.ENTER)
            sleep(0.1)
            keyboard.release(keycode_us.ENTER)
            
        us_layout.write("archinstall")
        sleep(0.1)
        keyboard.press(keycode_us.ENTER)
        sleep(0.1)
        keyboard.release(keycode_us.ENTER)
        
            
    if btn_de_layout.value:
        us_layout = us(keyboard)
        de_layout = de.KeyboardLayout(keyboard)
        us_layout.write("loadkeys de-latin1")
        keyboard.press(keycode_us.ENTER)
        sleep(0.1)
        keyboard.release(keycode_us.ENTER)
        sleep(0.1)
        de_layout.write("iwctl station "+device+' scan')
        keyboard.press(keycode_de.ENTER)
        sleep(0.1)
        keyboard.release(keycode_de.ENTER)
        sleep(0.1)
        de_layout.write("iwctl station "+device+" get-networks")
        keyboard.press(keycode_de.ENTER)
        sleep(0.1)
        keyboard.release(keycode_de.ENTER)
        if wifi_has_password == 1:
            de_layout.write("iwctl --passphrase "+password+" station "+device+" connect "+wifi_SSID)
            sleep(0.1)
            keyboard.press(keycode_de.ENTER)
            sleep(0.1)
            keyboard.release(keycode_de.ENTER)
            sleep(0.1)
            de_layout.write("timedatectl set-ntp true")
            sleep(0.1)
            keyboard.press(keycode_de.ENTER)
            sleep(0.1)
            keyboard.release(keycode_de.ENTER)
        
        if wifi_has_password != 1:
            de_layout.write("iwctl station wlan0 connect", wifi_SSID)
            sleep(0.1)
            keyboard.press(keycode_de.ENTER)
            sleep(0.1)
            keyboard.release(keycode_de.ENTER)
            sleep(0.1)
            de_layout.write("timedatectl set-ntp true")
            sleep(0.1)
            keyboard.press(keycode_de.ENTER)
            sleep(0.1)
            keyboard.release(keycode_de.ENTER)
            
        de_layout.write("archinstall")
        sleep(0.1)
        keyboard.press(keycode_de.ENTER)
        sleep(0.1)
        keyboard.release(keycode_de.ENTER)
        
    if btn_dvo_layout.value:
        us_layout = us(keyboard)
        dvo_layout = dvorak.KeyboardLayout(keyboard)
        us_layout.write("loadkeys dvorak")
        keyboard.press(keycode_us.ENTER)
        sleep(0.1)
        keyboard.release(keycode_us.ENTER)
        sleep(0.1)
        dvo_layout.write("iwctl station "+device+' scan')
        keyboard.press(keycode_dvo.ENTER)
        sleep(0.1)
        keyboard.release(keycode_dvo.ENTER)
        sleep(0.1)
        dvo_layout.write("iwctl station "+device+" get-networks")
        keyboard.press(keycode_dvo.ENTER)
        sleep(0.1)
        keyboard.release(keycode_dvo.ENTER)
        
        if wifi_has_password == 1:
            dvo_layout.write("iwctl --passphrase "+password+" station "+device+" connect "+wifi_SSID)
            sleep(0.1)
            keyboard.press(keycode_dvo.ENTER)
            sleep(0.1)
            keyboard.release(keycode_dvo.ENTER)
            sleep(0.1)
            dvo_layout.write("timedatectl set-ntp true")
            sleep(0.1)
            keyboard.press(keycode_dvo.ENTER)
            sleep(0.1)
            keyboard.release(keycode_dvo.ENTER)
        
        if wifi_has_password != 1:
            dvo_layout.write("iwctl station wlan0 connect", wifi_SSID)
            sleep(0.1)
            keyboard.press(keycode_dvo.ENTER)
            sleep(0.1)
            keyboard.release(keycode_dvo.ENTER)
            sleep(0.1)
            dvo_layout.write("timedatectl set-ntp true")
            sleep(0.1)
            keyboard.press(keycode_dvo.ENTER)
            sleep(0.1)
            keyboard.release(keycode_dvo.ENTER)
            
        dvo_layout.write("archinstall")
        sleep(0.1)
        keyboard.press(keycode_dvo.ENTER)
        sleep(0.1)
        keyboard.release(keycode_dvo.ENTER)
        
    if btn_br_layout.value:
        us_layout = us(keyboard)
        br_layout = br.KeyboardLayout(keyboard)
        us_layout.write("loadkeys br-abnt")
        sleep(0.1)
        keyboard.press(keycode_us.ENTER)
        sleep(0.1)
        keyboard.press(keycode_us.ENTER)
        sleep(0.1)
        br_layout.write("iwctl station "+device+' scan')
        sleep(0.1)
        keyboard.press(keycode_br.ENTER)
        sleep(0.1)
        keyboard.release(keycode_br.ENTER)
        sleep(0.1)
        br_layout.write("iwctl station "+device+" get-networks")
        sleep(0.1)
        keyboard.press(keycode_br.ENTER)
        sleep(0.1)
        keyboard.release(keycode_br.ENTER)
        if wifi_has_password == 1:
            br_layout.write("iwctl --passphrase "+password+" station "+device+" connect "+wifi_SSID)
            sleep(0.1)
            keyboard.press(keycode_br.ENTER)
            sleep(0.1)
            keyboard.release(keycode_br.ENTER)
            sleep(0.1)
            br_layout.write("timedatectl set-ntp true")
            sleep(0.1)
            keyboard.press(keycode_br.ENTER)
            sleep(0.1)
            keyboard.release(keycode_br.ENTER)
        
        if wifi_has_password != 1:
            br_layout.write("iwctl station wlan0 connect", wifi_SSID)
            sleep(0.1)
            keyboard.press(keycode_br.ENTER)
            sleep(0.1)
            keyboard.release(keycode_br.ENTER)
            sleep(0.1)
            br_layout.write("timedatectl set-ntp true")
            sleep(0.1)
            keyboard.press(keycode_br.ENTER)
            sleep(0.1)
            keyboard.release(keycode_br.ENTER)
            
        br_layout.write("archinstall")
        sleep(0.1)
        keyboard.press(keycode_br.ENTER)
        sleep(0.1)
        keyboard.release(keycode_br.ENTER)
        
    if btn_cz_layout.value:
        us_layout = us(keyboard)
        cz_layout = cz.KeyboardLayout(keyboard)
        us_layout.write("loadkeys de-latin1")
        sleep(0.1)
        keyboard.press(keycode_us.ENTER)
        sleep(0.1)
        keyboard.release(keycode_us.ENTER)
        sleep(0.1)
        cz_layout.write("iwctl station "+device+' scan')
        sleep(0.1)
        keyboard.press(keycode_cz.ENTER)
        sleep(0.1)
        keyboard.release(keycode_cz.ENTER)
        sleep(0.1)
        cz_layout.write("iwctl station "+device+" get-networks")
        keyboard.press(keycode_cz.ENTER)
        sleep(0.1)
        keyboard.release(keycode_cz.ENTER)
        if wifi_has_password == 1:
            cz_layout.write("iwctl --passphrase "+password+" station "+device+" connect "+wifi_SSID)
            sleep(0.1)
            keyboard.press(keycode_cz.ENTER)
            sleep(0.1)
            keyboard.release(keycode_cz.ENTER)
            sleep(0.1)
            cz_layout.write("timedatectl set-ntp true")
            sleep(0.1)
            keyboard.press(keycode_cz.ENTER)
            sleep(0.1)
            keyboard.release(keycode_cz.ENTER)
        
        if wifi_has_password != 1:
            cz_layout.write("iwctl station wlan0 connect", wifi_SSID)
            sleep(0.1)
            keyboard.press(keycode_cz.ENTER)
            sleep(0.1)
            keyboard.release(keycode_cz.ENTER)
            sleep(0.1)
            cz_layout.write("timedatectl set-ntp true")
            sleep(0.1)
            keyboard.press(keycode_cz.ENTER)
            sleep(0.1)
            keyboard.release(keycode_cz.ENTER)
            
        cz_layout.write("archinstall")
        sleep(0.1)
        keyboard.press(keycode_cz.ENTER)
        sleep(0.1)
        keyboard.release(keycode_cz.ENTER)
        
    if btn_cz1_layout.value:
        us_layout = us(keyboard)
        cz1_layout = cz1.KeyboardLayout(keyboard)
        us_layout.write("loadkeys cz-qwerty")
        keyboard.press(keycode_us.ENTER)
        sleep(0.1)
        keyboard.release(keycode_us.ENTER)
        sleep(0.1)
        cz1_layout.write("iwctl station "+device+' scan')
        keyboard.press(keycode_cz1.ENTER)
        sleep(0.1)
        keyboard.release(keycode_cz1.ENTER)
        sleep(0.1)
        cz1_layout.write("iwctl station "+device+" get-networks")
        keyboard.press(keycode_cz1.ENTER)
        sleep(0.1)
        keyboard.release(keycode_cz1.ENTER)
        if wifi_has_password == 1:
            cz1_layout.write("iwctl --passphrase "+password+" station "+device+" connect "+wifi_SSID)
            sleep(0.1)
            keyboard.press(keycode_cz1.ENTER)
            sleep(0.1)
            keyboard.release(keycode_cz1.ENTER)
            sleep(0.1)
            cz1_layout.write("timedatectl set-ntp true")
            sleep(0.1)
            keyboard.press(keycode_cz1.ENTER)
            sleep(0.1)
            keyboard.release(keycode_cz1.ENTER)
        
        if wifi_has_password != 1:
            cz1_layout.write("iwctl station wlan0 connect", wifi_SSID)
            sleep(0.1)
            keyboard.press(keycode_cz1.ENTER)
            sleep(0.1)
            keyboard.release(keycode_cz1.ENTER)
            sleep(0.1)
            cz1_layout.write("timedatectl set-ntp true")
            sleep(0.1)
            keyboard.press(keycode_cz1.ENTER)
            sleep(0.1)
            keyboard.release(keycode_cz1.ENTER)
            
        cz1_layout.write("archinstall")
        sleep(0.1)
        keyboard.press(keycode_cz1.ENTER)
        sleep(0.1)
        keyboard.release(keycode_cz1.ENTER)
        
    if btn_es_layout.value:
        us_layout = us(keyboard)
        es_layout = es.KeyboardLayout(keyboard)
        us_layout.write("loadkeys es")
        keyboard.press(keycode_us.ENTER)
        sleep(0.1)
        keyboard.release(keycode_us.ENTER)
        sleep(0.1)
        es_layout.write("iwctl station "+device+' scan')
        keyboard.press(keycode_es.ENTER)
        sleep(0.1)
        keyboard.release(keycode_es.ENTER)
        sleep(0.1)
        es_layout.write("iwctl station "+device+" get-networks")
        keyboard.press(keycode_es.ENTER)
        sleep(0.1)
        keyboard.release(keycode_es.ENTER)
        if wifi_has_password == 1:
            es_layout.write("iwctl --passphrase "+password+" station "+device+" connect "+wifi_SSID)
            sleep(0.1)
            keyboard.press(keycode_es.ENTER)
            sleep(0.1)
            keyboard.release(keycode_es.ENTER)
            sleep(0.1)
            es_layout.write("timedatectl set-ntp true")
            sleep(0.1)
            keyboard.press(keycode_es.ENTER)
            sleep(0.1)
            keyboard.release(keycode_es.ENTER)
        
        if wifi_has_password != 1:
            es_layout.write("iwctl station wlan0 connect", wifi_SSID)
            sleep(0.1)
            keyboard.press(keycode_es.ENTER)
            sleep(0.1)
            keyboard.release(keycode_es.ENTER)
            sleep(0.1)
            es_layout.write("timedatectl set-ntp true")
            sleep(0.3)
            keyboard.press(keycode_es.ENTER)
            sleep(0.1)
            keyboard.release(keycode_es.ENTER)
            
        es_layout.write("archinstall")
        sleep(0.1)
        keyboard.press(keycode_es.ENTER)
        sleep(0.1)
        keyboard.release(keycode_es.ENTER)
        
    if btn_fr_layout.value:
        us_layout = us(keyboard)
        fr_layout = fr.KeyboardLayout(keyboard)
        us_layout.write("loadkeys fr")
        keyboard.press(keycode_us.ENTER)
        sleep(0.1)
        keyboard.release(keycode_us.ENTER)
        sleep(0.1)
        fr_layout.write("iwctl station "+device+' scan')
        keyboard.press(keycode_fr.ENTER)
        sleep(0.1)
        keyboard.release(keycode_fr.ENTER)
        sleep(0.1)
        fr_layout.write("iwctl station "+device+" get-networks")
        keyboard.press(keycode_fr.ENTER)
        sleep(0.1)
        keyboard.release(keycode_fr.ENTER)
        if wifi_has_password == 1:
            fr_layout.write("iwctl --passphrase "+password+" station "+device+" connect "+wifi_SSID)
            sleep(0.1)
            keyboard.press(keycode_fr.ENTER)
            sleep(0.1)
            keyboard.release(keycode_fr.ENTER)
            sleep(0.1)
            fr_layout.write("timedatectl set-ntp true")
            sleep(0.1)
            keyboard.press(keycode_fr.ENTER)
            sleep(0.1)
            keyboard.release(keycode_fr.ENTER)
        
        if wifi_has_password != 1:
            de_layout.write("iwctl station wlan0 connect", wifi_SSID)
            sleep(0.1)
            keyboard.press(keycode_fr.ENTER)
            sleep(0.1)
            keyboard.release(keycode_fr.ENTER)
            sleep(0.1)
            fr_layout.write("timedatectl set-ntp true")
            sleep(0.1)
            keyboard.press(keycode_fr.ENTER)
            sleep(0.1)
            keyboard.release(keycode_fr.ENTER)
            
        fr_layout.write("archinstall")
        sleep(0.1)
        keyboard.press(keycode_fr.ENTER)
        sleep(0.1)
        keyboard.release(keycode_fr.ENTER)
        
    if btn_hu_layout.value:
        us_layout = us(keyboard)
        hu_layout = hu.KeyboardLayout(keyboard)
        us_layout.write("loadkeys de-latin1")
        keyboard.press(keycode_us.ENTER)
        sleep(0.1)
        keyboard.release(keycode_us.ENTER)
        sleep(0.1)
        hu_layout.write("iwctl station "+device+' scan')
        keyboard.press(keycode_hu.ENTER)
        sleep(0.1)
        keyboard.release(keycode_hu.ENTER)
        sleep(0.1)
        hu_layout.write("iwctl station "+device+" get-networks")
        keyboard.press(keycode_hu.ENTER)
        sleep(0.1)
        keyboard.release(keycode_hu.ENTER)
        if wifi_has_password == 1:
            hu_layout.write("iwctl --passphrase "+password+" station "+device+" connect "+wifi_SSID)
            sleep(0.1)
            keyboard.press(keycode_hu.ENTER)
            sleep(0.1)
            keyboard.release(keycode_hu.ENTER)
            sleep(0.1)
            hu_layout.write("timedatectl set-ntp true")
            sleep(0.1)
            keyboard.press(keycode_hu.ENTER)
            sleep(0.1)
            keyboard.release(keycode_hu.ENTER)
        
        if wifi_has_password != 1:
            hu_layout.write("iwctl station wlan0 connect", wifi_SSID)
            sleep(0.1)
            keyboard.press(keycode_hu.ENTER)
            sleep(0.1)
            keyboard.release(keycode_hu.ENTER)
            sleep(0.1)
            hu_layout.write("timedatectl set-ntp true")
            sleep(0.1)
            keyboard.press(keycode_hu.ENTER)
            sleep(0.1)
            keyboard.release(keycode_hu.ENTER)
            
        hu_layout.write("archinstall")
        sleep(0.1)
        keyboard.press(keycode_hu.ENTER)
        sleep(0.1)
        keyboard.release(keycode_hu.ENTER)
        
    if btn_it_layout.value:
        us_layout = us(keyboard)
        it_layout = it.KeyboardLayout(keyboard)
        us_layout.write("loadkeys de-latin1")
        keyboard.press(keycode_us.ENTER)
        sleep(0.1)
        keyboard.release(keycode_us.ENTER)
        sleep(0.1)
        it_layout.write("iwctl station "+device+' scan')
        keyboard.press(keycode_it.ENTER)
        sleep(0.1)
        keyboard.release(keycode_it.ENTER)
        sleep(0.1)
        it_layout.write("iwctl station "+device+" get-networks")
        keyboard.press(keycode_it.ENTER)
        sleep(0.1)
        keyboard.release(keycode_it.ENTER)
        if wifi_has_password == 1:
            it_layout.write("iwctl --passphrase "+password+" station "+device+" connect "+wifi_SSID)
            sleep(0.1)
            keyboard.press(keycode_it.ENTER)
            sleep(0.1)
            keyboard.release(keycode_it.ENTER)
            sleep(0.1)
            it_layout.write("timedatectl set-ntp true")
            sleep(0.1)
            keyboard.press(keycode_it.ENTER)
            sleep(0.1)
            keyboard.release(keycode_it.ENTER)
        
        if wifi_has_password != 1:
            it_layout.write("iwctl station wlan0 connect", wifi_SSID)
            sleep(0.1)
            keyboard.press(keycode_it.ENTER)
            sleep(0.1)
            keyboard.release(keycode_it.ENTER)
            sleep(0.1)
            it_layout.write("timedatectl set-ntp true")
            sleep(0.1)
            keyboard.press(keycode_it.ENTER)
            sleep(0.1)
            keyboard.release(keycode_it.ENTER)

        it_layout.write("archinstall")
        sleep(0.1)
        keyboard.press(keycode_it.ENTER)
        sleep(0.1)
        keyboard.release(keycode_it.ENTER)
        
    if btn_po_layout.value:
        us_layout = us(keyboard)
        po_layout = po.KeyboardLayout(keyboard)
        us_layout.write("loadkeys pt-latin1")
        keyboard.press(keycode_us.ENTER)
        sleep(0.1)
        keyboard.release(keycode_us.ENTER)
        sleep(0.1)
        po_layout.write("iwctl station "+device+' scan')
        keyboard.press(keycode_po.ENTER)
        sleep(0.1)
        keyboard.release(keycode_po.ENTER)
        sleep(0.1)
        po_layout.write("iwctl station "+device+" get-networks")
        keyboard.press(keycode_po.ENTER)
        sleep(0.1)
        keyboard.release(keycode_po.ENTER)
        if wifi_has_password == 1:
            po_layout.write("iwctl --passphrase "+password+" station "+device+" connect "+wifi_SSID)
            sleep(0.1)
            keyboard.press(keycode_po.ENTER)
            sleep(0.1)
            keyboard.release(keycode_po.ENTER)
            sleep(0.1)
            po_layout.write("timedatectl set-ntp true")
            sleep(0.1)
            keyboard.press(keycode_po.ENTER)
            sleep(0.1)
            keyboard.release(keycode_po.ENTER)
        
        if wifi_has_password != 1:
            po_layout.write("iwctl station wlan0 connect", wifi_SSID)
            sleep(0.1)
            keyboard.press(keycode_po.ENTER)
            sleep(0.1)
            keyboard.release(keycode_po.ENTER)
            sleep(0.1)
            po_layout.write("timedatectl set-ntp true")
            sleep(0.1)
            keyboard.press(keycode_po.ENTER)
            sleep(0.1)
            keyboard.release(keycode_po.ENTER)
            
        po_layout.write("archinstall")
        sleep(0.1)
        keyboard.press(keycode_po.ENTER)
        sleep(0.1)
        keyboard.release(keycode_po.ENTER)
        
    if btn_sw_layout.value:
        us_layout = us(keyboard)
        sw_layout = sw.KeyboardLayout(keyboard)
        us_layout.write("loadkeys sv-latin1")
        keyboard.press(keycode_us.ENTER)
        sleep(0.1)
        keyboard.release(keycode_us.ENTER)
        sleep(0.1)
        sw_layout.write("iwctl station "+device+' scan')
        keyboard.press(keycode_sw.ENTER)
        sleep(0.1)
        keyboard.release(keycode_sw.ENTER)
        sleep(0.1)
        sw_layout.write("iwctl station "+device+" get-networks")
        keyboard.press(keycode_sw.ENTER)
        sleep(0.1)
        keyboard.release(keycode_sw.ENTER)
        if wifi_has_password == 1:
            sw_layout.write("iwctl --passphrase "+password+" station "+device+" connect "+wifi_SSID)
            sleep(0.1)
            keyboard.press(keycode_sw.ENTER)
            sleep(0.1)
            keyboard.release(keycode_sw.ENTER)
            sleep(0.1)
            sw_layout.write("timedatectl set-ntp true")
            sleep(0.1)
            keyboard.press(keycode_sw.ENTER)
            sleep(0.1)
            keyboard.release(keycode_sw.ENTER)
        
        if wifi_has_password != 1:
            sw_layout.write("iwctl station wlan0 connect", wifi_SSID)
            sleep(0.1)
            keyboard.press(keycode_sw.ENTER)
            sleep(0.1)
            keyboard.release(keycode_sw.ENTER)
            sleep(0.1)
            sw_layout.write("timedatectl set-ntp true")
            sleep(0.1)
            keyboard.press(keycode_sw.ENTER)
            sleep(0.1)
            keyboard.release(keycode_sw.ENTER)
            
        sw_layout.write("archinstall")
        sleep(0.1)
        keyboard.press(keycode_sw.ENTER)
        sleep(0.1)
        keyboard.release(keycode_sw.ENTER)
        
    if btn_tr_layout.value:
        us_layout = us(keyboard)
        tr_layout = tr.KeyboardLayout(keyboard)
        us_layout.write("loadkeys trq")
        keyboard.press(keycode_us.ENTER)
        sleep(0.1)
        keyboard.release(keycode_us.ENTER)
        sleep(0.1)
        tr_layout.write("iwctl station "+device+' scan')
        keyboard.press(keycode_tr.ENTER)
        sleep(0.1)
        keyboard.release(keycode_tr.ENTER)
        sleep(0.1)
        de_layout.write("iwctl station "+device+" get-networks")
        keyboard.press(keycode_tr.ENTER)
        sleep(0.1)
        keyboard.release(keycode_tr.ENTER)
        if wifi_has_password == 1:
            tr_layout.write("iwctl --passphrase "+password+" station "+device+" connect "+wifi_SSID)
            sleep(0.1)
            keyboard.press(keycode_tr.ENTER)
            sleep(0.1)
            keyboard.release(keycode_tr.ENTER)
            sleep(0.1)
            tr_layout.write("timedatectl set-ntp true")
            sleep(0.1)
            keyboard.press(keycode_tr.ENTER)
            sleep(0.1)
            keyboard.release(keycode_tr.ENTER)
        
        if wifi_has_password != 1:
            tr_layout.write("iwctl station wlan0 connect", wifi_SSID)
            sleep(0.1)
            keyboard.press(keycode_tr.ENTER)
            sleep(0.1)
            keyboard.release(keycode_tr.ENTER)
            sleep(0.1)
            tr_layout.write("timedatectl set-ntp true")
            sleep(0.1)
            keyboard.press(keycode_tr.ENTER)
            sleep(0.1)
            keyboard.release(keycode_tr.ENTER)
            
        tr_layout.write("archinstall")
        sleep(0.1)
        keyboard.press(keycode_tr.ENTER)
        sleep(0.1)
        keyboard.release(keycode_tr.ENTER)
        
