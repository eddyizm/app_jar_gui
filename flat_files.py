'''
front end for extracting flat files from sql scripts
'''
from appJar import gui
#funtions
def generate_file(name):
  print (name)
  print ('extension:')
  print (win.getRadioButton('f_ext'))
  
  if not win.getEntry('f1'):
    print ('sql file empty?')
  else:
    print ('sql file:')
    print (win.getEntry('f1'))

  if win.getOptionBox('file seperator'):
    print ('options:')
    print (win.getOptionBox('file seperator')) 
  else:
    win.popUp('Error', 'please select a file seperator', kind='error')
    
win = gui(title='File exporter')
win.setIcon('images/Extract.ico')
win.addLabel('tx_1', 'select sql script')
win.addFileEntry('f1')
#win.addStatusbar(header='file extension selected: ')
FILE_SEP = ['- select file seperator -', 'comma ( , )', 'tab ( )', 'pipe ( | )']
win.addOptionBox('file seperator', FILE_SEP)

with win.labelFrame('file extension'):
  win.addRadioButton('f_ext', '.csv')
  win.addRadioButton('f_ext', '.txt')
  
win.addButton('generate file', generate_file)

win.go()
