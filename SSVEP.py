#author: John Naulty Jr.
#date: July 2014
#SSVEP class.

from psychopy import visual, core, event
import csv_collector

class SSVEP(object):
    #init sets the window(mywin), and the frequency of the flashing(frame_on, frame_off)
    #Frame duration in seconds = 1/monitorframerate(in Hz)
    #Thus the fastest frame rate could be 1 frame on 1 frame off
    #which equals 2/60 == 30Hz
    #Flash frequency = refreshrate/(frame_on+frame_off)
    
    def __init__(self, mywin= visual.Window([800, 600], monitor='testMonitor', units='deg'),
                frame_on=5, frame_off=5, trialtime = 5.0, fname='SSVEP.csv'):
        
        self.mywin = mywin
        self.pattern1 = visual.GratingStim(win=self.mywin, name='pattern1',units='cm', 
                        tex=None, mask=None,
                        ori=0, pos=[0, 0], size=3, sf=1, phase=0.0,
                        color=[1,1,1], colorSpace='rgb', opacity=1,
                        texRes=256, interpolate=True, depth=-1.0)
        self.pattern2 = visual.GratingStim(win=self.mywin, name='pattern2',units='cm', 
                        tex=None, mask=None,
                        ori=0, pos=[0, 0], size=3, sf=1, phase=0,
                        color=[-1,-1,-1], colorSpace='rgb', opacity=1,
                        texRes=256, interpolate=True, depth=-2.0)
        self.fixation = visual.GratingStim(win=self.mywin, size = 0.3, pos=[0,0], sf=0, rgb=-1)
        self.frame_on = frame_on
        self.frame_off = frame_off
        self.trialtime = trialtime
        self.fname = fname

        
    def start(self):
        print self.mywin.getActualFrameRate()
        Trialclock = core.Clock()
        self.freq = 60/(self.frame_on+self.frame_off)
        #self.collector = csv_collector.CSVCollector(fname=self.fname)
        #self.collector.start()
        
        #possibly convert trialtime into frames given refresh rate (normally set at 60Hz)
        #self.framerate = self.mywin.getActualFrameRate()
        #self.trialframes = trialtime/self.framerate
     
        while Trialclock.getTime()<self.trialtime:
    
            self.pattern1.setAutoDraw(True)
            self.fixation.setAutoDraw(True)
            #self.collector.tag(self.freq)
   
            for frameN in range(self.frame_on):
                self.mywin.flip()
                
            self.pattern1.setAutoDraw(False)
            self.pattern2.setAutoDraw(True)
            
            for frameN in range(self.frame_off):
                self.mywin.flip()
            self.pattern2.setAutoDraw(False)
            #self.collector.tag(0)

  
#test cases 

if "__name__" == "__main__":
    stimuli75Hz = SSVEP(frame_on=4, frame_off=4)
    stimuli75Hz.start()

    stimuli12=SSVEP(frame_on=3, frame_off=2)
    stimuli12.start()

    stimuli20=SSVEP(frame_on=2, frame_off=1)
    stimuli20.start()

   



