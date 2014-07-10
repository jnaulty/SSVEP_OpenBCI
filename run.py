
#author:John Naulty
#date: july 2014
#SSVEP Example with Psychopy and OpenBCI
#stimuli frequency = 60/(frame_on+frame_off)


from SSVEP import *
from psychopy import gui
import csv_collector



# Store info about the experiment session
expName = 'SSVP5_75'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u'001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: 
    core.quit()  # user pressed cancel


# Setup filename for saving
filename = 'data/%s_%s' %(expInfo['participant'], expInfo['session'])

#set of stimuli followed by frequency of stimuli. 

stimuli75 = SSVEP(frame_on=4, frame_off=4, fname=filename)
stimuli75.start()

stimuli12=SSVEP(frame_on=3, frame_off=2, fname=filename)
stimuli12.start()

stimuli20=SSVEP(frame_on=2, frame_off=1, fname=filename)
stimuli20.start()

