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
        self.text1='Right-Hand'
        self.text2='Left-Hand'
        self.text3='Feet'
        self.text4='Tongue'
        self.pattern1 = visual.TextStim(win=self.mywin, text=self.text1)
        self.pattern2 = visual.TextStim(win=self.mywin, text=self.text2)
        self.pattern3 = visual.TextStim(win=self.mywin, text=self.text3)
        self.pattern4 = visual.TextStim(win=self.mywin, text=self.text4)

        

    def collecting(self):
        self.collector = csv_collector.CSVCollector(fname=self.fname, port= self.port)
        self.collector.start()

    def epoch(self, mark):
        self.collector.tag(mark)
        
   
    def start(self):
        
        
        
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
                    self.pattern1.draw()
                    self.mywin.flip()
                
                elif self.count == 1:
                    self.pattern2.draw()
                    self.mywin.flip()
                elif self.count == 2:
                    self.pattern3.draw()
                    self.mywin.flip()
                elif self.count == 3:
                    self.pattern4.draw()
                    self.mywin.flip()
                    
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

motorimagery = MotorImagery()

motorimagery.start()



   



