import asyncio
import logging
from hardware.led_hal import RgbLedHAL


class LEDControl():
    """
        Control RGB Leds
    """

    def __init__(self):
        """
            Initializes RGB strip and turn all leds blue
        """
        self.led = RgbLedHAL()
        self.led_numbers = 12  # half stripe
        self.all_leds_blue()

    def display_joystick_pos(self, pos):
        """
            Switch leds on and off depending on joystick position

            Parameters:
                pos: position of joystick, between -1 and 1
        """
        pos = pos * self.led_numbers
        self.led.configure_individual_leds([10, 0, 10], pos)

    def all_leds_blue(self):
        """
            Turns all led blue
        """
        self.led.configure_all_leds([10, 0, 10])

    def all_leds_green(self):
        """
            Turns all led green
        """
        self.led.configure_all_leds([10, 0, 0])

    async def score_leds(self, time: float):
        """
            Blink score leds
        """

        self.led.led_score_on([10, 0, 0])
        await asyncio.sleep(time)
        self.led.led_score_off()

    def switch_off_leds(self):
        """
            Switches all leds off
        """
        self.led.close()
