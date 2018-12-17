# login form
from appJar import gui
win = gui(title='Login')

win.setBg('green')
win.setFg('white')
win.setFont(16)
win.addLabel('label_0', 'Login Window')
win.addLabelEntry('Username')
win.addLabelEntry('Password')

def press(name):
    print(name, 'pressed')
    if name =='Cancel':
        win.stop()
    elif name == 'Reset':
        win.clearEntry('Username')
        win.clearEntry('Password')
        win.setFocus('Username')
    elif name == 'Submit':
        username = win.getEntry('Username')
        password = win.getEntry('Password')
        if username == 'rjarvis' and password == 'password':
            win.infoBox('Success', 'Valid password')     
        else:
            win.errorBox('Error', 'Invalid password')    

win.addButtons(['Submit', 'Reset', 'Cancel'], press)    
win.go()
