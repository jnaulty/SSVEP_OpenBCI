
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
port_addr = expinfos.port_name()
print filename
flash_dur = expinfos.stim_duration()
trialnums = expinfos.stim_trials()
waitduration = expinfos.waitduration()
print port_addr
print type(port_addr)


#set of stimuli followed by frequency of stimuli. 

"""
stimuli75 = SSVEP(frame_on=4, frame_off=4, fname=filename, port=port_addr, trialdur=flash_dur, numtrials=trialnums, waitdur=waitduration)
stimuli75.start()
print 1
"""
"""
stimuli12=SSVEP(frame_on=3, frame_off=2, fname=filename, port=port_addr,
	trialdur=flash_dur, numtrials=trialnums, waitdur=waitduration)
stimuli12.start()
print 2
"""
stimuli20=SSVEP(frame_on=2, frame_off=1, fname=filename, port=port_addr,
	trialdur=flash_dur, numtrials=trialnums, waitdur=waitduration)
stimuli20.start()

