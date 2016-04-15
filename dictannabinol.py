#!/usr/bin/python3
#-*- coding: utf-8 -*-

import random

class Dictannabinol(dict):
    """
        Dictionnary that forgets things based on a trust ratio
        This trust ratio is the viability of the object (in percentage)

        All overrided functions have a (small) chance to loose some data
        the chance to remove the data is 1 minus threshold thus, being
        said here it wont be in each function comments


        A trust = 1 is correspond to an object that can only loose
    """


    #######################
    # Dictannabinol basis #
    #######################
    def __init__(self, trust_percent = 0.75):
        """
            Default constructor for a Dictannabinol
            
            _trust percentage of reliability of a dictannabinol (default: 0.75)
        """
        super().__init__(self)

        if  0 <= trust_percent <= 1:
            self._trust = trust_percent # _trust is protected (convention)
        else:
            raise ValueError('trust ratio must be within 0-1')


    @property
    def trust(self):
        return self._trust

    @trust.setter # This need the previous @property to work
    def trust(self, trust_percent):
        """
            Change trust ratio
            Using decorators to perform a simple check on values
        """
        if  0 <= trust_percent <= 1:
            self._trust = trust_percent
        else:
            raise ValueError('trust ratio must be within 0-1')




    ##################
    # Misc functions #
    ##################
    def __forgot(self, threshold, key=False):
        """
            Forgot something based on a treshold, if above treshold -> removed
            if no key specified the removal will be random

            threshold from 0 to 1, chance to not be removed

            If the object is trusty, you wont forget
        """
        # If trusty, stay trusty and don't forget
        if self._trust < 1:
            n = random.random()

            if key and key in super().keys() and n > threshold:
                super().__delitem__(key)
            elif n > threshold:
                key = random.choice(list(super().keys()))
                super().__delitem__(key)
            else:
                pass




    ###########################
    # Override dict functions #
    ###########################
    def __contains__(self, query):
        """ Give unreliable informations about the existence of keys in dict """

        # 1 - % chance of random removal
        self.__forgot(threshold = 0.98, key = query)

        # actual method
        if random.random() > self._trust:
            return False
        else:
            return super().__contains__(query)

    def __setitem__(self, key, value):
        """
            Add (or not) the key:value to the dictannabinol based
            on a trust value

            N.B. Here we use the __forgot function to simulate the "not adding
            the value"
        """
        super().__setitem__(key, value)
        self.__forgot(threshold = self._trust, key = key)

    def __getitem__(self, key):
        """
            Get value from key (or not) based on the trust value
        """
        # 1 - % chance of random removal
        self.__forgot(threshold = 0.95)

        # actual method
        if random.random() <= self._trust:
            return super().__getitem__(key)
        else:
            raise KeyError(key)
