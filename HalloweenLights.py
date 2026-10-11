#!/usr/bin/env python3
"""Sample script to run a few colour tests on the strip."""
import math
import time as t
from colorschemes import colorschemes
from datetime import datetime, time

NUM_LED = 144


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

#if(True):    
#Each 500 cycles = 10 seconds, so 90,000 = 30 minutes
# This is Christmas twinkle lights
#print('Twinkle Lights')
MY_CYCLE = colorschemes.Twinkle(num_led=NUM_LED, pause_value=0.01, num_steps_per_cycle=1, color =0x220006, color_brightness = 100, global_brightness = 100, \
                                  led_multiplier = 1, blink_factor = 200, blink_color = 0xFF0000, fade_time = 1, num_cycles=400)
MY_CYCLE.start()

#100 = 8 seconds
print('Purple Star Field')
MY_CYCLE = colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 1, pause_value=0.05, num_steps_per_cycle=1, color = 0x101000, global_brightness = 100, \
                                  blink_factor = 1, blink_color = 0xFFFFAA, num_cycles=300)
#TODO Add back
#MY_CYCLE.start()


print('Orange Star Field')
MY_CYCLE = colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 1, pause_value=.05, num_steps_per_cycle=1, color = 0x44000A, global_brightness = 100, \
                                  blink_factor = 1, blink_color = 0xFFFFAA, num_cycles=300)
#TODO Add back
#MY_CYCLE.start()

print('Dark Orange Star Field')
MY_CYCLE = colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 1, pause_value=.05, num_steps_per_cycle=1, color = 0x220006, global_brightness = 100, \
                                  blink_factor = 1, blink_color = 0xFFFFAA, num_cycles=300)
#TODO Add back
#MY_CYCLE.start()

#225 repeats of 4x2 seconds = 30 minutes
for i in range(4):
    #print('CollapseScanner')
    # if you want to cycle normally, num_steps_per_cycle should equal num_leds/2 + length
    MY_CYCLE = colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.005, num_steps_per_cycle=1, color = [0x153000], global_brightness = 100, \
                                            length = math.floor(NUM_LED / 2), fade_tail = 10, snake_separation = 0, num_cycles=1)
    #TODO Add back in
    MY_CYCLE.start()
    
    #print('CollapseScanner')
    # if you want to cycle normally, num_steps_per_cycle should equal num_leds/2 + length
    MY_CYCLE = colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.005, num_steps_per_cycle=72, color = [0x220006], global_brightness = 100, \
                                            length = math.floor(NUM_LED / 2), fade_tail = 10, snake_separation = 0, num_cycles=1)
    MY_CYCLE.start()
    
    #print('CollapseScanner')
    # if you want to cycle normally, num_steps_per_cycle should equal num_leds/2 + length
    MY_CYCLE = colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.005, num_steps_per_cycle=72, color = [0x00020], global_brightness = 100, \
                                            length = math.floor(NUM_LED / 2), fade_tail = 10, snake_separation = 0, num_cycles=1)
    MY_CYCLE.start()

#1000 cycles = 6 seconds
print('Warm Fade')
MY_CYCLE = colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 2, pause_value=0.005, num_steps_per_cycle=1, color =0xF00E80, color_brightness = 100, global_brightness = 20, \
                                   fade_time = 1, num_cycles=1500)
#MY_CYCLE.start()

#100 = 8 seconds
print('Star Field')
MY_CYCLE = colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 1, pause_value=0.03, num_steps_per_cycle=1, color = 0x000000, global_brightness = 100, \
                                  blink_factor = 1, blink_color = 0xFFFFAA, num_cycles=75)
#MY_CYCLE.start()

#Each 500 cycles = 10 seconds, so 90,000 = 30 minutes
print('Twinkle Lights')
MY_CYCLE = colorschemes.Twinkle(num_led=NUM_LED, pause_value=0.01, num_steps_per_cycle=1, color =0xFF1699, color_brightness = 100, global_brightness = 100, \
                                  led_multiplier = 2, blink_factor = 200, blink_color = 0xFFFFFF, fade_time = 1, num_cycles=500)
#MY_CYCLE.start() 

"""
30 seconds
MY_CYCLE = colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 1, pause_value=0.15, num_steps_per_cycle=1, color = 0x000000, global_brightness = 100, \
                                  blink_factor = 1, blink_color = 0xFFFFAA, num_cycles=200)
"""
#100 = 8 seconds
print('Star Field')
MY_CYCLE = colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 1, pause_value=0.02, num_steps_per_cycle=1, color = 0x000000, global_brightness = 100, \
                                  blink_factor = 1, blink_color = 0xFFFFAA, num_cycles=100)
#MY_CYCLE.start()

#225 repeats of 4x2 seconds = 30 minutes
for i in range(2):
    #print('CollapseScanner')
    # if you want to cycle normally, num_steps_per_cycle should equal num_leds/2 + length
    MY_CYCLE = colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.002, num_steps_per_cycle=82, color = [0x00FF00], global_brightness = 100, \
                                            length = math.floor(NUM_LED / 2), fade_tail = 1, snake_separation = 10, num_cycles=1)
    #MY_CYCLE.start()
    
    #print('CollapseScanner')
    # if you want to cycle normally, num_steps_per_cycle should equal num_leds/2 + length
    MY_CYCLE = colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.002, num_steps_per_cycle=82, color = [0x0000FF], global_brightness = 100, \
                                            length = math.floor(NUM_LED / 2), fade_tail = 1, snake_separation = 10, num_cycles=1)
    #MY_CYCLE.start()

print('Clear')
MY_CYCLE = colorschemes.Scanner(num_led=NUM_LED, pause_value=0.1, num_steps_per_cycle=1, color = [0x000000], global_brightness = 100,  \
                            num_cycles=1)
MY_CYCLE.start()
t.sleep(120)        

#Need to look into cleanup
