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
import mne

bp = mne.filter.band_pass_filter


#'/dev/tty.usbmodemfd121'
#Notes for using csv_collector.py
#initiate CSVCollector, takes filename, port, and baud as inputs
#start recording with start() method
#tag recording with tag() method
#what needs to be implemented
#   A if statement for multiprocessing/threading.

class SpectralPlotter(object):

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

        fs = len(self.times) / (self.times[-1] - self.times[0])

        wsize = 64
        #subplot(8, 1, i+1)
        signal = self.data[..., self.plot_channel-1]
        signal = signal[~np.isnan(signal)]
        signal = bp(signal, fs, 2, 55)

        X = mne.time_frequency.stft(signal, wsize)
        freqs = mne.time_frequency.stftfreq(wsize, sfreq=fs)

        plt.clf()
        imshow(np.log(abs(X[0])), aspect='auto',
               origin='lower', interpolation="None",
               vmin=-14, vmax=-4,
               extent=[0, 4, 0, max(freqs)])
        ylim([0, 60])

        draw()

    def background_plot(self):
        while self.should_plot:
            if len(self.data) > 100:
                self.plot()
            time.sleep(0.05)

    def receive_sample(self, sample):
        t = time.time()
        sample = sample.channels
        self.data = np.vstack( (self.data[-1000:, ...], sample) )
        self.times = np.append(self.times, t)
        self.times = self.times[-1000:]

    def start(self, channel):

        if self.bg_thread:
            self.stop()

        self.plot_channel = channel
        self.data = np.array([0]*8)
        self.times = np.array([time.time()])

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
