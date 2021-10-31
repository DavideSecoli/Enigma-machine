
from rotor_question_five import build_rotor, build_reflector
from plugboard import Plugboard
from ensemble import EnigmaSimulator


class EnigmaValueError(Exception):
    pass


# polymorphism with inheritance from EnigmaSimulator class
class EnigmaSimulatorQuestionFive(EnigmaSimulator):
    """Enigma Machine top-level class"""

    # method overriding
    @classmethod
    def input_parameters(cls, rotors=None, ring_settings=None, reflector=None, plugboard_settings=None):

        """ Function to build an Enigma simulator. Parameters:

               rotors: left to right rotors list of strings ["I", "III", "IV"] or "I III IV"

               ring_settings: list of integers between 1-26, a string ('A B C'), or None to represent
                              the rotors ring settings

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