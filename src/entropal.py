# This file contains driver code for generating passphrases from entropy
#
# Author: Josh McIntyre
#
import os
import entropallib

# PC or RPi based user interface for dice collection (with keyboard and terminal)
def collect_dierolls_pc(die, bits_needed):

    while die.bits_entropy < bits_needed:
        try:
            # Get the roll via the input device
            print("-----")
            while True:
                roll_raw = input(f"Enter die roll 1-{die.sides}: ")
                if roll_raw == "":
                    continue
                roll = int(roll_raw)
                break
           
            # Collect the roll and inform the user
            die.add_roll(roll)
            print(f"Added bits: {die.bits_last}")
            print(f"Total bits: {die.bits_entropy}")
            print(f"Entropy: {die.entropy_binary}")

        except ValueError as e:
            print(f"Invalid roll: {e}")

    return die

# PC or RPi based user interface for die selection (with keyboard and terminal)
def select_die_pc():

    try:
        print("------")
        die_options = ", ".join(entropallib.AVAILABLE_DIES)
        die_key = input(f"Enter die sides {die_options}: ")
        die = entropallib.AVAILABLE_DIES[die_key]

        return die
    except KeyError:
        print(f"Invalid selection, defaulting to 4 sided die")
        return entropallib.DiceEntropy4

# PC or RPi based user interface for die selection (with keyboard and terminal)
def select_wordlist_pc():

    try:
        print("------")
        for k,v in entropallib.AVAILABLE_WORDS_DESCRIPTIONS.items():
            print(f"{k}: {v}")
        word_options = ", ".join(entropallib.AVAILABLE_WORDS)
        word_key = input(f"Enter wordlist {word_options}: ")
        word = entropallib.AVAILABLE_WORDS[word_key]

        return word
    except KeyError:
        print(f"Invalid wordlist selection, defaulting to Heartsucker wordlist")
        return entropallib.HeartsuckerWords

# PC or RPi based user interface for continuing to another word
def select_cont_pc():

    print("------")
    cont = input("Add another word? (y/n)")
    if cont == "y":
        return True
    return False

# This is the main entry point for the program
def main():

    # Get the user's die selection and wordlist selection
    selected_die = select_die_pc()
    selected_wordlist = select_wordlist_pc()

    # Collect the dice entropy
    die = selected_die()
    die = collect_dierolls_pc(die, selected_wordlist.bits_per_word)

    # Fetch the word from the entropy
    # Default to the Heartsucker 8192 wordlist if none selected
    word = selected_wordlist(die.entropy)

    print("-----")
    print("Final entropy data")
    print(f"Entropy: {word.index_binary}")
    print(f"Index: {word.index}")
    print(f"Word: {word.word}")

if __name__ == "__main__":
    main()

