
#author:John Naulty
#date: july 2014
#SSVEP Example with Psychopy and OpenBCI
#stimuli frequency = 60/(frame_on+frame_off)


from SSVEP import *
from InputBox import InputBox
import csv_collector



expinfos = InputBox()
filename = expinfos.file()
print expinfos.port_name()
port_name = expinfos.port_name()
print filename

#set of stimuli followed by frequency of stimuli. 

stimuli75 = SSVEP(frame_on=4, frame_off=4, fname=filename, port = port_name)
stimuli75.start()

stimuli12=SSVEP(frame_on=3, frame_off=2, fname=filename, port = port_name)
stimuli12.start()

stimuli20=SSVEP(frame_on=2, frame_off=1, fname=filename, port = port_name)
stimuli20.start()

