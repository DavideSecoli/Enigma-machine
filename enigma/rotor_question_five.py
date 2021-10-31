from rotor import Rotor
from data_enigma_question_five import ROTOR_TYPES, REFLECTOR_MERGED_DICTS


class RotorValueError(Exception):
    pass


def build_rotor(rotor_type, ring_setting=0):
    """Function for building a rotor of specified type"""

    if rotor_type in ROTOR_TYPES:
        data = ROTOR_TYPES[rotor_type]
        return Rotor(rotor_type, data['mapping'], ring_setting, data['notch'])

    raise RotorValueError(f"{rotor_type} is not recognised")


def build_reflector(reflector_type):
    """Function for building a reflector of specified type"""

    if reflector_type in REFLECTOR_MERGED_DICTS:
        return Rotor(reflector_type, rotor_mapping=REFLECTOR_MERGED_DICTS[reflector_type])
    raise RotorValueError(f"{reflector_type} is not recognised")
