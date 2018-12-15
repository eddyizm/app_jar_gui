from appJar import gui

win = gui('Hello World')
win.addLabel('label1', 'hello world')
win.setBg('green')
win.setFont(20)
win.go()