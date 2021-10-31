"""This module contains the methods to add and encode plug leads in the plug board"""

import string
import collections
from itertools import chain


# set max number of leads
TOT_LEADS = 10


class PlugboardValueError(Exception):
    pass


class Plugboard:
    """ Connect up to 10 plug-leads and swap letters before and after the rotors"""

    # store plugged leads
    plugged_leads = []

    # store left plugs in plug board
    alphabet_string = string.ascii_uppercase
    plug_board = list(alphabet_string)

    def __init__(self, num_leads=None, plug_lead=None):

        """
        Map the plugboard with a list or tuple of integer pairs, or None.
        If no value is provided, there will not be plugboard connections. Parameters:

        num_leads: max 10 integer pairs between 0-25, inclusive. Each representing an
        input/output path through the plugboard. Same path cannot be repeated
        """

        # generate numerical list of alphabet length
        self.numerical_mapping = list(range(26))

        self.plug_lead = plug_lead

        # continue if no leads
        if not num_leads:
            return

        # check num leads dont exceed total
        if len(num_leads) > TOT_LEADS:
            raise PlugboardValueError(f'{TOT_LEADS} is the max number of leads allowed')

        # check there's no repetition in the list
        leads_checker = collections.Counter(chain.from_iterable(num_leads))
        combo, number = leads_checker.most_common(1)[0]
        if number != 1:
            raise PlugboardValueError(f"{combo} is a duplicate")

        # make the connections
        for lead_pair in num_leads:
            map_one = lead_pair[0]
            map_two = lead_pair[1]
            if not (0 <= map_one < 26) or not (0 <= map_two < 26):
                raise PlugboardValueError(f"{lead_pair} is not valid")

            self.numerical_mapping[map_one] = map_two
            self.numerical_mapping[map_two] = map_one

    def add(self, plug_lead):

        count_match = 0
        for lead in self.plug_board:
            if lead in plug_lead.map1:
                self.plug_board.remove(lead)
                count_match += 1
            elif lead in plug_lead.map2:
                self.plug_board.remove(lead)
                count_match += 1

        # raise error if leads already in use
        if count_match != 2:
            self.plug_board.extend([plug_lead.map1, plug_lead.map2])
            raise PlugboardValueError('Plug lead already in use')
        else:
            self.plugged_leads.append(plug_lead.map1 + plug_lead.map2)

    def encode(self, character):

        # accepts only one character
        if len(character) != 1:
            raise PlugboardValueError("Only one character can be parsed in")

        # return other end of the plug else character
        for char in self.plugged_leads:
            if char[0] in character:
                return char[1]
            elif char[1] in character:
                return char[0]
        return character

    @classmethod
    def pluglead_pairs(cls, pluglead_settings=None):
        """Input plug lead. Parameter:

        pluglead_settings: string of max length of 10 alphabetic pairs. e.g. 'AD SF GH JK UY IT RE WO MN XZ'
                           or None if no plugboard connections are made

        """

        alphabet_string = string.ascii_uppercase

        # check for no input
        if not pluglead_settings:
            return None

        pluglead_pairs = []

        upper_pairs = pluglead_settings.upper().split()

        for pluglead_pair in upper_pairs:
            if len(pluglead_pair) != 2:
                raise PlugboardValueError(f"{pluglead_pair} length can't be different than two")

            # map pluglead ends
            map_one = pluglead_pair[0]
            map_two = pluglead_pair[1]
            if map_one not in alphabet_string or map_two not in alphabet_string:
                raise PlugboardValueError(f"{pluglead_pair} is not a supported character")

            # transform to 0-25 digits
            pluglead_pairs.append((ord(map_one) - ord('A'), ord(map_two) - ord('A')))

        return cls(pluglead_pairs)

    def numerical_input_output(self, input_number):
        """ Return numerical output signal (0-25) given input_number (0-25)"""

        return self.numerical_mapping[input_number]

