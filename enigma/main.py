from ensemble import *


class MainEnigmaRun:

    """Class used for the Enigma machine demonstration in Part 1 to solve Example 1 and 2.
    Instantiate MainEnigmaRun class and run method enigma_machine_demonstration to encrypt/decrypt messages.

    Input parameters:

    rotors: left to right rotors list of strings ["I", "III", "IV"] or "I III IV"

    reflector: string indicating reflector type ('B','C','B-Thin','C-Thin')

    ring_settings: list of integers between 1-26, a string ('A B C'), or None to represent the rotors ring settings

    plugboard: string of up to 10 pairs of letters e.g. 'AD SF GH JK UY IT RE WO MN XZ'
                            or None if no plugboard connections are made

    starting_position: string of characters equal to num of rotors representing rotor starting position. e.g. 'A R D'

    ciphertext: string of text to encrypt or decrypt
    """

    @staticmethod
    def enigma_machine_demonstration(rotors, reflector, ring_settings, plugboard, starting_position, ciphertext):

        enigna_machine = EnigmaSimulator.input_parameters(
            rotors=rotors,
            reflector=reflector,
            ring_settings=ring_settings,
            plugboard_settings=plugboard)

        enigna_machine.starting_position(starting_position)

        ciphertext = ciphertext
        plaintext = enigna_machine.read(ciphertext)

        return plaintext
