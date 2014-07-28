
from psychopy import gui
import raw_plotter
import spectral_plotter
import multi_plotter


#class InputBox(object):

myDlg = gui.Dlg(title="OpenBCI Menu")
myDlg.addText('Subject info')
myDlg.addField('Participant')#0
myDlg.addField('Session', 001)#1
myDlg.addField('Port', '/dev/tty/ACM0')#2
myDlg.addText('Visual Options')
myDlg.addField('Plots:', choices=["None", "Spectral_Plot", "FFT",
"Spectogram"])#3
myDlg.addText('Experiment Choices')
myDlg.addField('Experiments', choices=["None", "SSVEP", "ERP",
	"Motor_Imagery"])#4
myDlg.show()  # show dialog and wait for OK or Cancel
if myDlg.OK:  # then the user pressed OK
  thisInfo = myDlg.data
  options = {'participant': thisInfo[0], 'session': thisInfo[1],'port': thisInfo[2], 'plot': thisInfo[3],'experiment': thisInfo[4]}
  fname = '%s_%s.csv' %(options['participant'],    options['session'])
  port = options['port']
		
		
		#iterate through dictionary to see if Function is called
		#right now just using print statements, soon insert actual python scripts
  for value in options.itervalues():
    if value == 'Spectral_Plot':
      time_plot=raw_plotter.RawPlotter()
      time_plot.start()				
    elif value == 'FFT':
      fft_plot=raw_plotter.RawPlotter()
      fft_plot.start()
    elif value == 'Spectogram':
      specgram=spectral_plotter.SpectralPlotter()
      specgram.start()
            
      print 'Spectogram'
    elif value == 'SSVEP':
      import run_ssvep
    elif value == 'ERP':
      print 'ERP'
    elif value == 'Motor_Imagery':
      print 'Imagine!'
    
			

else:
  print 'user cancelled'
