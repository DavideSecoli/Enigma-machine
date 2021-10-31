
"""File containing rotor & reflector types"""

ROTOR_TYPES = {
    'I': {'mapping': 'EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'notch': 'Q'},

    'II': {'mapping': 'AJDKSIRUXBLHWTMCQGZNPYFVOE', 'notch': 'E'},

    'III': {'mapping': 'BDFHJLCPRTXVZNYEIWGAKMUSQO', 'notch': 'V'},

    'IV': {'mapping': 'ESOVPZJAYQUIRHXLNFTGKDCMWB', 'notch': 'J'},

    'V': {'mapping': 'VZBRGITYUPSDNHLXAWMJQOFECK', 'notch': 'Z'},

    'VI': {'mapping': 'JPGVOUMFYQBENHZRDKASXLICTW', 'notch': 'ZM'},

    'VII': {'mapping': 'NZJHGRCXMYSWBOUFAIVLPEKQDT', 'notch': 'ZM'},

    'VIII': {'mapping': 'FKQHTLXOCBJSPDZRAMEWNIUYGV', 'notch': 'ZM'},

    'Beta': {'mapping': 'LEYJVCNIXWPBQMDRTAKZGFUHOS', 'notch': None},

    'Gamma': {'mapping': 'FSOKANUERHMBTIYCWLQPZXVGJD', 'notch': None},
}

REFLECTOR_TYPES = {
    'A': 'EJMZALYXVBWFCRQUONTSPIKHGD',
    'B': 'YRUHQSLDPXNGOKMIEBFZCWVJAT',
    'B-Thin': 'ENKQAUYWJICOPBLMDXZVFTHRGS',
    'C': 'FVPJIAOYEDRZXWGCTKUQSBNMHL',
    'C-Thin': 'RDOBJNTKVEHMLFCWZAXGYIPSUQ',
}
