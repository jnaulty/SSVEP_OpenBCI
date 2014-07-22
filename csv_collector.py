#!/usr/bin/env python2

import time
import threading
import csv
from open_bci import *
from multiprocessing import Process

#'/dev/tty.usbmodemfd121'
#Notes for using csv_collector.py
#initiate CSVCollector, takes filename, port, and baud as inputs
#start recording with start() method
#tag recording with tag() method
#what needs to be implemented
#   A if statement for multiprocessing/threading.

class CSVCollector(object):

    def __init__(self, fname = 'collect.csv',
                 port='/dev/ttyACM0', baud=115200):
        self.board = OpenBCIBoard(port, baud)
        self.fname = fname
        self.counter = 0
        self.file = None
        self.fieldnames = []
        self.channel_names = []
        for i in range(8):
            self.channel_names.append("channel_" + str(i))
        self.fieldnames.extend(self.channel_names)
        self.fieldnames.extend(['time', 'tag'])
            
        self.epoch = 0
        self.bg_thread = None
        
    def stop(self):
        # resolve files and stuff
        self.board.should_stream = False
        self.csv_writer = None
        self.data = []
        #self.bg_thread.join()
        self.bg_thread = None
        self.file.close()
        self.file = None
        self.epoch = 0

    def disconnect(self):
        self.board.disconnect()

    def receive_sample(self, sample):
        t = time.time()
        sample = sample.channels
        d = dict(zip(self.channel_names, sample))
        d['time'] = t
        d['tag'] = self.epoch
        self.csv_writer.writerow(d)
        self.file.flush()
        
    def start(self):
        if self.bg_thread:
            self.stop_bg_collection()

        self.file = open(self.fname, 'w')
            
        self.csv_writer = csv.DictWriter(self.file, self.fieldnames)
        self.csv_writer.writeheader()
        #create a new thread in which the OpenBCIBoard object will stream data
        self.bg_thread = threading.Thread(target=self.board.start, 
                                        args=(self.receive_sample, ))
        #self.bg_thread = Process(target=self.board.start_streaming,
        #                         args=(self.receive_sample, ))
        
        self.bg_thread.start()


    def tag(self, epoch):
        self.epoch = epoch
