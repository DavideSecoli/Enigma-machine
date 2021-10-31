import string
from ensemble import EnigmaSimulator
from itertools import product
from string import ascii_uppercase
from data_enigma_question_five import REFLECTOR_MERGED_DICTS
from ensemble_question_five import EnigmaSimulatorQuestionFive


# QUESTION 1

def part_two_code_one(reflectors, ciphertext, crib_q_one):
    """
    From the list of reflectors A, B, C check plaintext matching crib word SECRET
    The other parameters were provided
    """
    for input_reflectors in reflectors:

        enigna_machine = EnigmaSimulator.input_parameters(
            rotors='Beta Gamma V',
            reflector=input_reflectors,
            ring_settings='04 02 14',
            plugboard_settings='KI XN FL')

        # set machine initial starting position
        enigna_machine.starting_position('MJM')
        plaintext = enigna_machine.read(ciphertext)

        if crib_q_one in plaintext:
            return f'Output question 1: {plaintext}', f'Reflector type: {input_reflectors}'


# main function call
code_one = part_two_code_one(['A', 'B', 'C'], 'DMEXBMKYCVPNQBEDHXVPZGKMTFFBJRPJTLHLCHOTKOYXGGHZ', 'SECRET')

# print output
print(code_one)

# QUESTION 2

# generate list containing all starting positions
starting_positions_list = [''.join(i) for i in product(ascii_uppercase, repeat=3)]


def part_two_code_two(input_positions, ciphertext, crib_q_two):
    """
    Check starting position generated in line 6 matching plaintext with crib UNIVERSITY
    The remaining parameters were provided
    """

    for starting_position in input_positions:

        enigna_machine = EnigmaSimulator.input_parameters(
            rotors='Beta I III',
            reflector='B',
            ring_settings='23 02 10',
            plugboard_settings='VH PT ZG BJ EY FS')

        # set machine initial starting position
        enigna_machine.starting_position(starting_position)
        plaintext = enigna_machine.read(ciphertext)

        if crib_q_two in plaintext:
            return f'Output question 2: {plaintext}', f'Starting positions: {starting_position}'


# main function call
code_two = part_two_code_two(starting_positions_list, 'CMFSUPKNCBMUYEQVVDYKLRQZTPUFHSWWAKTUGXMPAMYAFITXIJKMH',
                             'UNIVERSITY')

# print output
print(code_two)

# QUESTION 3

# generate list containing all rotors combinations

rotors = ['II', 'IV', 'Beta', 'Gamma']
rotor_list = [' '.join(i) for i in product(rotors, repeat=3)]

# generate list containing all ring settings combinations
ring_settings = ['02', '04', '06', '08', '20', '22', '24', '26']
ring_settings_list = [' '.join(i) for i in product(ring_settings, repeat=3)]


def part_two_code_three(input_rotors, input_reflectors, input_ring_settings, ciphertext, crib_q_three):
    """
    Check each combination of rotors, reflector and ring settings that match plaintext with crib word THOUSANDS
    Rotors, reflector and ring settings parameters are not part of provided parameters. See lines 6 to 12 and 42
    """

    for rotor_group in input_rotors:
        for reflector_group in input_reflectors:
            for ring_settings_group in input_ring_settings:

                enigna_machine = EnigmaSimulator.input_parameters(
                    rotors=rotor_group,
                    reflector=reflector_group,
                    ring_settings=ring_settings_group,
                    plugboard_settings='FH TS BE UQ KD AL')

                # set machine initial starting position
                enigna_machine.starting_position('EMY')
                plaintext = enigna_machine.read(ciphertext)

                if crib_q_three in plaintext:
                    return f'Output question 3: {plaintext}', f'Rotors: {rotor_group}', \
                           f'Reflector: {reflector_group}', f'Ring settings: {ring_settings_group}'


# main function call
code_three = part_two_code_three(rotor_list, ['A', 'B', 'C'], ring_settings_list,
                                 'ABSKJAKKMRITTNYURBJFWQGRSGNNYJSDRYLAPQWIAGKJYEPCTAGDCTHLCDRZRFZHKNRSDLNPFPEBVESHPY',
                                 'THOUSANDS')

# print output
print(code_three)

# QUESTION 4

upper_letters = string.ascii_uppercase

# generate list containing all combinations of missing letters
plug_combinations = [''.join(i) for i in product(upper_letters, repeat=2) if
                     i[0] not in 'WPRJAVFIHNCGBS' and i[1] not in 'WPRJAVFIHNCGBS' and i[0] != i[1]]

# generate list containing all required combinations of plugs groups
plug_groups = [f'WP RJ A{i[0]} VF I{i[1]} HN CG BS' for i in plug_combinations]

solutions = []


def part_two_code_four(input_plugs, ciphertext, crib_q_four):
    """
    For each plug group in plug_groups check those matching the crib word TUTOR.
    The remaining parameters were provided
    """

    for plug_group in input_plugs:

        enigna_machine = EnigmaSimulator.input_parameters(
            rotors='V III IV',
            reflector='A',
            ring_settings='24 12 10',
            plugboard_settings=plug_group)

        # set machine initial starting position
        enigna_machine.starting_position('SWU')
        plaintext = enigna_machine.read(ciphertext)

        if crib_q_four in plaintext:
            solutions.extend([plaintext, plug_group])

    return solutions


# main function call
code_four = part_two_code_four(plug_groups, 'SDNTVTPHRBNWTLMZTQKZGADDQYPFNHBPNHCQGBGMZPZLUAVGDQVYRBFYYEIXQWVTHXGNW',
                               'TUTOR')

# note the output was filtered to print only the correct phrase
# for all output remove [4:6]
print("('Output question 4:", code_four[4:6], "')")

# QUESTION 5

crib = 'FACEBOOK'
crib2 = 'INSTAGRAM'
crib3 = 'TWITTER'
crib4 = 'TIKTOK'

# store all reflector combinations
keys_list = []
for key in REFLECTOR_MERGED_DICTS.keys():
    keys_list.append(key)


def part_two_code_five(input_reflectors, ciphertext):
    """For each reflector in key_list check if matches one of the crib words. The remaining parameters were provided"""

    for reflector in input_reflectors:

        enigna_machine = EnigmaSimulatorQuestionFive.input_parameters(
            rotors='V II IV',
            reflector=reflector,
            ring_settings='06 18 07',
            plugboard_settings='UG IE PO NX WT')

        # set machine initial starting position
        enigna_machine.starting_position('AJL')
        plaintext = enigna_machine.read(ciphertext)

        if crib in plaintext:
            return f'Output question 5: {plaintext}', f'Original reflector type: {reflector[:1]}', \
                   f'Reflector re-wiring: {REFLECTOR_MERGED_DICTS[reflector]}', f'Crib: {crib}'
        elif crib2 in plaintext:
            return f'Output question 5: {plaintext}', f'Original reflector type: {reflector[:1]}', \
                   f'Reflector re-wiring: {REFLECTOR_MERGED_DICTS[reflector]}', f'Crib: {crib2}'
        elif crib3 in plaintext:
            return f'Output question 5: {plaintext}', f'Original reflector type: {reflector[:1]}', \
                   f'Reflector re-wiring: {REFLECTOR_MERGED_DICTS[reflector]}', f'Crib: {crib3}'
        elif crib4 in plaintext:
            return f'Output question 5: {plaintext}', f'Original reflector type: {reflector[:1]}', \
                   f'Reflector re-wiring: {REFLECTOR_MERGED_DICTS[reflector]}', f'Crib: {crib4}'


# main function call
code_five = part_two_code_five(keys_list, 'HWREISXLGTTBYVXRCWWJAKZDTVZWKBDJPVQYNEQIOTIFX')

# print output
print(code_five)
