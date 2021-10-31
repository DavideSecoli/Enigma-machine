
from ensemble import EnigmaSimulator

""" Run the code to see what I think of this assignment :) 

    Use this module for quick encryption/decryption. This is similar to main.py but its not wrapped into a class method
    
    Parameters:

    rotors: left to right rotors list of strings ["I", "III", "IV"] or "I III IV"

    reflector: string indicating reflector type ('B','C','B-Thin','C-Thin')

    ring_settings: list of integers between 1-26, a string ('A B C'), or None to represent the rotors ring settings

    plugboard: string of up to 10 pairs of letters e.g. 'AD SF GH JK UY IT RE WO MN XZ'
                            or None if no plugboard connections are made

    starting_position: string of characters equal to num of rotors representing rotor starting position. e.g. 'A R D'

    ciphertext: string of text to encrypt or decrypt

"""

enigna_machine = EnigmaSimulator.input_parameters(
    rotors='Beta Gamma V',
    reflector='C',
    ring_settings='04 12 14',
    plugboard_settings='AQ FD TG KZ')

# set machine initial starting position
enigna_machine.starting_position('M J M')


ciphertext = 'SQAUYLLORQWXBPDQQPCKBKRLHCMIJVKNZFOTAPBWLQUBIKRGO'
plaintext = enigna_machine.read(ciphertext)

print(plaintext)