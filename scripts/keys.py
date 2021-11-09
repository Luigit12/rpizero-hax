import os, time

def send(keys):
	for element in range(0, len(keys)):
		if keys[element].isupper() == True:
			os.system('/home/pi/pizero-usb-hid-keyboard/sendkeys left-shift ' + keys[element].lower())
		elif keys[element].isupper() == False:
            		if keys[element] == "/":
                		os.system('/home/pi/pizero-usb-hid-keyboard/sendkeys ' + "slash")
            		elif keys[element] == ".":
                		os.system('/home/pi/pizero-usb-hid-keyboard/sendkeys ' + "period")
            		else:
                		os.system('/home/pi/pizero-usb-hid-keyboard/sendkeys ' + keys[element])
	print(keys)

def sendSpecial(keys):
	os.system('echo'+ keys + ' | /home/pi/hid-gadget-test /dev/hidg0 keyboard')
	print(keys)
