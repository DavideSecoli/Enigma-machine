
"""File containing rotor & reflector types"""

from itertools import permutations
from data_enigma_setup import ROTOR_TYPES, REFLECTOR_TYPES

ROTOR_TYPES = ROTOR_TYPES
REFLECTOR_TYPES = REFLECTOR_TYPES

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
            'U', 'V', 'W', 'X', 'Y', 'Z']

# generate reflector strings and create copies
reflector_a = 'EJMZALYXVBWFCRQUONTSPIKHGD'
reflector_b = 'YRUHQSLDPXNGOKMIEBFZCWVJAT'
reflector_c = 'FVPJIAOYEDRZXWGCTKUQSBNMHL'

ref_a_copy = list(reflector_a).copy()
ref_b_copy = list(reflector_b).copy()
ref_c_copy = list(reflector_c).copy()
ref_tot_copy = [ref_a_copy, ref_b_copy, ref_c_copy]

# create reflector pairs
reflector_a_pairs = ['AE', 'BJ', 'CM', 'DZ', 'FL', 'GY', 'HX', 'IV', 'KW', 'NR', 'OQ', 'PU', 'ST']
reflector_b_pairs = ['AY', 'BR', 'CU', 'DH', 'EQ', 'FS', 'GL', 'IP', 'JX', 'KN', 'MO', 'TZ', 'VW']
reflector_c_pairs = ['AF', 'BV', 'CP', 'DJ', 'EI', 'GO', 'HY', 'KR', 'LZ', 'MX', 'NW', 'QT', 'SU']
tot_ref_pairs = [reflector_a_pairs, reflector_b_pairs, reflector_c_pairs]

# generate permutations af reflector pairs
reflector_a_pairs_all_combo = list(permutations(reflector_a_pairs, 4))
reflector_b_pairs_all_combo = list(permutations(reflector_b_pairs, 4))
reflector_c_pairs_all_combo = list(permutations(reflector_c_pairs, 4))
tot_ref_all_combo = [reflector_a_pairs_all_combo, reflector_b_pairs_all_combo, reflector_c_pairs_all_combo]

# init variables
swap_b = []
current_reflector = []
ref_swap_one = []
ref_swap_two = []
ref_swap_three = []
ref_swap_four = []
ref_total_combos = []
final_reflectors = []

for ref_num, ref_combo in enumerate(tot_ref_all_combo):
    current_reflector = ref_tot_copy[ref_num].copy()

    # loops thru each reflector combo
    for sub_ref_combo in ref_combo:
        swap_a = list(sub_ref_combo[:2])
        swap_b = list(sub_ref_combo[2:])

        # include all four different pair combinations for swap a
        swap_a_combo = []
        swap_a_combo.extend([''.join(swap_a[0][0] + swap_a[1][0]), ''.join(swap_a[0][1] + swap_a[1][1])])
        swap_a_combo.extend([''.join(swap_a[0][0] + swap_a[1][1]), ''.join(swap_a[0][1] + swap_a[1][0])])

        # include all four different pair combinations for swap b
        swap_b_combo = []
        swap_b_combo.extend([''.join(swap_b[0][0] + swap_b[1][0]), ''.join(swap_b[0][1] + swap_b[1][1])])
        swap_b_combo.extend([''.join(swap_b[0][0] + swap_b[1][1]), ''.join(swap_b[0][1] + swap_b[1][0])])

        # four variables to include all different combo between swap a and b
        ref_swap_one.extend([''.join(swap_a_combo[0]), ''.join(swap_a_combo[1]), ''.join(swap_b_combo[0]),
                             ''.join(swap_b_combo[1])])
        ref_swap_two.extend([''.join(swap_a_combo[0]), ''.join(swap_a_combo[1]), ''.join(swap_b_combo[2]),
                             ''.join(swap_b_combo[3])])
        ref_swap_three.extend([''.join(swap_a_combo[2]), ''.join(swap_a_combo[3]), ''.join(swap_b_combo[0]),
                               ''.join(swap_b_combo[1])])
        ref_swap_four.extend([''.join(swap_a_combo[2]), ''.join(swap_a_combo[3]), ''.join(swap_b_combo[2]),
                              ''.join(swap_b_combo[3])])

        ref_total_combos = ref_swap_one, ref_swap_two, ref_swap_three, ref_swap_four

        # create new sub-reflectors for each new combo
        for sub_swap in ref_total_combos:
            for pair in sub_swap:
                two = 0
                for num, char in enumerate(alphabet):
                    if pair[0] == char:
                        current_reflector[num] = pair[1]
                        two += 1
                        if two == 2:
                            break
                    elif pair[1] == char:
                        current_reflector[num] = pair[0]
                        two += 1
                        if two == 2:
                            break

            final_reflectors.append(''.join(current_reflector))
            current_reflector = ref_tot_copy[ref_num].copy()

        # init variables to original state for new loop
        ref_total_combos = []
        ref_swap_one = []
        ref_swap_two = []
        ref_swap_three = []
        ref_swap_four = []
        swap_a = []
        swap_b = []


# create dict of reflectors
REFLECTOR_MERGED_DICTS = {}
for i in range(len(final_reflectors)):
    # reflector 'A '
    if i <= len(final_reflectors)/3:
        REFLECTOR_MERGED_DICTS[f'A{i}'] = final_reflectors[i]
    # reflector 'B'
    elif (len(final_reflectors)/3) + 1 <= i <= (len(final_reflectors)/2) * 3:
        REFLECTOR_MERGED_DICTS[f'B{i}'] = final_reflectors[i]
    # reflector 'C'
    else:
        REFLECTOR_MERGED_DICTS[f'C{i}'] = final_reflectors[i]