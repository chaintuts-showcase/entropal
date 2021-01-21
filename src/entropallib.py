# This file contains code for generating passphrases from entropy
# It can transform entropy to indexes for diceware wordlists such as 
# Heartsucker (13 bit words) and BIP39 (11 bit words)
#
# Author: Josh McIntyre
#

# Define classes for handling wordlists
# These classes will take any integer entropy and fetch the desired word by index
class EntropalWords:

    # Defaults to heartsucker words
    wordfile = "heartsucker_words.txt"
    bitmask = 0x1fff
    bits_per_word = 13

    # Public method for fetching a word from entropy
    def __init__(self, entropy):

        # Initialize the word object from the entropy
        self.entropy = entropy
        self._get_index()
        self._get_binary_index()
        self._get_word()

    # Fetch an index for words 
    def _get_index(self):

        self.index = self.entropy & self.bitmask

    # Fetch words from file
    def _get_word(self):

        # Get the line directly from the file rather than using list comprehension
        # This will preserve memory on small platforms
        i = 0
        with open(self.wordfile) as f:
            for word in f:
                if i == self.index:
                    self.word = word.strip()
                    return
                else:
                    i = i + 1


    # Represent the index in a nice binary format
    def _get_binary_index(self):

        self.index_binary = bin(self.index).replace("0b", "")


class Bip39Words(EntropalWords):
    wordfile= "bip39_words.txt"
    bitmask = 0x7ff
    bits_per_word = 11

class HeartsuckerWords(EntropalWords):
    wordfile = "heartsucker_words.txt"
    bitmask = 0x1fff
    bits_per_word = 13

AVAILABLE_WORDS = { "bip39" : Bip39Words,
                    "heartsucker" : HeartsuckerWords
}

AVAILABLE_WORDS_DESCRIPTIONS = { "bip39" : "BIP39 words - 11 bits per word, 2048 words total",
                                 "heartsucker" : "Heartsucker words - 13 bits per word, 8192 words total"
}

# Define classes that handle entropy collection from dice
# Each will collect and represent entropy as bits for easier understanding
class DiceEntropy:

    # Defaults to 2 bits (4 sided die)
    sides = 4
    bits = 2

    # State - the entropy value
    # Internal store of the number of bits of entropy
    entropy = 0
    bits_entropy = 0
    
    # Public method for adding entropy to the state
    def add_roll(self, roll):

        if roll > self.sides or roll <= 0:
            raise ValueError(f"Die roll must be from 1-{self.sides}")

        # Bit shift the existing state bits over
        self.entropy = self.entropy << self.bits

        # Add the new state on via bitwise-or
        self.entropy = self.entropy | roll

        # Increment the number of stored bits of entropy
        self.bits_entropy = self.bits_entropy + self.bits

        # Show the raw last added bits in the state
        self._bits_last = roll

    # Represent the entropy in a nice binary format
    def _get_binary_entropy(self):

        return bin(self.entropy).replace("0b", "")

    entropy_binary = property(fget=_get_binary_entropy)

    # Represent the last added bits as binary
    def _get_binary_roll(self):

        return bin(self._bits_last).replace("0b", "")

    bits_last = property(fget=_get_binary_roll)

class DiceEntropy4(DiceEntropy):
    # 4 sides = 2 bits of entropy - log2(4)
    sides = 4
    bits = 2

class DiceEntropy8(DiceEntropy):
    # 8 sides = 3 bits of entropy - log2(8)
    sides = 8
    bits = 3

AVAILABLE_DIES = { "4" : DiceEntropy4,
                   "8" : DiceEntropy8
}
