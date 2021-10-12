#!/usr/bin/env python3

import sys, os, time

class Memory_Check(object):
    def __init__(self):
        self.memory_limit = ""
        self.minutes = 0

    def main(self, memory_limit, minutes):
        self.memory_limit = memory_limit
        self.minutes = minutes
        
        self.memory_limit = self.convert_memory_limit_to_bytes(self.memory_limit)
        
        self.memory_limit = int(self.memory_limit)
        self.run_timers(self.memory_limit, self.minutes)

    def convert_memory_limit_to_bytes(self, memory_limit):
        if(memory_limit[-1] == "M"):
            memory_limit = float(memory_limit.replace("M", ""))
            memory_limit *= 10 ** 6
            return memory_limit

        elif(memory_limit[-1] == "G"):
            memory_limit = float(memory_limit.replace("G", ""))
            memory_limit *= 10 ** 9
            return memory_limit

        else:
            if(memory_limit.isnumeric()):
                memory_limit = float(memory_limit)
                return memory_limit
            else:
                print("Memory limit must be numeric or given in [M]egabytes or [G]igabytes.")

         
    def message_user(self, over_the_limit):
        if(over_the_limit == True):
            pass
        else:
            print("Memory limit has not been reached.")

    def run_timers(self, shorter, longer): #starta timers
        time_passed = 0
        while(True):
            if(time_passed < longer)    
                self.shorter_event()
                time.sleep(shorter)
                time_passed += shorter
            else:
                self.shorter_event()
                self.longer_event()
                time_passed = 0
        

    def shorter_event(self): #event var 5min, kolla om över 50Mb ram usage 
        print("5min")

    def longer_event(self): #event var 60min, kolla om över 1Gb ram usage
        print("60min")

if(__name__ == "__main__"):
    args = sys.argv[1:]

    memory_limit = args[0]
    minutes = int(args[1])

memory_check = Memory_Check()
memory_check.main(memory_limit, minutes)
