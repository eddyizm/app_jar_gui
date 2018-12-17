from appJar import gui
# global variables
count = 0
win = gui('Hello World')
# widgets
win.addLabel('label1', 'hello world')
win.addLabel('label2', 'python appJar test')
win.setBg('green')
win.setLabelBg('label2', 'blue')
win.setLabelFg('label2', 'yellow')
win.setFont(20)
win.setSize('400x200')
win.setResizable(False)
# buttons
def press(name):
    print (name, 'button pressed')
    win.setLabel('label1', 'pressed')

def press_btn(name):
    print(name, 'second button pressed')
    global count
    count += 1
    win.setLabel('label2', 'pressed: ' + str(count) + ' times!')
win.addButton('Press me', press)
win.addButton('button', press_btn)

win.go()