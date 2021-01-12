#!/usr/bin/env python3
from string import ascii_letters

class PasswordEntry():
    def __init__(self, entry_string):
        """
            entry_string will be the single line of
            the file. Upon ingesting, all computations
            of this password will be performed on it.
        """
        self.first = None
        self.second = None
        self.char_pol = ''
        self.pass_pol, self.password = entry_string.split(':')
        self.password = self.password.strip()
        self.pass_pol = self.pass_pol.strip()
        self._read_policy(self.pass_pol)

    def _read_policy(self, polstring):
        """
            It is expected that the polstring will be in the form of:
            x-y <alpha>

            where x and y are a number range, and <alpha> is a letter
            that must be included
        """
        num_range, self.char_pol = polstring.split(' ')
        low, high = num_range.split('-')
        self.first = int(low)
        self.second = int(high)

    def valid_password(self):
        """
            Returns True if the supplied password is valid, False otherwise.
        """
        pw_list = list(self.password)
        occur = 0
        try:
            if pw_list[self.first-1] == self.char_pol:
                occur += 1
            if pw_list[self.second-1] == self.char_pol:
                occur += 1
        except IndexError:
            # Out of bounds
            pass
        if occur == 1:
            return True
        return False

with open("./d2p1indata.txt", "r") as f:
    entries = f.read().splitlines()

sumtotal = 0
for entry in entries:
    check = PasswordEntry(entry)
    if check.valid_password():
        sumtotal += 1

print(f"Total valid passwords: {sumtotal}")