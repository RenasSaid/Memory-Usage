#!/usr/bin/env python3

import sys, os

class Memory_Check(object):
    def __init__(self):
        self.memory_limit = ""
        self.minutes = 0

    def main(self, memory_limit, minutes):
        self.memory_limit = memory_limit
        self.minutes = minutes

        over_the_limit = self.check_memory_usage(self.memory_limit, self.minutes)

        message_user(over_the_limit)

        pass

    def check_memory_usage(self, memory_limit, minutes):
        
    
    def message_user(self, over_the_limit):
        if(over_the_limit == True):
            pass
        else:
            print("Memory limit has not been reached.")

    pass

if(__name__ == "__main__"):
    args = sys.argv[1:]

    memory_limit = args[0]
    minutes = int(args[1])

memory_check = Memory_Check()
memory_check.main(memory_limit, minutes)
