# lights
from appJar import gui
import time

app=gui()
app.addRadioButton("song", "Killer Queen")
app.addRadioButton("song", "Paradise City")
app.addRadioButton("song", "Parklife")
def press(name):
  print (name)
  app.thread(animate)

app.addStatusbar()
app.setStatusbar('status...')
app.addButton('test', press)
#here is the animation
def animate():
    x = 10 
    while x > 0:
      #time.sleep(1)
      print (x)
      x -= 1
      app.queueFunction(app.setStatusbar, ('\r'+'generating files...|')) 
      time.sleep(0.1)
      app.queueFunction(app.setStatusbar, ('\r'+'generating files.../')) 
      time.sleep(0.1)
      app.queueFunction(app.setStatusbar, ('\r'+'generating files...-')) 
      time.sleep(0.1)
      app.queueFunction(app.setStatusbar, ('\r'+'generating files...\\')) 
      time.sleep(0.1)
    app.popUp('generating file', 'process complete')
    app.setStatusbar('status...')



app.go()