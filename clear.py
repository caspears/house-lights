NUM_LED = 1024


from colorschemes import colorschemes


print('Clear')
MY_CYCLE = colorschemes.Scanner(num_led=NUM_LED, pause_value=0.1, num_steps_per_cycle=1, color = [0x000000], global_brightness = 100,  \
                                    num_cycles=10)
MY_CYCLE.start()
print('Finished the test')
