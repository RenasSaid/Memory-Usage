#!/usr/bin/env python3

import sys, os, time

class Memory_Check(object):
    def __init__(self):
        self.memory_limit = ""
        self.minutes = 0

    def main(self, memory_limit, minutes):
        self.memory_limit = memory_limit
        self.minutes = minutes
        
        self.run_timers()

        over_the_limit = self.check_memory_usage(self.memory_limit, self.minutes)

        message_user(over_the_limit)

        pass

    def check_memory_usage(self, memory_limit, minutes):
        pass
        
    
    def message_user(self, over_the_limit):
        if(over_the_limit == True):
            pass
        else:
            print("Memory limit has not been reached.")

    def run_timers(self): #starta timers
        interval =0
        while(True):
            time.sleep(1)
            self.five_min_event()
            interval += 1

            if (interval == 12):
                self.five_min_event()
                self.sixty_min_event()
                interval = 0
        

    def five_min_event(self): #event var 5min, kolla om över 50Mb ram usage 
        print("5min")

    def sixty_min_event(self): #event var 60min, kolla om över 1Gb ram usage
        print("60min")

if(__name__ == "__main__"):
    args = sys.argv[1:]

    memory_limit = args[0]
    minutes = int(args[1])

memory_check = Memory_Check()
memory_check.main(memory_limit, minutes)
