"""This module contains the methods to add and encode plug leads"""


class PlugLeadValueError(Exception):
    pass


class PlugLead:

    def __init__(self, mapping):

        if len(mapping) != 2:
            raise PlugLeadValueError("PlugLead accepts only two characters string")
        if mapping[0] == mapping[1]:
            raise PlugLeadValueError("PlugLead characters must be different")
        
        # map first and second argument to two separate variables
        self.map1 = mapping[0] 
        self.map2 = mapping[1]

    def encode(self, trick):
        if trick == self.map1:
            swap_encode = self.map2
        elif trick == self.map2:
            swap_encode = self.map1
        else:
            swap_encode = trick
        return swap_encode
