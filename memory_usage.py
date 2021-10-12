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

   def run_timers(self, memory_limit, minutes): #starta timers
        minutes *= 60
        while(True): 
            self.check_memory_usage(memory_limit)
            time.sleep(minutes)  

    def check_memory_usage(self, memory_limit):
        current_memory_usage = os.popen("free -tm").read().splitlines()
        memory_line = current_memory_usage[1].split()
        
        memory_limit //= 1000
        current_used = memory_line[2]
        
        if(current_used > memory_limit):
            self.create_log()
        else:
            #write 1 line in log to say things are ok
         
    def create_log(self, over_the_limit):
        memory = os.popen("ps aux | grep -v python3 | grep -v aux").read().splitlines()
        memory_list = []

        for line in memory:
            memory_list.append(line.split())
        
        ## TODO: Rewrite this part to write to log instead
        for line in memory_list:
            if(line[4] == "VSZ"):
                print(line[1], ":", line[4], " - ", line[10])
            elif(int(line[4]) > 0):
         
if(__name__ == "__main__"):
    args = sys.argv[1:]

    memory_limit = args[0]
    minutes = int(args[1])

memory_check = Memory_Check()
memory_check.main(memory_limit, minutes)
