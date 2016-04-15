#!/usr/bin/python3
#-*- coding: utf-8 -*-

import random as rand

class Dictannabinol(dict):
    """
        Dictionnary that forgets things based on a trust ratio
        This trust ratio is the chance of forgetting (in percentage)
    """

    # Constructors
    def __init__(self, trust_percent = 0.25):
        """
            Default constructor for a Dictannabinol
            
            _trust percentage of reliability of a dictannabinol (default: 0.25)
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


    # Override dict functions
    def __contains__(self, query):
        """ Give unreliable informations about the existence of keys in dict """
        if rand.random() > self._trust:
            return False
        else:
            return super().__contains__(query)

    def __setitem__(self, key, value):
        """
            Add (or not) the key:value to the dictannabinol
            The threshold is trust * 3

            if trust > 0.333.. the __setitem__ is reliable
        """
        treshold = self._trust * 3
        if rand.random() <= treshold:
            return super().__setitem__(key, value)
        else:
            pass

    def __getitem__(self, key):
        """
            Add (or not) the key:value to the dictannabinol
            The threshold is trust * 1.5

            if trust > 0.666.. the __getitem__ is reliable
        """
        treshold = self._trust * 1.5
        if rand.random() <= treshold:
            return super().__getitem__(key)
        else:
            raise KeyError(key)