#!/usr/bin/env python3
"""Sample script to run a few colour tests on the strip."""
import math
from colorschemes import colorschemes

NUM_LED = 144


print('Clear')
MY_CYCLE = colorschemes.Scanner(num_led=NUM_LED, pause_value=0.1, num_steps_per_cycle=1, color = [0x000000], global_brightness = 100,  \
                                    num_cycles=1000)
#MY_CYCLE.start()

# One Cycle with one step and a pause of three seconds. Hence three seconds of white light
#print('Three Seconds of white light')
MY_CYCLE = colorschemes.Solid(num_led=NUM_LED, pause_value=1,
                             num_steps_per_cycle=1, num_cycles=1)
#MY_CYCLE.start()


# One Cycle with of theater chase
#print('Three Seconds of white light')

MY_CYCLE = colorschemes.ChristmasTest(num_led=NUM_LED, pause_value=0.01,
                                  num_steps_per_cycle=NUM_LED, num_cycles=10)
#MY_CYCLE.start()


# One Cycle with one step and a pause of three seconds. Hence three seconds of white light
#print('Three Seconds of white light')
MY_CYCLE = colorschemes.Solid(num_led=NUM_LED, pause_value=3,
                             num_steps_per_cycle=1, num_cycles=1)
#MY_CYCLE.start()

# Go twice around the clock
#print('Go twice around the clock')
MY_CYCLE = colorschemes.RoundAndRound(num_led=NUM_LED, pause_value=0,
                                     num_steps_per_cycle=NUM_LED, num_cycles=2)
#MY_CYCLE.start()

# One cycle of red, green and blZue each
#print('One strandtest of red, green and blue each')
MY_CYCLE = colorschemes.StrandTest(num_led=NUM_LED, pause_value=0.04,
                                  num_steps_per_cycle=NUM_LED, color=0x000000,num_cycles=3)
#MY_CYCLE.start()

# One slow trip through the rainbow
print('One slow trip through the rainbow')
MY_CYCLE = colorschemes.Rainbow(num_led=NUM_LED, pause_value=0,
                               num_steps_per_cycle=255, num_cycles=10)
#MY_CYCLE.start()


# Five quick trips through the rainbow
#print('Five quick trips through the rainbow')
MY_CYCLE = colorschemes.TheaterChase(num_led=NUM_LED, pause_value=0.1,
                                    num_steps_per_cycle=35,  num_cycles=50)
#MY_CYCLE.start()


#Color is RBG

# Nice warm color 0xFF0F99, 0xF61288, 0xF00E80
# incandescent 0xF60F77

#wife approved 0xF00E80 (but this is brighter 0xFF1699 Now need to figure out how to do a blinking program. Chasing would be good., sparkling, with hints of cold lite.
# There is room to play with the R in wife approved from D8 to FF
#Create a sparkles program

#Good starfield spread out over the length. Need to find a way to blend in. Can also run by itself at times. Random Blink Frequency denominator of absolute 500 is good for blending.
# absolute 100 good for slow alone and 100 for pretty fast
# relative to num_led, num_led * 50 is very low and blinker_denominator = num_led * 25 is great for blinker_denominator = num_led * 15 random blending, blinker_denominator = num_led / 10 very fast
# Note that randint has a limit. 40 with an LED count of 240 (1/6 seems to be the limit).
# need to add a new variable for star field regarding randomness and count
# MY_CYCLE = colorschemes.StarField(num_led=NUM_LED, pause_value=0.001, num_steps_per_cycle=1, hold_time = 0, num_cycles=1000)




#create a loop that starts at a particular time (need a sleep command?) and ends adt a particular time
for i in range(0, 1):
    # One slow trip through the rainbow
    
    print('Warm Fade')
    MY_CYCLE = colorschemes.ColorFade(num_led=NUM_LED, pause_value=0.001, num_steps_per_cycle=1, color =0xFF05AA, global_brightness = 128, num_cycles=1000)
    #MY_CYCLE.start()
    
    print('Warm Fade')
    MY_CYCLE = colorschemes.ColorFade(num_led=NUM_LED, pause_value=0.001, num_steps_per_cycle=1, color =0xF61288, global_brightness = 20, num_cycles=1000)
    #MY_CYCLE.start()

    print('Warm Fade')
    MY_CYCLE = colorschemes.ColorFade(num_led=NUM_LED, pause_value=0.001, num_steps_per_cycle=1, color =0xF61288, global_brightness = 20, num_cycles=1000)
    #MY_CYCLE.start()
    
    print('Warm Fade')
    MY_CYCLE = colorschemes.ColorFade(num_led=NUM_LED, pause_value=0.001, num_steps_per_cycle=1, color =0xF00E80, color_brightness = 80, global_brightness = 20, \
                                      blink_factor = 200, blink_color = 0xFFFFFF, fade_time = 5, num_cycles=5000)
    #MY_CYCLE.start()
    
    print('Test Fade')
    MY_CYCLE = colorschemes.ColorFade(num_led=NUM_LED, pause_value=0.001, num_steps_per_cycle=1, color = 0xFFFFFF, global_brightness = 100, blink_factor = 100, \
                                      blink_color = 0xFFFFFF, fade_time = .05, num_cycles=2500)
    #MY_CYCLE.start()
    
    print('Star Field')
    MY_CYCLE = colorschemes.ColorFade(num_led=NUM_LED, pause_value=0.001, num_steps_per_cycle=1, color = 0x000000, global_brightness = 100, blink_factor = 1, blink_color = 0xFFFFAA, num_cycles=5000)
    #MY_CYCLE.start()
    
    print('Scanner')
    MY_CYCLE = colorschemes.Scanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.1, num_steps_per_cycle=50, color = [0xFF0000, 0x0000FF], global_brightness = 100, blink_factor = 500, blink_color = 0xFFFFAA, \
                                    length = 10, fade_tail = 1, snake_separation = 0, num_cycles=2)
    #MY_CYCLE.start()
    #225 repeats of 4x2 seconds = 30 minutes
    for i in range(225):
        #print('CollapseScanner')
        # if you want to cycle normally, num_steps_per_cycle should equal num_leds/2 + length
        MY_CYCLE = colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.02, num_steps_per_cycle=82, color = [0xFF0000], global_brightness = 100, \
                                                length = math.floor(NUM_LED / 2), fade_tail = 1, snake_separation = 10, num_cycles=1)
        #MY_CYCLE.start()
        
        #print('CollapseScanner')
        # if you want to cycle normally, num_steps_per_cycle should equal num_leds/2 + length
        MY_CYCLE = colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.02, num_steps_per_cycle=82, color = [0x0000FF], global_brightness = 100, \
                                                length = math.floor(NUM_LED / 2), fade_tail = 1, snake_separation = 10, num_cycles=1)
        #MY_CYCLE.start()
    
    
    print('Pulse Refresh')
    MY_CYCLE = colorschemes.PulseRefresh(num_led=NUM_LED, pause_value=0.05, num_steps_per_cycle=100, color = [0xFF0000, 0x0000FF], global_brightness = 100, blink_factor = 500, blink_color = 0xFFFFAA, \
                                    length = 5, fade_tail = 1, snake_separation = -1, num_cycles=2)
    #MY_CYCLE.start()
    


    print('Carnival')
    MY_CYCLE = colorschemes.Carnival(num_led=NUM_LED, pause_value=0.001, num_steps_per_cycle=30, color = [0xFF0000, 0x0000FF, 0xFF0699], global_brightness = 100, \
                                    length = 3, fade_tail = 0, snake_separation = 3, rotate = 0, num_cycles=50)
    #MY_CYCLE.start()

    print('Carnival')
    MY_CYCLE = colorschemes.Carnival(num_led=NUM_LED, pause_value=0.08, num_steps_per_cycle=100, color = [0xFF0000, 0x0000FF, 0xFF0699], global_brightness = 100, \
                                    length = 3, fade_tail = 1, snake_separation = 3, rotate = 1, num_cycles=1)
    #MY_CYCLE.start()
    
    print('Carnival')
    MY_CYCLE = colorschemes.Carnival(num_led=NUM_LED, pause_value=0.08, num_steps_per_cycle=100, color = [0xFF0000, 0x0000FF, 0xFF0699, 0x00FF00], global_brightness = 100, \
                                    length = 3, fade_tail = 1, snake_separation = 3, rotate = 1, num_cycles=3)
    #MY_CYCLE.start()
    
    
    #Each 500 cycles = 10 seconds, so 90,000 = 30 minutes
    print('Twinkle Lights')
    MY_CYCLE = colorschemes.Twinkle(num_led=NUM_LED, pause_value=0.01, num_steps_per_cycle=1, color =0xFF1699, color_brightness = 100, global_brightness = 100, \
                                      led_multiplier = 2, blink_factor = 200, blink_color = 0xFFFFFF, fade_time = 1, num_cycles=90000)
    #MY_CYCLE.start()

    """
    30 seconds
    MY_CYCLE = colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 1, pause_value=0.15, num_steps_per_cycle=1, color = 0x000000, global_brightness = 100, \
                                      blink_factor = 1, blink_color = 0xFFFFAA, num_cycles=200)
    """
    #this is just over 2 minutes
    print('Star Field')
    MY_CYCLE = colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 1, pause_value=0.15, num_steps_per_cycle=1, color = 0x000000, global_brightness = 100, \
                                      blink_factor = 1, blink_color = 0xFFFFAA, num_cycles=800)
    #MY_CYCLE.start()

print('Star Field')
    #MY_CYCLE = colorschemes.StarField(num_led=NUM_LED, pause_value=0.001, num_steps_per_cycle=1, num_cycles=1000)
    #MY_CYCLE.start()

print('Green Fade')
MY_CYCLE = colorschemes.ColorFade(num_led=NUM_LED, pause_value=0.001, num_steps_per_cycle=1, color =0x0000FF, global_brightness = 128, num_cycles=1000)
#MY_CYCLE.start()


print('Red Fade')
MY_CYCLE = colorschemes.ColorFade(num_led=NUM_LED, pause_value=0.001, num_steps_per_cycle=1, color =0xFF0000, global_brightness = 128, num_cycles=1000)
#MY_CYCLE.start()















#create a loop that starts at a particular time (need a sleep command?) and ends adt a particular time

while (True):
#225 repeats of 4x2 seconds = 30 minutes
    for i in range(225):
        #print('CollapseScanner')
        # if you want to cycle normally, num_steps_per_cycle should equal num_leds/2 + length
        MY_CYCLE = colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.02, num_steps_per_cycle=82, color = [0xFF0000], global_brightness = 100, \
                                                length = math.floor(NUM_LED / 2), fade_tail = 1, snake_separation = 10, num_cycles=1)
        MY_CYCLE.start()
        
        #print('CollapseScanner')
        # if you want to cycle normally, num_steps_per_cycle should equal num_leds/2 + length
        MY_CYCLE = colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.02, num_steps_per_cycle=82, color = [0x0000FF], global_brightness = 100, \
                                                length = math.floor(NUM_LED / 2), fade_tail = 1, snake_separation = 10, num_cycles=1)
        MY_CYCLE.start()
    
 
    #Each 500 cycles = 10 seconds, so 90,000 = 30 minutes
    print('Twinkle Lights')
    MY_CYCLE = colorschemes.Twinkle(num_led=NUM_LED, pause_value=0.01, num_steps_per_cycle=1, color =0xFF1699, color_brightness = 100, global_brightness = 100, \
                                      led_multiplier = 2, blink_factor = 200, blink_color = 0xFFFFFF, fade_time = 1, num_cycles=90000)
    MY_CYCLE.start()

    """
    30 seconds
    MY_CYCLE = colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 1, pause_value=0.15, num_steps_per_cycle=1, color = 0x000000, global_brightness = 100, \
                                      blink_factor = 1, blink_color = 0xFFFFAA, num_cycles=200)
    """
    #this is just over 2 minutes
    print('Star Field')
    MY_CYCLE = colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 1, pause_value=0.15, num_steps_per_cycle=1, color = 0x000000, global_brightness = 100, \
                                      blink_factor = 1, blink_color = 0xFFFFAA, num_cycles=800)
    MY_CYCLE.start()













# Five quick trips through the rainbow
#print('Five quick trips through the rainbow')
MY_CYCLE = colorschemes.TheaterChase(num_led=NUM_LED, pause_value=0.04,
                                    num_steps_per_cycle=35, num_cycles=50)
#MY_CYCLE.start()



    
    
print('Clear')
MY_CYCLE = colorschemes.Scanner(num_led=NUM_LED, pause_value=0.1, num_steps_per_cycle=1, color = [0x000000], global_brightness = 100,  \
                                    num_cycles=1)
MY_CYCLE.start()
print('Finished the test')
