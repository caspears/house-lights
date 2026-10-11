#!/usr/bin/env python3
"""Sample script to run a few colour tests on the strip."""
import math
import random
import time as t
from colorschemes import colorschemes
from datetime import datetime, time

NUM_LED = 480
#colorList = [0x220006, 0x101000, 0x000010]
#colorList = [0xCCCC33, 0x77FF00]
colorList = [0xFF5555, 0xFF0000]
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

    #if(is_time_between(time(15,30), time(23,30)) or is_time_between(time(4,30), time(7,30))):
    if(True):
        print('Start')
   
        #print('Twinkle Lights')
        #400 = 6 seconds
        MY_CYCLE = colorschemes.Twinkle(num_led=NUM_LED, pause_value=0.01, num_steps_per_cycle=1, color =colorList[random.randint(0, len(colorList) - 1)], color_brightness = 100, global_brightness = 100, \
                                          led_multiplier = 2, blink_factor = 200, blink_color = 0xFF0000, fade_time = 1, num_cycles=200)
        #MY_CYCLE.start()

        #300 = 14 seconds
        print('Color Star Field')
        MY_CYCLE = colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 1, pause_value=0.025, num_steps_per_cycle=1, color = colorList[random.randint(0, len(colorList) - 1)], global_brightness = 100, \
                                          blink_factor = 1, blink_color = 0xFFFFAA, num_cycles=300)
        #TODO Add back
        #MY_CYCLE.start()


        print('Orange Star Field')
        MY_CYCLE = colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 1, pause_value=.025, num_steps_per_cycle=1, color = colorList[random.randint(0, len(colorList) - 1)], global_brightness = 100, \
                                          blink_factor = 1, blink_color = 0xFFFFAA, num_cycles=300)
        #TODO Add back
        #MY_CYCLE.start()

        print('Dark Orange Star Field')
        MY_CYCLE = colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 1, pause_value=.025, num_steps_per_cycle=1, color = colorList[random.randint(0, len(colorList) - 1)], global_brightness = 100, \
                                          blink_factor = 1, blink_color = 0xFFFFAA, num_cycles=300)
        #TODO Add back
        #MY_CYCLE.start()

        #225 repeats of 4x2 seconds = 30 minutes
        for i in range(2):
            #print('CollapseScanner')
            # if you want to cycle normally, num_steps_per_cycle should equal num_leds/2 + length
            MY_CYCLE = colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.01, num_steps_per_cycle=1, color = [colorList[random.randint(0, len(colorList) - 1)]], global_brightness = 100, \
                                                    length = math.floor(NUM_LED / 2), fade_tail = 1, snake_separation = 0, num_cycles=1)
            #TODO Add back in
            MY_CYCLE.start()
            
            
            
            
            #print('CollapseScanner')
            # if you want to cycle normally, num_steps_per_cycle should equal num_leds/2 + length
            MY_CYCLE = colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.001, num_steps_per_cycle=1, color = [colorList[random.randint(0, len(colorList) - 1)]], global_brightness = 100, \
                                                    length = math.floor(NUM_LED / 2), fade_tail = 1, snake_separation = 0, num_cycles=1)
            #MY_CYCLE.start()
            
            #print('CollapseScanner')
            # if you want to cycle normally, num_steps_per_cycle should equal num_leds/2 + length
            MY_CYCLE = colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.05, num_steps_per_cycle=1, color = [colorList[random.randint(0, len(colorList) - 1)]], global_brightness = 100, \
                                                    length = math.floor(NUM_LED / 2), fade_tail = 1, snake_separation = 0, num_cycles=1)
            #MY_CYCLE.start()
        for i in range(2):
            #print('Twinkle Lights')
            #400 = 6 seconds
            MY_CYCLE = colorschemes.Twinkle(num_led=NUM_LED, pause_value=0.01, num_steps_per_cycle=1, color =colorList[random.randint(0, len(colorList) - 1)], color_brightness = 100, global_brightness = 100, \
                                              led_multiplier = 2, blink_factor = 200, blink_color = colorList[random.randint(0, len(colorList) - 1)], fade_time = 1, num_cycles=1200)
            #MY_CYCLE.start()
            
            MY_CYCLE = colorschemes.Twinkle(num_led=NUM_LED, pause_value=0.005, num_steps_per_cycle=1, color =colorList[0], color_brightness = 100, global_brightness = 100, \
                                              led_multiplier = 2, blink_factor = 2000, blink_color = colorList[1], fade_time = 1, num_cycles=1200)
            MY_CYCLE.start()
            
            MY_CYCLE = colorschemes.Twinkle(num_led=NUM_LED, pause_value=0.01, num_steps_per_cycle=1, color =colorList[1], color_brightness = 100, global_brightness = 100, \
                                              led_multiplier = 2, blink_factor = 2000, blink_color = colorList[0], fade_time = 1, num_cycles=1200)
            MY_CYCLE.start()
            
        #1500 cycles = 10 seconds
        print('Warm Fade')
        MY_CYCLE = colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 2, pause_value=0.005, num_steps_per_cycle=1, color =colorList[random.randint(0, len(colorList) - 1)], color_brightness = 100, global_brightness = 20, \
                                           fade_time = 1, num_cycles=15000)
        #MY_CYCLE.start()



        #Each 500 cycles = 10 seconds, so 90,000 = 30 minutes
        print('Twinkle Lights')
        MY_CYCLE = colorschemes.Twinkle(num_led=NUM_LED, pause_value=0.01, num_steps_per_cycle=1, color =colorList[random.randint(0, len(colorList) - 1)], color_brightness = 100, global_brightness = 100, \
                                          led_multiplier = 2, blink_factor = 200, blink_color = 0xFFFFFF, fade_time = 1, num_cycles=250)
        #MY_CYCLE.start() 

        """
        30 seconds
        MY_CYCLE = colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 1, pause_value=0.15, num_steps_per_cycle=1, color = 0x000000, global_brightness = 100, \
                                          blink_factor = 1, blink_color = 0xFFFFAA, num_cycles=200)
        """
        #100 = 8 seconds
        print('Star Field')
        MY_CYCLE = colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 1, pause_value=0.02, num_steps_per_cycle=1, color = colorList[random.randint(0, len(colorList) - 1)], global_brightness = 100, \
                                          blink_factor = 1, blink_color = 0xFFFFAA, num_cycles=300)
        #MY_CYCLE.start()

        #225 repeats of 4x2 seconds = 30 minutes
        for i in range(2):
            #print('CollapseScanner')
            # if you want to cycle normally, num_steps_per_cycle should equal num_leds/2 + length
            MY_CYCLE = colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.002, num_steps_per_cycle=82, color = [colorList[random.randint(0, len(colorList) - 1)]], global_brightness = 100, \
                                                    length = math.floor(NUM_LED / 2), fade_tail = 1, snake_separation = 10, num_cycles=1)
            #MY_CYCLE.start()
            
            #print('CollapseScanner')
            # if you want to cycle normally, num_steps_per_cycle should equal num_leds/2 + length
            MY_CYCLE = colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.002, num_steps_per_cycle=82, color = [colorList[random.randint(0, len(colorList) - 1)]], global_brightness = 100, \
                                                    length = math.floor(NUM_LED / 2), fade_tail = 1, snake_separation = 10, num_cycles=1)
            #MY_CYCLE.start()
        print('End')
    else:
        t.sleep(60) 
print('Clear')
MY_CYCLE = colorschemes.Scanner(num_led=NUM_LED, pause_value=0.1, num_steps_per_cycle=1, color = [0x000000], global_brightness = 100,  \
                            num_cycles=1)
MY_CYCLE.start()
t.sleep(120)        

#Need to look into cleanup
