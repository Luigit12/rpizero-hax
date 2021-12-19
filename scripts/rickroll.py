import time
import keys

w = lambda x=1: time.sleep(x)

for i in range(5, 0, -1):
    print('Firing in', i)
    w()

for _ in range(3):
    keys.sendSpecial('left-meta enter')
    w()
keys.sendSpecial('left-meta b')
w()
keys.sendSpecial('left-ctrl t')
w()
keys.sendSpecial('left-ctrl l')
w(2)
keys.send('youtu.be/ptCzSA1BY6s')
w()
keys.sendSpecial('enter')
w(2)
keys.sendSpecial('space')
while True:
    space = input('')
    if space:
        break
    keys.sendSpecial('space')

keys.sendSpecial('left-ctrl w')
w()
keys.sendSpecial('left-ctrl q')
w()
keys.sendSpecial('left-meta enter')
