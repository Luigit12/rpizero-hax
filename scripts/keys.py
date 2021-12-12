import os
import time

def send(keys, delay=.05):
    print(keys)
    for element in range(0, len(keys)):
        if keys[element].isupper() == True:
            os.system(f'echo "left-shift" {keys[element].lower()} | /home/pi/hid_gadget_test /dev/hidg0 keyboard')
        elif keys[element].isupper() == False:
            if keys[element] == "/":
                os.system('echo "slash" | /home/pi/hid_gadget_test /dev/hidg0 keyboard')
            elif keys[element] == ".":
                os.system('echo "period" | /home/pi/hid_gadget_test /dev/hidg0 keyboard')
            elif keys[element] == ":":
                os.system('echo "left-shift semicolon" | /home/pi/hid_gadget_test /dev/hidg0 keyboard')
            elif keys[element] == "=":
                os.system('echo "equals" | /home/pi/hid_gadget_test /dev/hidg0 keyboard')
            elif keys[element] == "?":
                os.system('echo "left-shift backslash" | /home/pi/hid_gadget_test /dev/hidg0 keyboard')
            elif keys[element] == "-":
                os.system('echo "minus" | /home/pi/hid_gadget_test /dev/hidg0 keyboard')
            elif keys[element] == ",":
                os.system('echo "comma" | /home/pi/hid_gadget_test /dev/hidg0 keyboard')
            elif keys[element] == "&":
                os.system('echo "left-shift 7" | /home/pi/hid_gadget_test /dev/hidg0 keyboard')
            else:
                os.system(f'echo {keys[element]} | /home/pi/hid_gadget_test /dev/hidg0 keyboard')
        time.sleep(delay)

def sendSpecial(keys):
    os.system('echo ' + keys + ' | /home/pi/hid_gadget_test /dev/hidg0 keyboard')
    time.sleep(0.1)
    print(keys)
