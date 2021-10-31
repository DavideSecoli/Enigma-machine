
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

    'IX': {'mapping': 'QKFTHLXOCBSJDPRAZEMWNUIYGV', 'notch': 'B'},

    'X': {'mapping': 'KEFMGLQDZVTNWOYHUXSAPBRIJC', 'notch': 'C'},

    'XI': {'mapping': 'JAKDISUXRBHWLMTQGCZPYNVOFE', 'notch': 'E'},

    'XII': {'mapping': 'DBHFLCJRTPVXNYZIWEAKGUSMQO', 'notch': 'D'},

    'XIII': {'mapping': 'ZBVRITGUYPDSHLNAWXMQJOECFK', 'notch': 'G'},

    'XIV': {'mapping': 'VBZGRTIUYSPDHNXLAMJWOQEFCK', 'notch': 'H'},

    'XV': {'mapping': 'NJZGHCRMYXWSOUBAIFLVEKPDTQ', 'notch': 'M'},

    'XVI': {'mapping': 'ZNHJGCRXYMWSOBUAFIVLPEKQDT', 'notch': 'O'},

    'XVII': {'mapping': 'KFQHLTXOBCJSPZDRAEWMNUYIGV', 'notch': 'Q'},

    'XVIII': {'mapping': 'QFTKHXOLCSJBDRPAEZWMNIYGUV', 'notch': 'D'},

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
