"""Rotor class for the Enigma machine"""

import string
import collections
from data_enigma_setup import ROTOR_TYPES, REFLECTOR_TYPES

# all characters uppercase
UPPERCASE = string.ascii_uppercase

# variable to ensure there's just one letter
ONE_LETTER = set((character, 1) for character in UPPERCASE)


class RotorValueError(Exception):
    pass


class RotorSimpleExample:

    def __init__(self):
        self.pos = 0

    @staticmethod
    def encode_right_to_left(input_letter):
        """Function to return rotor I encoded letter.
           For demonstration only purposes. Not used as part of the enigma machine"""

        # check input_letter is a string
        if not isinstance(input_letter, str):
            raise RotorValueError(f"{input_letter} is not a string")

        convert = ord(input_letter) - 65

        rotor_one = 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'

        return rotor_one[convert]

    @staticmethod
    def encode_left_to_right(input_letter):
        """Function to return rotor I encoded letter.
           For demonstration only purposes. Not used as part of the enigma machine"""

        # check input_letter is a string
        if not isinstance(input_letter, str):
            raise RotorValueError(f"{input_letter} is not a string")

        rotor_one = 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'
        char = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        for num, letter in enumerate(rotor_one):
            if letter == input_letter:
                return char[num]


class Rotor:

    def __init__(self, rotor_type, rotor_mapping, ring_setting=0, notch=None):
        """Rotor parameters:

        rotor_type: I, II, III, IV, V, Beta, Gamma

        rotor_mapping: 26 alphabetic characters that maps internal wiring

        ring_setting: integer from 0-25 to offset rotor starting position

        notch: turnover parameter for the rotors. See notch parameters in data_enigma_setup.py

        """

        self.rotor_type = rotor_type
        self.rotor_mapping = rotor_mapping.upper()
        self.rotor_position = 0
        self.ring_setting = ring_setting
        self.mapping_dict = ""
        self.show_value = ""
        self.cycle_count = 0
        self.position = 0

        # check length of mapping
        if len(self.rotor_mapping) != 26:
            raise RotorValueError("Incorrect mapping length")

        # check character mapping occurs just once
        character_input = set(collections.Counter(self.rotor_mapping).items())
        if character_input != ONE_LETTER:
            raise RotorValueError("Incorrect character mapping")

        # check ring_setting is either int or 0 - 25
        if not isinstance(ring_setting, int) or not (0 <= ring_setting < 26):
            raise RotorValueError("Incorrect ring_setting")

        # map numerical values to positions
        self.mapping_dict = {}
        for number in range(26):
            self.mapping_dict[chr(ord('A') + number)] = (number - self.ring_setting) % 26

        # reverse dictionary to map positions to numerical values
        self.reverse_mapping_dict = {v: k for k, v in self.mapping_dict.items()}

        # rotor numerical right mapping (entry)
        self.right_mapping = [ord(rotor_pin) - ord('A') for rotor_pin in self.rotor_mapping]

        # rotor numerical left mapping (exit)
        self.left_mapping = [0] * 26
        for number, value in enumerate(self.right_mapping):
            self.left_mapping[value] = number

        # create set of positions where notches are set to allow the pawls to move
        self.position_step = set()
        if notch is not None:
            for position in notch:
                if position in self.mapping_dict:
                    self.position_step.add(position)
                else:
                    raise RotorValueError(f"Notch error at position: {position}")

        # init display value
        self.starting_position('A')

    def starting_position(self, values):
        """Set the rotor to specified starting point

        Values: accept characters from 'A' to 'Z'

        For a value of 'A" sets the rotor in position 0 if ring_setting is 0
        """

        char = values.upper()
        if char not in self.mapping_dict:
            raise RotorValueError(f"Incorrect character {char}")

        self.rotor_position = self.mapping_dict[char]
        self.show_value = char
        self.cycle_count = 0

    def get_rotor_position(self):
        """Returns rotor position"""
        return self.show_value

    def entry_signal(self, entry_signal_number):
        """Matches signal entering the right rotor to output number

        entry_signal_number: integer between 0 and 25.
        """
        
        # calculate what pin there is at that position
        pin_position = (entry_signal_number + self.rotor_position) % 26

        # map pin position with internal wiring
        map_pin_position = self.right_mapping[pin_position]

        # back into position following rotation
        return (map_pin_position - self.rotor_position) % 26

    def exit_signal(self, exit_signal_number):
        """Matches signal entering the left rotor to output number

        exit_signal_number: integer between 0 and 25.
        """
        
        # calculate what pin there is at that position
        pin_position = (exit_signal_number + self.rotor_position) % 26

        # map pin position with internal wiring
        map_pin_position = self.left_mapping[pin_position]

        # back into position following rotation
        return (map_pin_position - self.rotor_position) % 26

    def stepping_position(self):
        """Returns True if rotor has a notch in stepping position else
        False
        """
        return self.show_value in self.position_step

    def rotation(self):
        """Rotates the rotor forward"""

        self.rotor_position = (self.rotor_position + 1) % 26
        self.show_value = self.reverse_mapping_dict[self.rotor_position]
        self.cycle_count += 1


def rotor_from_name(rotor_type):
    """ Function to return rotor type"""
    return rotor_type


def build_rotor(rotor_type, ring_setting=0):
    """Function for building a rotor of specified type"""

    if rotor_type in ROTOR_TYPES:
        data = ROTOR_TYPES[rotor_type]
        return Rotor(rotor_type, data['mapping'], ring_setting, data['notch'])

    raise RotorValueError(f"{rotor_type} is not recognised")


def build_reflector(reflector_type):
    """Function for building a reflector of specified type"""

    # normal case
    if reflector_type in REFLECTOR_TYPES:
        return Rotor(reflector_type, rotor_mapping=REFLECTOR_TYPES[reflector_type])

    raise RotorValueError(f"{reflector_type} is not recognised")
