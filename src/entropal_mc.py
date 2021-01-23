# This file contains driver code for generating passphrases from entropy
#
# Author: Josh McIntyre
#

import busio
import board
import digitalio
import adafruit_matrixkeypad
import adafruit_character_lcd.character_lcd_i2c as character_lcd
import time
import os
import entropallib

def init_keypad_mc():

    cols = [digitalio.DigitalInOut(x) for x in (board.D9, board.D7, board.D2)]
    rows = [digitalio.DigitalInOut(x) for x in (board.D13, board.D12, board.D11, board.D10)]
    keys = ((1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        ('*', 0, '#'))

    keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)

    return keypad

def init_display_mc():

    # Initialize the board
    i2c = busio.I2C(board.SCL, board.SDA)
    cols = 20
    rows = 4
    lcd = character_lcd.Character_LCD_I2C(i2c, cols, rows)
    lcd.backlight = True

    return lcd

# Collect dice entropy via the keypad
def collect_dierolls_mp(die, bits_needed, lcd, keypad):

    while die.bits_entropy < bits_needed:
        try:
            # Get the roll via the input device
            while True:
                lcd.clear()
                lcd.message = f"Enter die roll 1-{die.sides}"
                while True:
                    keys = keypad.pressed_keys
                    time.sleep(0.3)
                    if len(keys) == 1:
                        roll_raw = keys[0]
                        roll = int(roll_raw)
                        break

                # Collect the roll and inform the user
                die.add_roll(roll)
                lcd.clear()
                lcd.message = f"Added bits: {die.bits_last()}\nTotal bits: {die.bits_entropy}\nEnt: {die.entropy_binary()}\nPress # for next"

                # Wait to continue
                while True:
                    keys = keypad.pressed_keys
                    time.sleep(0.3)
                    if len(keys) == 1:
                        key = keys[0]
                        if key == "#":
                            break

                break # Break to the outer bits entropy check

        except ValueError as e:
            lcd.clear()
            lcd.message = "Invalid roll"
            time.sleep(0.5)

    return die

# This is the main driver for the entropal program on a microprocessor
def main():

    # Initialize components
    lcd = init_display_mc()
    keypad = init_keypad_mc()

    # Enter the main word selection loop
    while True:

        # Set default die - 4 sided
        die = entropallib.DiceEntropy4()

        # Collect die entropy
        die = collect_dierolls_mp(die, entropallib.HeartsuckerWords.bits_per_word, lcd, keypad)

        # Fetch the word from the entropy
        # Default to the Heartsucker 8192 wordlist
        word = entropallib.HeartsuckerWords(die.entropy)

        # Display the final result
        lcd.clear()
        lcd.message = f"Word: {word.word}\nEnt: {word.index_binary}\nIndex: {word.index}\nPress # for new"

        # Wait to continue
        while True:
            keys = keypad.pressed_keys
            time.sleep(0.3)
            if len(keys) == 1:
                key = keys[0]
                if key == "#":
                    break

if __name__ == "__main__":
    main()
