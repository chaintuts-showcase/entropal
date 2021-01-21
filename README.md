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
* Allows inputs from 4 or 8 sided die
* Supports the BIP39 wordlist (11 bit words, 2048 total)
* Supports the Heartsucker wordlist (13 bit words, 8192 total)
* Shows the entropy collected as binary

### Requirements
* Requires Python

### Platforms
* Windows
* MacOSX
* Linux
* Raspberry Pi

## Usage
____________

### PC or Raspberry Pi Command-line Usage
* Enter your die selection (defaults to 4 sided die)
* Enter your wordlist selection (defaults to Heartsucker wordlist)
* Enter each roll as an integer number
* Final word and entropy data will be shown once enough entropy is collected
