__author__ = 'Osvaldo Demo'

#
# Minimal functionality to read and use passwords from vSphere Credential Store
#
#

import xml.etree.ElementTree as ET
from sys import platform as _platform
import os
import os.path


class PasswordEntry(object):
    """
    Abstraction object that translates from obfuscated password to usable text
    """

    def __init__ (self, host=None, username=None, password=None):
        self.host = host
        self.username = username
        self.password = password

    def __str__ (self):
        return '{Host: ' + self.host + ' User: ' + self.username + ' Pwd: ' + self.password

    def __unicode__ (self):
        self.__str__()

    def _compute_hash (self, text):

        boundary = 0x7FFFFFFF
        negative = 0x80000000

        # hash = s[0]*31^(n-1) + s[1]*31^(n-2) + ... + s[n-1]

        hash_value = 0
        for my_char in text:
            hash_value = hash_value * 31 + ord(my_char)
            if (hash_value & negative):
                hash_value |= ~boundary
            else:
                hash_value &= boundary

        return hash_value

    def _deobfuscate (self):
        hashmod = 256
        password = self.password.decode('base64')
        hash_value = self._compute_hash(self.host + self.username) % hashmod
        crypt = chr(hash_value & 0xFF) * len(password)
        password_final = []
        for n in range(0, len(password)):
            password_final.append(ord(password[n]) ^ ord(crypt[n]))
        decrypted_pwd = ''
        for ci in password_final:
            if ci == 0:
                break
            decrypted_pwd += chr(ci)

        return decrypted_pwd

    def getPwd (self):
        return self._deobfuscate()

    def getUser (self):
        return self.username

    def getHost (self):
        return self.host


class HostNotFoundException(Exception):
    pass


class NoCredentialsFileFound(Exception):
    pass


class VICredStore(object):
    """
    Helper class that mimicks VICredStore perl module.
    """

    hostdata = {}

    FILE_PATH_UNIX = '/.vmware/credstore/vicredentials.xml'
    FILE_PATH_WIN = '/VMware/credstore/vicredentials.xml'

    def __init__ (self, path=None):
        if path is None:
            try:
                if os.environ['VI_CREDSTORE'] is not None:
                    self.path = os.environ['VI_CREDSTORE']
            except KeyError:
                if _platform == "linux" or _platform == "linux2":
                    self.path = os.environ['HOME'] + self.FILE_PATH_UNIX
                elif _platform == "darwin":
                    raise Exception('Unsupported platform! (' + _platform + ')')
                elif _platform == "win32":
                    self.path = os.environ['APPDATA'] + self.FILE_PATH_WIN
        else:
            self.path = path

        if os.path.exists(self.path):
            self.tree = ET.parse(self.path)
            self.root = self.tree.getroot()
            self.hostdata = self._populate_data()
        else:
            self.root = None
            self.tree = None
            raise NoCredentialsFileFound('Credential filename [' + self.path + '] doesn\'t exist!')

    def get_userpwd (self, hostname):
        try:
            entry = self.hostdata[hostname]
        except KeyError:
            raise HostNotFoundException("Host " + hostname + " does not exist in the credential store!")

        return (entry.getUser(), entry.getPwd())

    def get_pwd_entry_list (self):
        tmp_list = []
        for entry in self.root:
            if entry.tag == "passwordEntry":
                tmp_list.append(entry)

        pwdentries = []
        for entry in tmp_list:
            host = None
            user = None
            pwd = None
            for child in entry:
                if child.tag == "host":
                    host = child.text
                if child.tag == "username":
                    user = child.text
                if child.tag == "password":
                    pwd = child.text

            if host != None and user != None and pwd != None:
                pwdentries.append(PasswordEntry(host, user, pwd))

        return pwdentries

    def list_entries (self):
        for entry in sorted(self.hostdata.keys()):
            print entry  # + '\t' + self.hostdata[entry].getUser()

    def _populate_data (self):
        pwd_list = self.get_pwd_entry_list()
        new_hostdata = {}
        for entry in pwd_list:
            new_hostdata[entry.getHost()] = entry

        return new_hostdata
