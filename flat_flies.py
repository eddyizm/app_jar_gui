'''
front end for extracting flat files from sql scripts
'''
from appJar import gui
win = gui(title='File exporter')
win.setIcon('images/Extract.ico')
win.addLabel('tx_1', 'select sql script')
win.addFileEntry("f1")
win.go()
