import os, time

def send(keys):
	for element in range(0, len(keys)):
		if keys[element].isupper() == True:
			os.system('echo' + keys[element].lower() + ' | /home/pi/hid_gadget_test /dev/hidg0 keyboard')
		elif keys[element].isupper() == False:
            		if keys[element] == "/":
                		os.system('echo "slash" | /home/pi/hid_gadget_test /dev/hidg0 keyboard')
            		elif keys[element] == ".":
                		os.system('echo "period" | /home/pi/hid_gadget_test /dev/hidg0 keyboard')
            		else:
                		os.system('/home/pi/pizero_usb_hid_keyboard/sendkeys ' + keys[element])
	print(keys)

def sendSpecial(keys):
	os.system('echo'+ keys + ' | /home/pi/hid_gadget_test /dev/hidg0 keyboard')
	print(keys)
