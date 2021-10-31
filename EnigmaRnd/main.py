
from ensemble_rnd import EnigmaSimulator

""" Use this module to run encryption/decryption messages. Run the function with current settings to know how I am :)

    Parameters:

    rotors: left to right rotors list of strings ["I", "III", "IV"] or "I III IV"

    reflector: string indicating reflector type ('B','C','B-Thin','C-Thin')

    ring_settings: list of integers between 1-26, a string ('A B C'), or None to represent the rotors ring settings

    plugboard: string of up to 10 pairs of letters e.g. 'AD SF GH JK UY IT RE WO MN XZ'
                            or None if no plugboard connections are made
                            
    seed: list of integers with values 0-N. Number of seeds must match number of plugboard settings

    starting_position: string of characters equal to num of rotors representing rotor starting position. e.g. 'A R D'

    ciphertext: string of text to encrypt or decrypt

"""

enigna_machine = EnigmaSimulator.input_parameters(
    rotors='Beta Gamma V',
    reflector='B',
    ring_settings='04 02 14',
    plugboard_settings='AA CD EF GH IJ KL MN GG HT BH ND',
    seed=[42, 76, 32, 5, 56, 34, 2, 88, 76, 54, 69])

# set machine initial starting position
enigna_machine.starting_position('MTM')

# type in the message to encrypt or decrypt
ciphertext = 'WJGNOIQIGCQBQFKRBVH'
plaintext = enigna_machine.read(ciphertext)

print(plaintext)