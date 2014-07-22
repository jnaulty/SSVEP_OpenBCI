"""
Author:JOHN NAULTY 
DATE: JULY 2014
SSVEP_GUI
"""

from psychopy import gui

class InputBox(object):

	def __init__(self):
		# Store info about the experiment session
		self.expName = 'SSVEP'
		self.expInfo = {u'session': u'001', u'participant': u'001', u'port': u'COM9',
				 u'flash_duration': u'5', u'numtrials': u'1', u'waitdur': u'2'}
		self.dlg = gui.DlgFromDict(dictionary=self.expInfo, title=self.expName)
		if self.dlg.OK == False: 
		    core.quit()  # user pressed cancel


		# Setup filename for saving
		self.fname = '%s_%s.csv' %(self.expInfo['participant'], self.expInfo['session'])
		#port name
		self.port = '%s' %self.expInfo['port']
		#flash duration
		self.flash_duration= '%s' %self.expInfo['flash_duration']
		#number of trials
		self.num_trials= '%s' %self.expInfo['numtrials']
		#time to wait between trials
		self.wait_dur= '%s' %self.expInfo['waitdur']

	def file(self):
		return self.fname

	def port_name(self):
		return self.port

	def stim_duration(self):
		return int(self.flash_duration)
	
	def stim_trials(self):
		return int(self.num_trials)
	
	def waitduration(self):
		return int(self.wait_dur)

