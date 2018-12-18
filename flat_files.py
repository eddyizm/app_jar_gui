'''
front end for extracting flat files from sql scripts
'''
from appJar import gui
#funtions
def press(name):
  print (name)
  print ('extension:')
  print (win.getRadioButton('f_ext'))
  print ('options:')
  print (win.getOptionBox('file seperator')) 

win = gui(title='File exporter')
win.setIcon('images/Extract.ico')
win.addLabel('tx_1', 'select sql script')
win.addFileEntry("f1")
#win.addStatusbar(header='file extension selected: ')
FILE_SEP = ['- select file seperator -', 'comma ( , )', 'tab ( )', 'pipe ( | )']
win.addOptionBox('file seperator', FILE_SEP)

with win.labelFrame('file extension'):
  win.addRadioButton('f_ext', '.csv')
  win.addRadioButton('f_ext', '.txt')
  
win.addButton('generate file', press)

win.go()
