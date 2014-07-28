#author: John Naulty Jr.
#date: July 2014
#SSVEP class.

from psychopy import visual, core, event
import random
import csv_collector

class MotorImagery(object):
    #init sets the window(mywin), and the frequency of the flashing(frame_on, frame_off)
    #Frame duration in seconds = 1/monitorframerate(in Hz)
    #Thus the fastest frame rate could be 1 frame on 1 frame off
    #which equals 2/60 == 30Hz
    #Flash frequency = refreshrate/(frame_on+frame_off)
    
    def __init__(self, mywin= visual.Window([800, 600], fullscr=False, monitor='testMonitor',units='deg'),
                 trialdur = 10.0, port=None,
                 fname='motor_imagery.csv', num_repeats=4, waitdur=5):
        
        self.mywin = mywin
        self.trialdur = trialdur
        self.fname = fname
        self.num_repeats = num_repeats
        self.waitdur = waitdur
        self.port = port
        self.labels = ['Right hand', 'Left hand', 'Feet', 'Tongue']
        self.patterns = [ visual.TextStim(win=self.mywin, text=lbl) for lbl in self.labels ]

                

    def collecting(self):
        self.collector = csv_collector.CSVCollector(fname=self.fname, port= self.port)
        self.collector.start()

    def epoch(self, mark):
        self.collector.tag(mark)
        
    def generate_pattern_order(self):
        self.pattern_order = list()
        for i in range(self.num_repeats):
            x = list(range(len(self.labels)))
            random.shuffle(x)
            self.pattern_order.extend(x)
        
    def start(self):
        
        
        
        ###Testing framerate grabber###
        print self.mywin.getActualFrameRate()
        self.Trialclock = core.Clock()

        #possibly convert trialdur into frames given refresh rate (normally set at 60Hz)
        # self.framerate = self.mywin.getActualFrameRate()
        # self.trialframes = self.trialdur * self.framerate
        
        self.generate_pattern_order()
        self.count = 0
        self.trial_num = 0
        
        #start saving data from EEG device.
        self.collecting()

        while self.trial_num < len(self.labels) * self.num_repeats:

            
            #reset tagging
            self.should_tag = False
            self.epoch(0)

            # self.Trialclock.reset()    

            p = self.pattern_order[self.trial_num]
            
            self.patterns[p].draw()
            self.mywin.flip()
            self.epoch(p)
            core.wait(self.trialdur)
                
            #clean black screen off
            self.mywin.flip()
            self.epoch(0)
            #wait certain time for next trial
            core.wait(self.waitdur)

            #count number of trials
            self.trial_num += 1
     
        self.collector.stop()
        self.collector.disconnect()
            

  
"""
Here are some test cases 
Just run this program by itself if you don't want to use run.py

"""

if __name__ == '__main__':
    motorimagery = MotorImagery()
    motorimagery.start()



   



