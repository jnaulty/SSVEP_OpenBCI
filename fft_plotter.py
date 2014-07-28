#!/usr/bin/env python2

import time
import threading
import csv
import numpy as np
from multiprocessing import Process
import sys

sys.path.append('..')
from open_bci import *
from pylab import *

#'/dev/tty.usbmodemfd121'
#Notes for using csv_collector.py
#initiate CSVCollector, takes filename, port, and baud as inputs
#start recording with start() method
#tag recording with tag() method
#what needs to be implemented
#   A if statement for multiprocessing/threading.

class RawPlotter(object):

    def __init__(self, port=None, baud=115200):
        self.board = OpenBCIBoard(port, baud)
        self.bg_thread = None
        self.bg_draw_thread = None
        self.data = np.array([0]*8)
        self.should_plot = False
        
    def stop(self):
        # resolve files and stuff
        self.board.should_stream = False
        self.should_plot = False
        #self.bg_thread.join()
        self.bg_thread = None
        self.data = np.array([0]*8)
        
    def disconnect(self):
        self.board.disconnect()

    def plot(self):

        plt.clf()

        hold(True)
        
        for i in range(8):
            #subplot(8, 1, i+1)
            signal = self.data[..., i]
            signal = signal[~np.isnan(signal)]
            #signal = signal * np.hamming(len(signal))
            fourier = np.fft.rfft(signal)
            freq = np.fft.rfftfreq(signal.size, d=1.0/250.0)
            # plot(signal, label=str(i+1))
            plot(freq, np.log(abs(fourier)), label=str(i+1))
            
            #title('channel {0}'.format(i+1))
        # ylim([-0.0005, 0.0005])
        ylim([-12, 0])
        legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
               ncol=4, mode="expand", borderaxespad=0.)

        # plot(freq, np.log(abs(fourier)))
        draw()
        
    def background_plot(self):
        while self.should_plot:
            if len(self.data) > 10:
                self.plot()
            time.sleep(0.05)
        
    def receive_sample(self, sample):
        t = time.time()
        sample = sample.channels
        self.data = np.vstack( (self.data[-250:, ...], sample) )

        
    def start(self):
        
        if self.bg_thread:
            self.stop()

            
        #create a new thread in which the OpenBCIBoard object will stream data
        self.bg_thread = threading.Thread(target=self.board.start, 
                                        args=(self.receive_sample, ))
        # self.bg_thread = Process(target=self.board.start,
        #                         args=(self.receive_sample, ))

        self.bg_thread.start()

        # self.bg_draw_thread = threading.Thread(target=self.background_plot,
        #                                        args=())

        # self.bg_draw_thread.start()
        
        ion()
        figure()
        show()

        self.should_plot = True
        
        self.background_plot()

