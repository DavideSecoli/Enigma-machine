"""This module contains the EnigmaSimulation class for the Enigma Machine"""

import string
from ensemble import EnigmaSimulator


class EnigmaValueError(Exception):
    pass


# store uppercase alphabetic characters
KEYBOARD_CHARACTERS = string.ascii_uppercase
KEYBOARD_CHARACTER_SET = set(KEYBOARD_CHARACTERS)


# polymorphism with inheritance from EnigmaSimulator class
class EnigmaSimulatorOnlyRotors(EnigmaSimulator):

    # method overriding
    def _encrypt_decrypt(self, plugboard_signal_input):
        """Perform encryption / decryption operations. Parameter:

        plugboard_signal_input: integer 0-25

        Returns corresponding lamp integer number from 0-25 to light

        """
        # get position from plugboard
        current_position = plugboard_signal_input

        # entry signal position
        for rotor in reversed(self.rotors):
            current_position = rotor.entry_signal(current_position)

        current_position = self.reflector.entry_signal(current_position)

        # exit signal position
        for rotor in self.rotors:
            current_position = rotor.exit_signal(current_position)

        return current_position
