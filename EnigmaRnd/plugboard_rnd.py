"""This module contains the methods to add and encode plug leads in the plug board"""

import string
import numpy as np

# set max number of leads
TOT_LEADS = 11


class PlugboardValueError(Exception):
    pass


class Plugboard:
    """ Connect up to 13 plug-leads and swap letters before and after the rotors"""

    # store plugged leads
    plugged_leads = []

    # store left plugs in plug board
    alphabet_string = string.ascii_uppercase
    plug_board = list(alphabet_string)

    def __init__(self, num_leads=None, plug_lead=None):

        """ Map the plugboard with a list or tuple of integer pairs, or None.
        If no value is provided, there will not be plugboard connections. Parameters:

        num_leads: max 10 integer pairs between 0-25, inclusive. Each representing an
        input/output path through the plugboard. Same path can be repeated

        """

        # generate numerical list of alphabet length
        self.numerical_mapping = list(range(26))

        self.plug_lead = plug_lead

        # continue if no leads
        if not num_leads:
            return

        if len(num_leads) > TOT_LEADS:
            raise PlugboardValueError(f'{TOT_LEADS} is the max numbers of leads allowed')

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
    def pluglead_pairs(cls, pluglead_settings=None, seeds=None):
        """Input plug leads. Parameter:

        pluglead_settings: string of max length of 10 alphabetic pairs. e.g. 'AD SF GH JK UY IT RE WO MN XZ'
                           or None if no plugboard connections are made

        seeds:  0-N list of integers with length equal to num of plug leads, used for feeding pseudo-random number
                generator for plugboard pairs
        """

        alphabet_string = string.ascii_uppercase

        if not pluglead_settings:
            return None

        pluglead_pairs = []
        # create ord list of uppercase numbers
        ord_upper_list = list(range(ord('A'), ord('Z') + 1))

        # create 0-25 list to represent a-z letters in numerical form
        pluglead_pairs_numbers = list(range(26))

        upper_pairs = pluglead_settings.upper().split()

        for num_pair, pluglead_pair in enumerate(upper_pairs):
            if len(pluglead_pair) != 2:
                raise PlugboardValueError(f"{pluglead_pair} length can't be different than two")

            map_one = pluglead_pair[0]
            map_two = pluglead_pair[1]
            if map_one not in alphabet_string or map_two not in alphabet_string:
                raise PlugboardValueError(f"{pluglead_pair} is not a supported character")

            # init random sequence
            np.random.seed(seeds[num_pair])

            # generate ord list of uppercase chars
            ord_numbers = np.arange(start=65, stop=91)

            # generate random numbers from ord_numbers set of pluglead length
            rnd = np.random.choice(ord_numbers, size=2)

            # convert rnd to characters
            rnd_list = [i for i in rnd]

            # sum map and random num
            maps_one_sum = ord(map_one) + rnd_list[1]
            maps_two_sum = ord(map_two) + rnd_list[0]

            # generate new pluglead char by looping through alphabet maps_one_sum number of times
            i = ord(pluglead_pair[0])
            while i != maps_one_sum:
                i += 1
            map_one_rnd = ord_upper_list[i % len(ord_upper_list)]

            # generate new pluglead 65-90 decimals by looping through alphabet maps_one_sum number of times
            i = ord(pluglead_pair[1])
            while i != maps_two_sum:
                i += 1
            map_two_rnd = ord_upper_list[i % len(ord_upper_list)]

            # transform character to 0-25 numbers
            map_one_rnd_num = map_one_rnd - ord('A')
            map_two_rnd_num = map_two_rnd - ord('A')

            # if numbers already in use get last item in list
            if map_one_rnd_num in pluglead_pairs_numbers:
                map_one_idx = pluglead_pairs_numbers.index(map_one_rnd_num)
                del pluglead_pairs_numbers[map_one_idx]
            else:
                map_one_rnd_num = pluglead_pairs_numbers[-1]
                del pluglead_pairs_numbers[-1]

            if map_two_rnd_num in pluglead_pairs_numbers:
                map_two_idx = pluglead_pairs_numbers.index(map_two_rnd_num)
                del pluglead_pairs_numbers[map_two_idx]
            else:
                map_two_rnd_num = pluglead_pairs_numbers[-1]
                del pluglead_pairs_numbers[-1]

            pluglead_pairs.append((map_one_rnd_num, map_two_rnd_num))

        return cls(pluglead_pairs)

    def numerical_input_output(self, input_number):
        """ Return numerical output signal (0-25) given input_number (0-25)"""

        return self.numerical_mapping[input_number]