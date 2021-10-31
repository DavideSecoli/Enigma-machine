
"""This module contains the EnigmaSimulator class for the Enigma Machine"""

import string
from rotor import build_rotor, build_reflector
from plugboard import Plugboard


class EnigmaValueError(Exception):
    pass


# store uppercase alphabetic characters
KEYBOARD_CHARACTERS = string.ascii_uppercase
KEYBOARD_CHARACTER_SET = set(KEYBOARD_CHARACTERS)


class EnigmaSimulator:
    """Enigma Machine top-level class"""

    def __init__(self, rotors, reflector, plugboard):
        """Following are the Enigma simulator parameters:

        plugboard: object that represents all plug-lead connections

        rotors: list containing 3 or 4 rotor objects from left-most to right-most

        reflector: - rotor like object representing the reflector (UKW)
        """

        if len(rotors) not in [3, 4]:
            raise EnigmaValueError("Machine supports 3 or 4 rotors")

        self.rotors = rotors
        self.rotors_number = len(rotors)
        self.reflector = reflector
        self.plugboard = plugboard

    @classmethod
    def input_parameters(cls, rotors=None, ring_settings=None, reflector=None, plugboard_settings=None):

        """Function to build an Enigma simulator. Following are the parameters:

        rotors: left to right rotors list of strings ["I", "III", "IV"] or "I III IV"

        ring_settings: list of integers between 1-26, a string ('A B C'), or None to represent the rotors ring settings

        reflector: string indicating reflector type ('B','C','B-Thin','C-Thin')

        plugboard_settings: string of up to 10 pairs of letters e.g. 'AD SF GH JK UY IT RE WO MN XZ'
                            or None if no plugboard connections are made
        """
        # check rotors input is a string
        if isinstance(rotors, str):
            rotors = rotors.split()

        # check num of rotors is 3 or 4
        rotors_count = len(rotors)
        if rotors_count not in (3, 4):
            raise EnigmaValueError("Machine supports 3 or 4 rotors")

        # check if there are ring settings
        if ring_settings is None:
            ring_settings = [0] * rotors_count

        elif isinstance(ring_settings, str):
            ring_setting_strings = ring_settings.split()
            ring_settings = []
            # if char transform to 0-25
            for ring_setting_string in ring_setting_strings:
                if ring_setting_string.isalpha():
                    ring_settings.append(ord(ring_setting_string.upper()) - ord('A'))
                # if digit -1
                elif ring_setting_string.isdigit():
                    ring_settings.append(int(ring_setting_string) - 1)
                else:
                    raise EnigmaValueError(f"Ring setting not supported: {ring_setting_string}")

        # check rotors match ring settings
        if rotors_count != len(ring_settings):
            raise EnigmaValueError("Rotors and ring settings number don't match")

        # create rotors
        ensembled_rotors = [build_rotor(r[0], r[1]) for r in zip(rotors, ring_settings)]

        return cls(ensembled_rotors,
                   build_reflector(reflector),
                   Plugboard.pluglead_pairs(plugboard_settings))

    def starting_position(self, initial_position):
        """Set rotor initial position

        'initial_position': string containing rotors starting position from left to right ("AAB")

        """
        # split if input is given in string separated form
        if len(initial_position) >= 5:
            initial_position = initial_position.split()

        if len(initial_position) != self.rotors_number:
            raise EnigmaValueError(f"{initial_position} is an incorrect parameter length")

        for number, rotor in enumerate(reversed(self.rotors)):
            rotor.starting_position(initial_position[-1 - number])

    def keyboard(self, keyboard_key):
        """This is the operator keyboard.

        keyboard_key: string representing the letter pressed

        At each key press the rotors move forward and a simulated current run through the machine
        The returned string is the corresponding lamp lit by the key press

        """

        if keyboard_key not in KEYBOARD_CHARACTER_SET:
            raise EnigmaValueError(f'{keyboard_key} is not supported')

        # move rotors forward
        self._rotors_forward_step()

        # simulate electric signal:
        signal_number = ord(keyboard_key) - ord('A')
        lamp_number = self._encrypt_decrypt(signal_number)
        return KEYBOARD_CHARACTERS[lamp_number]

    def _rotors_forward_step(self):
        """Simulate rotors forward movement when key is pressed"""

        first_rotor = self.rotors[-1]
        second_rotor = self.rotors[-2]
        third_rotor = self.rotors[-3]

        # assess rotors movement
        rotate_two = first_rotor.stepping_position() or second_rotor.stepping_position()
        rotate_three = second_rotor.stepping_position()

        # move rotors forward
        first_rotor.rotation()
        if rotate_two:
            second_rotor.rotation()
        if rotate_three:
            third_rotor.rotation()

    def _encrypt_decrypt(self, plugboard_signal_input):
        """Perform encryption / decryption operations. Parameter:

        plugboard_signal_input: integer 0-25

        Returns corresponding lamp integer number from 0-25 to light

        """
        # get position from plugboard
        current_position = self.plugboard.numerical_input_output(plugboard_signal_input)

        # entry signal position
        for rotor in reversed(self.rotors):
            current_position = rotor.entry_signal(current_position)

        current_position = self.reflector.entry_signal(current_position)

        # exit signal position
        for rotor in self.rotors:
            current_position = rotor.exit_signal(current_position)

        return self.plugboard.numerical_input_output(current_position)

    def read(self, input_characters, character_replace='Z'):
        """Read each input character. Parameters:

        input_characters: uppercase converted text to process

        character_replace: replace character with 'Z' if character not in KEYBOARD_CHARACTER_SET

        """
        result = []
        for character in input_characters:
            upper_character = character.upper()

            if upper_character not in KEYBOARD_CHARACTER_SET:
                if character_replace:
                    character = character_replace
                else:
                    continue

            result.append(self.keyboard(character))

        return ''.join(result)

    def get_rotors_rotations_number(self):
        """Return list containing rotors total number of rotations"""
        return [rotor.rotations for rotor in self.rotors]
