""" Class to manage path, directories and files """

import os

class FilesManager():
    _path = os.getcwd()
    _split_p = _path.split("/")
    _dirs = []
    _files = []
    _def_path = os.path.realpath(__file__)


    def get_path(self):
        """ Returns path """
        return self._path


    def set_path(self):
        """ Sets path """
        self._path = os.getcwd()


    def get_split_path(self):
        """ Returns splitted path """
        return self._split_p


    def set_split_path(self):
        """ Split path in list """
        self._split_p = self._path.split("/")


    def set_dirs(self):
        """ Refreshes directories """
        self._dirs = [d for d in os.listdir(self._path) if os.path.isdir(d)]
        self._dirs.sort(key=lambda s: s.lower())

    def get_dirs(self):
        """ Returns directories of current path """
        return self._dirs


    def set_files(self):
        """ Refreshes files """
        self._files = [d for d in os.listdir(self._path) if os.path.isfile(d)]
        self._files.sort(key=lambda s: s.lower())

    def get_files(self):
        """ Returns files of current path """
        return self._files


    def get_def_path(self):
        """ Returns default path """
        return self._def_path
