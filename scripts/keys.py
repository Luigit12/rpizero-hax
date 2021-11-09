import os, time

def send(keys):
	for element in range(0, len(keys)):
		if keys[element].isupper() == True:
			os.system('echo left-shift ' + keys[element].lower() + ' | /home/pi/hid_gadget_test /dev/hidg0 keyboard')
		elif keys[element].isupper() == False:
            		if keys[element] == "/":
                		os.system('echo "slash" | /home/pi/hid_gadget_test /dev/hidg0 keyboard')
            		elif keys[element] == ".":
                		os.system('echo "period" | /home/pi/hid_gadget_test /dev/hidg0 keyboard')
            		else:
                		os.system('echo ' + keys[element] + ' | /home/pi/hid_gadget_test /dev/hidg0 keyboard')
	time.sleep(0.1)
	print(keys)

def sendSpecial(keys):
	os.system('echo '+ keys + ' | /home/pi/hid_gadget_test /dev/hidg0 keyboard')
	time.sleep(0.1)
	print(keys)
