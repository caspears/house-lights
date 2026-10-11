"""The module contains templates for colour cycles"""
import time
from driver import apa102

class ColorCycleTemplate:
    """This class is the basis of all color cycles.
    This file is usually used "as is" and not being changed.

    A specific color cycle must subclass this template, and implement at least the
    'update' method.
    """
        
    def __init__(self, num_led, pause_value = 0, num_steps_per_cycle = 100,
                 num_cycles = -1, global_brightness = 255, led_multiplier = 1, color = [0xFFFFFF], color_brightness = 100, blink_factor = 0, blink_color = 0xFFFFFF, fade_time = 0, length = 0, fade_tail = 0, snake_separation = -1, rotate = 0,
                 order = 'rbg', mosi = 10, sclk = 11):
        self.num_led = num_led # The number of LEDs in the strip
        self.pause_value = pause_value # How long to pause between two runs
        self.num_steps_per_cycle = num_steps_per_cycle # Steps in one cycle.
        self.num_cycles = num_cycles # How many times will the program run
        self.global_brightness = global_brightness # Brightness of the strip
        self.led_multiplier = led_multiplier
        self.order = order # Strip colour ordering
        self.color = color # Strip colour
        self.color_brightness = color_brightness
        self.blink_factor = blink_factor
        self.blink_color = blink_color
        self.fade_time = fade_time
        self.length = length
        self.fade_tail = fade_tail
        self.snake_separation = snake_separation
        self.rotate = rotate
        self.mosi = mosi # Master out slave in of the SPI protocol
        self.sclk = sclk # Clock line of the SPI protocol

    def init(self, strip, num_led):
        """This method is called to initialize a color program.

        The default does nothing. A particular subclass could setup
        variables, or even light the strip in an initial color.
        """
        pass

    def shutdown(self, strip, num_led):
        """This method is called before exiting.

        The default does nothing
        """
        pass

    def update(self, strip, num_led, num_steps_per_cycle, color, current_step,
               current_cycle):
        """This method paints one subcycle. It must be implemented.

        current_step:  This goes from zero to numStepsPerCycle-1, and then
          back to zero. It is up to the subclass to define what is done in
          one cycle. One cycle could be one pass through the rainbow.
          Or it could be one pixel wandering through the entire strip
          (so for this case, the numStepsPerCycle should be equal to numLEDs).
        current_cycle: Starts with zero, and goes up by one whenever a full
          cycle has completed.
        """

        raise NotImplementedError("Please implement the update() method")

    def cleanup(self, strip):
        """Cleanup method."""
        self.shutdown(strip, self.num_led)
        strip.clear_strip()
        strip.cleanup()


    def start(self):
        """This method does the actual work."""
        try:
            strip = apa102.APA102(num_led=self.num_led, led_multiplier=self.led_multiplier,
                                  global_brightness=self.global_brightness,
                                  mosi = self.mosi, sclk = self.sclk,
                                  order=self.order) # Initialize the strip
            strip.clear_strip()
            self.init(strip, self.num_led) # Call the subclasses init method
            strip.show()
            current_cycle = 0
            while True:  # Loop forever
                for current_step in range (self.num_steps_per_cycle):
                    need_repaint = self.update(strip, self.num_led,
                                               self.num_steps_per_cycle,
                                               current_step, current_cycle)
                    if need_repaint:
                        strip.show() # repaint if required
                    time.sleep(self.pause_value) # Pause until the next step
                current_cycle += 1
                if self.num_cycles != -1:
                    if current_cycle >= self.num_cycles:
                        break
            # Finished, cleanup everything
            self.cleanup(strip)

        except KeyboardInterrupt:  # Ctrl-C can halt the light program
            print('Interrupted...')
            self.cleanup(strip)
