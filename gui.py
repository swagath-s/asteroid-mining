
import config
from main import *
from Tkinter import *
import os

window = Tk()
"""
os.remove('config.py')
temp = open('config.py', 'w')  #to make sure some old data isn't being carried over
print temp.name
temp.close() """

def callback(event):
	findAsteroid()


config.canv = Canvas(window, height=100, width=400)
config.entr = Entry(window)
config.entr.focus()
goButton = Button(window, text="Go", command = findAsteroid)
goButton.bind('<Return>', callback)


config.entr.pack()
goButton.pack()
window.mainloop()

