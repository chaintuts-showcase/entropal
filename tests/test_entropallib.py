# This file contains unit tests for Entropal library functionality
#
# Author: Josh McIntyre
#
import unittest

import entropallib

class TestDiceEntropy(unittest.TestCase):

    # Test basic construction of classes
    def test_DiceEntropy(self):
        d4 = entropallib.DiceEntropy4()
        d8 = entropallib.DiceEntropy8()
        
        assert isinstance(d4, entropallib.DiceEntropy)
        assert isinstance(d8, entropallib.DiceEntropy)
        
        assert d4.sides == 4
        assert d8.sides == 8
        
    # Test basic die calculations
    def test_DiceEntropy_calculations(self):
        d4 = entropallib.DiceEntropy4()
        
        # Assert 3 is the entropy - entropy is always (roll - 1) since die does not include 0
        d4.add_roll(4)
        assert d4.entropy == 3
        assert d4.entropy_binary() == "11"
        

    def test_DiceEntropy_bad_roll(self):
        d4 = entropallib.DiceEntropy4()
        
        with self.assertRaises(ValueError):
            d4.add_roll(5)

        with self.assertRaises(ValueError):
            d4.add_roll(0)
