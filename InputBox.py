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
		self.expInfo = {u'session': u'001', u'participant': u'001', u'port': u'COM9'}
		self.dlg = gui.DlgFromDict(dictionary=self.expInfo, title=self.expName)
		if self.dlg.OK == False: 
		    core.quit()  # user pressed cancel


		# Setup filename for saving
		self.fname = '%s_%s.csv' %(self.expInfo['participant'], self.expInfo['session'])
		#port name
		self.port = '%s' %self.expInfo['port']

	def file(self):
		return self.fname

	def port_name(self):
		return self.port

