#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 13 Sythesizing tasks 1-7"""

import os
import pickle

class PickleCache(object):
    """This is a new class PickleCache. 
    Attributes:
        data(dictionary)
    """
    def __init__(self, file_path='datastore.pkl', autosync=False):
        """This is a new function __init__"""
        self.__file_path = file_path
        self.autosync = autosync
        self.__data = {}
        self.load()

    def __setitem__(self, key, value):
        """This is a new function __setitem__"""
        self.__data[key] = value
        if self.autosync is True:
            self.flush()

    def __len__(self):
        """This is a new function __len__"""
        return len(self.__data)

    def __getitem__(self, key):
        """This is a new function __getitem__"""
        try:
            return self.__data[key]
        except:
            raise KeyError('a key cannot be found')

    def __delitem__(self, key):
        """This is a new function __delitem__"""
        del self.__data[key]
        if self.autosync is True:
            self.flush()

    def load(self):
        """This is a new function load"""
        if os.path.exists(self.__file_path) is True\
           and os.path.getsize(self.__file_path) > 0:
            fhandler = open(self.__file_path, 'r')
            self.__data = pickle.load(fhandler)
            fhandler.close()

    def flush(self):
        """This is a new function flush"""
        fhandler = open(self.__file_path, 'w')
        pickle.dump(self.__data, fhandler)
        fhandler.close()
