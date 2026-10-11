#!/usr/bin/env python3
"""Sample script to run a few colour tests on the strip."""
import math
import random
import time as t
from colorschemes import colorschemes
from datetime import datetime, time

NUM_LED = 480
colorList = [0x0000FF, 0x00FF00, 0x00FF00, 0x0000FF]
colorIndex = -1

def is_time_between(begin_time, end_time, check_time=None):
    # If check time is not given, default to current UTC time
    #check_time = check_time or datetime.utcnow().time()
    check_time = check_time or datetime.now().time()
    if begin_time < end_time:
        return check_time >= begin_time and check_time <= end_time
    else: # crosses midnight
        return check_time >= begin_time or check_time <= end_time

#TODO Add Back
#t.sleep(5) 
while(True):

    if(True):
        print('Start')
        #colorIndex = (colorIndex + 1) % len(colorList)
 
        #225 repeats of 4x2 seconds = 30 minutes
        for i in range(2):
            #print('CollapseScanner')
            # if you want to cycle normally, num_steps_per_cycle should equal num_leds/2 + length
            MY_CYCLE = colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.002, num_steps_per_cycle=82, color = [colorList[random.randint(0, 2)]], global_brightness = 100, \
                                                    length = math.floor(NUM_LED / 2), fade_tail = 1, snake_separation = 10, num_cycles=1)
            MY_CYCLE.start()
            
            #print('CollapseScanner')
            # if you want to cycle normally, num_steps_per_cycle should equal num_leds/2 + length
            MY_CYCLE = colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.002, num_steps_per_cycle=82, color = [colorList[random.randint(0, 2)]], global_brightness = 100, \
                                                    length = math.floor(NUM_LED / 2), fade_tail = 1, snake_separation = 10, num_cycles=1)
            MY_CYCLE.start()
        print('End')
    else:
        t.sleep(60) 
print('Clear')
MY_CYCLE = colorschemes.Scanner(num_led=NUM_LED, pause_value=0.1, num_steps_per_cycle=1, color = [0x000000], global_brightness = 100,  \
                            num_cycles=1)
MY_CYCLE.start()
t.sleep(120)        

#Need to look into cleanup
