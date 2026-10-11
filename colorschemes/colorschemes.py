"""This module contains a few concrete colour cycles to play with"""
import time
import math
from driver import colorcycletemplate
from random import randint





class StrandTest(colorcycletemplate.ColorCycleTemplate):
    """Runs a simple strand test (9 LEDs wander through the strip)."""

    color = None



    def update(self, strip, num_led, num_steps_per_cycle, current_step,
               current_cycle):
        # One cycle = The 9 Test-LEDs wander through numStepsPerCycle LEDs.
        if current_step == 0:
            self.color >>= 8  # Red->green->blue->black
        if self.color == 0:
            self.color = 0xFF0000  # If black, reset to red
        bloblen = 9
        if num_led - 1 < bloblen:
            bloblen = num_led - 3
        if num_led <= 0:
            bloblen = 1 
        # The head pixel that will be turned on in this cycle
        head = (current_step + bloblen) % num_steps_per_cycle
        tail = current_step # The tail pixel that will be turned off
        strip.set_pixel_rgb(head, self.color)  # Paint head
        strip.set_pixel_rgb(tail, 0)  # Clear tail

        return 1 # Repaint is necessary

class ChristmasTest(colorcycletemplate.ColorCycleTemplate):
    """Runs a simple strand test (9 LEDs wander through the strip)."""

    color = None

    def init(self, strip, num_led):
        self.color = 0x000000  # Initialize with black

    def update(self, strip, num_led, num_steps_per_cycle, current_step,
               current_cycle):
        # One cycle = The 9 Test-LEDs wander through numStepsPerCycle LEDs.
        if current_step == 0:
            self.color >>= 8  # Red->green->blue->black
        if self.color == 0:
            self.color = 0xFF0000  # If black, reset to red
        if self.color == 0x00FF00:
            self.color = 0x0000FF  # If black, reset to red
        bloblen = 9
        if num_led - 1 < bloblen:
            bloblen = num_led - 3
        if num_led <= 0:
            bloblen = 1 
        # The head pixel that will be turned on in this cycle
        head = (current_step + bloblen) % num_steps_per_cycle
        tail = current_step # The tail pixel that will be turned off
        strip.set_pixel_rgb(head, self.color)  # Paint head
        strip.set_pixel_rgb(tail, 0)  # Clear tail

        return 1 # Repaint is necessary


class TheaterChase(colorcycletemplate.ColorCycleTemplate):
    """Runs a 'marquee' effect around the strip."""
    def update(self, strip, num_led, num_steps_per_cycle, current_step,
               current_cycle):
        # One cycle = One trip through the color wheel, 0..254
        # Few cycles = quick transition, lots of cycles = slow transition
        # Note: For a smooth transition between cycles, numStepsPerCycle must
        # be a multiple of 7
        start_index = current_step % 7 # One segment is 2 blank, and 5 filled
        color_index = strip.wheel(int(round(255/num_steps_per_cycle *
                                            current_step, 0)))
        for pixel in range(num_led):
            # Two LEDs out of 7 are blank. At each step, the blank
            # ones move one pixel ahead.
            if ((pixel+start_index) % 7 == 0) or ((pixel+start_index) % 7 == 1):
                strip.set_pixel_rgb(pixel, 0)
            else: strip.set_pixel_rgb(pixel, color_index)
        return 1


class RoundAndRound(colorcycletemplate.ColorCycleTemplate):
    """Runs three LEDs around the strip."""

    def init(self, strip, num_led):
        strip.set_pixel_rgb(0, 0xFF0000)
        strip.set_pixel_rgb(1, 0xFF0000, 5) # Only 5% brightness
        strip.set_pixel_rgb(2, 0xFF0000)

    def update(self, strip, num_led, num_steps_per_cycle, current_step,
               current_cycle):
        # Simple class to demonstrate the "rotate" method
        strip.rotate()
        return 1


class Solid(colorcycletemplate.ColorCycleTemplate):
    """Paints the strip with one colour."""

    def update(self, strip, num_led, num_steps_per_cycle, current_step,
               current_cycle):
        if (current_step == 0):
            stripcolour = 0xFFFFFF
        if (current_step == 1):
            stripcolour = 0xFF0000
        if (current_step == 2):
            stripcolour = 0x00FF00
        if (current_step == 3):
            stripcolour = 0x0000FF
        for led in range(0, num_led):
            strip.set_pixel_rgb(led,stripcolour,5) # Paint 5% white  
        return 1


class Rainbow(colorcycletemplate.ColorCycleTemplate):
    """Paints a rainbow effect across the entire strip."""
    def update(self, strip, num_led, num_steps_per_cycle, current_step,
               current_cycle):
        # One cycle = One trip through the color wheel, 0..254
        # Few cycles = quick transition, lots of cycles = slow transition
        # -> LED 0 goes from index 0 to 254 in numStepsPerCycle cycles.
        #     So it might have to step up more or less than one index
        #     depending on numStepsPerCycle.
        # -> The other LEDs go up to 254, then wrap around to zero and go up
        #     again until the last one is just below LED 0. This way, the
        #     strip always shows one full rainbow, regardless of the
        #     number of LEDs
        scale_factor = 255 / num_led # Index change between two neighboring LEDs
        start_index = 255 / num_steps_per_cycle * current_step # LED 0
        for i in range(num_led):
            # Index of LED i, not rounded and not wrapped at 255
            led_index = start_index + i * scale_factor
            # Now rounded and wrapped
            led_index_rounded_wrapped = int(round(led_index, 0)) % 255
            # Get the actual color out of the wheel
            pixel_color = strip.wheel(led_index_rounded_wrapped)
            strip.set_pixel_rgb(i, pixel_color)
        return 1 # All pixels are set in the buffer, so repaint the strip now
    
    
class ColorFade(colorcycletemplate.ColorCycleTemplate):
    """Paints a rainbow effect across the entire strip."""
    def update(self, strip, num_led, num_steps_per_cycle, current_step,
               current_cycle):
        # One cycle = One trip through the color wheel, 0..254
        # Few cycles = quick transition, lots of cycles = slow transition
        # -> LED 0 goes from index 0 to 254 in numStepsPerCycle cycles.
        #     So it might have to step up more or less than one index
        #     depending on numStepsPerCycle.
        # -> The other LEDs go up to 254, then wrap around to zero and go up
        #     again until the last one is just below LED 0. This way, the
        #     strip always shows one full rainbow, regardless of the
        #     number of LEDs
        
        fade_cycles = self.fade_time / self.pause_value
        
        scale_factor = 255 / num_led # Index change between two neighboring LEDs
        start_index = 255 / num_steps_per_cycle * current_step # LED 0
        #peak_cycle = self.num_cycles / 2
        
        if (self.num_cycles > (fade_cycles * 2)):
            first_bright_cycle = fade_cycles
            last_bright_cycle = self.num_cycles - first_bright_cycle
        else:
            # Set to a 20% fade time
            first_bright_cycle = self.num_cycles * .20
            last_bright_cycle = self.num_cycles - first_bright_cycle
        
        if (self.fade_time == 0):
            current_brightness = 100
        
            # the below calculation could be simplified
        elif (current_cycle <= first_bright_cycle):
            current_brightness = (current_cycle / first_bright_cycle) * 100
        elif (current_cycle >= last_bright_cycle):
            current_brightness = ((self.num_cycles - current_cycle) / first_bright_cycle) * 100
            #print(current_cycle)
        else:
            current_brightness = 100
        
        current_brightness = int(round(( current_brightness / 100) * self.color_brightness))
        #print(current_brightness)
            
        #if (current_cycle <= peak_cycle):
        #    current_brightness = (current_cycle / peak_cycle) * 100
        #else:
        #    current_brightness = ((peak_cycle - (current_cycle - peak_cycle)) / peak_cycle) * 100
            
            
        #if (current_step == 0):
            #print(current_brightness)
        #print(randint(0, 10))
        #blinker_denominator = 10000
        #blinker = randint(0, blinker_denominator)
        blinker_denominator = num_led * self.blink_factor
        blinker = randint(0, blinker_denominator)
        for i in range(num_led):
            # Index of LED i, not rounded and not wrapped at 255
            ##led_index = start_index + i * scale_factor
            # Now rounded and wrapped
            ##led_index_rounded_wrapped = int(round(led_index, 0)) % 255
            # Get the actual color out of the wheel
            ##pixel_color = strip.wheel(led_index_rounded_wrapped)
            if (blinker != 0):
                if ((blinker != 0) & (i % blinker_denominator == blinker)):
                    strip.set_pixel_rgb(i, self.blink_color, 100)
                else:
                    strip.set_pixel_rgb(i, self.color, current_brightness)
            else:
                strip.set_pixel_rgb(i, self.color, current_brightness)
            
            #strip.set_pixel_rgb(i, color, (i * 5) % 100)
            #strip.set_pixel_rgb(i, pixel_color)
        #time.sleep(.5)
        #if (current_cycle == peak_cycle):
        #    time.sleep(self.hold_time)
        return 1 # All pixels are set in the buffer, so repaint the strip now

class Scanner(colorcycletemplate.ColorCycleTemplate):
    """Paints a rainbow effect across the entire strip."""
    def update(self, strip, num_led, num_steps_per_cycle, current_step,
               current_cycle):
        # One cycle = One trip through the color wheel, 0..254
        # Few cycles = quick transition, lots of cycles = slow transition
        # -> LED 0 goes from index 0 to 254 in numStepsPerCycle cycles.
        #     So it might have to step up more or less than one index
        #     depending on numStepsPerCycle.
        # -> The other LEDs go up to 254, then wrap around to zero and go up
        #     again until the last one is just below LED 0. This way, the
        #     strip always shows one full rainbow, regardless of the
        #     number of LEDs
        
        #TODO back and forth
        # Fade end options
        # Multiple colors for single snake.
        if (current_step == 0):
            if (self.length == 0):
                self.length = num_led
                
                #self.snake_separation
            # issue, unable to use the first LED
            if (self.snake_separation == -1):
                # single snake
                current_head = current_step + 1 % num_led
                current_tail = current_head - self.length - 1
                if (self.fade_tail == 1):
                    for led in range(current_tail, current_head):
                        current_brightness = ((led - current_tail) / self.length) * 100
                        strip.set_pixel_rgb(led, self.color, current_brightness) # Paint 5% white
                        
                else:
                    strip.set_pixel_rgb(current_head, self.color[0], 100)
                    strip.set_pixel_rgb(current_tail, 0x000000, 100)
            else:
                current_head = current_step + 1 % num_led
                current_tail = current_head - self.length - 1
                if (self.fade_tail == 1):
                    for led in range(current_tail, current_head):
                        current_brightness = ((led - current_tail) / self.length) * 100
                        strip.set_pixel_rgb(led, self.color[0], current_brightness) # Paint 5% white
                        
                else:
                    strip.set_pixel_rgb(current_head, self.color[0], 100)
                    strip.set_pixel_rgb(current_tail, 0x000000, 100)
                    
                    
                    
                
                full_length = self.length + self.snake_separation
                current_head = current_step % full_length # One segment is 2 blank, and 5 filled
                
                
                for pixel in range(num_led):
                    # Two LEDs out of 7 are blank. At each step, the blank
                    # ones move one pixel ahead.
                    #revPixel = num_led - pixel
                    #if (( revPixel+current_head) % self.length == 0) or ((revPixel+current_head) % self.length == 1):
                     #   strip.set_pixel_rgb(revPixel, 0)
                    #else:
                    current_color = self.color[int(pixel / full_length) % len(self.color)]
                    
                    #print(self.color[current_color])
                    #print((pixel % full_length))
                    if (((pixel  + current_head) % full_length)  > self.length):
                        current_brightness = 0
                    else: 
                        #current_brightness = (((pixel+current_head) % full_length) / full_length) * 100
                        current_brightness = 100 - (((pixel + current_head) % full_length) / self.length) * 100
                    #((pixel - current_tail) / self.length) * 100
                    #strip.set_pixel_rgb(led, self.color, current_brightness) # Paint 5% white
                    #print(pixel)
                    #print(current_brightness)
                    strip.set_pixel_rgb(num_led - pixel, int(current_color), current_brightness)
        
        if(int(((current_step / 100) % 2)) == 0):
            strip.rotate(positions = -1)
        else:
            strip.rotate(positions = 1)
                
                
                #if ((pixel+start_index) % 7 == 0) or ((pixel+start_index) % 7 == 1):
                    #strip.set_pixel_rgb(pixel, 0)
            #strip.set_pixel_rgb(i, color, (i * 5) % 100)
            #strip.set_pixel_rgb(i, pixel_color)
        #time.sleep(.5)
        #if (current_cycle == peak_cycle):
        #    time.sleep(self.hold_time)
        return 1 # All pixels are set in the buffer, so repaint the strip now
    
    
    #interesting pulse refresh affect
class PulseRefresh(colorcycletemplate.ColorCycleTemplate):
    """Paints a rainbow effect across the entire strip."""
    def update(self, strip, num_led, num_steps_per_cycle, current_step,
               current_cycle):
        # One cycle = One trip through the color wheel, 0..254
        # Few cycles = quick transition, lots of cycles = slow transition
        # -> LED 0 goes from index 0 to 254 in numStepsPerCycle cycles.
        #     So it might have to step up more or less than one index
        #     depending on numStepsPerCycle.
        # -> The other LEDs go up to 254, then wrap around to zero and go up
        #     again until the last one is just below LED 0. This way, the
        #     strip always shows one full rainbow, regardless of the
        #     number of LEDs
        
        #TODO back and forth
        # back and forth scanner pulse refresh
        if (self.length == 0):
            self.length = num_led
            
            #self.snake_separation
        # issue, unable to use the first LED
        if (self.snake_separation == -1):
            # single snake
            current_head = current_step + 1 % num_led
            current_tail = current_head - self.length - 1
            if (self.fade_tail == 1):
                for led in range(current_tail, current_head):
                    current_brightness = ((led - current_tail) / self.length) * 100
                    strip.set_pixel_rgb(led, self.color, current_brightness) # Paint 5% white
                    
            else:
                strip.set_pixel_rgb(current_head, self.color, 100)
                strip.set_pixel_rgb(current_tail, 0x000000, 100)
        else:
            current_head = current_step + 1 % num_led
            current_tail = current_head - self.length - 1
            if (self.fade_tail == 1):
                for led in range(current_tail, current_head):
                    current_brightness = ((led - current_tail) / self.length) * 100
                    strip.set_pixel_rgb(led, self.color[0], current_brightness) # Paint 5% white
                    
            else:
                strip.set_pixel_rgb(current_head, self.color[0], 100)
                strip.set_pixel_rgb(current_tail, 0x000000, 100)
                
                
                
            
            full_length = self.length + self.snake_separation
            current_head = current_step % full_length # One segment is 2 blank, and 5 filled
            
            for pixel in range(num_led):
                # Two LEDs out of 7 are blank. At each step, the blank
                # ones move one pixel ahead.
                #revPixel = num_led - pixel
                #if (( revPixel+current_head) % self.length == 0) or ((revPixel+current_head) % self.length == 1):
                 #   strip.set_pixel_rgb(revPixel, 0)
                #else:
                current_color = self.color[int(pixel / full_length) % len(self.color)]
                
                #print(self.color[current_color])
                #print((pixel % full_length))
                if (((pixel  + current_head) % full_length)  > self.length):
                    current_brightness = 0
                else: 
                    #current_brightness = (((pixel+current_head) % full_length) / full_length) * 100
                    current_brightness = 100 - (((pixel + current_head) % full_length) / self.length) * 100
                #((pixel - current_tail) / self.length) * 100
                #strip.set_pixel_rgb(led, self.color, current_brightness) # Paint 5% white
                #print(pixel)
                #print(current_brightness)
                strip.set_pixel_rgb(num_led - pixel, int(current_color), current_brightness)
                
                
                
                #if ((pixel+start_index) % 7 == 0) or ((pixel+start_index) % 7 == 1):
                    #strip.set_pixel_rgb(pixel, 0)
            #strip.set_pixel_rgb(i, color, (i * 5) % 100)
            #strip.set_pixel_rgb(i, pixel_color)
        #time.sleep(.5)
        #if (current_cycle == peak_cycle):
        #    time.sleep(self.hold_time)
        return 1 # All pixels are set in the buffer, so repaint the strip now
    
    
class Carnival(colorcycletemplate.ColorCycleTemplate):
    """Paints a rainbow effect across the entire strip."""
    def update(self, strip, num_led, num_steps_per_cycle, current_step,
               current_cycle):
        # One cycle = One trip through the color wheel, 0..254
        # Few cycles = quick transition, lots of cycles = slow transition
        # -> LED 0 goes from index 0 to 254 in numStepsPerCycle cycles.
        #     So it might have to step up more or less than one index
        #     depending on numStepsPerCycle.
        # -> The other LEDs go up to 254, then wrap around to zero and go up
        #     again until the last one is just below LED 0. This way, the
        #     strip always shows one full rainbow, regardless of the
        #     number of LEDs
        
        #TODO back and forth
        # Fade end options
        # Multiple colors for single snake.
        if (current_step == 0):
            if (self.length == 0):
                self.length = num_led
                
                #self.snake_separation
            # issue, unable to use the first LED
            if (self.snake_separation == -1):
                # single snake
                current_head = current_step + 1 % num_led
                current_tail = current_head - self.length - 1
                if (self.fade_tail == 1):
                    for led in range(current_tail, current_head):
                        current_brightness = ((led - current_tail) / self.length) * 100
                        strip.set_pixel_rgb(led, self.color, current_brightness) # Paint 5% white
                        
                else:
                    strip.set_pixel_rgb(current_head, self.color[0], 100)
                    strip.set_pixel_rgb(current_tail, 0x000000, 100)
            else:
                current_head = current_step + 1 % num_led
                current_tail = current_head - self.length - 1
                if (self.fade_tail == 1):
                    for led in range(current_tail, current_head):
                        current_brightness = ((led - current_tail) / self.length) * 100
                        strip.set_pixel_rgb(led, self.color[0], current_brightness) # Paint 5% white
                        
                else:
                    strip.set_pixel_rgb(current_head, self.color[0], 100)
                    strip.set_pixel_rgb(current_tail, 0x000000, 100)
                    
                    
                    
                
                full_length = self.length + self.snake_separation
                current_head = current_step % full_length # One segment is 2 blank, and 5 filled
                
                
                for pixel in range(num_led):
                    # Two LEDs out of 7 are blank. At each step, the blank
                    # ones move one pixel ahead.
                    #revPixel = num_led - pixel
                    #if (( revPixel+current_head) % self.length == 0) or ((revPixel+current_head) % self.length == 1):
                     #   strip.set_pixel_rgb(revPixel, 0)
                    #else:
                    current_color = self.color[int(pixel / full_length) % len(self.color)]
                    
                    #print(self.color[current_color])
                    #print((pixel % full_length))
                    if (((pixel  + current_head) % full_length)  > self.length):
                        current_brightness = 0
                    else: 
                        #current_brightness = (((pixel+current_head) % full_length) / full_length) * 100
                        current_brightness = 100 - (((pixel + current_head) % full_length) / self.length) * 100
                    #((pixel - current_tail) / self.length) * 100
                    #strip.set_pixel_rgb(led, self.color, current_brightness) # Paint 5% white
                    #print(pixel)
                    #print(current_brightness)
                    strip.set_pixel_rgb(num_led - pixel, int(current_color), current_brightness)
        
        if (self.rotate != 0):            
            if(int(((current_step / 50) % 2)) == 0):
                strip.rotate(positions = -1)
            else:
                strip.rotate(positions = 1)
                
                
                #if ((pixel+start_index) % 7 == 0) or ((pixel+start_index) % 7 == 1):
                    #strip.set_pixel_rgb(pixel, 0)
            #strip.set_pixel_rgb(i, color, (i * 5) % 100)
            #strip.set_pixel_rgb(i, pixel_color)
        #time.sleep(.5)
        #if (current_cycle == peak_cycle):
        #    time.sleep(self.hold_time)
        return 1 # All pixels are set in the buffer, so repaint the strip now

#TODO Fairy light program
# every x (5) light that randomly twinkle (maybe also randome between which lights flicker?. maybe length of time on is also random. To do random distance in between each flicker,
# may need to load up a multi-dimensional list that includes the current state (turning on, turning off,off as well as a separate data point for the current brightness).
#all non flikering lights need to shimmer. The amount of shimmer during each cycle could be determined by the current state of the flickering leds
#  (being brighter when they have a lower brightness across the flickering ones).
class Twinkle(colorcycletemplate.ColorCycleTemplate):
    """Paints a rainbow effect across the entire strip."""
    
    def init(self, strip, num_led):

        self.led_array = [num_led]
        current_cycle = 0
        self.fade_factor = .1 #should be based on length of cycle
        #[always on = -1 / always off = 0 / is a blinker = 1, brightness , off=0 / turning on = 1 / turning off = -1, next blink start]
        for i in range(num_led):
            if(i % 5 == 0):
                next_blink_cycle = current_cycle + (1 / self.pause_value)
                #print(randint(current_blink_cycle + (1 / self.pause_value), (current_blink_cycle + (1 / self.pause_value)) * 5))
                self.led_array.append([1, 0, 0, randint(current_cycle + (1 / self.pause_value), (current_cycle + ((1 / self.pause_value)) * 5))])
            else:
                self.led_array.append([-1, 1, 1, -1])
        self.blinker_brightness = 0 
        
    def update(self, strip, num_led, num_steps_per_cycle, current_step,
               current_cycle):
        # One cycle = One trip through the color wheel, 0..254
        # Few cycles = quick transition, lots of cycles = slow transition
        # -> LED 0 goes from index 0 to 254 in numStepsPerCycle cycles.
        #     So it might have to step up more or less than one index
        #     depending on numStepsPerCycle.
        # -> The other LEDs go up to 254, then wrap around to zero and go up
        #     again until the last one is just below LED 0. This way, the
        #     strip always shows one full rainbow, regardless of the
        #     number of LEDs
        
        fade_cycles = self.fade_time / self.pause_value
        
        scale_factor = 255 / num_led # Index change between two neighboring LEDs
        start_index = 255 / num_steps_per_cycle * current_step # LED 0
        #peak_cycle = self.num_cycles / 2
        
        if (self.num_cycles > (fade_cycles * 2)):
            first_bright_cycle = fade_cycles
            last_bright_cycle = self.num_cycles - first_bright_cycle
        else:
            # Set to a 20% fade time
            first_bright_cycle = self.num_cycles * .20
            last_bright_cycle = self.num_cycles - first_bright_cycle
        
        if (self.fade_time == 0):
            current_brightness = 100
            # the below calculation could be simplified
        elif (current_cycle <= first_bright_cycle):
            current_brightness = (current_cycle / first_bright_cycle) * 100
        elif (current_cycle >= last_bright_cycle):
            current_brightness = ((self.num_cycles - current_cycle) / first_bright_cycle) * 100
            #print(current_cycle)
        else:
            current_brightness = 100
        
        current_brightness = int(round(( current_brightness / 100) * self.color_brightness))
        #print(current_brightness)
        #print(first_bright_cycle)
        #if (current_cycle <= peak_cycle):
        #    current_brightness = (current_cycle / peak_cycle) * 100
        #else:
        #    current_brightness = ((peak_cycle - (current_cycle - peak_cycle)) / peak_cycle) * 100
        #print("test")
        #print(num_led)
        blinker_led_separation = 5
        is_blink_cycle=0
        if ((current_cycle % (1 / self.pause_value)) == 0):
            #current_brightness = current_brightness - (current_cycle % 10)
            #print(current_brightness - (current_cycle % 10))
            #Power draw code
            #current_brightness = current_brightness - 10
            is_blink_cycle=1
        
        #if (current_step == 0):
            #print(current_brightness)
        #print(randint(0, 10))
        #blinker_denominator = 10000
        #blinker = randint(0, blinker_denominator)
        blinker_denominator = num_led * self.blink_factor
        blinker = randint(0, blinker_denominator)
        
        blink_count = 0
        
        #current_brightness needs to be subtracted from led brightness based on current from blinkers (with a ceiling)

        blinker_brightness = 0 
        for i in range(num_led):
            #[always on = -1 / always off = 0 / is a blinker = 1, brightness , off=0 / turning on = 1 / turning off = -1, next blink start]
            #if always off
            if(self.led_array[i+1][0] == 0):
                self.led_array[i+1][1] = 0x000000
            #else if always on
            elif(self.led_array[i+1][0] == -1):
                #This is a regular always on light, but needs to be dimmed based on the "draw" from the flickering lights
                self.led_array[i+1][1] = current_brightness
            #Else if a blinker and this is the start cycle, turning on
            elif((self.led_array[i+1][0] == 1) & (self.led_array[i+1][3] == current_cycle)):
            #TODO complex fade logic
                self.led_array[i+1][2] = 1
                #Next random on should be set when this led turns off (when brightness <= 0)
                self.led_array[i+1][3] = randint(current_cycle + (1 / self.pause_value), (current_cycle + ((1 / self.pause_value)) * 5))
                
                self.led_array[i+1][1] = self.led_array[i+1][1] + (current_brightness * self.fade_factor)
                blinker_brightness = blinker_brightness + self.led_array[i+1][1]
                #self.led_array[i+1][1] = this_led_brightness
            #else if turning on blinker
            elif (self.led_array[i+1][2] == 1):
                #print("onning")
               # print(self.led_array[i+1][1])
                this_led_brightness = self.led_array[i+1][1] + (current_brightness * self.fade_factor)
                self.led_array[i+1][1] = this_led_brightness
                if(this_led_brightness >= current_brightness):
                    this_led_brightness = current_brightness
                    #set to turning off
                    self.led_array[i+1][2] = -1
                blinker_brightness = blinker_brightness + self.led_array[i+1][1]
               
                
            #else if turning off blinker
            elif (self.led_array[i+1][2] == -1):
                self.led_array[i+1][1] = self.led_array[i+1][1] - (current_brightness * self.fade_factor)
                if(self.led_array[i+1][1] <= 0):
                    self.led_array[i+1][1] = 0
                    self.led_array[i+1][2] = 0
                blinker_brightness = blinker_brightness + self.led_array[i+1][1]
            
            if(blinker_brightness > self.blinker_brightness):
                #print(blinker_brightness)
                self.blinker_brightness = blinker_brightness 
        for i in range(num_led):
            
          
            
            #[always on = -1 / always off = 0 / is a blinker = 1, brightness , off=0 / turning on = 1 / turning off = -1, next blink start]
            #if always off
            if (0):
                if(self.led_array[i+1][0] == 0):
                    strip.set_pixel_rgb(i, 0x000000)
                #else if always on
                elif(self.led_array[i+1][0] == -1):
                    #This is a regular always on light, but needs to be dimmed based on the "draw" from the flickering lights
                    if(current_brightness != self.color_brightness):
                        strip.set_pixel_rgb(i, self.color, current_brightness)
                    else:
                        #determine the draw brightness drop (needs to be calculated in a loop beforehand, which will determine brightness across all flickering LEDs
                        strip.set_pixel_rgb(i, self.blink_color, current_brightness)
                #Else if a blinker and this is the start cycle, turning on
                elif((self.led_array[i+1][0] == 1) & (self.led_array[i+1][3] == current_cycle)):
                #TODO complex fade logic
                    #print(self.led_array[i+1][1])
                    #print(current_brightness)
                    #print(self.fade_factor)
                    #print(current_brightness * self.fade_factor)
                    self.led_array[i+1][2] = 1
                    #Next random on should be set when this led turns off (when brightness <= 0)
                    self.led_array[i+1][3] = randint(current_cycle + (1 / self.pause_value), (current_cycle + ((1 / self.pause_value)) * 5))
                    
                    self.led_array[i+1][1] = self.led_array[i+1][1] + (current_brightness * self.fade_factor)
                    
                    #self.led_array[i+1][1] = this_led_brightness
                    strip.set_pixel_rgb(i, self.color, self.led_array[i+1][1])
                   
                #else if turning on blinker
                elif (self.led_array[i+1][2] == 1):
                    #print("onning")
                   # print(self.led_array[i+1][1])
                    this_led_brightness = self.led_array[i+1][1] + (current_brightness * self.fade_factor)
                    self.led_array[i+1][1] = this_led_brightness
                    if(this_led_brightness >= current_brightness):
                        this_led_brightness = current_brightness
                        #set to turning off
                        self.led_array[i+1][2] = -1
                        
                    strip.set_pixel_rgb(i, self.color, this_led_brightness)
                    
                #else if turning off blinker
                elif (self.led_array[i+1][2] == -1):
                    self.led_array[i+1][1] = self.led_array[i+1][1] - (current_brightness * self.fade_factor)
                    if(self.led_array[i+1][1] <= 0):
                        self.led_array[i+1][1] = 0
                        self.led_array[i+1][2] = 0
                    strip.set_pixel_rgb(i, self.color, self.led_array[i+1][1])
            
            if (self.led_array[i+1][0] == -1):
                blinker_brightness
                strip.set_pixel_rgb(i, self.color, self.led_array[i+1][1] - (blinker_brightness * .05))
            else:
                strip.set_pixel_rgb(i, self.blink_color, min(self.led_array[i+1][1], current_brightness - (blinker_brightness * .05)))
            #else:
                #always off
                #strip.set_pixel_rgb(i, self.color, 0)
        #time.sleep(.5)
        #if (current_cycle == peak_cycle):
        #    time.sleep(self.hold_time)
        return 1 # All pixels are set in the buffer, so repaint the strip now



class CollapseScanner(colorcycletemplate.ColorCycleTemplate):
    """Paints a rainbow effect across the entire strip."""
    
    def init(self, strip, num_led):
        self.num_steps_per_cycle = math.ceil(((num_led + 1) / 2)) + self.length
            
    def update(self, strip, num_led, num_steps_per_cycle, current_step,
               current_cycle):
        # One cycle = One trip through the color wheel, 0..254
        # Few cycles = quick transition, lots of cycles = slow transition
        # -> LED 0 goes from index 0 to 254 in numStepsPerCycle cycles.
        #     So it might have to step up more or less than one index
        #     depending on numStepsPerCycle.
        # -> The other LEDs go up to 254, then wrap around to zero and go up
        #     again until the last one is just below LED 0. This way, the
        #     strip always shows one full rainbow, regardless of the
        #     number of LEDs
        
        # when cycling, clear out the ends
        #TODO
        #inward/outward direction (need a variable)
        # Address a color arra
        #Fading tail
        if(current_step == 0):
            strip.set_pixel_rgb(0, 0)
            strip.set_pixel_rgb(num_led - 1, 0)
            self.start_right = math.ceil(((num_led + 1) / 2))
            self.start_left = math.floor(((num_led + 1) / 2))
            self.num_steps_per_cycle = self.start_right + self.length
        
        #Outward
        # Right Side
        #if wanting to do a fade, need to have a loop changing the color.
        current_brightness = 100
        #if(self.fade_tail):
        #    current_brightness = 1
        strip.set_pixel_rgb(self.start_right + current_step, self.color[0], current_brightness)
        if(current_step >= self.length):
            strip.set_pixel_rgb(self.start_right + current_step - self.length, 0)
            
        #left side
        strip.set_pixel_rgb(self.start_left - current_step, self.color[0], current_brightness)
        if(current_step >= self.length):
            strip.set_pixel_rgb(self.start_left - current_step + self.length, 0)
        """ 
            
        #inward 
        # Right Side
        strip.set_pixel_rgb(current_step, self.color[0])
        #if(current_step >= self.length):
        #    strip.set_pixel_rgb(current_step - self.length, 0)
          
        #left side
        strip.set_pixel_rgb(num_led - current_step, self.color[0])
        if(current_step >= self.length):
            strip.set_pixel_rgb(self.start_left - current_step + self.length, 0)
        """
        """
        
        full_length = min(self.length, current_step + 1)
        for pixel in range(full_length):
            print(pixel)
            current_pixel = pixel + self.head_right + current_step
            #print(current_pixel)
            strip.set_pixel_rgb(current_pixel, self.color[0])
        """
        """
        #if(current_step > self.length):
            #print(current_pixel - self.length,)
        strip.set_pixel_rgb(current_pixel - self.length, 0)
        #print(current_pixel - self.length)
        
        
        for pixel in range(self.length):
            current_pixel = math.floor((num_led / 2)) - (pixel + current_step)
            strip.set_pixel_rgb(current_pixel, self.color[0])
            
        strip.set_pixel_rgb(current_pixel + self.length, 0)
        #print(current_pixel)
        """
        """
        for pixel in range(num_led):
            # Two LEDs out of 7 are blank. At each step, the blank
            # ones move one pixel ahead.
            if ((pixel+start_index) % 7 == 0) or ((pixel+start_index) % 7 == 1):
                strip.set_pixel_rgb(pixel, 0)
            else: strip.set_pixel_rgb(pixel, self.color[0])
            """
        return 1
       
        #TODO
        """            
        if (current_step == 0):
            if (self.length == 0):
                self.length = num_led
                
                #self.snake_separation
            # issue, unable to use the first LED
            #TODO, = -1
            if (self.snake_separation == -1):
                # single snake
                current_head = current_step + 1 % num_led
                current_tail = current_head - self.length - 1
                if (self.fade_tail == 1):
                    for led in range(current_tail, current_head):
                        current_brightness = ((led - current_tail) / self.length) * 100
                        strip.set_pixel_rgb(led, self.color, current_brightness) # Paint 5% white
                        
                else:
                    strip.set_pixel_rgb(current_head, self.color[0], 100)
                    strip.set_pixel_rgb(current_tail, 0x000000, 100)
            else:
                current_head = current_step + 1 % num_led
                current_tail = current_head - self.length - 1
                if (self.fade_tail == 1):
                    for led in range(current_tail, current_head):
                        current_brightness = ((led - current_tail) / self.length) * 100
                        strip.set_pixel_rgb(led, self.color[0], current_brightness) # Paint 5% white
                        
                else:
                    strip.set_pixel_rgb(current_head, self.color[0], 100)
                    strip.set_pixel_rgb(current_tail, 0x000000, 100)
                    
                    
                    
                
                full_length = self.length + self.snake_separation
                current_head = current_step % full_length # One segment is 2 blank, and 5 filled
                
                
                for pixel in range(num_led):
                    # Two LEDs out of 7 are blank. At each step, the blank
                    # ones move one pixel ahead.
                    #revPixel = num_led - pixel
                    #if (( revPixel+current_head) % self.length == 0) or ((revPixel+current_head) % self.length == 1):
                     #   strip.set_pixel_rgb(revPixel, 0)
                    #else:
                    current_color = self.color[int(pixel / full_length) % len(self.color)]
                    
                    #print(self.color[current_color])
                    #print((pixel % full_length))
                    if (((pixel  + current_head) % full_length)  > self.length):
                        current_brightness = 0
                    else: 
                        #current_brightness = (((pixel+current_head) % full_length) / full_length) * 100
                        current_brightness = 100 - (((pixel + current_head) % full_length) / self.length) * 100
                    #((pixel - current_tail) / self.length) * 100
                    #strip.set_pixel_rgb(led, self.color, current_brightness) # Paint 5% white
                    #print(pixel)
                    #print(current_brightness)
                    strip.set_pixel_rgb(num_led - pixel, int(current_color), current_brightness)
        
        #if(int(((current_step / 100) % 2)) == 0):
        #    
        #else:
        #    strip.rotate(positions = 1)
        strip.rotate(positions = -1)
                
                #if ((pixel+start_index) % 7 == 0) or ((pixel+start_index) % 7 == 1):
                    #strip.set_pixel_rgb(pixel, 0)
            #strip.set_pixel_rgb(i, color, (i * 5) % 100)
            #strip.set_pixel_rgb(i, pixel_color)
        #time.sleep(.5)
        #if (current_cycle == peak_cycle):
        #    time.sleep(self.hold_time)
        """
        return 1 # All pixels are set in the buffer, so repaint the strip now
    
  
     