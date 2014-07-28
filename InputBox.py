"""
Author:JOHN NAULTY 
DATE: JULY 2014
SSVEP_GUI
"""

from psychopy import gui



class InputBox(object):

  def __init__(self):
    self.myDlg = gui.Dlg(title="OpenBCI Menu")
    self.myDlg.addText('Subject info')
    self.myDlg.addField('Participant:')#0
    self.myDlg.addField('Session', 001)#1
    self.myDlg.addField('Port', '/dev/tty/ACM0')#2
    self.myDlg.addText('Frequency Selction')
    self.myDlg.addField('Frequency', choices=["None", "6", "7","10","12", "15", "20"])#3
    self.myDlg.addText('Flash Duration')
    self.myDlg.addField('Duration', '5')#4
    self.myDlg.addText('Time after stimulus')
    self.myDlg.addField('InterTrialTime', '2')#5
    self.myDlg.addText('Choose Number of Trials')
    self.myDlg.addField('NumberTrials', '1')#6
    self.myDlg.show()  # show dialog and wait for OK or Cancel
    if self.myDlg.OK:  # then the user pressed OK
      self.thisInfo = self.myDlg.data
      self.options = {'participant': self.thisInfo[0], 'session': self.thisInfo[1], 'port': self.thisInfo[2], 'Frequency': self.thisInfo[3], 'Duration': self.thisInfo[4], 'InterTrialTime': self.thisInfo[5], 'NumberTrials': self.thisInfo[6]}
    
    else:
      print 'User Cancelled'

            # Setup filename for saving
    self.fname = '%s_%s.csv' %(self.options['participant'], self.options['session'])
    #port name
    self.port = '%s' %self.options['port']
    #flash duration
    self.flash_duration= '%s' %self.options['Duration']
    #number of trials
    self.num_trials= '%s' %self.options['NumberTrials']
    #time to wait between trials
    self.wait_dur= '%s' %self.options['InterTrialTime']

  def file(self):
          return str(self.fname)

  def port_name(self):
          return str(self.port)

  def stim_duration(self):
          return int(self.flash_duration)
  
  def stim_trials(self):
          return int(self.num_trials)
  
  def waitduration(self):
          return int(self.wait_dur)

