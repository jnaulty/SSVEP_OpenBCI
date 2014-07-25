from Tkinter import *

win = Tk()
f = Frame(win)



l = Label(win, text="OpenBCI Plot")
plot = Button(f, text='Time Plot')
fft = Button(f, text='FFT')
specgram = Button(f, text='Spectogram')
ssvep = Button(f, text='SSVEP_Trial')

plot.pack(side=LEFT)
specgram.pack(side=LEFT)
fft.pack(side=LEFT)
ssvep.pack(side=LEFT)
l.pack()
f.pack()


