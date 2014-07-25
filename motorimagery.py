#author: John Naulty Jr.
#date: July 2014
#SSVEP class.

from psychopy import visual, core, event
import csv_collector

class MotorImagery(object):
    #init sets the window(mywin), and the frequency of the flashing(frame_on, frame_off)
    #Frame duration in seconds = 1/monitorframerate(in Hz)
    #Thus the fastest frame rate could be 1 frame on 1 frame off
    #which equals 2/60 == 30Hz
    #Flash frequency = refreshrate/(frame_on+frame_off)
    
    def __init__(self, mywin= visual.Window([800, 600], fullscr=False, monitor='testMonitor',units='deg'),
                frame_on=5, frame_off=5, trialdur = 5.0, port='/dev/ttyACM0',
                fname='SSVEP.csv', numtrials=4, waitdur=2):
        
        self.mywin = mywin
        self.frame_on = frame_on
        self.frame_off = frame_off
        self.trialdur = trialdur
        self.fname = fname
        self.numtrials = numtrials
        self.waitdur = waitdur
        self.port = port

    def collecting(self):
        self.collector = csv_collector.CSVCollector(fname=self.fname, port= self.port)
        self.collector.start()

    def epoch(self, mark):
        self.collector.tag(mark)
        
   
    def start(self):
        
        self.text1='Right-Hand'
        self.text2='Left-Hand'
        self.text3='Feet'
        self.text4='Tongue'
        self.pattern1 = visual.TextStim(win=self.mywin, text=self.text1, font='', pos=(0.0, 0.0), depth=0, rgb=None, color=(1.0, 1.0, 1.0),
         colorSpace='rgb', opacity=1.0,contrast=1.0, units='', ori=0.0,
          height=None, antialias=True, bold=False, italic=False, alignHoriz='center',
          alignVert='center', fontFiles=[],
         wrapWidth=None, flipHoriz=False, flipVert=False, name=None, autoLog=None)
        self.pattern2 = visual.TextStim(win=self.mywin, text=self.text1, font='', pos=(0.0, 0.0), depth=0, rgb=None, color=(1.0, 1.0, 1.0),
         colorSpace='rgb', opacity=1.0,contrast=1.0, units='', ori=0.0,
          height=None, antialias=True, bold=False, italic=False, alignHoriz='center',
          alignVert='center', fontFiles=[],
         wrapWidth=None, flipHoriz=False, flipVert=False, name=None, autoLog=None)
        self.pattern3 = visual.TextStim(win=self.mywin, text=self.text1, font='', pos=(0.0, 0.0), depth=0, rgb=None, color=(1.0, 1.0, 1.0),
         colorSpace='rgb', opacity=1.0,contrast=1.0, units='', ori=0.0,
          height=None, antialias=True, bold=False, italic=False, alignHoriz='center',
          alignVert='center', fontFiles=[],
         wrapWidth=None, flipHoriz=False, flipVert=False, name=None, autoLog=None)
        self.pattern4 = visual.TextStim(win=self.mywin, text=self.text1, font='', pos=(0.0, 0.0), depth=0, rgb=None, color=(1.0, 1.0, 1.0),
         colorSpace='rgb', opacity=1.0,contrast=1.0, units='', ori=0.0,
          height=None, antialias=True, bold=False, italic=False, alignHoriz='center',
          alignVert='center', fontFiles=[],
         wrapWidth=None, flipHoriz=False, flipVert=False, name=None, autoLog=None)
        """
        self.pattern2 = visual.TextStim(win=self.mywin, name=self.text2, units='cm', 
                        tex=None, mask=None,
                        ori=0, pos=[0, 0], size=10, sf=1, phase=0,
                        color=[-1,-1,-1], colorSpace='rgb', opacity=1,
                        texRes=256, interpolate=True, depth=-2.0)
        self.pattern3 = visual.TextStim(win=self.mywin, text=self.text3, name='pattern1',units='cm', 
                        tex=None, mask=None,
                        ori=0, pos=[0, 0], size=10, sf=1, phase=0.0,
                        color=[1,1,1], colorSpace='rgb', opacity=1, 
                        texRes=256, interpolate=True, depth=-1.0)
        self.pattern4 = visual.TextStim(win=self.mywin, name=self.text4 ,units='cm', 
                        tex=None, mask=None,
                        ori=0, pos=[0, 0], size=10, sf=1, phase=0,
                        color=[-1,-1,-1], colorSpace='rgb', opacity=1,
                        texRes=256, interpolate=True, depth=-2.0)
        """
        ###Testing framerate grabber###
        print self.mywin.getActualFrameRate()
        self.Trialclock = core.Clock()
        self.freq = 60/(self.frame_on+self.frame_off)

        #start saving data from EEG device.
        #self.collecting()

        #possibly convert trialdur into frames given refresh rate (normally set at 60Hz)
        self.framerate = self.mywin.getActualFrameRate()
        #divison here makes it tricky
        self.trialframes = self.trialdur/60
        self.count = 0
        

        while self.count<self.numtrials:

            
            #reset tagging
            self.should_tag = False
            #self.epoch(0)
            while self.Trialclock.getTime()<self.trialdur:

                #draws square and fixation on screen.
                if self.count == 0:
                    self.pattern1.setAutoDraw(True)
                elif self.count == 1:
                    self.pattern2.setAutoDraw(True)
                elif self.count == 2:
                    self.pattern3.setAutoDraw(True)
                elif self.count == 3:
                    self.pattern4.setAutoDraw(True)

                """         
                ###Tagging the data with the calculated frequency###
                Attempting to only get 1 sample tagged, however, this is hard.
                """         
                """alternative way to tag
                if self.should_tag == False:
                    #self.epoch(self.freq)
                    self.epoch(70)
                    self.mywin.flip()
                
                self.epoch(0)
                self.should_tag = True
                """
                #self.epoch(70)
                
            #self.epoch(0)
            #clean black screen off
            self.mywin.flip()
            #wait certain time for next trial
            core.wait(self.waitdur)
            #reset clock for next trial
            self.Trialclock.reset()    
            #count number of trials
            self.count+=1
     
            """
            ###Tagging the Data at end of stimulus###
            
    """          
        #self.collector.disconnect()
            

  
"""
Here are some test cases 
Just run this program by itself if you don't want to use run.py

"""

if "__name__" == "__main__":
    motorimagery = MotorImagery()
    motorimagery.start()


   



