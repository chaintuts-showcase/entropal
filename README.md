## General
____________

### Author
* Josh McIntyre

### Website
* jmcintyre.net

### Overview
* Entropal demonstrates the concept of entropy with diceware passphrase generation

## Development
________________

### Git Workflow
* master for releases (merge development)
* development for bugfixes and new features

### Building
* make build
Build the application
* make clean
Clean the build directory

### Features
* Allows inputs from a 4 sided die (PC, RPi, Adafruit M4)
* Allows inputs from an 8 sided die (PC, RPi)
* Supports the BIP39 wordlist (11 bit words, 2048 total) (PC, RPi)
* Supports the Heartsucker wordlist (13 bit words, 8192 total) (PC, RPi, Adafruit M4)
* Shows the entropy collected as binary

### Requirements
* Requires Python (PC, RPi)
* Requires I2C character LCD and Matrix Keypad (Adafruit M4)

### Platforms
* Windows
* MacOSX
* Linux
* Raspberry Pi
* Adafruit M4 Microprocessor

## Usage
____________

### PC or Raspberry Pi Command-line Usage
* Enter your die selection (defaults to 4 sided die)
* Enter your wordlist selection (defaults to Heartsucker wordlist)
* Enter each roll as an integer number
* Final word and entropy data will be shown once enough entropy is collected

### Adafruit M4 Microcontroller Usage
* Enter each roll via the matrix keypad, then press #
* Final word and entropy data will be shown once enough entropy is collected
* Press # to collect entropy for another word