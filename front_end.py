from appJar import gui

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

win.addButton('Press me', press)
win.go()