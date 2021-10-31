from ensemble_only_rotors import EnigmaSimulatorOnlyRotors


class RotorsQuestions:

    """Class used for the Multiple Rotor demonstration in Part 1 to show rotors work correctly.

    Instantiate RotorsQuestions class and run method rotors_question to check rotor's functionality.

    Input parameters:

    rotors: left to right rotors list of strings ["I", "III", "IV"] or "I III IV"

    reflector: string indicating reflector type ('B','C','B-Thin','C-Thin')

    ring_settings: list of integers between 1-26, a string ('A B C'), or None to represent the rotors ring settings

    starting_position: string of characters equal to num of rotors representing rotor starting position. e.g. 'A R D'

    ciphertext: string of text to encrypt or decrypt
    """

    @staticmethod
    def rotors_question(rotors, reflector, ring_settings, starting_position, ciphertext):
        enigna_machine_one = EnigmaSimulatorOnlyRotors.input_parameters(
            rotors=rotors,
            reflector=reflector,
            ring_settings=ring_settings)

        enigna_machine_one.starting_position(starting_position)
        plaintext_one = enigna_machine_one.read(ciphertext)
        return plaintext_one
